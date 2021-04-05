# OSNICK=stretch|bionic|buster
ARG OSNICK=bionic

#----------------------------------------------------------------------------------------------
FROM redisfab/redisedge:0.4.0-x64-${OSNICK}

# This is due on the following error on ARMv8:
# /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block 
# Something is exausting TLS, causing libgomp to fail. Preloading it as a workaround helps.
# ENV LD_PRELOAD /usr/lib/aarch64-linux-gnu/libgomp.so.1

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update

RUN set -ex ;\
	apt-get install -y python3 python3-pip ;\
	pip3 install --upgrade pip

WORKDIR /app
ADD . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]
