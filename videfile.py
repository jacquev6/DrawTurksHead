from ViDE.Project.Description import *
from Tools.Cairo import Cairomm, PyCairo
from Tools.Boost import BoostPython, BoostProgramOptions

################################################################################
#################################################################### Libraries #
################################################################################

turkshead = CppDynamicLibrary(
    name = "turkshead",
    sources = [ "src/TurksHead/TurksHead.cpp" ],
    headers = [ "src/TurksHead/TurksHead.hpp" ],
    stripHeaders = lambda h: h[4:],
    localLibraries = [],
    externalLibraries = [ Cairomm ]
)

PythonPackage(
    name = "turkshead",
    sources = [ "src/PythonPackage/turkshead.py" ],
    strip = lambda f: f[18:],
    modules = [
        CppPythonModule(
            name = "_turkshead",
            sources = [ "src/PythonPackage/module.cpp" ],
            localLibraries = [ turkshead ],
            externalLibraries = [ Cairomm, BoostPython, PyCairo ]
        )
    ]
)

################################################################################
######################################################### Executables examples #
################################################################################

# C++
CppExecutable(
    name = "draw_turkshead_cpp",
    sources = [ "src/draw_turkshead_cpp.cpp" ],
    localLibraries = [ turkshead ],
    externalLibraries = [ Cairomm, BoostProgramOptions ]
)

# Python
PythonScript(
    source = "src/draw_turkshead_python.py"
)
