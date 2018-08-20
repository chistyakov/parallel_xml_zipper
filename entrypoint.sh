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
fi

if [ "$1" = "analyze" ]
then
  echo "run analyzer"
fi
