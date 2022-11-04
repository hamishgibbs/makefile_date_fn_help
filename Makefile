PYTHON_INTERPRETER = python3

.PHONY: default

default: \
	${PWD}/data/grouped/events_20160101.csv

${PWD}/data/grouped/events_20160101.csv: ${PWD}/src/group_data.py \
		${PWD}/data/raw/events_20160101.csv
	$(PYTHON_INTERPRETER) $^ $@
