import sys
from pathlib import Path

from conan import ConanFile
from conan.tools.apple import is_apple_os
from conan.tools.cmake import CMakeToolchain

required_conan_version = ">=2.0"


class OpenStudioEnumBuildRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        if is_apple_os(self):
            self.requires("boost/1.86.0", force=True, options={"visibility": "global"})
        else:
            self.requires("boost/1.86.0", force=True)  # cpprestsdk doesn't build with boost 1.87.0
        self.requires("fmt/12.1.0")
