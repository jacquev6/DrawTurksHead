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

void set_source_hsv( Cairo::RefPtr< Cairo::Context > context, float h, float s, float v ) {
    int hi = h / 60;
    float f = h / 60. - hi;
    hi %= 60;
    float p = v * ( 1 - s );
    float q = v * ( 1 - f * s );
    float t = v * ( 1 - ( 1 - f ) * s );
    switch( hi ) {
        case 0: return context->set_source_rgb( v, t, p );
        case 1: return context->set_source_rgb( q, v, p );
        case 2: return context->set_source_rgb( p, v, t );
        case 3: return context->set_source_rgb( p, q, v );
        case 4: return context->set_source_rgb( t, p, v );
        case 5: return context->set_source_rgb( v, p, q );
    }
}

TurksHead::TurksHead( int m_width, int m_height, int leads, int bights, double deltaRadius, double lineWidth ) :
    m_width( m_width ),
    m_height( m_height ),
    m_leads( leads ),
    m_bights( bights ),
    m_margin( 10 ),
    m_deltaRadius( deltaRadius ),
    m_lineWidth( lineWidth )
{
    if( boost::math::gcd( m_leads, m_bights ) != 1 ) throw 0;
}

void TurksHead::draw( Cairo::RefPtr< Cairo::Context > context, bool onlyPositiveZ ) const {
    double maxTheta = maximumAngle();
    double stepTheta = stepAngle();

    for( double theta1 = 0; theta1 <= maxTheta; theta1 += stepTheta ) {
        double r1, z1; boost::tie( r1, z1 ) = coordinates( theta1 );
        if( !onlyPositiveZ || z1 > 0 ) {
            double theta0 = theta1 - stepTheta;
            double r0, z0; boost::tie( r0, z0 ) = coordinates( theta0 );
            double theta2 = theta1 + stepTheta;
            double r2, z2; boost::tie( r2, z2 ) = coordinates( theta2 );

            set_source_hsv( context, theta1 / maxTheta * 360, 0.5, 0.5 + z1 / 2 );

            context->move_to( r0 * std::cos( theta0 ), r0 * std::sin( theta0 ) );
            context->line_to( r1 * std::cos( theta1 ), r1 * std::sin( theta1 ) );
            context->line_to( r2 * std::cos( theta2 ), r2 * std::sin( theta2 ) );

            context->stroke();
        }
    }
}

void TurksHead::draw( Cairo::RefPtr< Cairo::Context > context ) const {
    set_source_hsv( context, 60, 0.25, 1 );
    context->paint();

    context->translate( m_width / 2, m_height / 2 );

    double scale = std::min( ( m_width - m_margin * 2 ) / m_width, ( m_height - m_margin * 2 ) / m_height );
    context->scale( scale, scale );

    int scaleRef = std::min( m_height, m_width );
    scale = scaleRef / 2 / ( 1. + m_deltaRadius + m_lineWidth / 2 );
    context->scale( scale, -scale );

    context->set_line_width( m_lineWidth );

    draw( context, false );
    draw( context, true );
}

boost::tuple< double, double > TurksHead::coordinates( double theta ) const {
    double r = 1. + m_deltaRadius * cos( m_bights * theta / m_leads );
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

void TurksHead::incrementLeads() {
    do {
        ++m_leads;
    } while( boost::math::gcd( m_leads, m_bights ) != 1 );
}

void TurksHead::decrementLeads() {
    do {
        --m_leads;
    } while( m_leads > 0 && boost::math::gcd( m_leads, m_bights ) != 1 );
    if( m_leads == 0 ) {
        m_bights = 1;
        m_leads = 1;
    }
}

void TurksHead::incrementBights() {
    do {
        ++m_bights;
    } while( boost::math::gcd( m_leads, m_bights ) != 1 );
}

void TurksHead::decrementBights() {
    do {
        --m_bights;
    } while( m_bights > 0 && boost::math::gcd( m_leads, m_bights ) != 1 );
    if( m_bights == 0 ) {
        m_bights = 1;
        m_leads = 1;
    }
}

void TurksHead::setHeight( double h ) {
    m_height = h;
}

void TurksHead::setWidth( double w ) {
    m_width = w;
}

void TurksHead::incrementDeltaRadius() {
    m_deltaRadius += 0.05;
}

void TurksHead::decrementDeltaRadius() {
    m_deltaRadius -= 0.05;
}

void TurksHead::incrementLineWidth() {
    m_lineWidth += 0.01;
}

void TurksHead::decrementLineWidth() {
    m_lineWidth -= 0.01;
}

} // Namespace
