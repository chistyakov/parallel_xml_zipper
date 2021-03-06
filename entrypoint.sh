#!/usr/bin/env sh


cd ./xml_zipper/src

if [ "$1" = "tests" ]
then
  echo "run tests"
  python -m pytest ../tests/ -vv
fi

if [ "$1" = "generate" ]
then
  echo "run generator"
  python -m xml_zipper.main generate /data
fi

if [ "$1" = "analyze" ]
then
  echo "run analyzer"
  python -m xml_zipper.main analyze /data
fi
