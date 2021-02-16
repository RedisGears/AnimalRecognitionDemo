
# OSNICK=stretch|bionic|buster
ARG OSNICK=bionic

#----------------------------------------------------------------------------------------------
FROM redisfab/redisedge:0.2.0-x64-${OSNICK}

# This is due on the following error on ARMv8:
# /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block 
# Something is exausting TLS, causing libgomp to fail. Preloading it as a workaround helps.
# ENV LD_PRELOAD /usr/lib/aarch64-linux-gnu/libgomp.so.1

ENV LD_LIBRARY_PATH /usr/lib/redis/modules/

WORKDIR /data

EXPOSE 6379
ENTRYPOINT ["redis-server"]

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

CMD ["--loadmodule", "/usr/lib/redis/modules/redisai.so", \
	"--loadmodule", "/usr/lib/redis/modules/redisgears.so", \
	"PythonHomeDir", "/opt/redislabs/lib/modules/python3/"]

# ADD redisedge.conf /etc

# CMD ['/etc/redisedge.conf']
