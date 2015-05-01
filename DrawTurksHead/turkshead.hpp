// Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

#ifndef turkshead_hpp
#define turkshead_hpp

// Standard library
#include <list>
#include <map>
#include <set>

// Boost
#include <boost/operators.hpp>
#include <boost/tuple/tuple.hpp>

// Cairo
#include <cairomm/cairomm.h>

#define STRONG_TYPEDEF(T, D) \
struct D : \
    boost::operators<D>, \
    boost::operators<D, T> \
{ \
    explicit D(T t_) : t(t_) {}\
    T index() const { return t; } \
\
    /*bool operator=(D);*/ \
    bool operator=(T); \
\
    void operator++() { ++t; } \
    void operator--() { --t; } \
    D operator-() const; \
\
    D operator+=(D d) { t += d.t; return *this; } \
    D operator+=(T d) { t += d;   return *this; } \
    D operator-=(D d) { t -= d.t; return *this; } \
    D operator-=(T d) { t -= d;   return *this; } \
    D operator*=(T); \
    D operator/=(T d) { t /= d;   return *this; } \
    D operator%=(D d) { t %= d.t; return *this; } \
    D operator%=(T); \
\
    bool operator==(D d) const { return t == d.t; } \
    bool operator==(T d) const { return t == d; } \
    bool operator<(D d) const { return t <d.t; } \
    bool operator<(T d) const { return t <d; } \
\
private: \
    T t; \
};

namespace turkshead {

class TurksHead {
public:
    TurksHead(int leads, int bights, double innerRadius, double outerRadius, double lineWidth);
    virtual ~TurksHead();

public:
    void draw(Cairo::RefPtr<Cairo::Context>) const;
    int get_p() const;
    int get_q() const;
    int get_d() const;

protected: /// @todo Remove this work arround: this function should be private. MAYBE...
    STRONG_TYPEDEF(int, Theta)
    STRONG_TYPEDEF(int, Path)

private:
    struct Intersection {
        Intersection(Path, Theta, Path, Theta);
        Path m;
        Theta theta_on_path_m;
        Path n;
        Theta theta_on_path_n;
    };

    struct Segment {
        Segment(Theta min, Theta max);
        Theta min_theta;
        Theta max_theta;
    };

private:
    void setup_drawing(Cairo::RefPtr<Cairo::Context>) const;
    void teardown_drawing() const;

    void draw_all_paths() const;
    void draw_path(Path k) const;
    void draw_segment(Path k, Theta minTheta, Theta maxTheta) const;
    void draw_step(Path k, Theta theta) const;
    void redraw_all_intersections() const;
    void redraw_intersection(const Intersection&) const;

    void set_source(Path k, Theta) const;

protected: /// @todo Remove this work arround: this function should be private
    virtual boost::tuple<double, double, double> compute_color_hsv(int, int) const;

private:
    boost::tuple<double, double> get_coordinates(Path k, Theta theta) const;
    boost::tuple<double, double> get_inner_coordinates(Path k, Theta theta) const;
    boost::tuple<double, double> get_outer_coordinates(Path k, Theta theta) const;
    boost::tuple<double, double> get_normal(Path k, Theta theta) const;
    double get_radius(Path k, Theta theta) const;
    boost::tuple<double, double> convert_radial_to_cartesian_coordinates(double radius, Theta theta) const;

    Theta phi(Path k) const;

protected: /// @todo Remove this work arround: this function should be private. MAYBE...
    double get_altitude(Path k, Theta theta) const;

private:
    void compute_known_altitudes();

    void compute_intersections();
    std::list<std::pair<Path, Path> > all_path_pairs() const;
    void compute_path_pair_intersections(Path m, Path n);
    void add_intersection(Path m, Path n, int a, int b);

    void clip_region(Path k, Theta theta) const;
    void redraw_region(Path k, Theta theta) const;
    void clip_segment(Path k, Theta minTheta, Theta maxTheta) const;

    void path_segment(Path k, Theta minTheta, Theta maxTheta) const;

    void move_to(const boost::tuple<double, double>&) const;
    void line_to(const boost::tuple<double, double>&) const;

    void set_source_hsv(boost::tuple<double, double, double>) const;
    void set_source_hsv(double h, double s, double v) const;

    double angle_from_theta(Theta theta) const;

    std::pair<Theta, double> get_prev_known_altitude(Path k, Theta theta) const;
    std::pair<Theta, double> get_next_known_altitude(Path k, Theta theta) const;

    Theta get_prev_redraw_limit(Path k, Theta theta) const;
    Theta get_next_redraw_limit(Path k, Theta theta) const;

private:
    int p;
    int q;
private:
    int d;
    int theta_steps;
    Theta max_theta_on_path;
    std::map<Path, std::map<Theta, double> > known_altitudes;
    std::list<Intersection> intersections;
private:
    double radius;
    double delta_radius;
private:
    double line_width;

private:
    mutable Cairo::RefPtr<Cairo::Context> ctx;
};

} // Namespace

#endif // Include guard
