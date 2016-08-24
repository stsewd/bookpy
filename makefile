VENV_DIR = venv

PYTHON = python3

TEST_FLAGS = discover -v

TEST_MODULE = unittest

all:
	echo "Nothing yet"

test: venv
	${PYTHON} -m ${TEST_MODULE} ${TEST_FLAGS}

venv:
	source ${VENV_DIR}/bin/activate
