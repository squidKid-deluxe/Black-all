# usr/bin/python3.7
"""
A simple script that compresses *.jpg image files.
"""

# Import necessary modules
import os
from time import time


def main():
    """
    Main process, does it all
    """
    # Get the start time
    start = time()

    # Clear the screen
    print("\033c")

    # Get all of the python files in the current folder
    pythons = [
        filer
        for filer in os.listdir()
        if filer.endswith(".py")
    ]


    # For every file in that list:
    for name in pythons:
        # Print the script we are blacking.
        print("Blacking script:", name)

        # Black the script.
        os.system(f"black {name}")

        # Say we are done.
        print("Done.")

        # Print a divider.
        print("-" * 100)

    # Get the end time:
    end = time()

    # Find the time it took to black the scripts.
    took = end - start

    # Print that time.
    print("Blacking", len(pythons), "scripts took", took, "seconds.")


if __name__ == "__main__":
    main()
