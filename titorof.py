import os

# Define paths to the Titanium and RoF2 directories
titanium_dir = 'F:/eqti'
rof2_dir = 'C:/Users/Dan/Desktop/rof/everquest_rof2'

# Get list of .s3d and .zone files in each directory
titanium_files = {f for f in os.listdir(titanium_dir)}
rof2_files = {f for f in os.listdir(rof2_dir)}

# Find files in Titanium that are not in RoF2
titanium_only_files = sorted(titanium_files - rof2_files, key=lambda s: s.lower())

# Optionally, write the results to a file
with open("titanium_only_files.txt", "w") as output_file:
    for file in titanium_only_files:
        output_file.write(f"{file}\n")
