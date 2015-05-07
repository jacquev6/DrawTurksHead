// Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

#include <cmath>

#include <boost/function.hpp>
#include <boost/python.hpp>
#include <boost/python/stl_iterator.hpp>
namespace bp = boost::python;
#include <pycairo.h>
static Pycairo_CAPI_t* Pycairo_CAPI;  // http://www.cairographics.org/documentation/pycairo/2/pycairo_c_api.html
#include <cairomm/cairomm.h>


template<typename T>
std::vector<T> extract_vector(const bp::list& list) {
    std::vector<T> vector;
    for(bp::stl_input_iterator<T> it(list), end; it != end; ++it) {
        vector.push_back(*it);
    }
    return vector;
}


boost::tuple<float, float, float> hsv_to_rgb(float h, float s, float v) {
    int hi = h / 60;
    double f = h / 60 - hi;
    double p = v * (1 - s);
    double q = v * (1 - f * s);
    double t = v * (1 - (1 - f) * s);
    switch(hi % 6) {
        case 0: return boost::make_tuple(v, t, p);
        case 1: return boost::make_tuple(q, v, p);
        case 2: return boost::make_tuple(p, v, t);
        case 3: return boost::make_tuple(p, q, v);
        case 4: return boost::make_tuple(t, p, v);
        case 5: return boost::make_tuple(v, p, q);
    }
}


class Drawer {
private:
// End = collections.namedtuple("End", "theta, altitude")
// Segment = collections.namedtuple("Segment", "begin, end")
// Bridge = collections.namedtuple("Bridge", "before, after, tunnel")
// Tunnel = collections.namedtuple("Tunnel", "k, before, after")
// String = collections.namedtuple("String", "k, segments, bridges")
    struct End {
        const int theta;
        const float altitude;
    };
    struct Segment {
        const End begin;
        const End end;
    };
    struct Tunnel {
        const int k;
        const Segment before;
        const Segment after;
    };
    struct Bridge {
        const Segment before;
        const Segment after;
        const Tunnel tunnel;
    };
    struct String {
        const int k;
        const std::vector<Segment> segments;
        const std::vector<Bridge> bridges;
    };

    static Segment make_segment(int theta_steps, bp::tuple segment_) {
        bp::tuple begin = bp::extract<bp::tuple>(segment_.attr("begin"));
        bp::tuple end = bp::extract<bp::tuple>(segment_.attr("end"));

        return Segment{
            End{bp::extract<int>(begin.attr("theta")) * theta_steps, bp::extract<int>(begin.attr("altitude"))},
            End{bp::extract<int>(end.attr("theta")) * theta_steps, bp::extract<int>(end.attr("altitude"))}
        };
    }

    static std::vector<String> make_strings(int p, bp::list strings_) {
        int theta_steps = 2 * std::max(1, 509 / p);

        std::vector<String> strings;
        for(const bp::tuple& string_: extract_vector<bp::tuple>(strings_)) {
            int k = bp::extract<int>(string_.attr("k"));

            std::vector<Segment> segments;
            for(const bp::tuple& segment_: extract_vector<bp::tuple>(bp::extract<bp::list>(string_.attr("segments")))) {
                segments.push_back(make_segment(theta_steps, segment_));
            }

            std::vector<Bridge> bridges;
            for(const bp::tuple& brigde_: extract_vector<bp::tuple>(bp::extract<bp::list>(string_.attr("bridges")))) {
                bp::tuple tunnel_ = bp::extract<bp::tuple>(brigde_.attr("tunnel"));
                bridges.push_back(
                    Bridge{
                        make_segment(theta_steps, bp::extract<bp::tuple>(brigde_.attr("before"))),
                        make_segment(theta_steps, bp::extract<bp::tuple>(brigde_.attr("after"))),
                        Tunnel{
                            bp::extract<int>(tunnel_.attr("k")),
                            make_segment(theta_steps, bp::extract<bp::tuple>(tunnel_.attr("before"))),
                            make_segment(theta_steps, bp::extract<bp::tuple>(tunnel_.attr("after"))),
                        }
                    }
                );
            }

            strings.push_back(String{k, segments, bridges});
        }
        return strings;
    }

    typedef boost::function<boost::tuple<float, float, float> (int, int, float)> ComputeColor;

    class HsvComputeColor {
    public:
        HsvComputeColor(const bp::object& knot_, const bp::object& colorer_):
            knot(knot_),
            compute_color_hsv(colorer_.attr("compute_color_hsv"))
        {}

        boost::tuple<float, float, float> operator()(int k, float angle, float altitude) {
            bp::object hsv = compute_color_hsv(knot, k, angle, altitude);
            float h = bp::extract<float>(hsv[0]);
            float s = bp::extract<float>(hsv[1]);
            float v = bp::extract<float>(hsv[2]);
            return hsv_to_rgb(h, s, v);
        }
    private:
        bp::object knot;
        bp::object compute_color_hsv;
    };

    class RgbComputeColor {
    public:
        RgbComputeColor(const bp::object& knot_, const bp::object& colorer_):
            knot(knot_),
            compute_color_rgb(colorer_.attr("compute_color_rgb"))
        {}

        boost::tuple<float, float, float> operator()(int k, float angle, float altitude) {
            bp::object hsv = compute_color_rgb(knot, k, angle, altitude);
            float h = bp::extract<float>(hsv[0]);
            float s = bp::extract<float>(hsv[1]);
            float v = bp::extract<float>(hsv[2]);
            return boost::make_tuple(h, s, v);
        }
    private:
        bp::object knot;
        bp::object compute_color_rgb;
    };

    static ComputeColor make_compute_color(const bp::object& knot_, const bp::object& colorer_) {
        if(PyObject_HasAttrString(colorer_.ptr(), "compute_color_rgb")) {
            return RgbComputeColor(knot_, colorer_);
        } else {
            return HsvComputeColor(knot_, colorer_);
        }
    }

public:
    Drawer(bp::object knot_, bp::object colorer_, bp::list strings_):
        Drawer(
            bp::extract<int>(knot_.attr("p")),
            bp::extract<int>(knot_.attr("q")),
            bp::extract<int>(knot_.attr("d")),
            bp::extract<int>(knot_.attr("p_prime")),
            bp::extract<int>(knot_.attr("q_prime")),
            bp::extract<float>(knot_.attr("inner_radius")),
            bp::extract<float>(knot_.attr("outer_radius")),
            bp::extract<float>(knot_.attr("line_width")),
            make_compute_color(knot_, colorer_),
            make_strings(bp::extract<int>(knot_.attr("p")), strings_)
        )
    {}

private:
    Drawer(int p_, int q_, int d_, int p_prime_, int q_prime_, float inner_radius_, float outer_radius_, float line_width_, ComputeColor compute_color_, const std::vector<String>& strings_):
        p(p_),
        q(q_),
        d(d_),
        p_prime(p_prime_),
        q_prime(q_prime_),
        average_radius((inner_radius_ + outer_radius_) / 2),
        delta_radius((outer_radius_ - inner_radius_ -line_width_) / 2),
        line_width(line_width_),
        theta_step(1. / (2 * p * std::max(1, 509 / p))),
        compute_color(compute_color_),
        strings(strings_)
    {}


public:
    void draw(bp::object ctx_) {
        Cairo::RefPtr<Cairo::Context> ctx(new Cairo::Context(PycairoContext_GET(ctx_.ptr())));

        ctx->save();
        ctx->set_antialias(Cairo::ANTIALIAS_NONE);
        draw_strings(ctx);
        redraw_intersections(ctx);
        ctx->restore();
    }

private:
    void draw_strings(Cairo::RefPtr<Cairo::Context> ctx) {
        for(const String& string: strings) {
            for(const Segment& segment: string.segments) {
                draw_segment(ctx, string.k, segment);
            }
        }
    }

    void draw_segment(Cairo::RefPtr<Cairo::Context> ctx, int k, const Segment& segment) {
        for(int theta = segment.begin.theta; theta != segment.end.theta; ++theta) {
            float altitude = segment.begin.altitude + (segment.end.altitude - segment.begin.altitude) * float(theta - segment.begin.theta) / (segment.end.theta - segment.begin.theta);
            float r, g, b;
            boost::tie(r, g, b) = compute_color(k, (theta % (4 * p * q_prime * std::max(1, 509 / p))) * theta_step * M_PI, altitude);
            ctx->set_source_rgb(r, g, b);
            path_segment(ctx, k, theta, theta +1);
            ctx->fill();
        }
    }

    void path_segment(Cairo::RefPtr<Cairo::Context> ctx, int k, int min_theta, int max_theta) {
        move_to_outer(ctx, k, min_theta);
        for(int theta=min_theta; theta != max_theta; ++theta) {
            line_to_outer(ctx, k, theta + 1);
        }
        for(int theta=max_theta; theta != min_theta; --theta) {
            line_to_inner(ctx, k, theta);
        }
        line_to_inner(ctx, k, min_theta);
        ctx->close_path();
    }

    void line_to_inner(Cairo::RefPtr<Cairo::Context> ctx, int k, int theta) {
        float x, y, nx, ny;
        boost::tie(x, y, nx, ny) = compute_all_coordinates(k, theta);
        ctx->line_to(x + nx, y + ny);
    }

    void line_to_outer(Cairo::RefPtr<Cairo::Context> ctx, int k, int theta) {
        float x, y, nx, ny;
        boost::tie(x, y, nx, ny) = compute_all_coordinates(k, theta);
        ctx->line_to(x - nx, y - ny);
    }

    void move_to_outer(Cairo::RefPtr<Cairo::Context> ctx, int k, int theta) {
        float x, y, nx, ny;
        boost::tie(x, y, nx, ny) = compute_all_coordinates(k, theta);
        ctx->move_to(x - nx, y - ny);
    }

    boost::tuple<float, float, float, float> compute_all_coordinates(int k, int theta) {
        float angle = theta * theta_step * M_PI;

        float x0, y0;
        boost::tie(x0, y0) = compute_middle_coordinates(k, angle - 0.001);
        float x1, y1;
        boost::tie(x1, y1) = compute_middle_coordinates(k, angle + 0.001);

        float x, y;
        boost::tie(x, y) = compute_middle_coordinates(k, angle);
        // float x = (x0 + x1) / 2;
        // float y = (y0 + y1) / 2;

        float dx = x1 - x0;
        float dy = y1 - y0;
        float n = std::sqrt(dx * dx + dy * dy);

        float nx = -line_width * dy / n / 2;
        float ny = line_width * dx / n / 2;

        return boost::make_tuple(x, y, nx, ny);
    }

    boost::tuple<float, float> compute_middle_coordinates(int k, float angle) {
        float r = average_radius + delta_radius * std::cos((p * angle - 2 * k * M_PI) / q);
        float x = r * std::cos(angle);
        float y = r * std::sin(angle);
        return boost::make_tuple(x, y);
    }

    void redraw_intersections(Cairo::RefPtr<Cairo::Context> ctx) {
        for(const String& string: strings) {
            for(const Bridge& bridge: string.bridges) {
                const Tunnel& tunnel = bridge.tunnel;
                path_segment(ctx, tunnel.k, tunnel.before.begin.theta, tunnel.after.end.theta);
                ctx->clip();
                draw_segment(ctx, string.k, bridge.before);
                draw_segment(ctx, string.k, bridge.after);
                ctx->reset_clip();
            }
        }
    }

private:
    const int p;
    const int q;
    const int d;
    const int p_prime;
    const int q_prime;
    const float average_radius;
    const float delta_radius;
    const float line_width;
    const float theta_step;
    const ComputeColor compute_color;
    const std::vector<String> strings;
};


bp::tuple hsv_to_rgb_py(float h, float s, float v) {
    float r, g, b;
    boost::tie(r, g, b) = hsv_to_rgb(h, s, v);
    return bp::make_tuple(r, g, b);
}


BOOST_PYTHON_MODULE(_turkshead) {
    Pycairo_IMPORT;  // Initialization of Pycairo_CAPI

    bp::class_<Drawer>("Drawer", bp::init<bp::object, bp::object, bp::list>(bp::args("self", "knot", "colorer", "strings")))
        .def("draw", &Drawer::draw, bp::args("self", "ctx"))
    ;

    bp::def("hsv_to_rgb", &hsv_to_rgb_py, bp::args("h", "s", "v"));  // Exposed only for unit tests
}
