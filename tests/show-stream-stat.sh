#!/bin/bash

if [[ -z $DOCKER_HOST ]]; then
	host_arg=""
else
	host_arg="-h $(echo $DOCKER_HOST|cut -d: -f1)"
fi

stream_size() {
	echo $(redis-cli $host_arg xlen $1|cat)
}

echo camera: $(stream_size camera:0)
echo all: $(stream_size all)
echo cats: $(stream_size cats)
echo log: $(stream_size log)
