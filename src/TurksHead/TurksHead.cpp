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

TurksHead::TurksHead( int leads, int bights, double innerRadius, double outerRadius, double lineWidth ) :
    m_leads( leads ),
    m_bights( bights ),
    m_radius( ( innerRadius + outerRadius ) / 2 ),
    m_deltaRadius( ( outerRadius - innerRadius - lineWidth ) / 2 ),
    m_lineWidth( lineWidth )
{
}

void TurksHead::draw( bool onlyPositiveZ ) const {
    double maxTheta = maximumAngle();
    double stepTheta = stepAngle();

    for( double theta1 = 0; theta1 <= maxTheta; theta1 += stepTheta ) {
        double r1, z1; boost::tie( r1, z1 ) = coordinates( theta1 );
        if( !onlyPositiveZ || z1 > 0 ) {
            double theta0 = theta1 - stepTheta;
            double r0, z0; boost::tie( r0, z0 ) = coordinates( theta0 );
            double theta2 = theta1 + stepTheta;
            double r2, z2; boost::tie( r2, z2 ) = coordinates( theta2 );

            setSourceHsv( theta1 / maxTheta * 360, 0.5, 0.5 + z1 / 2 );

            m_ctx->move_to( r0 * std::cos( theta0 ), r0 * std::sin( theta0 ) );
            m_ctx->line_to( r1 * std::cos( theta1 ), r1 * std::sin( theta1 ) );
            m_ctx->line_to( r2 * std::cos( theta2 ), r2 * std::sin( theta2 ) );

            m_ctx->stroke();
        }
    }
}

void TurksHead::draw( Cairo::RefPtr< Cairo::Context > context ) const {
    m_ctx = context;
    m_ctx->set_line_width( m_lineWidth );

    draw( false );
    draw( true );
}

boost::tuple< double, double > TurksHead::coordinates( double theta ) const {
    double r = m_radius + m_deltaRadius * cos( m_bights * theta / m_leads );
    double z = 1.;

    {
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
    }

    return boost::make_tuple( r, z );
}

double TurksHead::maximumAngle() const {
    return m_leads * 2 * std::acos( -1 );
}

double TurksHead::stepAngle() const {
    return std::acos( -1 ) / 500;
}

} // Namespace
