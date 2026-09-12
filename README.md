# Pothole Detection and Severity Analysis Using Computer Vision

## 1. Project Overview

This project develops a computer vision system for detecting potholes in road images using a YOLO-based object detection model.

The system detects potholes, counts the detected potholes, estimates their severity based on their relative image area, and evaluates the trained model using standard object detection metrics.

## 2. Features

- Pothole dataset preparation
- Training, validation, and testing dataset split
- Image preprocessing
- YOLO-based pothole detection
- Pothole counting
- Image-based severity estimation
- Model evaluation
- Automated project validation
- Command-line execution
- Annotated output generation
- Automated pothole detection report generation

## 3. Technologies Used

- Python 3.11
- Ultralytics YOLO
- PyTorch
- OpenCV
- Git and GitHub

## 4. Project Structure

```text
Pothole-Detection-Computer-Vision/
│
├── data.yaml
├── requirements.txt
├── statement.md
├── README.md
├── .gitignore
│
├── data/
│   ├── images/
│   ├── labels/
│   └── raw/
│
├── results/
│
└── src/
    ├── prepare_dataset.py
    ├── preprocess.py
    ├── train.py
    ├── detect.py
    ├── evaluate.py
    ├── severity.py
    ├── report.py
    └── test_project.py