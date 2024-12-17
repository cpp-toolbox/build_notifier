# build notifier
a tiny script that runs the cmake build command for conan building, has sound effects

Every project here uses conan for package management, so you usually have to run the command cmake --build --preset conan-release multiple times. This notifier makes it easier by playing a success or fail sound when compilation finishes, so you can stop staring at the build process and continue working in the meantime.


build for release
```sh
build.py -t r
```

build for debug
```sh
build.py -t d
```
