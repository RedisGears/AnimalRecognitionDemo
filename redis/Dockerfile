# FROM redisai/redisai:0.2.0 as redisai
# FROM redislabs/redisgears:0.2.1 as redisgears

# FROM redislabs/redisedge-arm:arm64-bionic

FROM raffapen/redisedge-arm:arm64-bionic as redisedge

ENV LD_LIBRARY_PATH /usr/lib/redis/modules/
ENV RUNTIME_DEPS "python python-setuptools python-pip python-dev build-essential libglib2.0-0 libsm6 libxext6 libfontconfig1 libxrender1"
ENV PYTHON_DEPS "setuptools redis argparse imageio opencv-python pybase64 redisAI"

WORKDIR /data

RUN set -ex;\
    apt-get update;\
    apt-get install -y --no-install-recommends $RUNTIME_DEPS;

COPY --from=redisedge ${LD_LIBRARY_PATH}/*.so ${LD_LIBRARY_PATH}/                                                                                             
COPY --from=redisedge /opt/redislabs/lib/modules/redisgears.so ${LD_LIBRARY_PATH}/                                                                                 
COPY --from=redisedge /opt/redislabs /opt/redislabs                                                                                                                
                                                                                                                                                                    
RUN pip install -t /usr/local/lib/python3/site-packages ${PYTHON_DEPS}

EXPOSE 6379
ENTRYPOINT ["redis-server"]

CMD ["--loadmodule", "/usr/lib/redis/modules/redistimeseries.so", \
     "--loadmodule", "/usr/lib/redis/modules/redisai.so", \
     "--loadmodule", "/usr/lib/redis/modules/redisgears.so", \
     "PythonHomeDir", "/opt/redislabs/lib/modules/python3/"]
