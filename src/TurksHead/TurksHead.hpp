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
    void drawPaths( bool onlyPositiveZ ) const;
    void drawPath( int path, bool onlyPositiveZ ) const;
    void drawSegment( double theta, bool onlyPositiveZ ) const;

    boost::tuple< double, double > getCoordinates( double theta ) const;
    double getRadius( double theta ) const;
    static boost::tuple< double, double > convertRadialToCartesianCoordinates( double radius, double theta );

    double getAltitude( double theta ) const;

    void setSourceHsv( double h, double s, double v ) const;

private:
    int m_leads;
    int m_bights;
    int m_paths;
    double m_maxThetaOnPath;
private:
    double m_radius;
    double m_deltaRadius;
private:
    double m_lineWidth;

private:
    mutable Cairo::RefPtr< Cairo::Context > m_ctx;

private:
    static const double s_stepTheta;
};

} // Namespace

#endif // Include guard
