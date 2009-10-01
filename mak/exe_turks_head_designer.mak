EXE_NAME := turks_head_designer

THIRD_PARTY_LIBS := gtkmm-2.4 boost_program_options
LOCAL_LIBS := thdui turkshead
SOURCES := src/turks_head_designer.cpp

include $(DEV_ENV_ROOT)/mak/link_exe.mak
