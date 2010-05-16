from ViDE.Project.Description import *

project = Project(
    artefacts = [
        DynamicLibrary(
            name = "turkshead",
            sources = AllCppIn( "src/turkshead" ),
            headers = AllHppIn( "src/turkshead" ),
            externalLibraries = [ "cairomm-1.0" ]
        ),
        DynamicLibrary(
            name = "thdui",
            sources = AllCppIn( "src/thdui" ),
            headers = AllHppIn( "src/thdui" ),
            localLibraries = [ "turkshead" ],
            externalLibraries = [ "gtkmm-2.4" ]
        ),
        Executable(
            name = "turks_head_designer",
            sources = [ "src/turks_head_designer.cpp" ],
            localLibraries = [ "thdui" ],
            externalLibraries = [ "boost_program_options" ]
        )
    ],
)
