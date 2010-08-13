from ViDE.Project.Description import *

DynamicLibrary(
    name = "turkshead",
    sources = AllCppIn( "src/TurksHead" ),
    publicHeaders = AllHppIn( "src/TurksHead" ),
    stripFromHeaders = "src/",
    localLibraries = [],
    externalLibraries = [ "cairomm-1.0" ]
)

Executable(
    name = "draw_turks_head",
    sources = [ "src/draw_turks_head.cpp" ],
    localLibraries = [ "turkshead" ],
    externalLibraries = [ "cairomm-1.0", "boost_program_options" ]
)

CppPythonModule(
    name = "turkshead._turkshead",
    sources = AllCppIn( "src/PythonModule" ),
    localLibraries = [ "turkshead" ],
    externalLibraries = [ "boost_python", "python2.7", "cairomm-1.0" ]
)

PythonPackage(
    name = "turkshead_package",
    pythonPythonModules = AllPyIn( "src/PythonModule" ),
    stripFromModules = lambda s: s.replace( "src/PythonModule", "turkshead" ),
    cppPythonModules = [ "turkshead._turkshead" ]
)

ExecutableScript(
    "src/draw_turks_head.py"
)

ExecutableScript(
    "src/draw_mosaic.py"
)
