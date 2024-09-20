#!/usr/bin/env python3

import subprocess
import os
import sys
import argparse

# Define the sound files
def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))

def play_sound(sound_file):
    script_dir = get_script_directory()
    sound_path = os.path.join(script_dir, sound_file)
    # Redirect stdout and stderr to /dev/null to suppress output
    os.system(f"mpg123 -q {sound_path} > /dev/null 2>&1")

def run_cmake_build(preset):
    try:
        command = f"cmake --build --preset {preset}"
        result = subprocess.run(command, shell=True, check=True)
        # Command succeeded
        play_sound("success.mp3")
    except subprocess.CalledProcessError:
        # Command failed
        play_sound("failure.mp3")

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run CMake build with a preset and play sound based on success or failure.")
    parser.add_argument("-t", "--type", choices=['r', 'd'], required=True, help="Build type: 'r' for release or 'd' for debug")
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
    run_cmake_build(preset)

if __name__ == "__main__":
    main()
