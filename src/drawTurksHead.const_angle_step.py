#!/bin/env python

import sys
import math
import fractions

import cairo

def rgb_from_hsv( h, s, v ):
    hi = int( h / 60. )
    f = h / 60. - hi
    hi %= 60;
    p = v * ( 1 - s )
    q = v * ( 1 - f * s )
    t = v * ( 1 - ( 1 - f ) * s )
    if hi == 0: return ( v, t, p )
    if hi == 1: return ( q, v, p )
    if hi == 2: return ( p, v, t )
    if hi == 3: return ( p, q, v )
    if hi == 4: return ( t, p, v )
    if hi == 5: return ( v, p, q )

class TurksHead:
    def __init__( self, leads, bights ):
        self.__leads = leads # spire
        self.__bights = bights # ganse

    def draw( self, context ):

        context.translate( 0.5, 0.5 )
        context.scale( 0.25, 0.25 )

        self.drawOne( context, self.drawCurve )
        self.drawOne( context, self.drawCurve, self.filterForeground )

    def drawOne( self, context, drawingFunction, filterFunction = lambda path, nbPaths, step, nbSteps, deltaTheta: True ):
        nbStepsByLead = 50 * self.__bights
        deltaTheta =  2 * math.pi / nbStepsByLead
        nbSteps = nbStepsByLead * self.__leads
        nbPaths = fractions.gcd( self.__leads, self.__bights )
        for path in range( nbPaths ):
            for step in range( 0, nbSteps / nbPaths ):
                if filterFunction( path, nbPaths, step, nbSteps, deltaTheta ):
                    context.set_source_rgb( *self.color( path, nbPaths, step, nbSteps, deltaTheta ) )
                    drawingFunction( context, path, nbPaths, step, nbSteps, deltaTheta )

    def filterForeground( self, path, nbPaths, step, nbSteps, deltaTheta ):
        theta0 = path * 2 * math.pi / self.__bights
        theta = step * deltaTheta
        return self.altitude( theta0, theta ) >= 0

    def drawCurve( self, context, path, nbPaths, step, nbSteps, deltaTheta ):
        theta0 = path * 2 * math.pi / self.__bights
        theta = step * deltaTheta
        xA, yA = self.coordinates( theta0, theta - deltaTheta )
        xB, yB = self.coordinates( theta0, theta - deltaTheta / 1.8 )
        xC, yC = self.coordinates( theta0, theta )
        xD, yD = self.coordinates( theta0, theta + deltaTheta / 1.8 )
        xE, yE = self.coordinates( theta0, theta + deltaTheta )

        x1, y1 = xB, yB
        d = 0.3
        x2, y2 = xB + d * ( xC - xA ), yB + d * ( yC - yA )
        x3, y3 = xD + d * ( xC - xE ), yD + d * ( yC - yE )
        x4, y4 = xD, yD
        context.move_to( x1, y1 )
        context.curve_to( x2, y2, x3, y3, x4, y4 )
        context.set_line_width( 0.1 )
        #context.set_line_width( 0.01 + 0.1 * ( self.altitude( theta0, theta ) + 1 ) )
        context.stroke()

    def color( self, path, nbPaths, step, nbSteps, deltaTheta ):
        theta0 = path * 2 * math.pi / self.__bights
        theta = step * deltaTheta
        return rgb_from_hsv( 360. * step / nbSteps * nbPaths, 1., 0.4 + 0.3 * ( 1. + self.altitude( theta0, theta ) ) );

    def coordinates( self, theta0, theta ):
        r = 1. + 0.5 * math.cos( self.__bights * theta / self.__leads )
        x = r * math.cos( theta0 + theta )
        y = r * math.sin( theta0 + theta )
        return ( x, y )

    def altitude( self, theta0, theta ):
        z = 1.
        previous_i = -1
        alt = 1
        for i in range( 1, 2 * self.__leads * self.__bights + 2 ):
            if i % self.__leads:
                angle = i * math.pi / self.__bights
                previous_angle = previous_i * math.pi / self.__bights
                previous_alt = -alt
                if previous_angle <= theta and angle > theta:
                    z = previous_alt + ( alt - previous_alt ) * ( theta - previous_angle ) / ( angle - previous_angle )
                    break
                previous_i = i
                alt *= -1

        return z

if __name__ == "__main__":
    minLeads = 1
    maxLeads = 4
    minBights = 1
    maxBights = 4
    unitSize = 400

    img = cairo.ImageSurface( cairo.FORMAT_RGB24, 50 + unitSize * ( maxLeads - minLeads + 1 ), 50 + unitSize * ( maxBights - minBights + 1 ) )
    ctx = cairo.Context( img )
    ctx.set_source_rgb( 1, 1, 0.8 )
    ctx.paint()
    ctx.set_source_rgb( 0, 0, 0 )
    ctx.translate( 25, 25 )
    ctx.scale( unitSize, unitSize )
    #ctx.set_antialias( cairo.ANTIALIAS_NONE )

    for leads in range( minLeads, maxLeads + 1):
        for bights in range( minBights, maxBights + 1 ):
            ctx.save()

            ctx.translate( leads - minLeads, bights - minBights )

            ctx.rectangle( 0, 0, 1, 1 )
            ctx.save()
            ctx.identity_matrix()
            ctx.stroke()
            ctx.restore()

            t = TurksHead( leads, bights )
            t.draw( ctx )

            ctx.restore()

    img.write_to_png( "test.png" )
