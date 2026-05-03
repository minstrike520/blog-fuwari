#!/usr/bin/env python3

import os
import shutil
import subprocess
import sys
from pathlib import Path

def sync_and_build(blog_content_folder):
    # Convert strings to Path objects for easier manipulation
    content_src_dir = Path(blog_content_folder)
    target_dir = Path("src/content")
    sync_list_file = Path("sync-list.txt")

    # 1. Validation
    if not content_src_dir.exists():
        print(f"Error: Source folder '{blog_content_folder}' does not exist.")
        return

    if not sync_list_file.exists():
        print(f"Error: '{sync_list_file}' not found.")
        return

    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)

    # 2. Read sync-list.txt and copy files
    try:
        with open(sync_list_file, "r") as f:
            # Read lines, strip whitespace, and ignore empty lines
            items_to_copy = [line.strip() for line in f if line.strip()]

        for item in items_to_copy:
            source_path = content_src_dir / item
            destination_path = target_dir / item

            if source_path.exists():
                print(f"Syncing: {item} -> {target_dir}")
                
                # Handle both files and directories
                if source_path.is_dir():
                    # dirs_exist_ok=True allows overwriting existing folders (Python 3.8+)
                    shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
                else:
                    shutil.copy2(source_path, destination_path)
            else:
                print(f"Warning: {item} not found in {content_src_dir}. Skipping.")

    except Exception as e:
        print(f"An error occurred during sync: {e}")
        return

    # 3. Run pnpm build
    print("\nRunning 'pnpm build'...")
    try:
        # shell=True is used if pnpm is an alias/cmd on Windows; 
        # check_True ensures we stop if the build fails.
        subprocess.run(["pnpm", "build"], check=True)
        print("Build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error code: {e.returncode}")
    except FileNotFoundError:
        print("Error: 'pnpm' command not found. Is it installed?")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sync_and_build.py <blog_content_folder>")
    else:
        sync_and_build(sys.argv[1])

"""
args: $1(blog_content_folder): a folder path string

run:
read file "sync-list.txt"
the file is a list of files or folders
foreach $file:
    cp -R $blog_content_folder/$file to src/content/
run command "pnpm build"
"""
