LIB_NAME := turkshead

THIRD_PARTY_LIBS := cairomm-1.0
LOCAL_LIBS :=
SOURCES := $(filter src/turkshead/%, $(SRC_ALL))
HEADERS := $(filter src/turkshead/%, $(HDR_ALL))

include $(DEV_ENV_ROOT)/mak/link_lib.mak
