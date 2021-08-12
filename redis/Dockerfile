
# OSNICK=stretch|bionic|buster
ARG OSNICK=buster

#----------------------------------------------------------------------------------------------
FROM redis

# This is due on the following error on ARMv8:
# /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block 
# Something is exausting TLS, causing libgomp to fail. Preloading it as a workaround helps.
# ENV LD_PRELOAD /usr/lib/aarch64-linux-gnu/libgomp.so.1

ENV LD_LIBRARY_PATH /usr/lib/redis/modules/

WORKDIR /data

EXPOSE 6379
ENTRYPOINT ["redis-server"]

CMD ["--loadmodule", "/usr/lib/redis/modules/redisai.so", \
	 "--loadmodule", "/usr/lib/redis/modules/redisgears.so", \
	 "PythonHomeDir", "/opt/redislabs/lib/modules/python3/"]

# ADD redisedge.conf /etc

# CMD ['/etc/redisedge.conf']
