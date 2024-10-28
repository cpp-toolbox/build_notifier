#!/usr/bin/env python3
import subprocess
import os
import sys
import argparse
import platform

# Define the sound files
def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))


def play_sound(sound_file):
    script_dir = get_script_directory()
    sound_path = os.path.join(script_dir, sound_file)

    if platform.system() == "Windows":
        # Use start command for Windows
        os.system(f'start "{sound_path}"')
    else:
        # Use ffplay for Linux
        os.system(f"ffplay -nodisp -autoexit {sound_path} > /dev/null 2>&1")

def run_cmake_generate(preset):
    try:
        command = f"cmake --preset {preset}"
        result = subprocess.run(command, shell=True, check=True)
        # Command succeeded
        if (preset == "conan-release"): 
            play_sound("sounds/release_generate_success.wav")
        elif (preset == "conan-debug"):
            play_sound("sounds/debug_generate_success.wav")

    except subprocess.CalledProcessError:
        if (preset == "conan-release"): 
            play_sound("sounds/release_generate_success.wav")
        elif (preset == "conan-debug"):
            play_sound("sounds/debug_generate_success.wav")
        pass
        # Command failed
        # if (preset == "conan-release"): 
        #     play_sound("sounds/release_build_failure.mp3")
        # elif (preset == "conan-debug"):
        #     play_sound("sounds/debug_build_failure.wav")

def run_cmake_build(preset):
    try:
        command = f"cmake --build --preset {preset}"
        result = subprocess.run(command, shell=True, check=True)
        # Command succeeded
        if (preset == "conan-release"): 
            play_sound("sounds/release_build_success.mp3")
        elif (preset == "conan-debug"):
            play_sound("sounds/debug_build_success.wav")

    except subprocess.CalledProcessError:
        # Command failed
        if (preset == "conan-release"): 
            play_sound("sounds/release_build_failure.mp3")
        elif (preset == "conan-debug"):
            play_sound("sounds/debug_build_failure.wav")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run CMake build with a preset and play sound based on success or failure.")
    parser.add_argument("-t", "--type", choices=['r', 'd'], required=True, help="Build type: 'r' for release or 'd' for debug")
    parser.add_argument('-g', "--generate", action='store_true', help="Generates the build system before building")
    args = parser.parse_args()

    # Determine the preset based on the argument
    if args.type == 'r':
        preset = "conan-release"
    elif args.type == 'd':
        preset = "conan-debug"
    else:
        parser.print_help()
        sys.exit(1)

    # Run the CMake build
    if args.generate:
        run_cmake_generate(preset)
    run_cmake_build(preset)

if __name__ == "__main__":
    main()
