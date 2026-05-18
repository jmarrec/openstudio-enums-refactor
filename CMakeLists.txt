cmake_minimum_required(VERSION 3.20)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# Do not enable compiler specific extensions, for eg on GCC use -std=c++1z (=c++17) and not -std=gnu++17
set(CMAKE_CXX_EXTENSIONS OFF)

project(test_enum VERSION 0.1.0 LANGUAGES CXX)

find_package(fmt)
find_package(Boost)

# High level project configuration
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/Products")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/Products")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/Products")

set(LIBRARY_SEARCH_DIRECTORY "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}" "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/Release" "${CMAKE_LIBRARY_OUTPUT_DIRECTORY}/Debug")

if(UNIX)

  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -fPIC -fno-strict-aliasing")

  # all warnings
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -fPIC -fno-strict-aliasing")
endif()

if(MSVC)
  # warning level 3
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W3")
  add_compile_options(/utf-8)

endif()

# Enable runtime checking features
if(CMAKE_CXX_COMPILER_ID MATCHES ".*Clang")

  option(ENABLE_BUILD_TIME_TRACE "Enable -ftime-trace feature on clang" OFF)
  if (ENABLE_BUILD_TIME_TRACE)
    add_definitions(-ftime-trace)
  endif()

  mark_as_advanced(ENABLE_BUILD_TIME_TRACE)

endif()

# Add to include path

# Project source directory
include_directories("${PROJECT_SOURCE_DIR}/src/")

# Project binary directory
include_directories("${PROJECT_BINARY_DIR}/src/")

add_subdirectory(src/generateiddfactory)
add_subdirectory(src/utilities)
add_subdirectory(src/model)
add_subdirectory(src/lib)

add_executable(main
  src/main.cpp
)

target_link_libraries(main PRIVATE openstudiolib)
