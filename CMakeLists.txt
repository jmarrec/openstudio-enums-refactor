cmake_minimum_required(VERSION 3.20)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# Do not enable compiler specific extensions, for eg on GCC use -std=c++1z (=c++17) and not -std=gnu++17
set(CMAKE_CXX_EXTENSIONS OFF)

project(test_enum VERSION 0.1.0 LANGUAGES CXX)

find_package(fmt)
find_package(Boost)

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

add_subdirectory(src/utilities)
add_subdirectory(src/model)
add_subdirectory(src/lib)

add_executable(main
  src/main.cpp
)

target_link_libraries(main PRIVATE openstudiolib)
