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
    
    double getAltitude( int k, int theta ) {
        return TurksHead::TurksHead::getAltitude(
            TurksHead::TurksHead::Path( k ),
            TurksHead::TurksHead::Theta( theta )
        );
    }

private:
    boost::tuple< double, double, double > computeColorHsv( int k, int theta ) const {
        //return TurksHead::TurksHead::computeColorHsv( k, theta );
        if( boost::python::override f = this->get_override( "computeColorHsv" ) ) {
            boost::python::tuple r = f( k, theta );
            double h = boost::python::extract< double >( r[0] );
            double s = boost::python::extract< double >( r[1] );
            double v = boost::python::extract< double >( r[2] );
            return boost::make_tuple( h, s, v );
        } else {
            return TurksHead::TurksHead::computeColorHsv( k, theta );
        }
    }
};

}

BOOST_PYTHON_MODULE( _turkshead ) {
    Pycairo_IMPORT; // Initialization of Pycairo_CAPI
    
    /// @todo Look at http://www.boost.org/doc/libs/1_43_0/libs/parameter/doc/html/python.html to add named parameters to the constructor
    boost::python::class_< PythonTurksHead >( "TurksHead", boost::python::init< int, int, double, double, double >() )
        .def( "draw", &PythonTurksHead::draw )
        .add_property( "p", &TurksHead::TurksHead::getP )
        .add_property( "q", &TurksHead::TurksHead::getQ )
        .add_property( "d", &TurksHead::TurksHead::getD )
        .def( "getAltitude", &PythonTurksHead::getAltitude )
    ;
}
