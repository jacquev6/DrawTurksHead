#!/usr/bin/env python

import sys
sys.path.append( "../../DrawTurksHead/build/darwin_gcc_debug/pyd" )

import django.core.management
import settings

django.core.management.execute_manager( settings )
