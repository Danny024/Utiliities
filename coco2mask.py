'''
This code is a property of Seebyte and it was written in order to convert a COCO json dataset format into
a label and mask ........

'''
import json
import numpy as np
import skimage
import tifffile
import os
import shutil


def create_mask(image_info, annotations, output_folder):
    # Create an empty mask as a numpy array
    mask_np = np.zeros((image_info['height'], image_info['width']), dtype=np.uint16)

    # Counter for the object number
    object_number = 1

    for ann in annotations:
        if ann['image_id'] == image_info['id']:
            # Extract segmentation polygon
            for seg in ann['segmentation']:
                # Convert polygons to a binary mask and add it to the main mask
                rr, cc = skimage.draw.polygon(seg[1::2], seg[0::2], mask_np.shape)
                mask_np[rr, cc] = object_number
                object_number += 1 #We are assigning each object a unique integer value (labeled mask)

    # Save the numpy array as a TIFF using tifffile library
    mask_path = os.path.join(output_folder, image_info['file_name'].replace('.tif', '_mask.tif'))
    tifffile.imwrite(mask_path, mask_np)

    print(f"Saved mask for {image_info['file_name']} to {mask_path}")


def main(json_file, mask_output_folder, image_output_folder, original_image_dir):
    # Load COCO JSON annotations
    with open(json_file, 'r') as f:
        data = json.load(f)

    images = data['images']
    annotations = data['annotations']

    # Ensure the output directories exist
    if not os.path.exists(mask_output_folder):
        os.makedirs(mask_output_folder)
    if not os.path.exists(image_output_folder):
        os.makedirs(image_output_folder)

    for img in images:
        # Create the masks
        create_mask(img, annotations, mask_output_folder)
        
        # Copy original images to the specified folder
        original_image_path = os.path.join(original_image_dir, img['file_name'])
    
        new_image_path = os.path.join(image_output_folder, os.path.basename(original_image_path))
        shutil.copy2(original_image_path, new_image_path)
        print(f"Copied original image to {new_image_path}")



if __name__ == '__main__':
    original_image_dir = 'C:/Users/danie/OneDrive/Documents/SeeByte/semantic_map/labeled_image'  # Where your original images are stored
    json_file = 'C:/Users/danie/OneDrive/Documents/SeeByte/semantic_map/annotation/train_annotations.coco.json'
    mask_output_folder = 'C:/Users/danie/OneDrive/Documents/SeeByte/semantic_map/mask'  # Modify this as needed. Using val2 so my data is not overwritten
    image_output_folder = 'C:/Users/danie/OneDrive/Documents/SeeByte/semantic_map/output'  # 
    main(json_file, mask_output_folder, image_output_folder, original_image_dir)


