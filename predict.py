import os
import shutil
import piexif
from ultralytics import YOLO
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# path to trained model
model_path = os.path.join(script_dir, 'train_runs', 'runs', 'detect', 'train4', 'weights', 'best.pt')
model = YOLO(model_path)

# path to predicted image
predict_path = os.path.join(script_dir, 'runs', 'detect', 'predict')

# no detection folder
undetected_path = os.path.join(script_dir, 'no_detection')
if not os.path.exists(undetected_path):
    os.mkdir(undetected_path)

# folder containg images to run inferences on
source_folder = os.path.join(script_dir, 'prediction_images')

results = model.predict(source=source_folder, show_conf=True, save=True)

for result in results:
    bboxes = result.boxes.xywh
    img_path = predict_path + '/' + str(result.path.split('\\')[-1])
    if len(bboxes) == 0:
        shutil.move(img_path, undetected_path)


def append_gps_data(source_folder, destination_folder):
    source_images = os.listdir(source_folder)

    for source_image_name in source_images:
        destination_image_name = source_image_name

        source_image_path = os.path.join(source_folder, source_image_name)
        destination_image_path = os.path.join(destination_folder, destination_image_name)

        if not source_image_name.lower().endswith(('.jpg', '.jpeg', '.tiff', '.tif')):
            continue

        if not os.path.exists(destination_image_path):
            continue

        source_exif_dict = piexif.load(source_image_path)
        gps_data = source_exif_dict.get("GPS")

        if os.path.exists(destination_image_path):
            destination_exif_dict = piexif.load(destination_image_path)
        else:
            destination_exif_dict = {}

        destination_exif_dict["GPS"] = gps_data

        exif_bytes = piexif.dump(destination_exif_dict)
        piexif.insert(exif_bytes, destination_image_path)


append_gps_data(source_folder, predict_path)
