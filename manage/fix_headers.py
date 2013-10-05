#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright                                                                    #
#                                                                              #
# This file is part of DrawTurksHead. http://jacquev6.github.com/DrawTurksHead #
#                                                                              #
# DrawTurksHead is free software: you can redistribute it and/or modify it     #
# under the terms of the GNU Lesser General Public License as published by the #
# Free Software Foundation, either version 3 of the License, or (at your       #
# option) any later version.                                                   #
#                                                                              #
# DrawTurksHead is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License  #
# for more details.                                                            #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with DrawTurksHead. If not, see <http://www.gnu.org/licenses/>.        #
#                                                                              #
################################################################################

import fnmatch
import os
import subprocess
import itertools
import textwrap


licenseText = [
    "This file is part of DrawTurksHead. http://jacquev6.github.com/DrawTurksHead",
    "DrawTurksHead is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.",
    "DrawTurksHead is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.",
    "You should have received a copy of the GNU Lesser General Public License along with DrawTurksHead. If not, see <http://www.gnu.org/licenses/>.",
]

endsOfHeader = [
    "################################################################################",
    "\\******************************************************************************/",
]


def generateSharpedLicenseSection(filename):
    yield "############################ Copyrights and license ############################"
    yield "#                                                                              #"
    for year, name in sorted(listContributors(filename)):
        line = "# Copyright " + year + " " + name
        line += (79 - len(line)) * " " + "#"
        yield line
    yield "#                                                                              #"
    for paragraph in licenseText:
        for line in textwrap.wrap(paragraph, width=78, initial_indent="# ", subsequent_indent="# "):
            yield line + (79 - len(line)) * " " + "#"
        yield "#                                                                              #"
    yield 80 * "#"


def generateCppLicenseSection(filename):
    yield "/*************************** Copyrights and license ***************************\\"
    yield "*                                                                              *"
    for year, name in sorted(listContributors(filename)):
        line = "* Copyright " + year + " " + name
        line += (79 - len(line)) * " " + "*"
        yield line
    yield "*                                                                              *"
    for paragraph in licenseText:
        for line in textwrap.wrap(paragraph, width=78, initial_indent="* ", subsequent_indent="* "):
            yield line + (79 - len(line)) * " " + "*"
        yield "*                                                                              *"
    yield "\\******************************************************************************/"


def listContributors(filename):
    contributors = set()
    for line in subprocess.check_output(["git", "log", "--format=format:%ad %an <%ae>", "--date=short", "--", filename]).split("\n"):
        year = line[0:4]
        name = line[11:]
        contributors.add((year, name))
    return contributors


def extractBodyLines(lines):
    bodyLines = []

    seenEndOfHeader = False

    for line in lines:
        if len(line) > 0 and line[0] not in [ "#", "*" ] and not line.startswith("/*") and not line in endsOfHeader:
            seenEndOfHeader = True
        if seenEndOfHeader:
            bodyLines.append(line)
        if line in endsOfHeader:
            seenEndOfHeader = True

    return bodyLines


class PythonHeader:
    def fix(self, filename, lines):
        isExecutable = lines[0].startswith("#!")
        newLines = []

        if isExecutable:
            newLines.append("#!/usr/bin/env python")
        newLines.append("# -*- coding: utf-8 -*-")
        newLines.append("")

        for line in generateSharpedLicenseSection(filename):
            newLines.append(line)

        bodyLines = extractBodyLines(lines)

        if len(bodyLines) > 0 and bodyLines[0] != "":
            newLines.append("")
            if "import " not in bodyLines[0] and bodyLines[0] != '"""' and not bodyLines[0].startswith("##########"):
                newLines.append("")
        newLines += bodyLines

        return newLines


class ShellHeader:
    def fix(self, filename, lines):
        isExecutable = lines[0].startswith("#!")
        newLines = []

        if isExecutable:
            newLines.append("#!/bin/bash")
        newLines.append("# -*- coding: utf-8 -*-")
        newLines.append("")

        for line in generateSharpedLicenseSection(filename):
            newLines.append(line)

        newLines += extractBodyLines(lines)

        return newLines


class StandardHeader:
    def fix(self, filename, lines):
        newLines = []

        for line in generateSharpedLicenseSection(filename):
            newLines.append(line)

        bodyLines = extractBodyLines(lines)

        if len(bodyLines) and bodyLines[0] != "" > 0:
            newLines.append("")
        newLines += bodyLines

        return newLines


class CppHeader:
    def fix(self, filename, lines):
        newLines = []

        for line in generateCppLicenseSection(filename):
            newLines.append(line)

        bodyLines = extractBodyLines(lines)

        if len(bodyLines) and bodyLines[0] != "" > 0:
            newLines.append("")
        newLines += bodyLines

        return newLines


def findHeadersAndFiles():
    for root, dirs, files in os.walk('.', topdown=True):
        if ".git" in dirs:
            dirs.remove(".git")
        if "build" in dirs:
            dirs.remove("build")
        if "dist" in dirs:
            dirs.remove("dist")

        for filename in files:
            fullname = os.path.join(root, filename)
            if filename.endswith(".py"):
                yield (PythonHeader(), fullname)
            elif filename.endswith(".cpp") or filename.endswith(".hpp"):
                yield (CppHeader(), fullname)
            elif filename.endswith(".sh"):
                yield (ShellHeader(), fullname)
            elif filename in ["COPYING", "COPYING.LESSER"]:
                pass
            elif filename.endswith(".rst") or filename.endswith(".md"):
                pass
            elif filename == ".gitignore" or filename.endswith(".txt"):
                yield (StandardHeader(), fullname)
            elif fullname.endswith(".pyc"):
                pass
            else:
                print "Don't know what to do with", filename, "in", root


def main():
    for header, filename in findHeadersAndFiles():
        print "Analyzing", filename
        with open(filename) as f:
            lines = list(line.rstrip() for line in f)
        newLines = header.fix(filename, lines)
        if newLines != lines:
            print " => actually modifying", filename
            with open(filename, "w") as f:
                for line in newLines:
                    f.write(line + "\n")


if __name__ == "__main__":
    main()
