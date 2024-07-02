import os
import numpy as np
import tifffile as tf

def combine_tiff_to_stack(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all TIFF files in the input folder
    tiff_files = [f for f in os.listdir(input_folder) if f.endswith('.tiff')]
    
    # Sort TIFF files based on their names
    tiff_files.sort()
    
    # Create a list to store image data
    images = []
    
    # Load each TIFF file and append it to the image list
    for tiff_file in tiff_files:
        images.append(tf.imread(os.path.join(input_folder, tiff_file)))
    
    # Save the TIFF stack with explicit compression
    output_path = os.path.join(output_folder, 'stack.tiff')
    tf.imwrite(output_path, np.asarray(images), imagej=True)
    print("Combined TIFF images into TIFF stack.")

# Set the input and output folders
input_folder = 'C:/Users/danie/OneDrive/Documents/SeeByte/semantic_map/mask'  # Change this to your input folder containing TIFF images
output_folder = 'C:/Users/danie/OneDrive/Documents/SeeByte/semantic_map/mask_stack'  # Change this to the desired output folder for the TIFF stack

# Call the function
combine_tiff_to_stack(input_folder, output_folder)
