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
    p( bights ),
    q( leads ),
    d( boost::math::gcd( p, q ) ),
    m_thetaSteps( 100 ),
    m_maxThetaOnPath( 2 * q * p * m_thetaSteps / d ),
    m_radius( ( innerRadius + outerRadius ) / 2 ),
    m_deltaRadius( ( outerRadius - innerRadius - lineWidth ) / 2 ),
    m_lineWidth( lineWidth )
{
    computeCrossingThetas();
    computeKnownAltitudes();
}

void TurksHead::computeCrossingThetas() {
    for( int a = 1; a < q; ++a ) {
        for( int b = std::ceil( float( a ) * p / q ); b <= ( 2 - float( a ) / q ) * p; ++b ) {
            int theta1 = ( q * b - a * p ) * m_thetaSteps;
            int theta2 = ( q * b + a * p ) * m_thetaSteps;
            m_crossingThetas[ theta1 ] = theta2;
            m_crossingThetas[ theta2 ] = theta1;
        }
    }
}

void TurksHead::computeKnownAltitudes() {
    if( m_crossingThetas.empty() ) {
        m_knownAltitudes[ -m_thetaSteps ] = 1;
        m_knownAltitudes[ ( 2 * q * p + 1 ) * m_thetaSteps ] = 1;
    } else {
        m_knownAltitudes[ -m_thetaSteps ] = 1;
        int alt = -1;
        typedef std::pair< int, int > Pii;
        foreach( Pii p, m_crossingThetas ) {
            m_knownAltitudes[ p.first ] = alt;
            alt *= -1;
        }
        m_knownAltitudes[ ( 2 * q * p + 1 ) * m_thetaSteps ] = alt;
    }
}

void TurksHead::draw( Cairo::RefPtr< Cairo::Context > context ) const {
    m_ctx = context;
    m_ctx->save();
    m_ctx->set_antialias( Cairo::ANTIALIAS_NONE );

    drawPaths();

    m_ctx->restore();
}

void TurksHead::drawPaths() const {
    for( int path = 0; path < d; ++path ) {
        drawPath( path );
    }
}

void TurksHead::drawPath( int path ) const {
    for( int theta = 0; theta <= m_maxThetaOnPath; ++theta ) {
        drawSegment( path, theta );
    }
    /*typedef std::pair< int, int > Pii;
    foreach( Pii p, m_crossingThetas ) {
        assert( m_knownAltitudes.find( p.first ) != m_knownAltitudes.end() );
        if( m_knownAltitudes.find( p.first )->second == -1 ) {
            redraw( p.first, p.second );
        } else {
            redraw( p.second, p.first );
        }
    }*/
}

void TurksHead::drawSegment( int path, int theta ) const {
    pathSegment( path, theta - 1, theta + 1 );
    //setSourceHsv( theta * 360. / m_maxThetaOnPath, 0.5, 0.5 + getAltitude( theta ) / 2 );
    setSourceHsv( path * 360. / d, 0.5, 0.8 );
    m_ctx->fill();
}

void TurksHead::pathSegment( int path, int minTheta, int maxTheta ) const {
    moveTo( getOuterCoordinates( path, minTheta ) );
    for( int theta = minTheta + 1; theta <= maxTheta; ++theta ) {
        lineTo( getOuterCoordinates( path, theta ) );
    }
    for( int theta = maxTheta; theta >= minTheta; --theta ) {
        lineTo( getInnerCoordinates( path, theta ) );
    }
    m_ctx->close_path();
}

boost::tuple< double, double > TurksHead::getOuterCoordinates( int path, int theta ) const {
    double x, y; boost::tie( x, y ) = getCoordinates( path, theta );
    double nx, ny; boost::tie( nx, ny ) = getNormal( path, theta );
    return boost::make_tuple( x + nx, y + ny );
}

boost::tuple< double, double > TurksHead::getInnerCoordinates( int path, int theta ) const {
    double x, y; boost::tie( x, y ) = getCoordinates( path, theta );
    double nx, ny; boost::tie( nx, ny ) = getNormal( path, theta );
    return boost::make_tuple( x - nx, y - ny );
}

boost::tuple< double, double > TurksHead::getNormal( int path, int theta ) const {
    double x0, y0; boost::tie( x0, y0 ) = getCoordinates( path, theta - 1 );
    double x1, y1; boost::tie( x1, y1 ) = getCoordinates( path, theta + 1 );

    double dx = x1 - x0;
    double dy = y1 - y0;
    double n = std::sqrt( dx * dx + dy * dy );

    double nx = -m_lineWidth * dy / n / 2;
    double ny = m_lineWidth * dx / n / 2;

    return boost::make_tuple( nx, ny );
}

boost::tuple< double, double > TurksHead::getCoordinates( int path, int theta ) const {
    return convertRadialToCartesianCoordinates( getRadius( path, theta ), theta );
}

double TurksHead::getRadius( int path, int theta ) const {
    return m_radius + m_deltaRadius * cos( p * angleFromTheta( theta + phi( path ) ) / q );
}

double TurksHead::angleFromTheta( int theta ) const {
    return M_PI * theta / p / m_thetaSteps;
}

int TurksHead::phi( int path ) const {
    return 2 * path * m_thetaSteps;
}

boost::tuple< double, double > TurksHead::convertRadialToCartesianCoordinates( double radius, int theta ) const {
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

/*void TurksHead::redraw( int thetaLow, int thetaHight ) const {
    m_ctx->save();
    clip( thetaLow );

    std::map< int, int >::const_iterator it = m_knownAltitudes.find( thetaHight );
    assert( it != m_knownAltitudes.begin() );
    assert( it != m_knownAltitudes.end() );
    assert( boost::next( it ) != m_knownAltitudes.end() );

    int minTheta = getPreviousCheckPoint( it );
    int maxTheta = getNextCheckPoint( it );
    for( int theta = minTheta; theta <= maxTheta; ++theta ) {
        // Draw several times the same thing, to fight the antialiasing
        //drawSegment( theta );
        drawSegment( theta );
        drawSegment( theta );
    }
    m_ctx->restore();
}

int TurksHead::getPreviousCheckPoint( std::map< int, int >::const_iterator it ) const {
    if( q < 3 ) {
        return ( boost::prior( it )->first + it->first ) / 2;
    } else if( p < 3 ) {
        return ( boost::prior( it )->first + it->first ) / 2; /// @todo Rework...
    } else {
        return boost::prior( it )->first + 1;
    }
}

int TurksHead::getNextCheckPoint( std::map< int, int >::const_iterator it ) const {
    if( q < 3 ) {
        return ( boost::next( it )->first + it->first ) / 2;
    } else if( p < 3 ) {
        return ( boost::next( it )->first + it->first ) / 2; /// @todo Rework...
    } else {
        return boost::next( it )->first - 1;
    }
}

void TurksHead::clip( int thetaLow ) const {
    std::map< int, int >::const_iterator it = m_knownAltitudes.find( thetaLow );
    assert( it != m_knownAltitudes.begin() );
    assert( it != m_knownAltitudes.end() );
    assert( boost::next( it ) != m_knownAltitudes.end() );

    pathSegment( getPreviousCheckPoint( it ), getNextCheckPoint( it ) );
    m_ctx->clip();
}*/

double TurksHead::getAltitude( int theta ) const {
    std::map< int, int >::const_iterator nextIt = m_knownAltitudes.lower_bound( theta );
    assert( nextIt != m_knownAltitudes.begin() );
    assert( nextIt != m_knownAltitudes.end() );
    std::map< int, int >::const_iterator prevIt = boost::prior( nextIt );
    return prevIt->second + ( nextIt->second - prevIt->second ) * ( theta - prevIt->first ) / float( nextIt->first - prevIt->first );
}

} // Namespace
