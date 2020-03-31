
start:
	@docker-compose up -d

stop:
	@docker-compose down

build:
	@docker-compose build

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
	@curl -s -L https://github.com/docker/compose/releases/download/1.25.4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose ;\
	chmod +x /usr/local/bin/docker-compose
	@wget -q https://github.com/git-lfs/git-lfs/releases/download/v2.10.0/git-lfs-linux-amd64-v2.10.0.tar.gz -O /tmp/git-lfs.tar.gz ;\
    cd /tmp; tar xf git-lfs.tar.gz; ./install.sh
	@git lfs pull

.PHONY: start stop build test camera setup
