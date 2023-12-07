# Automatic Pothole Detection from Images with EXIF Data

Welcome to the Automatic Pothole Detection project! This repository contains Python code designed to automatically detect potholes in user-submitted images. The system utilizes YOLO (You Only Look Once) for object detection and incorporates EXIF data for improved accuracy.

## Overview
Detected potholes are visualized in an interactive web interface, and the results of predictions are stored in the `runs/detect/predict` folder. Images without detections are moved to the `no_detection` folder.

Explore the [Detected Potholes Map](https://your-username.github.io/your-repository/detected.html) - an interactive map of detected potholes.

## Getting Started

### Prerequisites

- Python 3.6 or later
- [Git](https://git-scm.com/)

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

#### Install Dependencies
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Run the Prediction Script
```bash
python predict.py
```

1. Ensure your images are in the prediction_images folder.
2. Predictions will be saved in the runs/detect/predict folder.
3. Images without detections will be moved to the no_detection folder.
4. Verify that your images have EXIF data, including GPS information for accurate predictions.

#### Run the Automation Script
```bash
# Note: Only run automation.py if your images contain EXIF data
python automation.py
```

- This script generates an interactive map named `detected.html` showcasing the locations of detected potholes.

- Ensure GPS data is available in the images for accurate mapping.

## Project Structure

- **predict.py**: Python script for predicting potholes using YOLO and processing images.

- **automation.py**: Python script for generating an interactive map of detected potholes.

- **GPS_extraction.py**: Dependency for extracting GPS location from images.

- **prediction_images/**: Folder containing images for prediction.

- **train_runs/**: Folder containing YOLO training runs.

- **runs/**: Folder for storing detection results.
  - **detect/**: Subfolder for detection results.
    - **predict/**: Subfolder for predicted images.

- **no_detection/**: Folder for images with no detected potholes.

## View the Deployed Example

Explore the [Detected Potholes Map](https://your-username.github.io/your-repository/detected.html) - an interactive map of detected potholes.

## Contributing

Contributions are welcome! If you'd like to contribute to the development of this project, please open an issue or submit a pull request.






