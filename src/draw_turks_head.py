import cairo

import turkshead


print dir( turkshead )

t = turkshead.TurksHead( 2, 3, 100, 400, 25 )

img = cairo.ImageSurface( cairo.FORMAT_RGB24, 800, 600 )
ctx = cairo.Context( img )

#t.draw( ctx )

img.write_to_png( "turks_head.png" )
