

#----------------------------------------------------------------------------------------------
FROM redislabs/redismod:edge

# This is due on the following error on ARMv8:
# /usr/lib/aarch64-linux-gnu/libgomp.so.1: cannot allocate memory in static TLS block 
# Something is exausting TLS, causing libgomp to fail. Preloading it as a workaround helps.
# ENV LD_PRELOAD /usr/lib/aarch64-linux-gnu/libgomp.so.1

WORKDIR /data

EXPOSE 6379

# ADD redisedge.conf /etc

# CMD ['/etc/redisedge.conf']
