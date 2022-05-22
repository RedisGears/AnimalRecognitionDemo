define HELP
make start    # Start containers
make stop     # Stop containers
make clean    # Remove demo containers and images
make test     # Run test
  VERBOSE=1     # Show more detailed information
make camera   # Start camera process
make setup    # Install prerequisites

endef

#----------------------------------------------------------------------------------------------

start:
	@docker-compose up -d

stop:
	@docker-compose down

build:
	@docker-compose build

test:
	@./tests/cats-n-dogs.sh

clean:
	@./tests/cats-n-dogs.sh clean

ifdef REDIS
CAMERA_ARG=-u $(REDIS)
endif

camera:
ifeq ($(VIRTUAL_ENV),'')
	python3 -m venv venv
	. ./venv/bin/activate; pip install -r camera/requirements.txt
	. ./venv/bin/activate; python camera/read_camera.py $(CAMERA_ARG)
else
	python3 camera/read_camera.py $(CAMERA_ARG)
endif

setup:
	@$(SUDO) curl -s -L https://github.com/docker/compose/releases/download/1.25.4/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose ;\
	$(SUDO) chmod +x /usr/local/bin/docker-compose
	@wget -q https://github.com/git-lfs/git-lfs/releases/download/v2.10.0/git-lfs-linux-amd64-v2.10.0.tar.gz -O /tmp/git-lfs.tar.gz ;\
    cd /tmp; tar xf git-lfs.tar.gz; $(SUDO) ./install.sh
	@git lfs pull

.PHONY: start stop build test camera setup help

#----------------------------------------------------------------------------------------------

ifneq ($(HELP),) 
ifneq ($(filter help,$(MAKECMDGOALS)),)
HELPFILE:=$(shell mktemp /tmp/make.help.XXXX)
endif
endif

help:
	$(file >$(HELPFILE),$(HELP))
	@echo
	@cat $(HELPFILE)
	@echo
	@-rm -f $(HELPFILE)
