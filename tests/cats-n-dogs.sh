#!/bin/bash

[[ $VERBOSE == 1 ]] && set -x

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"  
cd $HERE/..

if [[ -z $DOCKER_HOST ]]; then
	host_arg=""
else
	host_arg="-h $(echo $DOCKER_HOST|cut -d: -f1)"
fi

PROJECT=catsndogs
DOCKER_LOG=/tmp/cats-n-dogs.log
SPEC="--no-ansi -p $PROJECT -f docker-compose.yaml -f tests/cats-n-dogs.yaml"

rm -f $DOCKER_LOG

start() {
	if [[ $VERBOSE == 1 ]]; then
		ANIMAL=$1 docker-compose $SPEC up -d
	else
		ANIMAL=$1 docker-compose $SPEC up -d >> $DOCKER_LOG 2>&1
	fi
}

stop() {
	if [[ $VERBOSE == 1 ]]; then
		ANIMAL=$1 docker-compose $SPEC down -v --remove-orphans
	else
		ANIMAL=$1 docker-compose $SPEC down -v --remove-orphans >> $DOCKER_LOG 2>&1
	fi
}

cats_demo() {
	echo "Testing ${1}s ..."
	# local PROJECT=${PROJECT}_$1
	start $1
	sleep 3
	num_cats=$(redis-cli $host_arg xlen cats | cat)
	stop $1
}

if [[ $1 == help ]]; then
	echo "$0: [start ANIMAL|stop|help]"
	exit 0
elif [[ $1 == start ]]; then
	shift
	VERBOSE=1 start $1
elif [[ $1 == stop ]]; then
	shift
	VERBOSE=1 stop $1
else
	cats_demo cat
	if [[ $num_cats == 0 ]]; then
		echo "cats: FAIL"
		exit 1
	fi
	echo "cats: OK"

	cats_demo dog
	if [[ $num_cats != 0 ]]; then
		echo "dogs: FAIL"
		exit 1
	fi

	echo "dogs: OK"
fi
exit 0
