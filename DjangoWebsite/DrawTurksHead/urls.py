from django.conf.urls.defaults import patterns

urlpatterns = patterns( "",
    ( r"^$", "DrawTurksHead.views.index" ),
    ( r"^draw$", "DrawTurksHead.views.draw" ),
)
