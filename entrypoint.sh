#!/usr/bin/env sh

firstarg=$1
shift;

cd ./retail_calc/src

if [ "$firstarg" = "tests" ]
then
  echo "run tests"
  python -m unittest discover -s ../tests "$@"
fi

if [ "$firstarg" = "calc" ]
then
  echo "run calc"
  python -m calc.main "$@"
fi

if [ "$firstarg" = "format" ]
then
  echo "run format"
  black . "$@"
fi

if [ "$firstarg" = "static_check" ]
then
  echo "run static check of code"
  echo "run black"
  black --check .
  echo "run mypy"
  mypy .
fi
