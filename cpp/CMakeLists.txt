cmake_minimum_required(VERSION 3.10)
project(AlgorithmTasks)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add Glob files to prevent list them individualy
file(GLOB SOURCES "src/*.cpp")
file(GLOB DECIMAL_SOURCES "src/common/decimal/*.cpp")
file(GLOB HELPER_SOURCES "src/common/helper/*.cpp")

# Add source files
add_executable(AlgorithmTasks
    src/main.cpp
    ${DECIMAL_SOURCES}
    ${HELPER_SOURCES}
)

# Include directories to ensure all headers included and libraries
target_include_directories(AlgorithmTasks PRIVATE
    src/puzzles/fibonacci
    src/common/decimal
    src/common/helper
)