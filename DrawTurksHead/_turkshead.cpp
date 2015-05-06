// Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

#include <cmath>

#include <boost/python.hpp>
namespace bp = boost::python;


class Coordinates {
public:
    Coordinates(float theta_step_, int bights_, int leads_, float inner_, float outer_, float line_):
        theta_step(theta_step_),
        p(bights_),
        q(leads_),
        average_radius((inner_ + outer_) / 2),
        delta_radius((outer_ - inner_ -line_) / 2),
        line_width(line_)
    {}

    bp::tuple get_inner(int k, int theta) {
        float x, y, nx, ny;
        boost::tie(x, y, nx, ny) = get_all(k, theta);
        return bp::make_tuple(x + nx, y + ny);
    }

    bp::tuple get_outer(int k, int theta) {
        float x, y, nx, ny;
        boost::tie(x, y, nx, ny) = get_all(k, theta);
        return bp::make_tuple(x - nx, y - ny);
    }

private:
    boost::tuple<float, float, float, float> get_all(int k, int theta) {
        float angle = theta * theta_step * M_PI;

        float x0, y0;
        boost::tie(x0, y0) = get(k, angle - 0.001);
        float x1, y1;
        boost::tie(x1, y1) = get(k, angle + 0.001);

        float x, y;
        boost::tie(x, y) = get(k, angle);
        // float x = (x0 + x1) / 2;
        // float y = (y0 + y1) / 2;

        float dx = x1 - x0;
        float dy = y1 - y0;
        float n = std::sqrt(dx * dx + dy * dy);

        float nx = -line_width * dy / n / 2;
        float ny = line_width * dx / n / 2;

        return boost::make_tuple(x, y, nx, ny);
    }

    boost::tuple<float, float> get(int k, float angle) {
        float r = average_radius + delta_radius * std::cos((p * angle - 2 * k * M_PI) / q);
        float x = r * std::cos(angle);
        float y = r * std::sin(angle);
        return boost::make_tuple(x, y);
    }

private:
    float theta_step;
    int p;
    int q;
    float average_radius;
    float delta_radius;
    float line_width;
};

BOOST_PYTHON_MODULE(_turkshead) {
    bp::class_<Coordinates>("Coordinates", bp::init<float, int, int, float, float, float>(bp::args("self", "theta_step", "bights", "leads", "inner", "outer", "line")))
        .def("get_inner", &Coordinates::get_inner, bp::args("self", "k", "theta"))
        .def("get_outer", &Coordinates::get_outer, bp::args("self", "k", "theta"))
    ;
}
