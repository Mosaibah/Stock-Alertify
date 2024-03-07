#!/bin/bash

SCRIPTPATH="$(pwd)/dev_setup"

docker-compose -f $SCRIPTPATH/docker-compose.yml up -d

sleep 3

# SETUP DATABASE ROLES AND PERMISSIONS
docker exec database-node sh -c "/cockroach/cockroach sql -u root --insecure  --host=database-node < /docker-entrypoint-initdb.d/init.sql"
