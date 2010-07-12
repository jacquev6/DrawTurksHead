#!/bin/env python

import sys
import math
import fractions

import cairo

def rgb_from_hsv( h, s, v ):
    h *= 360.
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

        self.drawPaths( context, False )
        self.drawPaths( context, True )

    def drawPaths( self, context, fgOnly ):
        nbPaths = fractions.gcd( self.__leads, self.__bights )
        for path in range( nbPaths ):
            thetaPath = path * 2 * math.pi / self.__bights
            self.drawPath( context, thetaPath, fgOnly )

    def drawPath( self, context, thetaPath, fgOnly ):
        thetaMax = self.__leads * 2 * math.pi
        theta = 0.
        deltaTheta = math.pi / 25
        while theta < thetaMax:
            if not fgOnly or self.altitude( theta ) > 0:
                context.set_source_rgb( *rgb_from_hsv( theta / thetaMax, 1., 1. ) )
                context.set_line_width( 0.01 + 0.1 * ( self.altitude( theta ) + 1 ) )
                self.drawArc( context, thetaPath, theta, deltaTheta )
            theta += deltaTheta

    def drawArc( self, context, thetaPath, theta, deltaTheta ):
        xA, yA = self.xy( thetaPath, theta - deltaTheta )
        xB, yB = self.xy( thetaPath, theta - deltaTheta / 1.8 )
        xC, yC = self.xy( thetaPath, theta )
        xD, yD = self.xy( thetaPath, theta + deltaTheta / 1.8 )
        xE, yE = self.xy( thetaPath, theta + deltaTheta )

        x1, y1 = xB, yB
        d = 0.3
        x2, y2 = xB + d * ( xC - xA ), yB + d * ( yC - yA )
        x3, y3 = xD + d * ( xC - xE ), yD + d * ( yC - yE )
        x4, y4 = xD, yD

        context.move_to( x1, y1 )
        context.curve_to( x2, y2, x3, y3, x4, y4 )
        context.stroke()

    def r( self, theta ):
        return 1. + 0.5 * math.cos( self.__bights * theta / self.__leads )

    def xy( self, thetaPath, theta ):
        r = self.r( theta )
        x = r * math.cos( thetaPath + theta )
        y = r * math.sin( thetaPath + theta )
        return ( x, y )

    def altitude( self, theta ):
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
    minLeads = 3
    maxLeads = 4
    minBights = 4
    maxBights = 5
    unitSize = 400

    img = cairo.ImageSurface( cairo.FORMAT_RGB24, 50 + unitSize * ( maxLeads - minLeads + 1 ), 50 + unitSize * ( maxBights - minBights + 1 ) )
    ctx = cairo.Context( img )
    ctx.set_source_rgb( 1, 1, 0.8 )
    ctx.paint()
    ctx.set_source_rgb( 0, 0, 0 )
    ctx.translate( 25, 25 )
    ctx.scale( unitSize, unitSize )

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
