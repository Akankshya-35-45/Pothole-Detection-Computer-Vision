from ultralytics import YOLO
from pathlib import Path
import argparse

from severity import analyze_detections
from report import generate_report


def detect_potholes(model_path, input_path, output_path, report_path):
    model = YOLO(model_path)

    results = model.predict(
        source=input_path,
        save=True,
        conf=0.25
    )

    result = results[0]

    output_path = Path(output_path)
    report_path = Path(report_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    # Locate YOLO-generated image
    generated_file = Path(result.save_dir) / Path(input_path).name

    if generated_file.exists():
        generated_file.replace(output_path)

    # Get image dimensions
    image_height, image_width = result.orig_shape

    # Get bounding boxes
    boxes = result.boxes.xyxy.cpu().numpy()

    # Get confidence scores
    confidences = result.boxes.conf.cpu().numpy()

    # Analyze severity
    severity_results = analyze_detections(
        boxes,
        image_width,
        image_height
    )

    # Add confidence to each detection
    for item, confidence in zip(severity_results, confidences):
        item["confidence"] = float(confidence)

    # Generate text report
    generate_report(
        severity_results,
        report_path
    )

    print("\n===== Pothole Detection Report =====")
    print(f"Potholes detected: {len(severity_results)}")

    for item in severity_results:
        print(
            f"Pothole {item['pothole']}: "
            f"Confidence={item['confidence']:.2f}, "
            f"Severity={item['severity']}, "
            f"Area={item['area_percentage']:.2f}%"
        )

    print(f"\nOutput image: {output_path}")
    print(f"Detection report: {report_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Detect potholes and estimate their severity."
    )

    parser.add_argument(
        "--model",
        required=True,
        help="Path to trained YOLO model"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input image"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path for output image"
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Path for detection report"
    )

    args = parser.parse_args()

    detect_potholes(
        args.model,
        args.input,
        args.output,
        args.report
    )