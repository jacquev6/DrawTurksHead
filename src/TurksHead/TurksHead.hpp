#ifndef TurksHead_TurksHead_hpp
#define TurksHead_TurksHead_hpp

// Standard library
#include <map>
#include <set>
#include <list>

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
    struct Intersection {
        int m;
        int thetaOnPathM;
        int n;
        int thetaOnPathN;
    };

private:
    void setupDrawing( Cairo::RefPtr< Cairo::Context > ) const;
    void teardownDrawing() const;

    void drawAllPaths() const;
    void drawPath( int k ) const;
    void drawSegment( int k, int minTheta, int maxTheta ) const;
    void drawStep( int k, int theta ) const;
    void redrawAllIntersections() const;
    void redrawIntersection( const Intersection& ) const;

    boost::tuple< double, double > getCoordinates( int k, int theta ) const;
    boost::tuple< double, double > getInnerCoordinates( int k, int theta ) const;
    boost::tuple< double, double > getOuterCoordinates( int k, int theta ) const;
    boost::tuple< double, double > getNormal( int k, int theta ) const;
    double getRadius( int k, int theta ) const;
    boost::tuple< double, double > convertRadialToCartesianCoordinates( double radius, int theta ) const;

    int phi( int k ) const;

    double getAltitude( int k, int theta ) const;
    void computeKnownAltitudes();

    void computeIntersections();
    std::list< std::pair< int, int > > allPathPairs() const;
    void computePathPairIntersections( int m, int n );
    void addIntersection( int m, int n, int a, int b );

    void clipRegion( int k, int theta ) const;
    void redrawRegion( int k, int theta ) const;
    void clipSegment( int k, int minTheta, int maxTheta ) const;

    void pathSegment( int k, int minTheta, int maxTheta ) const;

    void moveTo( const boost::tuple< double, double >& ) const;
    void lineTo( const boost::tuple< double, double >& ) const;

    void setSourceHsv( double h, double s, double v ) const;

    double angleFromTheta( int theta ) const;

    std::pair< int, double > getPrevKnownAltitude( int k, int theta ) const;
    std::pair< int, double > getNextKnownAltitude( int k, int theta ) const;

    int getPrevRedrawLimit( int k, int theta ) const;
    int getNextRedrawLimit( int k, int theta ) const;

private:
    int p;
    int q;
private:
    int d;
    int m_thetaSteps;
    int m_maxThetaOnPath;
    std::vector< std::map< int, double > > m_knownAltitudes;
    std::list< Intersection > m_intersections;
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
