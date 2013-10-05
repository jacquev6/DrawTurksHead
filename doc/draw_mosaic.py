#!/usr/bin/env python

import cairo

import turkshead

class MyTurksHead( turkshead.TurksHead ):
    def computeColorHsv( self, k, theta ):
        return ( ( k * 360. / self.d + 240. ) % 360., 0.5, 0.5 + self.getAltitude( k, theta ) / 2 )

width = 9
height = 5
size = 100

img = cairo.ImageSurface( cairo.FORMAT_RGB24, width * size, height * size )
ctx = cairo.Context( img )
ctx.set_source_rgb( 1, 1, 0xBF / 255. )
ctx.paint()
ctx.translate( -size / 2, -size / 2 )
ctx.set_source_rgb( 0, 0, 0 )

for leads in range( 1, height + 1 ):
    for bights in range( 1, width + 1 ):
        ctx.save()
        ctx.translate( size * bights, size * leads )
        t = MyTurksHead( leads, bights, size / 8. * 0.9, size / 2. * 0.9, size / 15. )
        t.draw( ctx )
        ctx.restore()

img.write_to_png( "mosaic.png" )
