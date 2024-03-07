#!/bin/bash

SCRIPTPATH="$(pwd)/dev_setup"

docker-compose -f $SCRIPTPATH/docker-compose.yml down  --remove-orphans --volumes
