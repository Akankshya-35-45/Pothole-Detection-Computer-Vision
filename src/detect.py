from ultralytics import YOLO
from pathlib import Path
import argparse
import cv2

from severity import analyze_detections
from report import generate_report


def detect_potholes(
    model_path,
    input_path,
    output_path,
    report_path,
    confidence_threshold=0.25
):
    # Convert paths to Path objects
    model_path = Path(model_path)
    input_path = Path(input_path)
    output_path = Path(output_path)
    report_path = Path(report_path)

    # Validate model file
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found: {model_path}"
        )

    # Validate input image
    if not input_path.exists():
        raise FileNotFoundError(
            f"Input image not found: {input_path}"
        )

    # Validate confidence threshold
    if not 0.0 <= confidence_threshold <= 1.0:
        raise ValueError(
            "Confidence threshold must be between 0.0 and 1.0."
        )

    # Create output directories if they do not exist
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    report_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Load trained YOLO model
    model = YOLO(str(model_path))

    # Run pothole detection
    results = model.predict(
        source=str(input_path),
        conf=confidence_threshold,
        save=False,
        verbose=False
    )

    # Make sure a result was returned
    if not results:
        raise RuntimeError(
            "No detection result was returned."
        )

    # Get the first image result
    result = results[0]

    # Generate annotated image
    annotated_image = result.plot()

    # Save annotated image
    success = cv2.imwrite(
        str(output_path),
        annotated_image
    )

    if not success:
        raise RuntimeError(
            f"Could not save output image: {output_path}"
        )

    # Get original image dimensions
    image_height, image_width = result.orig_shape

    # Get bounding boxes and confidence scores
    if result.boxes is not None and len(result.boxes) > 0:

        boxes = result.boxes.xyxy.cpu().numpy()

        confidences = result.boxes.conf.cpu().numpy()

    else:

        boxes = []

        confidences = []

    # Analyze severity of detected potholes
    severity_results = analyze_detections(
        boxes,
        image_width,
        image_height
    )

    # Add confidence score to each pothole
    for item, confidence in zip(
        severity_results,
        confidences
    ):
        item["confidence"] = float(confidence)

    # Generate detection report
    generate_report(
        severity_results,
        report_path
    )

    # Display detection summary
    print("\n===== Pothole Detection Report =====")

    print(
        f"Potholes detected: "
        f"{len(severity_results)}"
    )

    # Display information about each pothole
    for item in severity_results:

        print(
            f"Pothole {item['pothole']}: "
            f"Confidence={item['confidence']:.2f}, "
            f"Severity={item['severity']}, "
            f"Area={item['area_percentage']:.2f}%"
        )

    print(
        f"\nOutput image: {output_path}"
    )

    print(
        f"Detection report: {report_path}"
    )


if __name__ == "__main__":

    # Create command-line argument parser
    parser = argparse.ArgumentParser(
        description=(
            "Detect potholes and estimate "
            "their severity."
        )
    )

    # Model path argument
    parser.add_argument(
        "--model",
        required=True,
        help="Path to trained YOLO model"
    )

    # Input image argument
    parser.add_argument(
        "--input",
        required=True,
        help="Path to input image"
    )

    # Output image argument
    parser.add_argument(
        "--output",
        required=True,
        help="Path for output image"
    )

    # Report path argument
    parser.add_argument(
        "--report",
        required=True,
        help="Path for detection report"
    )

    # Confidence threshold argument
    parser.add_argument(
        "--conf",
        type=float,
        default=0.25,
        help=(
            "Minimum confidence threshold "
            "(default: 0.25)"
        )
    )

    # Read command-line arguments
    args = parser.parse_args()

    # Run pothole detection
    detect_potholes(
        model_path=args.model,
        input_path=args.input,
        output_path=args.output,
        report_path=args.report,
        confidence_threshold=args.conf
    )