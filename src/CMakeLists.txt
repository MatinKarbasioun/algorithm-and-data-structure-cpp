cmake_minimum_required(VERSION 3.28)
project(Algorithm)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)


# Source files
set(SOURCES
        src/main.cpp
        src/puzzle/puzzle.cpp
        src/puzzle/fibonacci/fibonacci.cpp
        src/common/decimal/decimal.cpp
        src/common/helper/elapse.cpp
        src/sorting/quick_sort.cpp
        src/sorting/sorting.cpp
        src/data_structure/stack/find_matched_brakcets.cpp
        src/data_structure/tree/binary/binary_tree.cpp
        src/data_structure/tree/binary/binary_tree.h
)

# Executable
add_executable(Algorithm ${SOURCES})


# Add included directories
target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_SOURCE_DIR}/include)


# Optional: Add any necessary libraries to link against
# target_link_libraries(${PROJECT_NAME} <library_name>)

# Optional: Add definitions or compile options
# target_compile_definitions(${PROJECT_NAME} PRIVATE <definitions>)
# target_compile_options(${PROJECT_NAME} PRIVATE <options>)