
# OSNICK=stretch|bionic|buster
ARG OSNICK=buster

#----------------------------------------------------------------------------------------------
FROM redisfab/redisedgevision-${OSNICK}:0.1.0

ENV LD_PRELOAD /usr/lib/aarch64-linux-gnu/libgomp.so.1
ENV LD_LIBRARY_PATH /usr/lib/redis/modules/

WORKDIR /data

EXPOSE 6379
ENTRYPOINT ["redis-server"]

CMD ["--loadmodule", "/usr/lib/redis/modules/redisai.so", \
	 "--loadmodule", "/usr/lib/redis/modules/redisgears.so", \
	 "PythonHomeDir", "/opt/redislabs/lib/modules/python3/"]
