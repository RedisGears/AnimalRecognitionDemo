# FROM redisai/redisai:0.2.0 as redisai
# FROM redislabs/redisgears:0.2.1 as redisgears

# FROM redislabs/redisedge-arm:arm64-bionic

FROM raffapen/redisedge-arm:arm64-bionic
# FROM raffapen/redisedge:x64-bionic

ENV LD_LIBRARY_PATH /usr/lib/redis/modules/
ENV DEBIAN_FRONTEND=noninteractive
ENV RUNTIME_DEPS "\
	libglib2.0-0 libsm6 libxext6 libfontconfig1 libxrender1 \
	ca-certificates curl \
	python3 python3-setuptools \
	python3-imageio"
ENV PYTHON_DEPS "redis"

WORKDIR /data

RUN set -ex;\
	apt-get update;\
	apt-get install -y --no-install-recommends $RUNTIME_DEPS;

RUN curl -s https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py; \
	python3 /tmp/get-pip.py

# COPY --from=redisedge ${LD_LIBRARY_PATH}/*.so ${LD_LIBRARY_PATH}/
# COPY --from=redisedge /opt/redislabs/lib/modules/redisgears.so ${LD_LIBRARY_PATH}/
# COPY --from=redisedge /opt/redislabs /opt/redislabs
# COPY /opt/redislabs/lib/modules/redisgears.so ${LD_LIBRARY_PATH}/
                                                                                                                                                                    
RUN pip3 install -t /usr/local/lib/python3/site-packages ${PYTHON_DEPS}

RUN apt-get install -y libswscale4 libtbb2 libjpeg8 libpng16-16 libtiff5 libavformat57 zlib1g 

EXPOSE 6379
ENTRYPOINT ["redis-server"]

CMD ["--loadmodule", "/usr/lib/redis/modules/redistimeseries.so", \
	 "--loadmodule", "/usr/lib/redis/modules/redisai.so", \
	 "--loadmodule", "/usr/lib/redis/modules/redisgears.so", \
	 "PythonHomeDir", "/opt/redislabs/lib/modules/python3/"]
