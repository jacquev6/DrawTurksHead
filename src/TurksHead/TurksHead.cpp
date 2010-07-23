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

TurksHead::TurksHead( int leads, int bights, double innerRadius, double outerRadius, double lineWidth ) :
    m_leads( leads ),
    m_bights( bights ),
    m_paths( boost::math::gcd( m_bights, m_leads ) ),
    m_maxThetaOnPath( 2 * m_leads * m_bights * s_stepsTheta / m_paths ),
    m_radius( ( innerRadius + outerRadius ) / 2 ),
    m_deltaRadius( ( outerRadius - innerRadius - lineWidth ) / 2 ),
    m_lineWidth( lineWidth )
{
    computeCrossingThetas();
    computeKnownAltitudes();
}

const int TurksHead::s_stepsTheta = 100;

void TurksHead::draw( Cairo::RefPtr< Cairo::Context > context ) const {
    m_ctx = context;
    m_ctx->save();
    m_ctx->set_antialias( Cairo::ANTIALIAS_NONE );

    drawPaths();

    m_ctx->restore();
}

void TurksHead::drawPaths() const {
    for( int path = 0; path < m_paths; ++path ) {
        drawPath( path );
        m_ctx->rotate( 2 * M_PI / m_paths );
    }
}

void TurksHead::drawPath( int path ) const {
    for( int theta = 0; theta <= m_maxThetaOnPath; ++theta ) {
        drawSegment( theta );
    }
    typedef std::pair< int, int > Pii;
    foreach( Pii p, m_crossingThetas ) {
        assert( m_knownAltitudes.find( p.first ) != m_knownAltitudes.end() );
        if( m_knownAltitudes.find( p.first )->second == -1 ) {
            redraw( p.first, p.second );
        } else {
            redraw( p.second, p.first );
        }
    }
}

void TurksHead::drawSegment( int theta ) const {
    moveTo( getOuterCoordinates( theta - 1 ) );
    lineTo( getOuterCoordinates( theta ) );
    lineTo( getOuterCoordinates( theta + 1 ) );
    lineTo( getInnerCoordinates( theta + 1 ) );
    lineTo( getInnerCoordinates( theta ) );
    lineTo( getInnerCoordinates( theta - 1) );
    double z = getAltitude( theta );
    setSourceHsv( theta * 360. / m_maxThetaOnPath, 0.5, 0.5 + z / 2 );
    m_ctx->fill();
}

void TurksHead::redraw( int thetaLow, int thetaHight ) const {
    m_ctx->save();
    clip( thetaLow );

    std::map< int, int >::const_iterator it = m_knownAltitudes.find( thetaHight );
    assert( it != m_knownAltitudes.begin() );
    assert( it != m_knownAltitudes.end() );
    assert( boost::next( it ) != m_knownAltitudes.end() );

    int minTheta = boost::prior( it )->first + 1;
    int maxTheta = boost::next( it )->first - 1;
    for( int theta = minTheta; theta <= maxTheta; ++theta ) {
        // Draw several times the same thing, to fight the antialiasing
        //drawSegment( theta );
        //drawSegment( theta );
        drawSegment( theta );
    }
    m_ctx->restore();
}

void TurksHead::clip( int thetaLow ) const {
    std::map< int, int >::const_iterator it = m_knownAltitudes.find( thetaLow );
    assert( it != m_knownAltitudes.begin() );
    assert( it != m_knownAltitudes.end() );
    assert( boost::next( it ) != m_knownAltitudes.end() );

    int minTheta = boost::prior( it )->first;
    int maxTheta = boost::next( it )->first;
    moveTo( getOuterCoordinates( minTheta ) );
    for( int theta = minTheta + 1; theta <= maxTheta; ++theta ) {
        lineTo( getOuterCoordinates( theta ) );
    }
    for( int theta = maxTheta; theta >= minTheta; --theta ) {
        lineTo( getInnerCoordinates( theta ) );
    }
    m_ctx->clip();
}

double TurksHead::getAltitude( int theta ) const {
    std::map< int, int >::const_iterator nextIt = m_knownAltitudes.lower_bound( theta );
    assert( nextIt != m_knownAltitudes.begin() );
    assert( nextIt != m_knownAltitudes.end() );
    std::map< int, int >::const_iterator prevIt = boost::prior( nextIt );
    return prevIt->second + ( nextIt->second - prevIt->second ) * ( theta - prevIt->first ) / float( nextIt->first - prevIt->first );
}

void TurksHead::computeCrossingThetas() {
    for( int a = 1; a < m_leads; ++a ) {
        for( int b = std::ceil( float( a ) * m_bights / m_leads ); b <= ( 2 - float( a ) / m_leads ) * m_bights; ++b ) {
            int theta1 = ( m_leads * b - a * m_bights ) * s_stepsTheta;
            int theta2 = ( m_leads * b + a * m_bights ) * s_stepsTheta;
            m_crossingThetas[ theta1 ] = theta2;
            m_crossingThetas[ theta2 ] = theta1;
        }
    }
}

void TurksHead::computeKnownAltitudes() {
    m_knownAltitudes[ -s_stepsTheta ] = -1;
    int alt = 1;
    typedef std::pair< int, int > Pii;
    foreach( Pii p, m_crossingThetas ) {
        m_knownAltitudes[ p.first ] = alt;
        alt *= -1;
    }
    m_knownAltitudes[ ( 2 * m_leads * m_bights + 1 ) * s_stepsTheta ] = alt;
}

boost::tuple< double, double > TurksHead::getOuterCoordinates( int theta ) const {
    double x0, y0; boost::tie( x0, y0 ) = getCoordinates( theta - 1 );
    double x1, y1; boost::tie( x1, y1 ) = getCoordinates( theta );
    double x2, y2; boost::tie( x2, y2 ) = getCoordinates( theta + 1 );

    double dx = x1 - x0;
    double dy = y1 - y0;
    double n = std::sqrt( dx * dx + dy * dy );

    double nx = -m_lineWidth * dy / n / 2;
    double ny = m_lineWidth * dx / n / 2;

    return boost::make_tuple( x1 + nx, y1 + ny );
}

boost::tuple< double, double > TurksHead::getInnerCoordinates( int theta ) const {
    double x0, y0; boost::tie( x0, y0 ) = getCoordinates( theta - 1 );
    double x1, y1; boost::tie( x1, y1 ) = getCoordinates( theta );
    double x2, y2; boost::tie( x2, y2 ) = getCoordinates( theta + 1 );

    double dx = x1 - x0;
    double dy = y1 - y0;
    double n = std::sqrt( dx * dx + dy * dy );

    double nx = -m_lineWidth * dy / n / 2;
    double ny = m_lineWidth * dx / n / 2;

    return boost::make_tuple( x1 - nx, y1 - ny );
}

boost::tuple< double, double > TurksHead::getCoordinates( int theta ) const {
    return convertRadialToCartesianCoordinates( getRadius( theta ), theta );
}

double TurksHead::getRadius( int theta ) const {
    return m_radius + m_deltaRadius * cos( m_bights * angleFromTheta( theta ) / m_leads );
}

boost::tuple< double, double > TurksHead::convertRadialToCartesianCoordinates( double radius, int theta ) const {
    return boost::make_tuple(
        radius * std::cos( angleFromTheta( theta ) ),
        radius * std::sin( angleFromTheta( theta ) )
    );
}

double TurksHead::angleFromTheta( int theta ) const {
    return M_PI * theta / m_bights / s_stepsTheta;
}

void TurksHead::moveTo( const boost::tuple< double, double >& p ) const {
    m_ctx->move_to( p.get< 0 >(), p.get< 1 >() );
}

void TurksHead::lineTo( const boost::tuple< double, double >& p ) const {
    m_ctx->line_to( p.get< 0 >(), p.get< 1 >() );
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

} // Namespace
