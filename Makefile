PYTHON_INTERPRETER = python3

.PHONY: default

default: \
	$(subst raw,grouped,$(wildcard ${PWD}/data/raw/events_*.csv))

${PWD}/data/grouped/events_%.csv: ${PWD}/src/group_data.py \
		${PWD}/data/raw/events_%.csv
	$(PYTHON_INTERPRETER) $^ $@
