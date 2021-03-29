# OSNICK=stretch|bionic|buster
ARG OSNICK=buster

#----------------------------------------------------------------------------------------------
FROM redisfab/redisedgevision-${OSNICK}:0.2.0

# This is due on the following error on ARMv8:
# /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block
# Something is exausting TLS, causing libgomp to fail. Preloading it as a workaround helps.

ENV LD_PRELOAD /usr/lib/aarch64-linux-gnu/libgomp.so.1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update && apt-get install -qqy wget python3-distutils patch
RUN wget -q https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && python3 /tmp/get-pip.py

WORKDIR /app
ADD . /app

# patch init script for aarch64
RUN patch init.py init.patch
RUN patch gear.py gear.patch

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]
