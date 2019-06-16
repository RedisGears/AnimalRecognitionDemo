ARG OSNICK=bionic

#----------------------------------------------------------------------------------------------
FROM redislabs/redisedgevision-${OSNICK}:0.1.1

ENV LD_LIBRARY_PATH /usr/lib/redis/modules/

WORKDIR /data

EXPOSE 6379
ENTRYPOINT ["redis-server"]

CMD ["--loadmodule", "/usr/lib/redis/modules/redisai.so", \
	 "--loadmodule", "/usr/lib/redis/modules/redisgears.so", \
	 "PythonHomeDir", "/opt/redislabs/lib/modules/python3/"]
