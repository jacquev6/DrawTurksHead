from django.conf.urls.defaults import patterns

urlpatterns = patterns( "",
    ( r"^$", "DrawTurksHead.views.index" ),
    ( r"^demonstration$", "DrawTurksHead.views.demonstration" ),
    ( r"^roadmap$", "DrawTurksHead.views.roadmap" ),
    ( r"^draw$", "DrawTurksHead.views.draw" ),
)
