// Header
#include "TurksHead.hpp"

// Standard library
#include <cmath>
#include <map>
#include <cassert>
#include <iostream> /// @todo Remove

// Boost
#include <boost/math/common_factor.hpp>
#include <boost/utility.hpp>
#include <boost/lambda/lambda.hpp>
#include <boost/foreach.hpp>
#include <boost/utility.hpp>
#include <boost/lexical_cast.hpp> /// @todo Remove

#define foreach BOOST_FOREACH

namespace TurksHead {

TurksHead::TurksHead( int leads, int bights, double innerRadius, double outerRadius, double lineWidth ) :
    p( bights ),
    q( leads ),
    d( boost::math::gcd( p, q ) ),
    m_thetaSteps( 15 ),
    m_maxThetaOnPath( 2 * q * p * m_thetaSteps / d ),
    m_radius( ( innerRadius + outerRadius ) / 2 ),
    m_deltaRadius( ( outerRadius - innerRadius - lineWidth ) / 2 ),
    m_lineWidth( lineWidth )
{
    computeIntersections();
    computeKnownAltitudes();
}

void TurksHead::computeIntersections() {
    typedef std::pair< int, int > Pii;
    foreach( Pii p, allPathPairs() ) {
        int m = p.first;
        int n = p.second;
        computePathPairIntersections( m, n );
    }
    assert( m_intersections.size() == p * ( q - 1 ) );
}

std::list< std::pair< int, int > > TurksHead::allPathPairs() const {
    std::list< std::pair< int, int > > allPairs;
    for( int m = 0; m != d; ++m ) {
        for( int n = m; n != d; ++n ) {
            allPairs.push_back( std::make_pair( m, n ) );
        }
    }
    return allPairs;
}

void TurksHead::computePathPairIntersections( int m, int n ) {
    int alpha = -( m + n );
    int beta = 2 * p * q / d - ( m + n );

    int minA = std::ceil( -1. * q / d );
    int maxA = std::ceil( 1. * q / d );

    int minB = std::ceil( -1. * ( m + n ) / q );
    int maxB = std::ceil( 2. * p / d - ( m + n ) / q );

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

void TurksHead::addIntersection( int m, int n, int a, int b ) {
    Intersection intersection;
    intersection.m = m;
    intersection.n = n;
    intersection.thetaOnPathN = ( a * p + b * q + m + n ) * m_thetaSteps;
    intersection.thetaOnPathM = intersection.thetaOnPathN - 2 * a * p * m_thetaSteps;

    /*std::cout << "Intersection between paths " << m << " and " << n << ", "
        "with a == " << a << " and b == " << b << ": "
        "theta_1 == " << angleFromTheta( intersection.thetaOnPathN ) / M_PI << ", "
        "theta_2 == " << angleFromTheta( intersection.thetaOnPathM ) / M_PI << ", "
        << std::endl;*/

    m_intersections.push_back( intersection );
}

void TurksHead::computeKnownAltitudes() {
    std::vector< std::set< int > > knownThetas;
    knownThetas.resize( d );
    m_knownAltitudes.resize( d );
    foreach( Intersection intersection, m_intersections ) {
        knownThetas[ intersection.m ].insert( intersection.thetaOnPathM );
        knownThetas[ intersection.n ].insert( intersection.thetaOnPathN );
    }
    int alt = 1;
    foreach( int theta, knownThetas[ 0 ] ) {
        m_knownAltitudes[ 0 ][ theta ] = alt;
        alt *= -1;
    }
    /// @todo Remove this loop, by making m_knownAltitudes a std::map< int, int > in stead of a std::vector< std::map< int, int > >
    /// And perform the rotation in getAltitude
    for( int k = 1; k != d; ++k ) {
        foreach( int theta, knownThetas[ k ] ) {
            int rotatedTheta = ( theta - phi( k ) + m_maxThetaOnPath ) % m_maxThetaOnPath;
            assert( m_knownAltitudes[ 0 ].find( rotatedTheta ) != m_knownAltitudes[ 0 ].end() );
            m_knownAltitudes[ k ][ theta ] = m_knownAltitudes[ 0 ][ rotatedTheta ];
        }
    }
}

void TurksHead::draw( Cairo::RefPtr< Cairo::Context > context ) const {
    m_ctx = context;
    m_ctx->save();
    m_ctx->set_antialias( Cairo::ANTIALIAS_NONE );

    drawPaths();
    //drawPath( 0 );

    /*// Debug drawings to be removed

    m_ctx->set_source_rgb( 0, 0, 0 );
    m_ctx->set_line_width( 6 );
    m_ctx->set_line_cap( Cairo::LINE_CAP_ROUND );
    foreach( Intersection intersection, m_intersections ) {
        moveTo( getCoordinates( intersection.m, intersection.thetaOnPathM ) );
        lineTo( getCoordinates( intersection.n, intersection.thetaOnPathN ) );
    }
    m_ctx->stroke();

    m_ctx->set_source_rgb( 1, 0, 0 );
    m_ctx->set_font_size( 25 );
    for( int k = 0; k != d; ++k ) {
        typedef std::pair< int, int > Pii;
        foreach( Pii p, m_knownAltitudes[ k ] ) {
            moveTo( getCoordinates( k, p.first ) );
            m_ctx->rel_move_to( 0, 20 * k );
            m_ctx->show_text(
                boost::lexical_cast< std::string >( k ) + ": "
                + boost::lexical_cast< std::string >( p.first / m_thetaSteps ) + ": "
                + boost::lexical_cast< std::string >( p.second )
            );
        }
    }
    // End of debug drawings/**/

    m_ctx->restore();
}

void TurksHead::drawPaths() const {
    for( int k = 0; k < d; ++k ) {
        drawPath( k );
    }
}

void TurksHead::drawPath( int k ) const {
    for( int theta = 0; theta <= m_maxThetaOnPath; ++theta ) {
        drawSegment( k, theta );
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

void TurksHead::drawSegment( int k, int theta ) const {
    pathSegment( k, theta, theta + 1 );
    //setSourceHsv( theta * 360. / m_maxThetaOnPath, 0.5, 0.5 + getAltitude( theta ) / 2 );
    setSourceHsv( k * 360. / d, 0.5, 0.5 + getAltitude( k, theta ) / 2 );
    m_ctx->fill();
}

void TurksHead::pathSegment( int k, int minTheta, int maxTheta ) const {
    moveTo( getOuterCoordinates( k, minTheta ) );
    for( int theta = minTheta + 1; theta <= maxTheta; ++theta ) {
        lineTo( getOuterCoordinates( k, theta ) );
    }
    for( int theta = maxTheta; theta >= minTheta; --theta ) {
        lineTo( getInnerCoordinates( k, theta ) );
    }
    m_ctx->close_path();
}

boost::tuple< double, double > TurksHead::getOuterCoordinates( int k, int theta ) const {
    double x, y; boost::tie( x, y ) = getCoordinates( k, theta );
    double nx, ny; boost::tie( nx, ny ) = getNormal( k, theta );
    return boost::make_tuple( x + nx, y + ny );
}

boost::tuple< double, double > TurksHead::getInnerCoordinates( int k, int theta ) const {
    double x, y; boost::tie( x, y ) = getCoordinates( k, theta );
    double nx, ny; boost::tie( nx, ny ) = getNormal( k, theta );
    return boost::make_tuple( x - nx, y - ny );
}

boost::tuple< double, double > TurksHead::getNormal( int k, int theta ) const {
    double x0, y0; boost::tie( x0, y0 ) = getCoordinates( k, theta - 1 );
    double x1, y1; boost::tie( x1, y1 ) = getCoordinates( k, theta + 1 );

    double dx = x1 - x0;
    double dy = y1 - y0;
    double n = std::sqrt( dx * dx + dy * dy );

    double nx = -m_lineWidth * dy / n / 2;
    double ny = m_lineWidth * dx / n / 2;

    return boost::make_tuple( nx, ny );
}

boost::tuple< double, double > TurksHead::getCoordinates( int k, int theta ) const {
    return convertRadialToCartesianCoordinates( getRadius( k, theta ), theta );
}

double TurksHead::getRadius( int k, int theta ) const {
    return m_radius + m_deltaRadius * cos( p * angleFromTheta( theta - phi( k ) ) / q );
}

double TurksHead::angleFromTheta( int theta ) const {
    return M_PI * theta / p / m_thetaSteps;
}

int TurksHead::phi( int k ) const {
    return 2 * k * m_thetaSteps;
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

double TurksHead::getAltitude( int k, int theta ) const {
    if( m_knownAltitudes[ k ].empty() ) {
        return 1;
    }

    std::map< int, int >::const_iterator nextIt = m_knownAltitudes[ k ].lower_bound( theta );

    std::pair< int, int > prev, next;

    if( nextIt == m_knownAltitudes[ k ].begin() ) {
        prev = *m_knownAltitudes[ k ].rbegin();
        prev.first -= m_maxThetaOnPath;
        next = *nextIt;
    } else if( nextIt == m_knownAltitudes[ k ].end() ) {
        prev = *m_knownAltitudes[ k ].rbegin();
        next = *m_knownAltitudes[ k ].begin();
        next.first += m_maxThetaOnPath;
    } else {
        prev = *boost::prior( nextIt );
        next = *nextIt;
    }

    return prev.second + ( next.second - prev.second ) * ( theta - prev.first ) / float( next.first - prev.first );
}

} // Namespace
