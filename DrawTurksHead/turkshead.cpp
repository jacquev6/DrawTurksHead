// Copyright 2013-2015 Vincent Jacques <vincent@vincent-jacques.net>

// Project
#include "turkshead.hpp"

// Standard library
#include <cassert>
#include <cmath>
#include <map>

// Boost
#include <boost/foreach.hpp>
#include <boost/lambda/lambda.hpp>
#include <boost/math/common_factor.hpp>
#include <boost/utility.hpp>
#include <boost/utility.hpp>

#define foreach BOOST_FOREACH

namespace turkshead {

TurksHead::Intersection::Intersection(Path m_, Theta theta_on_path_m_, Path n_, Theta theta_on_path_n_) :
    m(m_),
    theta_on_path_m(theta_on_path_m_),
    n(n_),
    theta_on_path_n(theta_on_path_n_)
{
}

TurksHead::Segment::Segment(Theta min, Theta max) :
    min_theta(min),
    max_theta(max)
{
}

TurksHead::~TurksHead() {
}

TurksHead::TurksHead(int leads_, int bights_, double inner_radius_, double outer_radius_, double line_width_) :
    p(bights_),
    q(leads_),
    d(boost::math::gcd(p, q)),
    theta_steps(100),
    max_theta_on_path(2 * q * p * theta_steps / d),
    radius((inner_radius_ + outer_radius_) / 2),
    delta_radius((outer_radius_ - inner_radius_ - line_width_) / 2),
    line_width(line_width_)
{
    compute_intersections();
    compute_known_altitudes();
}

void TurksHead::compute_intersections() {
    typedef std::pair<Path, Path> PP;
    foreach(PP pp, all_path_pairs()) {
        Path m = pp.first;
        Path n = pp.second;
        compute_path_pair_intersections(m, n);
    }
    assert(intersections.size() == size_t(p * (q - 1)));
}

std::list<std::pair<TurksHead::Path, TurksHead::Path> > TurksHead::all_path_pairs() const {
    std::list<std::pair<Path, Path> > allPairs;
    for(Path m(0); m != d; ++m) {
        for(Path n(m); n != d; ++n) {
            allPairs.push_back(std::make_pair(m, n));
        }
    }
    return allPairs;
}

void TurksHead::compute_path_pair_intersections(Path m, Path n) {
    int m_plus_n = m.index() + n.index();

    int alpha = -m_plus_n;
    int beta = 2 * p * q / d - m_plus_n;

    int minA = std::ceil(-1. * q / d);
    int maxA = std::ceil(1. * q / d);

    int minB = std::ceil(-1. * m_plus_n / q);
    int maxB = std::ceil(2. * p / d - m_plus_n / q);

    if(m == n) {
        minA = 1;
    }

    for(int a = minA; a < maxA; ++a) {
        for(int b = minB; b < maxB; ++b) {
            /// @todo Rework the inequalities on a and b, so that this test can be avoided
            /// And the loop on a, b will be logicaly cleaner and more significant (and maybe faster)
            if(alpha <= a * p + b * q && a * p + b * q < beta && alpha <= -a * p + b * q && -a * p + b * q < beta) {
                add_intersection(m, n, a, b);
            }
        }
    }
}

void TurksHead::add_intersection(Path m, Path n, int a, int b) {
    Theta theta_on_path_n((a * p + b * q + m.index() + n.index()) * theta_steps);
    Theta theta_on_path_m(theta_on_path_n - 2 * a * p * theta_steps);

    intersections.push_back(Intersection(m, theta_on_path_m, n, theta_on_path_n));
}

void TurksHead::compute_known_altitudes() {
    std::map<Path, std::set<Theta> > known_thetas;
    foreach(Intersection intersection, intersections) {
        known_thetas[intersection.m].insert(intersection.theta_on_path_m);
        known_thetas[intersection.n].insert(intersection.theta_on_path_n);
    }
    int alt = 1;
    foreach(Theta theta, known_thetas[Path(0)]) {
        known_altitudes[Path(0)][theta] = alt;
        alt *= -1;
    }
    /// @todo Remove this loop, by making known_altitudes a std::map<int, int> in stead of a std::vector<std::map<int, int> >
    /// And perform the rotation in get_altitude
    for(Path k(1); k != d; ++k) {
        foreach(Theta theta, known_thetas[k]) {
            Theta rotatedTheta((theta - phi(k) + max_theta_on_path) % max_theta_on_path);
            assert(known_altitudes[Path(0)].find(rotatedTheta) != known_altitudes[Path(0)].end());
            known_altitudes[k][theta] = known_altitudes[Path(0)][rotatedTheta];
        }
    }
}

void TurksHead::draw(Cairo::RefPtr<Cairo::Context> ctx_) const {
    setup_drawing(ctx_);
    draw_all_paths();
    redraw_all_intersections();
    teardown_drawing();
}

void TurksHead::setup_drawing(Cairo::RefPtr< Cairo::Context > ctx_) const {
    ctx = ctx_;
    ctx->save();
    ctx->set_antialias(Cairo::ANTIALIAS_NONE);
}

void TurksHead::teardown_drawing() const {
    ctx->restore();
    ctx.clear();
}

void TurksHead::draw_all_paths() const {
    for(Path k(0); k < d; ++k) {
        draw_path(k);
    }
}

void TurksHead::draw_path(Path k) const {
    draw_segment(k, Theta(0), max_theta_on_path);
}

void TurksHead::draw_segment(Path k, Theta min_theta, Theta max_theta) const {
    for(Theta theta = min_theta; theta <= max_theta; ++theta) {
        draw_step(k, theta);
    }
}

void TurksHead::draw_step(Path k, Theta theta) const {
    path_segment(k, theta, theta + 1);
    /// @todo Use a callback function given by the user to choose the color. Even better, this function could draw a portion of rope.
    set_source(k, theta);
    ctx->fill();
}

void TurksHead::set_source(Path k, Theta theta) const {
    set_source_hsv(compute_color_hsv(k.index(), theta.index()));
}

boost::tuple<double, double, double> TurksHead::compute_color_hsv(int k, int theta) const {
    return boost::make_tuple(k * 360. / d, 0.5, 0.5 + get_altitude(Path(k), Theta(theta)) / 2);
}

void TurksHead::path_segment(Path k, Theta min_theta, Theta max_theta) const {
    move_to(get_outer_coordinates(k, min_theta));
    for(Theta theta(min_theta + 1); theta <= max_theta; ++theta) {
        line_to(get_outer_coordinates(k, theta));
    }
    for(Theta theta = max_theta; theta >= min_theta; --theta) {
        line_to(get_inner_coordinates(k, theta));
    }
    ctx->close_path();
}

void TurksHead::redraw_all_intersections() const {
    foreach(Intersection intersection, intersections) {
        redraw_intersection(intersection);
    }
}

void TurksHead::redraw_intersection(const Intersection& intersection) const {
    if(get_altitude(intersection.m, intersection.theta_on_path_m) > get_altitude(intersection.n, intersection.theta_on_path_n)) {
        clip_region(intersection.n, intersection.theta_on_path_n);
        redraw_region(intersection.m, intersection.theta_on_path_m);
    /// @todo Understand why the next bloc is useless. Explain in the documentation article.
    /*} else {
        clip_region(intersection.m, intersection.theta_on_path_m);
        redraw_region(intersection.n, intersection.theta_on_path_n);*/
    }
    ctx->reset_clip();
}

boost::tuple< double, double > TurksHead::get_outer_coordinates(Path k, Theta theta) const {
    double x, y; boost::tie(x, y) = get_coordinates(k, theta);
    double nx, ny; boost::tie(nx, ny) = get_normal(k, theta);
    return boost::make_tuple(x + nx, y + ny);
}

boost::tuple< double, double > TurksHead::get_inner_coordinates(Path k, Theta theta) const {
    double x, y; boost::tie(x, y) = get_coordinates(k, theta);
    double nx, ny; boost::tie(nx, ny) = get_normal(k, theta);
    return boost::make_tuple(x - nx, y - ny);
}

boost::tuple< double, double > TurksHead::get_normal(Path k, Theta theta) const {
    double x0, y0; boost::tie(x0, y0) = get_coordinates(k, theta - 1);
    double x1, y1; boost::tie(x1, y1) = get_coordinates(k, theta + 1);

    double dx = x1 - x0;
    double dy = y1 - y0;
    double n = std::sqrt(dx * dx + dy * dy);

    double nx = -line_width * dy / n / 2;
    double ny = line_width * dx / n / 2;

    return boost::make_tuple(nx, ny);
}

boost::tuple< double, double > TurksHead::get_coordinates(Path k, Theta theta) const {
    return convert_radial_to_cartesian_coordinates(get_radius(k, theta), theta);
}

double TurksHead::get_radius(Path k, Theta theta) const {
    return radius + delta_radius * cos(p * angle_from_theta(theta - phi(k)) / q);
}

double TurksHead::angle_from_theta(Theta theta) const {
    return M_PI * theta.index() / p / theta_steps;
}

TurksHead::Theta TurksHead::phi(Path k) const {
    return Theta(2 * k.index() * theta_steps);
}

boost::tuple< double, double > TurksHead::convert_radial_to_cartesian_coordinates(double radius_, Theta theta) const {
    return boost::make_tuple(
        radius_ * std::cos(angle_from_theta(theta)),
        radius_ * std::sin(angle_from_theta(theta))
   );
}

void TurksHead::move_to(const boost::tuple< double, double >& p) const {
    ctx->move_to(p.get< 0 >(), p.get< 1 >());
}

void TurksHead::line_to(const boost::tuple< double, double >& p) const {
    ctx->line_to(p.get< 0 >(), p.get< 1 >());
}

void TurksHead::set_source_hsv(boost::tuple< double, double, double > hsv) const {
    set_source_hsv(hsv.get< 0 >(), hsv.get< 1 >(), hsv.get< 2 >());
}

void TurksHead::set_source_hsv(double h, double s, double v) const {
    int hi = h / 60;
    double f = h / 60 - hi;
    hi %= 60;
    double p = v * (1 - s);
    double q = v * (1 - f * s);
    double t = v * (1 - (1 - f) * s);
    switch(hi) {
        case 0: return ctx->set_source_rgb(v, t, p);
        case 1: return ctx->set_source_rgb(q, v, p);
        case 2: return ctx->set_source_rgb(p, v, t);
        case 3: return ctx->set_source_rgb(p, q, v);
        case 4: return ctx->set_source_rgb(t, p, v);
        case 5: return ctx->set_source_rgb(v, p, q);
    }
}

void TurksHead::clip_region(Path k, Theta theta) const {
    clip_segment(k, get_prev_redraw_limit(k, theta), get_next_redraw_limit(k, theta));
}

void TurksHead::clip_segment(Path k, Theta min_theta, Theta max_theta) const {
    path_segment(k, min_theta, max_theta);
    ctx->clip();
}

void TurksHead::redraw_region(Path k, Theta theta) const {
    draw_segment(k, get_prev_redraw_limit(k, theta), get_next_redraw_limit(k, theta));
}

TurksHead::Theta TurksHead::get_prev_redraw_limit(Path k, Theta theta) const {
    if(p < 3 || q < 3) {
        return (theta + get_prev_known_altitude(k, theta - 1).first) / 2;
    } else {
        return get_prev_known_altitude(k, theta - 1).first;
    }
}

TurksHead::Theta TurksHead::get_next_redraw_limit(Path k, Theta theta) const {
    if(p < 3 || q < 3) {
        return (theta + get_next_known_altitude(k, theta + 1).first) / 2;
    } else {
        return get_next_known_altitude(k, theta + 1).first;
    }
}

std::pair< TurksHead::Theta, double > TurksHead::get_prev_known_altitude(Path k, Theta theta) const {
    assert(known_altitudes.find(k) != known_altitudes.end());
    assert(!known_altitudes.find(k)->second.empty());

    const std::map< Theta, double >& knownAltitudes = known_altitudes.find(k)->second;

    std::map< Theta, double >::const_iterator nextIt = knownAltitudes.lower_bound(theta);

    if(nextIt == knownAltitudes.begin()) {
        std::pair< Theta, double > prev = *knownAltitudes.rbegin();
        prev.first -= max_theta_on_path;
        return prev;
    } else if(nextIt == knownAltitudes.end()) {
        return *knownAltitudes.rbegin();
    } else {
        return *boost::prior(nextIt);
    }
}

std::pair< TurksHead::Theta, double > TurksHead::get_next_known_altitude(Path k, Theta theta) const {
    assert(known_altitudes.find(k) != known_altitudes.end());
    assert(!known_altitudes.find(k)->second.empty());

    const std::map< Theta, double >& knownAltitudes = known_altitudes.find(k)->second;

    std::map< Theta, double >::const_iterator nextIt = knownAltitudes.lower_bound(theta);

    if(nextIt == knownAltitudes.begin()) {
        return *nextIt;
    } else if(nextIt == knownAltitudes.end()) {
        std::pair< Theta, double > next = *knownAltitudes.begin();
        next.first += max_theta_on_path;
        return next;
    } else {
        return *nextIt;
    }
}

double TurksHead::get_altitude(Path k, Theta theta) const {
    if(known_altitudes.find(k) == known_altitudes.end() ||
        known_altitudes.find(k)->second.empty()) {

        return 0;
    }

    std::pair< Theta, double > prev = get_prev_known_altitude(k, theta);
    std::pair< Theta, double > next = get_next_known_altitude(k, theta);

    return prev.second + (next.second - prev.second) * (theta - prev.first).index() / (next.first - prev.first).index();
}

int TurksHead::get_p() const {
    return p;
}

int TurksHead::get_q() const {
    return q;
}

int TurksHead::get_d() const {
    return d;
}

} // Namespace
