// Header
#include "DrawingArea.hpp"

bool DrawingArea::on_expose_event( GdkEventExpose* event ) {
    Glib::RefPtr< Gdk::Window > window = get_window();
    if( window ) {
        Cairo::RefPtr< Cairo::Context > context = window->create_cairo_context();
        Gtk::Allocation allocation = get_allocation();
        const int width = allocation.get_width();
        const int height = allocation.get_height();

        m_head.setWidth( width );
        m_head.setHeight( height );
        m_head.draw( context );
    }

    return true;
}
