// Boost
#include <boost/python.hpp>

// DrawTurksHead
#include <TurksHead/TurksHead.hpp>

BOOST_PYTHON_MODULE( _turkshead ) {
    using namespace boost::python;
    /// @todo Look at http://www.boost.org/doc/libs/1_43_0/libs/parameter/doc/html/python.html, to add named parameters to the constructor
    class_< TurksHead::TurksHead >( "TurksHead", init< int, int, double, double, double >() )
        .def( "draw", &TurksHead::TurksHead::draw )
    ;
}
