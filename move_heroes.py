#!/usr/bin/env python3
"""Move and Rename Files with Safety Checks"""

import shutil
import os

def main():
    """Main logic"""
    os.chdir("/home/student/mycode/")

    # Check if raynor.obj exists in battlecruiser
    if os.path.exists("battlecruiser/raynor.obj"):
        overwrite = input("raynor.obj already exists in battlecruiser. Overwrite? (yes/no): ")
        if overwrite.lower() != "yes":
            print("Operation canceled.")
            return

    # Move Raynor to battlecruiser
    shutil.move("raynor.obj", "battlecruiser/")

    # Prompt for Kerrigan's new name
    xname = input("What is the new name for kerrigan.obj? ")

    # Rename Kerrigan
    if os.path.exists(f"battlecruiser/{xname}"):
        overwrite = input(f"{xname} already exists in battlecruiser. Overwrite? (yes/no): ")
        if overwrite.lower() != "yes":
            print("Operation canceled.")
            return

    shutil.move("battlecruiser/kerrigan.obj", f"battlecruiser/{xname}")

main()

