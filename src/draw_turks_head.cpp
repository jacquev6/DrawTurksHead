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
        ( "radius-variation", po::value< double >()->default_value( 0.5 ), "variation of the radius" )
        ( "line-width", po::value< double >()->default_value( 0.25 ), "width of the line" )
    ;

    po::variables_map vm;
    po::store( po::parse_command_line( argc, argv, desc ), vm );
    po::notify( vm );

    if( vm.count( "help" ) ) {
        std::cout << desc << std::endl;
        return 0;
    }

    Cairo::RefPtr< Cairo::ImageSurface > image = Cairo::ImageSurface::create( Cairo::FORMAT_RGB24, vm[ "width" ].as< int >(), vm[ "height" ].as< int >() );
    Cairo::RefPtr< Cairo::Context > context = Cairo::Context::create( image );

    const TurksHead::TurksHead head(
        vm[ "width" ].as< int >(),
        vm[ "height" ].as< int >(),
        vm[ "leads" ].as< int >(),
        vm[ "bights" ].as< int >(),
        vm[ "radius-variation" ].as< double >(),
        vm[ "line-width" ].as< double >()
    );
    head.draw( context );

    image->write_to_png( "turks_head.png" );
}
