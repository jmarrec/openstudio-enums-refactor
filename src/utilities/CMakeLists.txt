set(target_name openstudio_utilities)

set(${target_name}_src
    UtilitiesAPI.hpp
    core/Enum.hpp
    bcl/BCLEnums.hpp
    ${CMAKE_CURRENT_BINARY_DIR}/idd/IddEnums.hxx
    ${CMAKE_CURRENT_BINARY_DIR}/idd/IddFactory.hxx
    ${CMAKE_CURRENT_BINARY_DIR}/idd/IddFactory.cxx
    idd/IddEnums.hpp
)


add_library(${target_name}
  OBJECT
  ${${target_name}_src}
)
set_target_properties(${target_name} PROPERTIES LINKER_LANGUAGE CXX)

set(${target_name}_depends
    fmt::fmt
    boost::boost
)
set(${target_name}_depends ${${target_name}_depends} PARENT_SCOPE)

target_link_libraries(${target_name} PUBLIC ${${target_name}_depends})
target_compile_definitions(${target_name} PRIVATE openstudio_utilities_EXPORTS SHARED_OS_LIBS)
target_include_directories(${target_name} PUBLIC ${PROJECT_BINARY_DIR})
target_include_directories(${target_name} PUBLIC ${PROJECT_BINARY_DIR}/src)
