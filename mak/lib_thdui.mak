LIB_NAME := thdui

THIRD_PARTY_LIBS := gtkmm-2.4
LOCAL_LIBS := turkshead
SOURCES := $(filter src/thdui/%, $(SRC_ALL))
HEADERS := $(filter src/thdui/%, $(HDR_ALL))

include $(DEV_ENV_ROOT)/mak/link_lib.mak
