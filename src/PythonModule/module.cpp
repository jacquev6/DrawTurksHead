// Boost
#include <boost/python.hpp>

// PyCairo
#include <pycairo/pycairo.h>
// See http://www.cairographics.org/documentation/pycairo/2/pycairo_c_api.html
static Pycairo_CAPI_t* Pycairo_CAPI;

// DrawTurksHead
#include <TurksHead/TurksHead.hpp>

namespace {

void drawTurksHead( TurksHead::TurksHead& t, boost::python::object context ) {
    t.draw( Cairo::RefPtr< Cairo::Context >( new Cairo::Context( PycairoContext_GET( context.ptr() ) ) ) );
}

}

BOOST_PYTHON_MODULE( _turkshead ) {
    using namespace boost::python;
    Pycairo_IMPORT; // Initialization of Pycairo_CAPI
    
    /// @todo Look at http://www.boost.org/doc/libs/1_43_0/libs/parameter/doc/html/python.html, to add named parameters to the constructor
    class_< TurksHead::TurksHead >( "TurksHead", init< int, int, double, double, double >() )
        .def( "draw", &drawTurksHead )
    ;
}
