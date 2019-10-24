
start:
ifeq ($(REBUILD),1)
	@docker-compose up --build -d
else
	@docker-compose up -d
endif

stop:
	@docker-compose down

test:
	@./tests/cats-n-dogs.sh

ifdef REDIS
CAMERA_ARG=-u $(REDIS)
endif

camera:
ifneq ($(VENV),0)
	python2 -m virtualenv venv
	. ./venv/bin/activate; pip install -r camera/requirements.txt
	. ./venv/bin/activate; python camera/read_camera.py $(CAMERA_ARG)
else
	python2 camera/read_camera.py $(CAMERA_ARG)
endif

setup:
	@if [ -z `command -v docker-compose` ]; then \
		curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose ;\
		chmod +x /usr/local/bin/docker-compose ;\
	fi

.PHONY: start stop test camera setup
