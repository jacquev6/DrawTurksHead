// Boost
#include <boost/python.hpp>

// PyCairo
#include <pycairo/pycairo.h>
// See http://www.cairographics.org/documentation/pycairo/2/pycairo_c_api.html
static Pycairo_CAPI_t* Pycairo_CAPI;

// DrawTurksHead
#include <TurksHead/TurksHead.hpp>

namespace {

class PythonTurksHead : public TurksHead::TurksHead, public boost::python::wrapper< TurksHead::TurksHead > {
public:
    PythonTurksHead( int leads, int bights, double innerRadius, double outerRadius, double lineWidth ) :
        TurksHead::TurksHead( leads, bights, innerRadius, outerRadius, lineWidth )
    {
    }
    
    PythonTurksHead( const TurksHead::TurksHead& t ) :
        TurksHead::TurksHead( t )
    {
    }

    void draw( boost::python::object context ) {
        TurksHead::draw( Cairo::RefPtr< Cairo::Context >( new Cairo::Context( PycairoContext_GET( context.ptr() ) ) ) );
    }

private:
    double doGetHue( int k, int theta ) const {
        using namespace boost::python;
        if( override f = this->get_override( "get_hue" ) ) {
            return f( k, theta );
        } else {
            return TurksHead::TurksHead::doGetHue( k, theta );
        }
    }
};

}

BOOST_PYTHON_MODULE( _turkshead ) {
    using namespace boost::python;
    Pycairo_IMPORT; // Initialization of Pycairo_CAPI
    
    /// @todo Look at http://www.boost.org/doc/libs/1_43_0/libs/parameter/doc/html/python.html, to add named parameters to the constructor
    class_< PythonTurksHead >( "TurksHead", init< int, int, double, double, double >() )
        .def( "draw", &PythonTurksHead::draw )
        .add_property( "d", &TurksHead::TurksHead::getD )
    ;
}
