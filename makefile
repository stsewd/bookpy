PYTHON = python3

TEST_FLAGS = discover -v

TEST_MODULE = unittest

all:
	echo "Nothing yet"

test:
	${PYTHON} -m ${TEST_MODULE} ${TEST_FLAGS}
