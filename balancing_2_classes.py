import os
import shutil

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Input and output folders
input_folder = r'F:\MS CS\1st Semester\Azheimer Classification\new_data_set'
output_base_folder = r'F:\MS CS\1st Semester\Azheimer Classification\two_classes_3k'

# Specify the folders to process
folders_to_process = ["NonDemented", "ModerateDemented"]

for class_folder in folders_to_process:
    class_path = os.path.join(input_folder, class_folder)
    if os.path.isdir(class_path):  # Ensure the folder exists in the input
        output_class_folder = os.path.join(output_base_folder, class_folder)
        create_directory(output_class_folder)

        # Get the list of image files in the folder
        image_files = [f for f in os.listdir(class_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

        selected_images = image_files[:3000]

        # Copy selected images to the new directory
        for image_file in selected_images:
            src_path = os.path.join(class_path, image_file)
            dest_path = os.path.join(output_class_folder, image_file)
            shutil.copy2(src_path, dest_path)

print("Image processing completed. Selected images stored in separate folders.")
