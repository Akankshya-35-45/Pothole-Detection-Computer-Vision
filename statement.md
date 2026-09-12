# Project Statement

## Project Title

Pothole Detection and Severity Analysis Using Computer Vision

## Problem Statement

Potholes on roads can create safety risks for drivers, damage vehicles, and contribute to poor road conditions. Manual identification of potholes over large road networks is time-consuming and difficult to scale.

This project aims to develop a computer vision system that automatically detects potholes in road images using a YOLO-based object detection model and provides an image-based severity estimate for each detected pothole.

## Scope of the Project

The system focuses on detecting potholes in road images using a trained object detection model.

The project includes:

- Dataset preparation and organization
- Image preprocessing
- YOLO-based pothole detection
- Pothole counting
- Image-based pothole severity estimation
- Model performance evaluation
- Generation of annotated output images

The severity estimation is based on the relative area occupied by a detected pothole in an image. It does not directly measure the physical depth or structural damage of a pothole.

## Target Users

The potential users of the system include:

- Road maintenance teams
- Municipal authorities
- Transportation departments
- Infrastructure monitoring teams
- Researchers and students working on road-condition analysis

## High-Level Features

1. **Dataset Preparation**
   - Organizes pothole images and annotations.
   - Splits the dataset into training, validation, and testing sets.

2. **Pothole Detection**
   - Detects potholes using a trained YOLO model.
   - Generates bounding boxes around detected potholes.

3. **Pothole Counting**
   - Counts the number of potholes detected in an input image.

4. **Severity Analysis**
   - Estimates severity as Low, Moderate, or High based on detected pothole area.

5. **Model Evaluation**
   - Evaluates the trained model using Precision, Recall, mAP@50, and mAP@50-95.

6. **Output Generation**
   - Produces an annotated image showing detected potholes.