ARG OSNICK=bionic

#----------------------------------------------------------------------------------------------
FROM raffapen/redisedgevision-${OSNICK}:latest

ENV LD_LIBRARY_PATH /usr/lib/redis/modules/

WORKDIR /data

EXPOSE 6379
ENTRYPOINT ["redis-server"]

# RUN apt-get install -y libtbb2 zlib1g libswscale4 libjpeg62 libjpeg8 libpng16-16 libtiff5 libavformat57 libilmbase12 libopenexr22

CMD ["--loadmodule", "/usr/lib/redis/modules/redistimeseries.so", \
	 "--loadmodule", "/usr/lib/redis/modules/redisai.so", \
	 "--loadmodule", "/usr/lib/redis/modules/redisgears.so", \
	 "PythonHomeDir", "/opt/redislabs/lib/modules/python3/"]
