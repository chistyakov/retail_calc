#!/usr/bin/env sh


cd ./retail_calc/src

if [ "$1" = "tests" ]
then
  echo "run tests"
  python -m unittest discover -s ../tests
fi

if [ "$1" = "calc" ]
then
  echo "run calc"
  python -m calc.main
fi

if [ "$1" = "format" ]
then
  echo "run format"
  black .
fi

if [ "$1" = "static_check" ]
then
  echo "run static check of code"
  echo "run black"
  black --check .
  echo "run mypy"
  mypy .
fi
