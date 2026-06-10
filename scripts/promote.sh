#!/bin/bash

SOURCE_IMAGE=$1
TARGET_IMAGE=$2

LOGFILE=promotion.log

echo "===================================" >> $LOGFILE
echo "Promotion Started: $(date)" >> $LOGFILE

echo "Pulling image..." >> $LOGFILE
docker pull $SOURCE_IMAGE

if [ $? -ne 0 ]; then
  echo "Pull failed" >> $LOGFILE
  exit 1
fi

echo "Tagging image..." >> $LOGFILE
docker tag $SOURCE_IMAGE $TARGET_IMAGE

echo "Validating image..." >> $LOGFILE
docker image inspect $TARGET_IMAGE > /dev/null

if [ $? -ne 0 ]; then
  echo "Validation failed" >> $LOGFILE
  exit 1
fi

echo "Pushing image..." >> $LOGFILE
docker push $TARGET_IMAGE

if [ $? -ne 0 ]; then
  echo "Push failed" >> $LOGFILE
  exit 1
fi

echo "Promotion Successful" >> $LOGFILE
echo "===================================" >> $LOGFILE
