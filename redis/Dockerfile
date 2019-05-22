# FROM redisai/redisai:0.2.0 as redisai
# FROM redislabs/redisgears:0.2.1 as redisgears

# FROM redislabs/redisedge-arm:arm64-bionic

FROM raffapen/redisedge-arm:arm64-bionic

ENV LD_LIBRARY_PATH /usr/lib/redis/modules/
ENV DEBIAN_FRONTEND=noninteractive
ENV RUNTIME_DEPS "libglib2.0-0 libsm6 libxext6 libfontconfig1 libxrender1 \
	python3 python3-setuptools python3-pip \
	python3-opencv python3-imageio"
ENV PYTHON_DEPS "setuptools wheel redis argparse pybase64"

WORKDIR /data

RUN set -ex;\
    apt-get update;\
    apt-get install -y --no-install-recommends $RUNTIME_DEPS;

# COPY --from=redisedge ${LD_LIBRARY_PATH}/*.so ${LD_LIBRARY_PATH}/
# COPY --from=redisedge /opt/redislabs/lib/modules/redisgears.so ${LD_LIBRARY_PATH}/
# COPY --from=redisedge /opt/redislabs /opt/redislabs
# COPY /opt/redislabs/lib/modules/redisgears.so ${LD_LIBRARY_PATH}/
                                                                                                                                                                    
RUN pip3 install -t /usr/local/lib/python3/site-packages ${PYTHON_DEPS}

EXPOSE 6379
ENTRYPOINT ["redis-server"]

CMD ["--loadmodule", "/usr/lib/redis/modules/redistimeseries.so", \
     "--loadmodule", "/usr/lib/redis/modules/redisai.so", \
     "--loadmodule", "/usr/lib/redis/modules/redisgears.so", \
     "PythonHomeDir", "/opt/redislabs/lib/modules/python3/"]
