PYTHON = python3

TEST_FLAGS = discover -v

TEST_MODULE = unittest

TEST_RESOURCES = tests_resources

TEST_RESOURCES_BACK = tests_resources_back

PIP = pip3

install-develop-mode:
	${PIP} install -e .

install:
	${PIP} install .

test: backup-test-resources recover-test-resources
	${PYTHON} -m ${TEST_MODULE} ${TEST_FLAGS}

recover-test-resources:
	rm -rf ${TEST_RESOURCES}/*
	cp $(TEST_RESOURCES_BACK)/* ${TEST_RESOURCES}

backup-test-resources:
	if [ -d ${TEST_RESOURCES_BACK} ]; then \
		echo "Backup already created"; \
	else \
		mkdir ${TEST_RESOURCES_BACK}; \
		cp ${TEST_RESOURCES}/* $(TEST_RESOURCES_BACK); \
	fi

clean-tests: recover-test-resources
	rm -rf ${TEST_RESOURCES_BACK}

clean: clean-tests
