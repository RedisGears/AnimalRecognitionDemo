FROM redisai/redisai:0.2.0 as redisai
FROM redislabs/redisgears:0.2.1 as redisgears

ENV LD_LIBRARY_PATH /usr/lib/redis/modules/
ENV RUNTIME_DEPS "python python-setuptools python-pip python-dev build-essential libglib2.0-0 libsm6 libxext6 libfontconfig1 libxrender1"
ENV PYTHON_DEPS "setuptools redis argparse imageio opencv-python pybase64 redisAI"

WORKDIR /data

RUN set -ex;\
    apt-get update;\
    apt-get install -y --no-install-recommends $RUNTIME_DEPS;

COPY --from=redisai /usr/lib/redis/modules/*.so* "$LD_LIBRARY_PATH"

RUN pip install -t /usr/local/lib/python2.7/site-packages ${PYTHON_DEPS}

EXPOSE 6379
ENTRYPOINT ["redis-server"]
CMD ["--loadmodule", "/usr/lib/redis/modules/redisai.so", \
    "--loadmodule", "/usr/lib/redis/modules/redisgears.so", \
    "PythonHomeDir", "/usr/lib/redis/modules/deps/cpython/"]
