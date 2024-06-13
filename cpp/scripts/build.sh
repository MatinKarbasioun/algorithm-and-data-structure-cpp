#!/bin/bash
if [ -z "$1" ]; then
  echo "No algorithm type specified. Usage: ./build.sh [greedy|puzzle|dynamic]"
  exit 1
fi

mkdir -p build
cd build

case "$1" in
  greedy)
    cmake -DGREEDY=ON ..
    ;;
  puzzle)
    cmake -DPUZZLE=ON ..
    ;;
  dynamic)
    cmake -DDYNAMIC_PROGRAMMING=ON ..
    ;;
  *)
    echo "Invalid algorithm type. Usage: ./build.sh [greedy|puzzle|dynamic]"
    exit 1
    ;;
esac

make
