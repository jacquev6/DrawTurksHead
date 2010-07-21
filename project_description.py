from ViDE.Project.Description import *

DynamicLibrary(
    name = "turkshead",
    sources = AllCppIn( "src/turkshead" ),
    publicHeaders = AllHppIn( "src/turkshead" ),
    stripFromHeaders = "src/",
    localLibraries = [],
    externalLibraries = [ "cairomm-1.0" ]
)

### @todo Delete this executable as soon as a Python script can drive the turkshead library
Executable(
    name = "draw_turks_head",
    sources = [ "src/draw_turks_head.cpp" ],
    localLibraries = [ "turkshead" ],
    externalLibraries = [ "boost_program_options" ]
)
