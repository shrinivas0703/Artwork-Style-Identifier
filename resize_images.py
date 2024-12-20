from PIL import Image
import os

def save_resized_images(input_folder, output_folder, target_size=(224, 224)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for art_style in os.listdir(input_folder):
        if art_style[0] == ".":
            continue
        
        art_style_path = os.path.join(input_folder, art_style)

        for file_name in os.listdir(art_style_path):
            if file_name[0] == ".":
                continue
            
            image_path = os.path.join(art_style_path, file_name)
            img = Image.open(image_path)
            img_resized = img.resize(target_size)
            
            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, art_style)
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            resized_image_path = os.path.join(output_path, file_name)
            img_resized.save(resized_image_path)

save_resized_images("data", "data_resized")