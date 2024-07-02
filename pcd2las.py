import numpy as np
import laspy

def pcd_to_las(pcd_filename, las_filename):
    # Read PCD file in binary mode and decode using 'utf-8'
    with open(pcd_filename, 'rb') as f:
        lines = f.readlines()

    # Convert bytes to string using 'utf-8' encoding
    lines = [line.decode('utf-8', errors='ignore') for line in lines]

    # Extract points from PCD file
    points = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 3:
            try:
                x, y, z = map(float, parts[:3])
                points.append([x, y, z])
            except ValueError:
                continue

    # Convert points to numpy array
    points_array = np.array(points)

    # Create a LAS file
    las_header = laspy.header.LasHeader()
    las_file = laspy.create(point_format=2, file_version='1.2')

    # Set LAS header and points
    las_file.header = las_header
    las_file.points = points_array

    # Write LAS file
    las_file.close()

    # Reopen the LAS file to write the points
    las_file = laspy.file.File(las_filename, mode='w', header=las_header)
    las_file.points = points_array

    # Close LAS file
    las_file.close()

# Usage
pcd_filename = 'C:/Users/danie/Downloads/1708531518.117043310 (1).pcd'
las_filename = 'lascheck.las'
pcd_to_las(pcd_filename, las_filename)
