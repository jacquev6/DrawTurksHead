// Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

#include <cmath>

#include <boost/foreach.hpp>
#define FOREACH BOOST_FOREACH
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
        default: return boost::make_tuple(v, p, q);
    }
}


class Drawer {
public:
    Drawer(bp::object knot_, bp::object colorer_, bp::list strings_):
        p(bp::extract<int>(knot_.attr("p"))),
        q(bp::extract<int>(knot_.attr("q"))),
        d(bp::extract<int>(knot_.attr("d"))),
        p_prime(bp::extract<int>(knot_.attr("p_prime"))),
        q_prime(bp::extract<int>(knot_.attr("q_prime"))),
        inner_radius(bp::extract<float>(knot_.attr("inner_radius"))),
        outer_radius(bp::extract<float>(knot_.attr("outer_radius"))),
        line_width(bp::extract<float>(knot_.attr("line_width"))),
        average_radius((inner_radius + outer_radius) / 2),
        delta_radius((outer_radius - inner_radius - line_width) / 2),
        // The value of theta_steps is a relic:
        // it *had* to be a multiple of 2 and p when using fractions in Python code.
        // We could carefully try to change it to something simpler.
        // Hint: try small primes and see if the drawing looks good.
        theta_steps(2 /** p*/ * std::max(1, 509 / p)),  // In a half bight
        max_theta(2 * p * q_prime * theta_steps),  // Equivalent to 2*q'*pi
        theta_unit(M_PI / theta_steps / p),  // Angle in radians represented by theta=1
        compute_color(make_compute_color(knot_, colorer_)),
        strings(make_strings(strings_))
    {}

private:
    struct End {
        End(int theta_, float altitude_):
            theta(theta_), altitude(altitude_)
        {}

        int theta;
        float altitude;
    };

    struct Segment {
        Segment(const End& begin_, const End& end_):
            begin(begin_), end(end_)
        {}

        End begin;
        End end;
    };

    struct Tunnel {
        Tunnel(int k_, const Segment& before_, const Segment& after_):
            k(k_), before(before_), after(after_)
        {}

        int k;
        Segment before;
        Segment after;
    };

    struct Bridge {
        Bridge(const Segment& before_, const Segment& after_, const Tunnel& tunnel_):
            before(before_), after(after_), tunnel(tunnel_)
        {}

        Segment before;
        Segment after;
        Tunnel tunnel;
    };

    struct String {
        String(int k_, const std::vector<Segment>& segments_, const std::vector<Bridge>& bridges_):
            k(k_), segments(segments_), bridges(bridges_)
        {}

        int k;
        std::vector<Segment> segments;
        std::vector<Bridge> bridges;
    };

    std::vector<String> make_strings(bp::list strings_) {
        std::vector<String> strings;
        FOREACH(const bp::tuple& string_, extract_vector<bp::tuple>(strings_)) {
            int k = bp::extract<int>(string_.attr("k"));

            std::vector<Segment> segments;
            FOREACH(const bp::tuple& segment_, extract_vector<bp::tuple>(bp::extract<bp::list>(string_.attr("segments")))) {
                segments.push_back(make_segment(segment_));
            }

            std::vector<Bridge> bridges;
            FOREACH(const bp::tuple& brigde_, extract_vector<bp::tuple>(bp::extract<bp::list>(string_.attr("bridges")))) {
                bp::tuple tunnel_ = bp::extract<bp::tuple>(brigde_.attr("tunnel"));
                bridges.push_back(
                    Bridge(
                        make_segment(bp::extract<bp::tuple>(brigde_.attr("before"))),
                        make_segment(bp::extract<bp::tuple>(brigde_.attr("after"))),
                        Tunnel(
                            bp::extract<int>(tunnel_.attr("k")),
                            make_segment(bp::extract<bp::tuple>(tunnel_.attr("before"))),
                            make_segment(bp::extract<bp::tuple>(tunnel_.attr("after")))
                        )
                    )
                );
            }

            strings.push_back(String(k, segments, bridges));
        }
        return strings;
    }

    Segment make_segment(bp::tuple segment_) {
        bp::tuple begin = bp::extract<bp::tuple>(segment_.attr("begin"));
        bp::tuple end = bp::extract<bp::tuple>(segment_.attr("end"));

        return Segment(
            End(bp::extract<int>(begin.attr("theta")) * theta_steps, bp::extract<int>(begin.attr("altitude"))),
            End(bp::extract<int>(end.attr("theta")) * theta_steps, bp::extract<int>(end.attr("altitude")))
        );
    }

private:
    typedef boost::function<boost::tuple<float, float, float> (int, int, float)> ComputeColor;

    ComputeColor make_compute_color(const bp::object& knot_, const bp::object& colorer_) {
        if(PyObject_HasAttrString(colorer_.ptr(), "compute_color_rgb")) {
            return RgbComputeColor(knot_, colorer_);
        } else {
            return HsvComputeColor(knot_, colorer_);
        }
    }

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
        FOREACH(const String& string, strings) {
            FOREACH(const Segment& segment, string.segments) {
                draw_segment(ctx, string.k, segment);
            }
        }
    }

    void draw_segment(Cairo::RefPtr<Cairo::Context> ctx, int k, const Segment& segment) {
        for(int theta = segment.begin.theta; theta != segment.end.theta; ++theta) {
            float altitude = segment.begin.altitude + (segment.end.altitude - segment.begin.altitude) * float(theta - segment.begin.theta) / (segment.end.theta - segment.begin.theta);
            float r, g, b;
            boost::tie(r, g, b) = compute_color(k, (theta % max_theta) * theta_unit, altitude);
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
        float angle = theta * theta_unit;

        float x0, y0;
        boost::tie(x0, y0) = compute_middle_coordinates(k, angle - 0.001);
        float x1, y1;
        boost::tie(x1, y1) = compute_middle_coordinates(k, angle + 0.001);

        float x = (x0 + x1) / 2;
        float y = (y0 + y1) / 2;

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
        FOREACH(const String& string, strings) {
            FOREACH(const Bridge& bridge, string.bridges) {
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
    const float inner_radius;
    const float outer_radius;
    const float line_width;
    const float average_radius;
    const float delta_radius;
    const int theta_steps;
    const int max_theta;
    const float theta_unit;
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
