from ViDE.Project.Description import *

DynamicLibrary(
    name = "turkshead",
    sources = AllCppIn( "src/turkshead" ),
    publicHeaders = AllHppIn( "src/turkshead" ),
    stripFromHeaders = "src/",
    localLibraries = [],
    externalLibraries = [ "cairomm-1.0" ]
)

DynamicLibrary(
    name = "thdui",
    sources = AllCppIn( "src/thdui" ),
    publicHeaders = AllHppIn( "src/thdui" ),
    stripFromHeaders = "src/",
    localLibraries = [ "turkshead" ],
    externalLibraries = [ "gtkmm-2.4" ]
)

Executable(
    name = "turks_head_designer",
    sources = [ "src/turks_head_designer.cpp" ],
    localLibraries = [ "thdui", "turkshead" ],
    externalLibraries = [ "boost_program_options" ]
)
