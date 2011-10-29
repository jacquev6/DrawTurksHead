from django.conf.urls.defaults import patterns

urlpatterns = patterns( "",
    ( r"^$", "DrawTurksHead.views.index" ),
    ( r"^demonstration$", "DrawTurksHead.views.demonstration" ),
    ( r"^draw$", "DrawTurksHead.views.draw" ),
)
