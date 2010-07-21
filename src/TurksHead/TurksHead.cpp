// Header
#include "TurksHead.hpp"

// Standard library
#include <map>
#include <iostream>

// Boost
#include <boost/math/common_factor.hpp>
#include <boost/utility.hpp>
#include <boost/lambda/lambda.hpp>

namespace TurksHead {

TurksHead::TurksHead( int leads, int bights, double innerRadius, double outerRadius, double lineWidth ) :
    m_leads( leads ),
    m_bights( bights ),
    m_paths( boost::math::gcd( m_bights, m_leads ) ),
    m_maxThetaOnPath( 2 * M_PI * m_leads / m_paths ),
    m_radius( ( innerRadius + outerRadius ) / 2 ),
    m_deltaRadius( ( outerRadius - innerRadius - lineWidth ) / 2 ),
    m_lineWidth( lineWidth )
{
}

const double TurksHead::s_stepTheta = M_PI / 500;

void TurksHead::draw( Cairo::RefPtr< Cairo::Context > context ) const {
    m_ctx = context;
    m_ctx->save();
    m_ctx->set_line_width( m_lineWidth );
    m_ctx->set_line_cap( Cairo::LINE_CAP_BUTT );

    drawPaths( false );
    drawPaths( true );

    m_ctx->restore();
}

void TurksHead::drawPaths( bool onlyPositiveZ ) const {
    for( int path = 0; path < m_paths; ++path ) {
        drawPath( path, onlyPositiveZ );
        m_ctx->rotate( 2 * M_PI / m_paths );
    }
}

void TurksHead::drawPath( int path, bool onlyPositiveZ ) const {
    for( double theta1 = 0; theta1 <= m_maxThetaOnPath; theta1 += s_stepTheta ) {
        drawSegment( theta1, onlyPositiveZ );
    }
}

void TurksHead::drawSegment( double theta, bool onlyPositiveZ ) const {
    double z = getAltitude( theta );
    if( !onlyPositiveZ || z > 0 ) {
        double theta_m = theta - s_stepTheta;
        double theta_p = theta + s_stepTheta;
        double x0, y0; boost::tie( x0, y0 ) = getCoordinates( theta_m );
        double x1, y1; boost::tie( x1, y1 ) = getCoordinates( theta );
        double x2, y2; boost::tie( x2, y2 ) = getCoordinates( theta_p );

        setSourceHsv( theta / m_maxThetaOnPath * 360, 0.5, 0.5 + z / 2 );

        m_ctx->move_to( x0, y0 );
        m_ctx->line_to( x1, y1 );
        m_ctx->line_to( x2, y2 );

        m_ctx->stroke();
    }
}

double TurksHead::getAltitude( double theta ) const {
    double z = 1.;

    int previous_i = -1;
    int alt = 1;
    for( int i = 1; i <= 2 * m_leads * m_bights + 1; ++i ) {
        if( i % m_leads ) {
            double angle = i * std::acos( -1 ) / m_bights;
            double previous_angle = previous_i * std::acos( -1 ) / m_bights;
            int previous_alt = -alt;

            if( previous_angle <= theta && angle > theta ) {
                z = previous_alt + ( alt - previous_alt ) * ( theta - previous_angle ) / ( angle - previous_angle );
                break;
            }
            previous_i = i;
            alt *= -1;
        }
    }

    return z;
}

boost::tuple< double, double > TurksHead::getCoordinates( double theta ) const {
    return convertRadialToCartesianCoordinates( getRadius( theta ), theta );
}

double TurksHead::getRadius( double theta ) const {
    return m_radius + m_deltaRadius * cos( m_bights * theta / m_leads );
}

boost::tuple< double, double > TurksHead::convertRadialToCartesianCoordinates( double radius, double theta ) {
    return boost::make_tuple(
        radius * std::cos( theta ),
        radius * std::sin( theta )
    );
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
