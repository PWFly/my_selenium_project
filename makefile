run-test:
    export PYTHONPATH=$(PWD) && python -m test.test_event_tracking
.PHONY: run-test

