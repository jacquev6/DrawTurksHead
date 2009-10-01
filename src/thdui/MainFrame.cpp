// Header
#include "MainFrame.hpp"

// Standard library
#include <iostream>

// gtkmm
#include <gtkmm/stock.h>

MainFrame::MainFrame() {
    //Create actions for menus and toolbars:
    m_refActionGroup = Gtk::ActionGroup::create();

    //File menu:
    m_refActionGroup->add(Gtk::Action::create("FileMenu", "File"));
    //Sub-menu.
    m_refActionGroup->add( Gtk::Action::create( "FileSave", Gtk::Stock::SAVE ) );
    m_refActionGroup->add( Gtk::Action::create( "FileQuit", Gtk::Stock::QUIT ),
        sigc::mem_fun( *this, &MainFrame::on_menu_file_quit ) );

    //Edit menu:
    m_refActionGroup->add( Gtk::Action::create( "EditMenu", "Edit" ) );
    m_refActionGroup->add( Gtk::Action::create( "EditIncLeads", "Increment leads number" ),
        sigc::mem_fun( *this, &MainFrame::on_menu_edit_inc_leads ) );
    m_refActionGroup->add( Gtk::Action::create( "EditDecLeads", "Decrement leads number" ),
        sigc::mem_fun( *this, &MainFrame::on_menu_edit_dec_leads ) );
    m_refActionGroup->add( Gtk::Action::create( "EditIncBights", "Increment bights number" ),
        sigc::mem_fun( *this, &MainFrame::on_menu_edit_inc_bights ) );
    m_refActionGroup->add( Gtk::Action::create( "EditDecBights", "Decrement bights number" ),
        sigc::mem_fun( *this, &MainFrame::on_menu_edit_dec_bights ) );
    m_refActionGroup->add( Gtk::Action::create( "EditIncDeltaRadius", "Increment delta radius" ),
        sigc::mem_fun( *this, &MainFrame::on_menu_edit_inc_delta_radius ) );
    m_refActionGroup->add( Gtk::Action::create( "EditDecDeltaRadius", "Decrement delta radius" ),
        sigc::mem_fun( *this, &MainFrame::on_menu_edit_dec_delta_radius ) );
    m_refActionGroup->add( Gtk::Action::create( "EditIncLineWidth", "Increment line width" ),
        sigc::mem_fun( *this, &MainFrame::on_menu_edit_inc_line_width ) );
    m_refActionGroup->add( Gtk::Action::create( "EditDecLineWidth", "Decrement line width" ),
        sigc::mem_fun( *this, &MainFrame::on_menu_edit_dec_line_width ) );

    m_refUIManager = Gtk::UIManager::create();
    m_refUIManager->insert_action_group( m_refActionGroup );

    add_accel_group( m_refUIManager->get_accel_group() );

    Glib::ustring ui_info =
        "<ui>"
        "  <menubar name='MenuBar'>"
        "    <menu action='FileMenu'>"
        "      <menuitem action='FileSave'/>"
        "      <separator/>"
        "      <menuitem action='FileQuit'/>"
        "    </menu>"
        "    <menu action='EditMenu'>"
        "      <menuitem action='EditIncLeads'/>"
        "      <menuitem action='EditDecLeads'/>"
        "      <menuitem action='EditIncBights'/>"
        "      <menuitem action='EditDecBights'/>"
        "      <menuitem action='EditIncDeltaRadius'/>"
        "      <menuitem action='EditDecDeltaRadius'/>"
        "      <menuitem action='EditIncLineWidth'/>"
        "      <menuitem action='EditDecLineWidth'/>"
        "    </menu>"
        "  </menubar>"
        "  <toolbar  name='ToolBar'>"
        "    <toolitem action='FileQuit'/>"
        "    <toolitem action='EditDecLeads'/>"
        "    <toolitem action='EditIncLeads'/>"
        "    <toolitem action='EditDecBights'/>"
        "    <toolitem action='EditIncBights'/>"
        "    <toolitem action='EditIncDeltaRadius'/>"
        "    <toolitem action='EditDecDeltaRadius'/>"
        "    <toolitem action='EditIncLineWidth'/>"
        "    <toolitem action='EditDecLineWidth'/>"
        "  </toolbar>"
        "</ui>";

    m_refUIManager->add_ui_from_string(ui_info);

    set_title( "Turk's Head Designer" );
    set_default_size( 800, 600 );

    add( m_box );

    Gtk::Widget* pMenubar = m_refUIManager->get_widget( "/MenuBar" );
    m_box.pack_start( *pMenubar, Gtk::PACK_SHRINK );

    Gtk::Widget* pToolbar = m_refUIManager->get_widget( "/ToolBar" );
    m_box.pack_start( *pToolbar, Gtk::PACK_SHRINK );

    m_box.pack_start( m_drawingArea, Gtk::PACK_EXPAND_WIDGET );

    show_all_children();
}

void MainFrame::on_menu_file_quit() {
    hide();
}

void MainFrame::on_menu_edit_inc_leads() {
    m_drawingArea.head().incrementLeads();
    queue_draw();
}

void MainFrame::on_menu_edit_dec_leads() {
    m_drawingArea.head().decrementLeads();
    queue_draw();
}

void MainFrame::on_menu_edit_inc_bights() {
    m_drawingArea.head().incrementBights();
    queue_draw();
}

void MainFrame::on_menu_edit_dec_bights() {
    m_drawingArea.head().decrementBights();
    queue_draw();
}

void MainFrame::on_menu_edit_inc_delta_radius() {
    m_drawingArea.head().incrementDeltaRadius();
    queue_draw();
}

void MainFrame::on_menu_edit_dec_delta_radius() {
    m_drawingArea.head().decrementDeltaRadius();
    queue_draw();
}

void MainFrame::on_menu_edit_inc_line_width() {
    m_drawingArea.head().incrementLineWidth();
    queue_draw();
}

void MainFrame::on_menu_edit_dec_line_width() {
    m_drawingArea.head().decrementLineWidth();
    queue_draw();
}
