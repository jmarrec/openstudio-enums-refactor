# Some operating systems don't like compiling a library with
# no source files
add_library(openstudiolib SHARED empty.cpp)

target_link_libraries(
 openstudiolib
 PRIVATE
 openstudio_utilities
 openstudio_model
)

target_link_libraries(
 openstudiolib
 INTERFACE
 boost::boost
 fmt::fmt
)
target_compile_definitions(openstudiolib INTERFACE "-DSHARED_OS_LIBS")

target_include_directories(
  openstudiolib
  INTERFACE
  $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/src>
  $<BUILD_INTERFACE:${PROJECT_BINARY_DIR}>
  $<BUILD_INTERFACE:${PROJECT_BINARY_DIR}/src>
)
