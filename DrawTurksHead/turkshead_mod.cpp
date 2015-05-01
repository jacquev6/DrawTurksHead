// Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

// Boost
#include <boost/python.hpp>

// PyCairo
#include <pycairo.h>
// See http://www.cairographics.org/documentation/pycairo/2/pycairo_c_api.html
static Pycairo_CAPI_t* Pycairo_CAPI;

// Project
#include "turkshead.hpp"

namespace {

typedef turkshead::TurksHead TurksHead;

class PythonTurksHead: public TurksHead, public boost::python::wrapper< TurksHead> {
public:
    PythonTurksHead(int leads, int bights, double innerRadius, double outerRadius, double lineWidth):
        TurksHead(leads, bights, innerRadius, outerRadius, lineWidth),
        python_compute_color_hsv(this->get_override("")),
        python_compute_color_hsv_initialized(false)
    {
    }

    PythonTurksHead(const TurksHead& t):
        TurksHead(t),
        python_compute_color_hsv(this->get_override("")),
        python_compute_color_hsv_initialized(false)
    {
    }

    void draw(boost::python::object context) {
        TurksHead::draw(Cairo::RefPtr< Cairo::Context >(new Cairo::Context(PycairoContext_GET(context.ptr()))));
    }

    double get_altitude(int k, int theta) {
        return TurksHead::get_altitude(
            TurksHead::Path(k),
            TurksHead::Theta(theta)
       );
    }

private:
    boost::tuple<double, double, double> compute_color_hsv(int k, int theta) const {
        if(!python_compute_color_hsv_initialized) {
            python_compute_color_hsv = this->get_override("compute_color_hsv");
            python_compute_color_hsv_initialized = true;
        }
        if(python_compute_color_hsv) {
            boost::python::tuple r = python_compute_color_hsv(k, theta);
            double h = boost::python::extract<double>(r[0]);
            double s = boost::python::extract<double>(r[1]);
            double v = boost::python::extract<double>(r[2]);
            return boost::make_tuple(h, s, v);
        } else {
            return TurksHead::compute_color_hsv(k, theta);
        }
    }

private:
    mutable boost::python::override python_compute_color_hsv;
    mutable bool python_compute_color_hsv_initialized;
};

} // Namespace

BOOST_PYTHON_MODULE(_turkshead) {
    Pycairo_IMPORT; // Initialization of Pycairo_CAPI

    // @todo Look at http://www.boost.org/doc/libs/1_43_0/libs/parameter/doc/html/python.html to add named parameters to the constructor
    boost::python::class_<PythonTurksHead>("TurksHead", boost::python::init<int, int, double, double, double>())
        .def("draw", &PythonTurksHead::draw)
        .add_property("p", &TurksHead::get_p)
        .add_property("q", &TurksHead::get_q)
        .add_property("d", &TurksHead::get_d)
        .def("get_altitude", &PythonTurksHead::get_altitude)
    ;
}
