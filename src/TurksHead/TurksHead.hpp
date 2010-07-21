#ifndef TurksHead_TurksHead_hpp
#define TurksHead_TurksHead_hpp

// Boost
#include <boost/tuple/tuple.hpp>

// Cairo
#include <cairomm/cairomm.h>

namespace TurksHead {

class TurksHead {
public:
    TurksHead( int width, int height, int leads, int bights, double deltaRadius, double lineWidth );

public:
    void draw( Cairo::RefPtr< Cairo::Context > ) const;

private:
    void paintBackground() const;
    void draw( bool onlyPositiveZ ) const;
    void setSourceHsv( double h, double s, double v ) const;

private:
    boost::tuple< double, double > coordinates( double theta ) const;
    double maximumAngle() const;
    double stepAngle() const;


private:
    double m_width;
    double m_height;
private:
    int m_leads;
    int m_bights;
private:
    double m_margin;
private:
    double m_deltaRadius;
    double m_lineWidth;

private:
    mutable Cairo::RefPtr< Cairo::Context > m_ctx;
};

} // Namespace

#endif // Include guard
