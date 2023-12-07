# Automatic Pothole Detection from Images with EXIF Data

## Overview

This repository contains Python code for automatically detecting potholes in user-submitted images. The system utilizes YOLO (You Only Look Once) for object detection and incorporates EXIF data for improved accuracy. Detected potholes are visualized in an interactive web interface, and the results of predictions are stored in the `runs/detect/predict` folder. Images without detections are moved to the `no_detection` folder.

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


