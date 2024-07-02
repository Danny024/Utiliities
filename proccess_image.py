import os
from PIL import Image

def convert_png_to_tiff(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)
        
        # Check if the file is a PNG image
        if os.path.isfile(input_path) and file_name.lower().endswith('.jpg'):
            # Load the image
            image = Image.open(input_path)
            
            # Construct the output file path with a .tiff extension
            output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.tiff')
            
            # Convert and save the image as TIFF
            image.save(output_path, format='TIFF')
            print(f"Converted {file_name} to TIFF.")

# Set the input and output folders
input_folder = 'C:/Users/danie/OneDrive/Documents/SeeByte/semantic_map/train'  # Change this to your input folder containing PNG images
output_folder = 'C:/Users/danie/OneDrive/Documents/SeeByte/semantic_map/labeled_image'  # Change this to the desired output folder for TIFF images

# Call the conversion function
convert_png_to_tiff(input_folder, output_folder)
