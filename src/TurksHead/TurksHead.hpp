#ifndef TurksHead_TurksHead_hpp
#define TurksHead_TurksHead_hpp

// Boost
#include <boost/tuple/tuple.hpp>

// Cairo
#include <cairomm/cairomm.h>

namespace TurksHead {

class TurksHead {
public:
    TurksHead( int leads, int bights, double innerRadius, double outerRadius, double lineWidth );

public:
    void draw( Cairo::RefPtr< Cairo::Context > ) const;

private:
    void draw( bool onlyPositiveZ ) const;
    void setSourceHsv( double h, double s, double v ) const;

private:
    boost::tuple< double, double > coordinates( double theta ) const;
    double maximumAngle() const;
    double stepAngle() const;

private:
    int m_leads;
    int m_bights;
private:
    double m_radius;
    double m_deltaRadius;
private:
    double m_lineWidth;

private:
    mutable Cairo::RefPtr< Cairo::Context > m_ctx;
};

} // Namespace

#endif // Include guard
