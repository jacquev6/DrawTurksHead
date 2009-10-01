#ifndef MainFrame_hpp
#define MainFrame_hpp

// gtkmm
#include <gtkmm/window.h>
#include <gtkmm/box.h>
#include <gtkmm/uimanager.h>
#include <gtkmm/actiongroup.h>

// TurksHeadDesigner
#include "DrawingArea.hpp"

class MainFrame : public Gtk::Window {
public:
    MainFrame();

private:
    void on_menu_file_quit();

    void on_menu_edit_inc_leads();
    void on_menu_edit_dec_leads();
    void on_menu_edit_inc_bights();
    void on_menu_edit_dec_bights();
    void on_menu_edit_inc_delta_radius();
    void on_menu_edit_dec_delta_radius();
    void on_menu_edit_inc_line_width();
    void on_menu_edit_dec_line_width();

private:
    DrawingArea m_drawingArea;
    Gtk::VBox m_box;

    Glib::RefPtr< Gtk::UIManager > m_refUIManager;
    Glib::RefPtr< Gtk::ActionGroup > m_refActionGroup;
};

#endif // Include guard
