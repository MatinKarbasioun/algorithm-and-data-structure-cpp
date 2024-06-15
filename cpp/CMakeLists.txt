cmake_minimum_required(VERSION 3.28)
project(Algorithm)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add included directories
include_directories(include)


# Source files
set(SOURCES
        src/main.cpp
        src/puzzle/puzzle.cpp
        src/puzzle/fibonacci/fibonacci.cpp
        src/common/decimal/decimal.cpp
        src/common/helper/elapse.cpp
)

# Executable
add_executable(Algorithm ${SOURCES})

