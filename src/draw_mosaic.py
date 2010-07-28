import optparse
import fractions

import cairo

import turkshead

width = 9
height = 9
size = 200

img = cairo.ImageSurface( cairo.FORMAT_RGB24, width * size, height * size )
ctx = cairo.Context( img )
ctx.set_source_rgb( 1, 1, 0xBF / 255. )
ctx.paint()
ctx.translate( -size / 2, -size / 2 )
ctx.set_source_rgb( 0, 0, 0 )

for leads in range( 1, width + 1 ):
    for bights in range( 1, height + 1 ):
        ctx.save()
        ctx.translate( size * bights, size * leads )
        t = turkshead.TurksHead( leads, bights, size / 8. * 0.9, size / 2. * 0.9, size / 15. )
        t.draw( ctx )
        ctx.restore()

img.write_to_png( "mosaic.png" )
