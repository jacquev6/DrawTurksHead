/*************************** Copyrights and license ***************************\
*                                                                              *
* Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 *
*                                                                              *
* This file is part of DrawTurksHead. http://jacquev6.github.com/DrawTurksHead *
*                                                                              *
* DrawTurksHead is free software: you can redistribute it and/or modify it     *
* under the terms of the GNU Lesser General Public License as published by the *
* Free Software Foundation, either version 3 of the License, or (at your       *
* option) any later version.                                                   *
*                                                                              *
* DrawTurksHead is distributed in the hope that it will be useful, but WITHOUT *
* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        *
* FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License  *
* for more details.                                                            *
*                                                                              *
* You should have received a copy of the GNU Lesser General Public License     *
* along with DrawTurksHead. If not, see <http://www.gnu.org/licenses/>.        *
*                                                                              *
\******************************************************************************/

// Header
#include "TurksHead.hpp"

// Standard library
#include <cmath>
#include <map>
#include <cassert>

// Boost
#include <boost/math/common_factor.hpp>
#include <boost/utility.hpp>
#include <boost/lambda/lambda.hpp>
#include <boost/foreach.hpp>
#include <boost/utility.hpp>

#define foreach BOOST_FOREACH

namespace TurksHead {

TurksHead::Intersection::Intersection( Path m_, Theta thetaOnPathM_, Path n_, Theta thetaOnPathN_ ) :
    m( m_ ),
    thetaOnPathM( thetaOnPathM_ ),
    n( n_ ),
    thetaOnPathN( thetaOnPathN_ )
{
}

TurksHead::Segment::Segment( Theta min, Theta max ) :
    minTheta( min ),
    maxTheta( max )
{
}

TurksHead::~TurksHead() {
}

TurksHead::TurksHead( int leads, int bights, double innerRadius, double outerRadius, double lineWidth ) :
    p( bights ),
    q( leads ),
    d( boost::math::gcd( p, q ) ),
    m_thetaSteps( 100 ),
    m_maxThetaOnPath( 2 * q * p * m_thetaSteps / d ),
    m_radius( ( innerRadius + outerRadius ) / 2 ),
    m_deltaRadius( ( outerRadius - innerRadius - lineWidth ) / 2 ),
    m_lineWidth( lineWidth )
{
    computeIntersections();
    computeKnownAltitudes();
}

void TurksHead::computeIntersections() {
    typedef std::pair< Path, Path > Pii;
    foreach( Pii p, allPathPairs() ) {
        Path m = p.first;
        Path n = p.second;
        computePathPairIntersections( m, n );
    }
    assert( m_intersections.size() == size_t( p * ( q - 1 ) ) );
}

std::list< std::pair< TurksHead::Path, TurksHead::Path > > TurksHead::allPathPairs() const {
    std::list< std::pair< Path, Path > > allPairs;
    for( Path m( 0 ); m != d; ++m ) {
        for( Path n( m ); n != d; ++n ) {
            allPairs.push_back( std::make_pair( m, n ) );
        }
    }
    return allPairs;
}

void TurksHead::computePathPairIntersections( Path m, Path n ) {
    int m_plus_n = m.index() + n.index();

    int alpha = -m_plus_n;
    int beta = 2 * p * q / d - m_plus_n;

    int minA = std::ceil( -1. * q / d );
    int maxA = std::ceil( 1. * q / d );

    int minB = std::ceil( -1. * m_plus_n / q );
    int maxB = std::ceil( 2. * p / d - m_plus_n / q );

    if( m == n ) {
        minA = 1;
    }

    for( int a = minA; a < maxA; ++a ) {
        for( int b = minB; b < maxB; ++b ) {
            /// @todo Rework the inequalities on a and b, so that this test can be avoided
            /// And the loop on a, b will be logicaly cleaner and more significant (and maybe faster)
            if( alpha <= a * p + b * q && a * p + b * q < beta && alpha <= -a * p + b * q && -a * p + b * q < beta ) {
                addIntersection( m, n, a, b );
            }
        }
    }
}

void TurksHead::addIntersection( Path m, Path n, int a, int b ) {
    Theta thetaOnPathN( ( a * p + b * q + m.index() + n.index() ) * m_thetaSteps );
    Theta thetaOnPathM( thetaOnPathN - 2 * a * p * m_thetaSteps );

    m_intersections.push_back( Intersection( m, thetaOnPathM, n, thetaOnPathN ) );
}

void TurksHead::computeKnownAltitudes() {
    std::map< Path, std::set< Theta > > knownThetas;
    foreach( Intersection intersection, m_intersections ) {
        knownThetas[ intersection.m ].insert( intersection.thetaOnPathM );
        knownThetas[ intersection.n ].insert( intersection.thetaOnPathN );
    }
    int alt = 1;
    foreach( Theta theta, knownThetas[ Path( 0 ) ] ) {
        m_knownAltitudes[ Path( 0 ) ][ theta ] = alt;
        alt *= -1;
    }
    /// @todo Remove this loop, by making m_knownAltitudes a std::map< int, int > in stead of a std::vector< std::map< int, int > >
    /// And perform the rotation in getAltitude
    for( Path k( 1 ); k != d; ++k ) {
        foreach( Theta theta, knownThetas[ k ] ) {
            Theta rotatedTheta( ( theta - phi( k ) + m_maxThetaOnPath ) % m_maxThetaOnPath );
            assert( m_knownAltitudes[ Path( 0 ) ].find( rotatedTheta ) != m_knownAltitudes[ Path( 0 ) ].end() );
            m_knownAltitudes[ k ][ theta ] = m_knownAltitudes[ Path( 0 ) ][ rotatedTheta ];
        }
    }
}

void TurksHead::draw( Cairo::RefPtr< Cairo::Context > context ) const {
    setupDrawing( context );
    drawAllPaths();
    redrawAllIntersections();
    teardownDrawing();
}

void TurksHead::setupDrawing( Cairo::RefPtr< Cairo::Context > context ) const {
    m_ctx = context;
    m_ctx->save();
    m_ctx->set_antialias( Cairo::ANTIALIAS_NONE );
}

void TurksHead::teardownDrawing() const {
    m_ctx->restore();
    m_ctx.clear();
}

void TurksHead::drawAllPaths() const {
    for( Path k( 0 ); k < d; ++k ) {
        draw( k );
    }
}

void TurksHead::draw( Path k ) const {
    drawSegment( k, Theta( 0 ), m_maxThetaOnPath );
}

void TurksHead::drawSegment( Path k, Theta minTheta, Theta maxTheta ) const {
    for( Theta theta = minTheta; theta <= maxTheta; ++theta ) {
        drawStep( k, theta );
    }
}

void TurksHead::drawStep( Path k, Theta theta ) const {
    pathSegment( k, theta, theta + 1 );
    /// @todo Use a callback function given by the user to choose the color. Even better, this function could draw a portion of rope.
    setSource( k, theta );
    m_ctx->fill();
}

void TurksHead::setSource( Path k, Theta theta ) const {
    setSourceHsv( computeColorHsv( k.index(), theta.index() ) );
}

boost::tuple< double, double, double > TurksHead::computeColorHsv( int k, int theta ) const {
    return boost::make_tuple( k * 360. / d, 0.5, 0.5 + getAltitude( Path( k ), Theta( theta ) ) / 2 );
}

void TurksHead::pathSegment( Path k, Theta minTheta, Theta maxTheta ) const {
    moveTo( getOuterCoordinates( k, minTheta ) );
    for( Theta theta( minTheta + 1 ); theta <= maxTheta; ++theta ) {
        lineTo( getOuterCoordinates( k, theta ) );
    }
    for( Theta theta = maxTheta; theta >= minTheta; --theta ) {
        lineTo( getInnerCoordinates( k, theta ) );
    }
    m_ctx->close_path();
}

void TurksHead::redrawAllIntersections() const {
    foreach( Intersection intersection, m_intersections ) {
        redrawIntersection( intersection );
    }
}

void TurksHead::redrawIntersection( const Intersection& intersection ) const {
    if( getAltitude( intersection.m, intersection.thetaOnPathM ) > getAltitude( intersection.n, intersection.thetaOnPathN ) ) {
        clipRegion( intersection.n, intersection.thetaOnPathN );
        redrawRegion( intersection.m, intersection.thetaOnPathM );
    /// @todo Understand why the next bloc is useless. Explain in the documentation article.
    /*} else {
        clipRegion( intersection.m, intersection.thetaOnPathM );
        redrawRegion( intersection.n, intersection.thetaOnPathN );*/
    }
    m_ctx->reset_clip();
}

boost::tuple< double, double > TurksHead::getOuterCoordinates( Path k, Theta theta ) const {
    double x, y; boost::tie( x, y ) = getCoordinates( k, theta );
    double nx, ny; boost::tie( nx, ny ) = getNormal( k, theta );
    return boost::make_tuple( x + nx, y + ny );
}

boost::tuple< double, double > TurksHead::getInnerCoordinates( Path k, Theta theta ) const {
    double x, y; boost::tie( x, y ) = getCoordinates( k, theta );
    double nx, ny; boost::tie( nx, ny ) = getNormal( k, theta );
    return boost::make_tuple( x - nx, y - ny );
}

boost::tuple< double, double > TurksHead::getNormal( Path k, Theta theta ) const {
    double x0, y0; boost::tie( x0, y0 ) = getCoordinates( k, theta - 1 );
    double x1, y1; boost::tie( x1, y1 ) = getCoordinates( k, theta + 1 );

    double dx = x1 - x0;
    double dy = y1 - y0;
    double n = std::sqrt( dx * dx + dy * dy );

    double nx = -m_lineWidth * dy / n / 2;
    double ny = m_lineWidth * dx / n / 2;

    return boost::make_tuple( nx, ny );
}

boost::tuple< double, double > TurksHead::getCoordinates( Path k, Theta theta ) const {
    return convertRadialToCartesianCoordinates( getRadius( k, theta ), theta );
}

double TurksHead::getRadius( Path k, Theta theta ) const {
    return m_radius + m_deltaRadius * cos( p * angleFromTheta( theta - phi( k ) ) / q );
}

double TurksHead::angleFromTheta( Theta theta ) const {
    return M_PI * theta.index() / p / m_thetaSteps;
}

TurksHead::Theta TurksHead::phi( Path k ) const {
    return Theta( 2 * k.index() * m_thetaSteps );
}

boost::tuple< double, double > TurksHead::convertRadialToCartesianCoordinates( double radius, Theta theta ) const {
    return boost::make_tuple(
        radius * std::cos( angleFromTheta( theta ) ),
        radius * std::sin( angleFromTheta( theta ) )
    );
}

void TurksHead::moveTo( const boost::tuple< double, double >& p ) const {
    m_ctx->move_to( p.get< 0 >(), p.get< 1 >() );
}

void TurksHead::lineTo( const boost::tuple< double, double >& p ) const {
    m_ctx->line_to( p.get< 0 >(), p.get< 1 >() );
}

void TurksHead::setSourceHsv( boost::tuple< double, double, double > hsv ) const {
    setSourceHsv( hsv.get< 0 >(), hsv.get< 1 >(), hsv.get< 2 >() );
}

void TurksHead::setSourceHsv( double h, double s, double v ) const {
    int hi = h / 60;
    double f = h / 60 - hi;
    hi %= 60;
    double p = v * ( 1 - s );
    double q = v * ( 1 - f * s );
    double t = v * ( 1 - ( 1 - f ) * s );
    switch( hi ) {
        case 0: return m_ctx->set_source_rgb( v, t, p );
        case 1: return m_ctx->set_source_rgb( q, v, p );
        case 2: return m_ctx->set_source_rgb( p, v, t );
        case 3: return m_ctx->set_source_rgb( p, q, v );
        case 4: return m_ctx->set_source_rgb( t, p, v );
        case 5: return m_ctx->set_source_rgb( v, p, q );
    }
}

void TurksHead::clipSegment( Path k, Theta minTheta, Theta maxTheta ) const {
    pathSegment( k, minTheta, maxTheta );
    m_ctx->clip();
}

void TurksHead::clipRegion( Path k, Theta theta ) const {
    clipSegment( k, getPrevRedrawLimit( k, theta ), getNextRedrawLimit( k, theta ) );
}

void TurksHead::redrawRegion( Path k, Theta theta ) const {
    drawSegment( k, getPrevRedrawLimit( k, theta ), getNextRedrawLimit( k, theta ) );
}

TurksHead::Theta TurksHead::getPrevRedrawLimit( Path k, Theta theta ) const {
    if( p < 3 || q < 3 ) {
        return ( theta + getPrevKnownAltitude( k, theta - 1 ).first ) / 2;
    } else {
        return getPrevKnownAltitude( k, theta - 1 ).first;
    }
}

TurksHead::Theta TurksHead::getNextRedrawLimit( Path k, Theta theta ) const {
    if( p < 3 || q < 3 ) {
        return ( theta + getNextKnownAltitude( k, theta + 1 ).first ) / 2;
    } else {
        return getNextKnownAltitude( k, theta + 1 ).first;
    }
}

std::pair< TurksHead::Theta, double > TurksHead::getPrevKnownAltitude( Path k, Theta theta ) const {
    assert( m_knownAltitudes.find( k ) != m_knownAltitudes.end() );
    assert( !m_knownAltitudes.find( k )->second.empty() );

    const std::map< Theta, double >& knownAltitudes = m_knownAltitudes.find( k )->second;

    std::map< Theta, double >::const_iterator nextIt = knownAltitudes.lower_bound( theta );

    if( nextIt == knownAltitudes.begin() ) {
        std::pair< Theta, double > prev = *knownAltitudes.rbegin();
        prev.first -= m_maxThetaOnPath;
        return prev;
    } else if( nextIt == knownAltitudes.end() ) {
        return *knownAltitudes.rbegin();
    } else {
        return *boost::prior( nextIt );
    }
}

std::pair< TurksHead::Theta, double > TurksHead::getNextKnownAltitude( Path k, Theta theta ) const {
    assert( m_knownAltitudes.find( k ) != m_knownAltitudes.end() );
    assert( !m_knownAltitudes.find( k )->second.empty() );

    const std::map< Theta, double >& knownAltitudes = m_knownAltitudes.find( k )->second;

    std::map< Theta, double >::const_iterator nextIt = knownAltitudes.lower_bound( theta );

    if( nextIt == knownAltitudes.begin() ) {
        return *nextIt;
    } else if( nextIt == knownAltitudes.end() ) {
        std::pair< Theta, double > next = *knownAltitudes.begin();
        next.first += m_maxThetaOnPath;
        return next;
    } else {
        return *nextIt;
    }
}

double TurksHead::getAltitude( Path k, Theta theta ) const {
    if( m_knownAltitudes.find( k ) == m_knownAltitudes.end() ||
        m_knownAltitudes.find( k )->second.empty() ) {

        return 0;
    }

    std::pair< Theta, double > prev = getPrevKnownAltitude( k, theta );
    std::pair< Theta, double > next = getNextKnownAltitude( k, theta );

    return prev.second + ( next.second - prev.second ) * ( theta - prev.first ).index() / ( next.first - prev.first ).index();
}

int TurksHead::getP() const {
    return p;
}

int TurksHead::getQ() const {
    return q;
}

int TurksHead::getD() const {
    return d;
}

} // Namespace
