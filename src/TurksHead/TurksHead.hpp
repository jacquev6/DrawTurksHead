#ifndef TurksHead_TurksHead_hpp
#define TurksHead_TurksHead_hpp

// Standard library
#include <map>
#include <set>
#include <list>

// Boost
#include <boost/tuple/tuple.hpp>
#include <boost/operators.hpp>

// Cairo
#include <cairomm/cairomm.h>

#define STRONG_TYPEDEF( T, D ) \
struct D : \
    boost::operators< D >, \
    boost::operators< D, T > \
{ \
    explicit D( T t_ ) : t( t_ ) {}\
    T index() const { return t; } \
\
    /*bool operator=( D );*/ \
    bool operator=( T ); \
\
    void operator++() { ++t; }\
    void operator--() { --t; }\
    D operator-() const; \
\
    D operator+=( D d ) { t += d.t; return *this; } \
    D operator+=( T d ) { t += d;   return *this; } \
    D operator-=( D d ) { t -= d.t; return *this; } \
    D operator-=( T d ) { t -= d;   return *this; } \
    D operator*=( T ); \
    D operator/=( T d ) { t /= d;   return *this; } \
    D operator%=( D d ) { t %= d.t; return *this; } \
    D operator%=( T ); \
\
    bool operator==( D d ) const { return t == d.t; } \
    bool operator==( T d ) const { return t == d; } \
    bool operator<( D d ) const { return t < d.t; } \
    bool operator<( T d ) const { return t < d; } \
\
private: \
    T t; \
};

namespace TurksHead {

class TurksHead {
public:
    TurksHead( int leads, int bights, double innerRadius, double outerRadius, double lineWidth );
    virtual ~TurksHead();

public:
    void draw( Cairo::RefPtr< Cairo::Context > ) const;
    int getD() const;
    int getP() const;
    int getQ() const;

private:
    STRONG_TYPEDEF( int, Theta )

    STRONG_TYPEDEF( int, Path )

    struct Intersection {
        Intersection( Path, Theta, Path, Theta );
        Path m;
        Theta thetaOnPathM;
        Path n;
        Theta thetaOnPathN;
    };

    struct Segment {
        Segment( Theta min, Theta max );
        Theta minTheta;
        Theta maxTheta;
    };

private:
    void setupDrawing( Cairo::RefPtr< Cairo::Context > ) const;
    void teardownDrawing() const;

    void drawAllPaths() const;
    void draw( Path k ) const;
    void drawSegment( Path k, Theta minTheta, Theta maxTheta ) const;
    void drawStep( Path k, Theta theta ) const;
    void redrawAllIntersections() const;
    void redrawIntersection( const Intersection& ) const;

public: /// @todo Remove this work arround: those functions should be private
    void setColor( Path k, Theta ) const;
    double getHue( Path, Theta ) const;
    virtual double doGetHue( int k, int theta ) const;
    double getSaturation( Path, Theta ) const;
    virtual double doGetSaturation( int k, int theta ) const;

private:
    boost::tuple< double, double > getCoordinates( Path k, Theta theta ) const;
    boost::tuple< double, double > getInnerCoordinates( Path k, Theta theta ) const;
    boost::tuple< double, double > getOuterCoordinates( Path k, Theta theta ) const;
    boost::tuple< double, double > getNormal( Path k, Theta theta ) const;
    double getRadius( Path k, Theta theta ) const;
    boost::tuple< double, double > convertRadialToCartesianCoordinates( double radius, Theta theta ) const;

    Theta phi( Path k ) const;

    double getAltitude( Path k, Theta theta ) const;
    void computeKnownAltitudes();

    void computeIntersections();
    std::list< std::pair< Path, Path > > allPathPairs() const;
    void computePathPairIntersections( Path m, Path n );
    void addIntersection( Path m, Path n, int a, int b );

    void clipRegion( Path k, Theta theta ) const;
    void redrawRegion( Path k, Theta theta ) const;
    void clipSegment( Path k, Theta minTheta, Theta maxTheta ) const;

    void pathSegment( Path k, Theta minTheta, Theta maxTheta ) const;

    void moveTo( const boost::tuple< double, double >& ) const;
    void lineTo( const boost::tuple< double, double >& ) const;

    void setSourceHsv( double h, double s, double v ) const;

    double angleFromTheta( Theta theta ) const;

    std::pair< Theta, double > getPrevKnownAltitude( Path k, Theta theta ) const;
    std::pair< Theta, double > getNextKnownAltitude( Path k, Theta theta ) const;

    Theta getPrevRedrawLimit( Path k, Theta theta ) const;
    Theta getNextRedrawLimit( Path k, Theta theta ) const;

private:
    int p;
    int q;
private:
    int d;
    int m_thetaSteps;
    Theta m_maxThetaOnPath;
    std::map< Path, std::map< Theta, double > > m_knownAltitudes;
    std::list< Intersection > m_intersections;
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
