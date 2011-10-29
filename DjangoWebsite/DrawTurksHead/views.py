import cairo
from django.views.generic import TemplateView
from django.http import HttpResponse

import turkshead

index = TemplateView.as_view( template_name = "DrawTurksHead/index.html" )

demonstration = TemplateView.as_view( template_name = "DrawTurksHead/demonstration.html" )

def draw( request ):
    if "leads" in request.GET:
        leads = int( request.GET[ "leads" ] )
    else:
        leads = 3
    
    if "bights" in request.GET:
        bights = int( request.GET[ "bights" ] )
    else:
        bights = 4
    
    if "line_width" in request.GET:
        line_width = int( request.GET[ "line_width" ] )
    else:
        line_width = 50
    
    if "radius_variation" in request.GET:
        radius_variation = int( request.GET[ "radius_variation" ] )
    else:
        radius_variation = 200
    
    width = 800
    height = 600
    outerRadius = min( width, height ) / 2 - 10
    radiusVariation = radius_variation
    innerRadius = outerRadius - radiusVariation
    
    img = cairo.ImageSurface( cairo.FORMAT_RGB24, width, height )
    ctx = cairo.Context( img )
    ctx.set_source_rgb( 1, 1, 0xBF / 255. )
    ctx.paint()
    ctx.translate( width / 2, height / 2 )
    ctx.scale( 1, -1 )
    
    t = turkshead.TurksHead( leads, bights, innerRadius, outerRadius, line_width )
    t.draw( ctx )
    
    response = HttpResponse( mimetype = 'image/png' )
    img.write_to_png( response )
    return response
