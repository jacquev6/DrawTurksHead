#ifndef TurksHead_hpp
#define TurksHead_hpp

// Boost
#include <boost/tuple/tuple.hpp>

// Cairo
#include <cairomm/cairomm.h>

class TurksHead {
public:
    TurksHead( int width, int height, int leads, int bights, double deltaRadius, double lineWidth );

public:
    void incrementLeads();
    void decrementLeads();
    void incrementBights();
    void decrementBights();
    void setHeight( double );
    void setWidth( double );
    void incrementDeltaRadius();
    void decrementDeltaRadius();
    void incrementLineWidth();
    void decrementLineWidth();

public:
    void draw( Cairo::RefPtr< Cairo::Context > ) const;

private:
    boost::tuple< double, double > coordinates( double theta ) const;
    double maximumAngle() const;
    double stepAngle() const;
    void draw( Cairo::RefPtr< Cairo::Context >, bool onlyPositiveZ ) const;

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
};


#endif // Include guard
