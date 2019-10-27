#!/bin/bash

# [[ $VERBOSE == 1 ]] && set -x

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
[[ $REBUILD == 1 ]] && BUILD_ARG=--build

rm -f $DOCKER_LOG

start() {
	if [[ $VERBOSE == 1 ]]; then
		docker-compose $SPEC up $BUILD_ARG -d
	else
		docker-compose $SPEC up $BUILD_ARG -d >> $DOCKER_LOG 2>&1
	fi
	BUILD_ARG=''
}

stop() {
	if [[ $VERBOSE == 1 ]]; then
		docker-compose $SPEC down -v --remove-orphans
	else
		docker-compose $SPEC down -v --remove-orphans >> $DOCKER_LOG 2>&1
	fi
}

build() {
	if [[ $VERBOSE == 1 ]]; then
		docker-compose $SPEC build
	else
		docker-compose $SPEC build >> $DOCKER_LOG 2>&1
	fi
}

show_logs() {
	docker-compose $SPEC logs $*
}

cats_demo() {
	echo "Testing ${ANIMAL}s ..."
	start
	sleep 3
	num_cats=$(redis-cli $host_arg xlen cats | cat)
	if [[ $VERBOSE == 1 ]]; then
		echo "num_cats=$num_cats"
		show_logs
	else
		echo "num_cats=$num_cats" >> $DOCKER_LOG
		show_logs >> $DOCKER_LOG
	fi
	stop
}

cmd=$1
shift
if [[ $cmd == help ]]; then
	echo "[ANIMAL=cat|dog] [VERBOSE=0|1] [REBUILD=0|1] $0 [start|stop|build|logs|help]"
	exit 0
elif [[ $cmd == start ]]; then
	start
elif [[ $cmd == stop ]]; then
	stop
elif [[ $cmd == build ]]; then
	build
elif [[ $cmd == logs ]]; then
	show_logs $*
else
	ANIMAL=cat cats_demo
	if [[ -z $num_cats || $num_cats == 0 ]]; then
		echo "cats: FAIL"
		exit 1
	fi
	echo "cats: OK"

	ANIMAL=dog cats_demo
	if [[ -z $num_cats || $num_cats != 0 ]]; then
		echo "dogs: FAIL"
		exit 1
	fi

	echo "dogs: OK"
fi
exit 0
