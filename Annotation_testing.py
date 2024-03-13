import json
import os
from PIL import Image

# Increase the maximum image pixel limit
Image.MAX_IMAGE_PIXELS = None

def crop_and_save_images(images_dir, coco_json_path):
    # Load COCO JSON file
    with open(coco_json_path, 'r') as f:
        coco_data = json.load(f)

    # Iterate through images
    for i, image_info in enumerate(coco_data['images'], start=1):
        image_id = image_info['id']
        image_file = image_info['file_name']
        image_path = os.path.join(images_dir, image_file)  # Use os.path.join for path concatenation
        
        # Load image
        img = Image.open(image_path)
        
        # Get annotations for current image
        image_annotations = [ann for ann in coco_data['annotations'] if ann['image_id'] == image_id]

        # Create a folder for the current page
        page_name = f"page_{i}"
        page_dir = os.path.join("output", page_name)
        os.makedirs(page_dir, exist_ok=True)

        # Iterate through annotations and crop images
        for j, annotation in enumerate(image_annotations, start=1):
            bbox = annotation['bbox']
            cropped_img = img.crop((bbox[0], bbox[1], bbox[0] + bbox[2], bbox[1] + bbox[3]))
            
            # Save cropped image
            output_image_path = os.path.join(page_dir, f"{page_name}_image{j}.jpg")
            cropped_img.save(output_image_path, dpi=(300, 300))  # Set resolution to 300 dpi
            print(f"Saved cropped image {output_image_path}")

# Example usage
images_dir = "C:/Projects/Image_extraction/Folder1_test"
coco_json_path = "C:/Projects/Image_extraction/Folder1_test/result.json"
crop_and_save_images(images_dir, coco_json_path)
