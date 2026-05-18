# Fake having produced the IddEnums.hxx file
configure_file(IddEnums.hxx "${CMAKE_CURRENT_BINARY_DIR}/../utilities/idd/IddEnums.hxx" COPYONLY)
configure_file(IddFactory.hxx "${CMAKE_CURRENT_BINARY_DIR}/../utilities/idd/IddFactory.hxx" COPYONLY)
configure_file(IddFactory.cxx "${CMAKE_CURRENT_BINARY_DIR}/../utilities/idd/IddFactory.cxx" COPYONLY)
