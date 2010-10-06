import math
import fractions
import cairo

colors = [
    ( 0, 0, 1 ),
    ( 0, 1, 0 ),
    ( 1, 0, 0 ),
    ( 0, 1, 1 ),
    ( 1, 0, 1 ),
    ( 1, 1, 0 ),
    ( 0, 0.5, 1 ),
    ( 1, 0, 0.5 ),
    ( 1, 0.5, 0 ),
]

def getCartesianCoordinates( r, theta ):
    x = r * math.cos( theta )
    y = r * math.sin( theta )
    return x, y

class TurksHead:
    def __init__( self, p, q ):
        self.p = p
        self.q = q
        self.d = fractions.gcd( p, q )
        self.r = 30
        self.dr = 15
        self.nbInter = 0
        self.badInter = 0

    def phi( self, k ):
        return 2 * k * math.pi / self.p

    def getRadius( self, k, theta ):
        return self.r + self.dr * math.cos( self.p * ( theta - self.phi( k ) ) / self.q )

    def drawPath( self, k, ctx = None ):
        if ctx is not None:
            self.ctx = ctx
        self.ctx.set_source_rgb( *colors[ k ] )
        theta = 0
        r = self.getRadius( k, theta )
        self.ctx.move_to( *getCartesianCoordinates( r, theta ) )
        for i in range( 1, 2 * self.q / self.d * 25 ):
            theta = i * math.pi / 25
            r = self.getRadius( k, theta )
            self.ctx.line_to( *getCartesianCoordinates( r, theta ) )
        self.ctx.close_path()
        self.ctx.stroke()

    def drawPaths( self, ctx = None ):
        if ctx is not None:
            self.ctx = ctx
        for k in range( self.d ):
            self.drawPath( k )

    def draw( self, ctx ):
        self.ctx = ctx
        self.drawPaths()

        for m in range( self.d ):
            for n in range( m, self.d ):
                self.curveIntersect( m, n )

        #print self.p, self.q, "=>", self.nbInter, "intersections", self.badInter, "bad inter", self.nbInter == self.p * ( self.q - 1 )
        #print self.p, self.q, "=>", self.badInter, self.nbInter == self.p * ( self.q - 1 )

    def drawPoints( self, n, theta_1, m, theta_2 ):
        r1 = self.getRadius( n, theta_1 )
        x1, y1 = getCartesianCoordinates( r1, theta_1 )
        r2 = self.getRadius( m, theta_2 )
        x2, y2 = getCartesianCoordinates( r2, theta_2 )

        self.ctx.set_line_cap( cairo.LINE_CAP_ROUND )
        self.ctx.set_source_rgb( 0, 0, 0 )
        self.ctx.set_line_width( 6 )
        self.ctx.move_to( x1, y1 )
        self.ctx.line_to( x2, y2 )
        self.ctx.stroke()

    def intersect( self, m, n, a, b ):
        theta_1 = ( a * self.p + b * self.q + m + n ) * math.pi/self.p
        theta_2 = theta_1 - 2 * a * math.pi

        #print self.p, self.q, self.d, "-", m, n, a, b, "=>", theta_1/math.pi, "pi,", theta_2/math.pi, "pi"

        self.nbInter += 1

        self.drawPoints( n, theta_1, m, theta_2 )

    def curveIntersect( self, m, n ):
        #  -( m + n ) <= a*p + b*q < 2*p*q/d - ( m + n )
        #  -( m + n ) <= -a*p + b*q < 2*p*q/d - ( m + n )
        alpha = -( m + n )
        beta = 2*self.p*self.q/self.d - ( m + n )

        minA = int( math.ceil( -1. * self.q / self.d ) )
        maxA = int( math.ceil( 1. * self.q / self.d ) )

        minB = int( math.ceil( -1. * ( m + n ) / self.q ) )
        maxB = int( math.ceil( 2. * self.p / self.d - ( m + n ) / self.q ) )

        for a in range( minA, maxA ):
            for b in range( minB, maxB ):
                if n == m and a <= 0:
                    continue
                if ( alpha <= a * self.p + b * self.q and a * self.p + b * self.q < beta
                and alpha <= -a * self.p + b * self.q and -a * self.p + b * self.q < beta ):
                    self.intersect( m, n, a, b )
                else:
                    self.badInter += 1

def draw( size, drawFunction, fileName ):
    img = cairo.ImageSurface( cairo.FORMAT_ARGB32, 100 * size, 100 * size )
    ctx = cairo.Context( img )
    ctx.set_source_rgb( 1, 1, 1 )
    ctx.paint()
    ctx.translate( 50, 50 )
    ctx.scale( 1, -1 )
    ctx.set_source_rgb( 0, 0, 0 )

    for p in range( size ):
        for q in range( size ):
            t = TurksHead( p + 1, q + 1 )
            ctx.save()
            ctx.translate( 100 * p, -100 * q )
            drawFunction( t, ctx )
            ctx.restore()

    img.write_to_png( fileName )

draw( 6, lambda t, ctx: t.drawPath( 0, ctx ), "basic_waves_1.png" )
draw( 6, lambda t, ctx: t.drawPaths( ctx ), "basic_waves_2.png" )
draw( 6, lambda t, ctx: t.draw( ctx ), "intersections.png" )
