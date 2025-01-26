import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

input_folder =r'F:\MS CS\1st Semester\Azheimer Classification\new_data_set'
output_base_folder = r'F:\MS CS\1st Semester\Azheimer Classification\data_3k'

for class_folder in os.listdir(input_folder):
    class_path = os.path.join(input_folder, class_folder)
    if os.path.isdir(class_path): 
        output_class_folder = os.path.join(output_base_folder, class_folder)
        create_directory(output_class_folder)

        image_files = [f for f in os.listdir(class_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

        selected_images = image_files[:3000]

        # Copy selected images to the new directory
        for image_file in selected_images:
            src_path = os.path.join(class_path, image_file)
            dest_path = os.path.join(output_class_folder, image_file)
            shutil.copy2(src_path, dest_path)

print("Image processing completed. Selected images stored in separate folders.")