// Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

// Boost
#include <boost/python.hpp>

// PyCairo
#include <pycairo.h>
// See http://www.cairographics.org/documentation/pycairo/2/pycairo_c_api.html
static Pycairo_CAPI_t* Pycairo_CAPI;

// Project
#include "turkshead.hpp"

typedef turkshead::TurksHead BaseTurksHead;
namespace bp = boost::python;

class TurksHead: public BaseTurksHead, public bp::wrapper<BaseTurksHead> {
public:
    TurksHead(int leads, int bights, double innerRadius, double outerRadius, double lineWidth):
        BaseTurksHead(leads, bights, innerRadius, outerRadius, lineWidth),
        python_compute_color_hsv(this->get_override("")),
        python_compute_color_hsv_initialized(false)
    {
    }

    TurksHead(const BaseTurksHead& t):
        BaseTurksHead(t),
        python_compute_color_hsv(this->get_override("")),
        python_compute_color_hsv_initialized(false)
    {
    }

    void draw(bp::object context) {
        BaseTurksHead::draw(Cairo::RefPtr<Cairo::Context>(new Cairo::Context(PycairoContext_GET(context.ptr()))));
    }

    double get_altitude(int k, int theta) {
        return BaseTurksHead::get_altitude(
            BaseTurksHead::Path(k),
            BaseTurksHead::Theta(theta)
       );
    }

    bp::tuple default_compute_color_hsv(int k, int theta) const {
        // @todo There must be a simpler way to convert from boost::tuple to bp::tuple.
        double h, s, v;
        boost::tie(h, s, v) = BaseTurksHead::compute_color_hsv(k, theta);
        return bp::make_tuple(h, s, v);
    }

private:
    boost::tuple<double, double, double> compute_color_hsv(int k, int theta) const {
        if(!python_compute_color_hsv_initialized) {
            python_compute_color_hsv = this->get_override("compute_color_hsv");
            python_compute_color_hsv_initialized = true;
        }
        if(python_compute_color_hsv) {
            // @todo There must be a simpler way to convert from bp::tuple to boost::tuple.
            bp::tuple r = python_compute_color_hsv(k, theta);
            double h = bp::extract<double>(r[0]);
            double s = bp::extract<double>(r[1]);
            double v = bp::extract<double>(r[2]);
            return boost::make_tuple(h, s, v);
        } else {
            return BaseTurksHead::compute_color_hsv(k, theta);
        }
    }

private:
    mutable bp::override python_compute_color_hsv;
    mutable bool python_compute_color_hsv_initialized;
};

BOOST_PYTHON_MODULE(_turkshead) {
    Pycairo_IMPORT; // Initialization of Pycairo_CAPI

    // @todo Look at http://www.boost.org/doc/libs/1_43_0/libs/parameter/doc/html/python.html to add named parameters to the constructor
    bp::class_<TurksHead>("TurksHead", "Turk's head objects.", bp::init<int, int, double, double, double>(bp::args("self", "leads", "bights", "inner", "outer", "line")))
        .def("draw", &TurksHead::draw, "Draw the Turk's head on a Cairo context.", bp::args("self", "ctx"))
        .add_property("p", &BaseTurksHead::get_p, "The number of bights.")
        .add_property("q", &BaseTurksHead::get_q, "The number of leads.")
        .add_property("d", &BaseTurksHead::get_d, "The GCD of :attr:`~.TurksHead.p` and :attr:`~.TurksHead.q`.")
        .def("get_altitude", &TurksHead::get_altitude, "Get the altitude (between -1 and 1) of the ``k``-th string at polar angle ``theta``. Typically used when overriding :meth:`~.TurksHead.compute_color_hsv`.", bp::args("self", "k", "theta"))
        .def("compute_color_hsv", &TurksHead::default_compute_color_hsv, "Method to override to draw Turk's heads with custom colors. Must return an ``(hue, saturation, value)`` tuple for the ``k``-th string at polar angle ``theta``.", bp::args("self", "k", "theta"))
    ;
}
