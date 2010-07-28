#ifndef TurksHead_TurksHead_hpp
#define TurksHead_TurksHead_hpp

// Standard library
#include <map>

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
    void drawPaths() const;
    void drawPath( int k ) const;
    void drawSegment( int k, int theta ) const;

    boost::tuple< double, double > getCoordinates( int k, int theta ) const;
    boost::tuple< double, double > getInnerCoordinates( int k, int theta ) const;
    boost::tuple< double, double > getOuterCoordinates( int k, int theta ) const;
    boost::tuple< double, double > getNormal( int k, int theta ) const;
    double getRadius( int k, int theta ) const;
    boost::tuple< double, double > convertRadialToCartesianCoordinates( double radius, int theta ) const;

    int phi( int k ) const;

    double getAltitude( int theta ) const;
    void computeKnownAltitudes();
    void computeCrossingThetas();

    void redraw( int thetaLow, int thetaHight ) const;
    void clip( int theta ) const;

    void pathSegment( int k, int minTheta, int maxTheta ) const;

    void moveTo( const boost::tuple< double, double >& ) const;
    void lineTo( const boost::tuple< double, double >& ) const;

    void setSourceHsv( double h, double s, double v ) const;

    double angleFromTheta( int theta ) const;

    int getPreviousCheckPoint( std::map< int, int >::const_iterator ) const;
    int getNextCheckPoint( std::map< int, int >::const_iterator ) const;

private:
    int p;
    int q;
private:
    int d;
    int m_thetaSteps;
    int m_maxThetaOnPath;
    std::map< int, int > m_knownAltitudes;
    std::map< int, int > m_crossingThetas;
private:
    double m_radius;
    double m_deltaRadius;
private:
    double m_lineWidth;

private:
    mutable Cairo::RefPtr< Cairo::Context > m_ctx;

private:
    static const int s_stepsTheta;
};

} // Namespace

#endif // Include guard
