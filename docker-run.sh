#!/usr/bin/env bash

case "$1" in
  build)
    docker build --tag frontend frontend/ &
    docker build --tag converter converter/ &
    docker build --tag store store/
    ;;
  run)
    docker network create --driver bridge --subnet=192.168.0.0/16 flask-net
    docker run -d --network flask-net --ip 192.168.1.1 --name converter converter &
    docker run -d --network flask-net --ip 192.168.1.2 --name store store &
    docker run -d --network flask-net --ip 192.168.1.3 -p 8080:5000 --name frontend frontend
    ;;
  kill)
    docker kill frontend converter store
    docker network rm flask-net
    ;;
  rm)
    docker container rm frontend store converter && docker image rm frontend:latest store:latest converter:latest
    ;;
  *)
    echo "usage $0 build | run | kill | rm"
    exit -1
    ;;
esac