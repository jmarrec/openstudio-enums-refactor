set(target_name openstudio_model)

set(${target_name}_src
  ModelObject.hpp
  ModelObject.cpp
  DefaultScheduleSet.hpp
  DefaultScheduleSet.cpp

  # Start Additions from the python script
  # End Additions from the python script
)

add_library(${target_name}
  OBJECT
  ${${target_name}_src}
)
set(${target_name}_depends
  ${openstudio_utilities_depends}
)

target_link_libraries(${target_name} PUBLIC ${${target_name}_depends})
target_compile_definitions(${target_name} PRIVATE openstudio_model_EXPORTS SHARED_OS_LIBS)
