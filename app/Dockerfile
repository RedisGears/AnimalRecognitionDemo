
#----------------------------------------------------------------------------------------------
FROM redislabs/redismod:edge

# This is due on the following error on ARMv8:
# /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block 
# Something is exausting TLS, causing libgomp to fail. Preloading it as a workaround helps.
# ENV LD_PRELOAD /usr/lib/aarch64-linux-gnu/libgomp.so.1

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update

RUN set -ex ;\
	apt-get -qq install -y python3 python3-pip > /dev/null;\
	python3 -m pip install --upgrade pip

WORKDIR /app
ADD . /app

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
