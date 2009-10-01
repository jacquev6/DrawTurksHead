#ifndef DrawingArea_hpp
#define DrawingArea_hpp

// gtkmm
#include <gtkmm/drawingarea.h>

// TurksHeadDesigner
#include <turkshead/TurksHead.hpp>

class DrawingArea : public Gtk::DrawingArea {
public:
    DrawingArea() : m_head( 800, 600, 4, 5, 0.25, 0.05 ) {}
protected:
    bool on_expose_event( GdkEventExpose* );
public:
    TurksHead& head() { return m_head; }
private:
    TurksHead m_head;
};

#endif // Include guard
