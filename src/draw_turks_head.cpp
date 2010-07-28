// Standard library
#include <iostream>

// Boost
#include <boost/lexical_cast.hpp>
#include <boost/program_options.hpp>
namespace po = boost::program_options;

// DrawTurksHead
#include <TurksHead/TurksHead.hpp>

int main( int argc, char* argv[]) {
    po::options_description desc("Allowed options");
    desc.add_options()
        ( "help", "produce help message" )
        ( "width", po::value< int >()->default_value( 800 ), "width of generated image" )
        ( "height", po::value< int >()->default_value( 600 ), "height of generated image" )
        ( "leads", po::value< int >()->default_value( 3 ), "number of leads" )
        ( "bights", po::value< int >()->default_value( 4 ), "number of bights" )
        ( "radius-variation", po::value< double >()->default_value( 200 ), "variation of the radius" )
        ( "line-width", po::value< double >()->default_value( 50 ), "width of the line" )
    ;

    po::variables_map vm;
    po::store( po::parse_command_line( argc, argv, desc ), vm );
    po::notify( vm );

    if( vm.count( "help" ) ) {
        std::cout << desc << std::endl;
        return 0;
    }

    int width = vm[ "width" ].as< int >();
    int height = vm[ "height" ].as< int >();
    double outerRadius = std::min( width, height ) / 2 - 10;
    double innerRadius = outerRadius - vm[ "radius-variation" ].as< double >();

    Cairo::RefPtr< Cairo::ImageSurface > image = Cairo::ImageSurface::create( Cairo::FORMAT_RGB24, width, height );
    Cairo::RefPtr< Cairo::Context > context = Cairo::Context::create( image );
    context->set_source_rgb( 1, 1, 0xBF / 255. );
    context->paint();
    context->set_source_rgb( 0, 0, 0 );
    context->rectangle( 10, 10, width - 20, height - 20 );
    context->translate( width / 2, height / 2 );
    context->move_to( -width, 0 );
    context->line_to( width, 0 );
    context->move_to( 0, -height );
    context->line_to( 0, height );
    context->stroke(); /// @todo Find, if possible, how to delete the current point of the context, while continuing to draw
    context->arc( 0, 0, outerRadius, 0, 2 * M_PI );
    context->stroke();
    context->arc( 0, 0, innerRadius, 0, 2 * M_PI );
    context->stroke();

    context->rotate( 0.000000001 ); /// @todo Understand why removing this rotate gives a strange sharp line for --leads=2 --bights=3

    const TurksHead::TurksHead head(
        vm[ "leads" ].as< int >(),
        vm[ "bights" ].as< int >(),
        innerRadius,
        outerRadius,
        vm[ "line-width" ].as< double >()
    );
    head.draw( context );

    image->write_to_png( "turks_head.png" );
}
