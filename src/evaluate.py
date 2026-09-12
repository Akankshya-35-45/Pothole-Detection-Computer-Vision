from ultralytics import YOLO
from pathlib import Path


# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to the trained pothole detection model
MODEL_PATH = (
    BASE_DIR
    / "results"
    / "pothole_model-2"
    / "weights"
    / "best.pt"
)

# Path to dataset configuration
DATA_YAML = BASE_DIR / "data.yaml"


def evaluate_model():
    """
    Evaluate the trained pothole detection model
    on the test dataset.
    """

    # Check whether the trained model exists
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Trained model not found: {MODEL_PATH}"
        )

    # Check whether dataset configuration exists
    if not DATA_YAML.exists():
        raise FileNotFoundError(
            f"Dataset configuration not found: {DATA_YAML}"
        )

    # Load the trained YOLO model
    model = YOLO(str(MODEL_PATH))

    # Evaluate the model on the test split
    metrics = model.val(
        data=str(DATA_YAML),
        split="test",
        imgsz=640,
        verbose=False
    )

    # Extract evaluation metrics
    precision = metrics.box.mp
    recall = metrics.box.mr
    map50 = metrics.box.map50
    map50_95 = metrics.box.map

    # Display evaluation results
    print("\n===== Pothole Detection Evaluation =====")

    print(
        f"Precision : {precision:.4f} "
        f"({precision * 100:.2f}%)"
    )

    print(
        f"Recall    : {recall:.4f} "
        f"({recall * 100:.2f}%)"
    )

    print(
        f"mAP@50    : {map50:.4f} "
        f"({map50 * 100:.2f}%)"
    )

    print(
        f"mAP@50-95 : {map50_95:.4f} "
        f"({map50_95 * 100:.2f}%)"
    )

    return metrics


if __name__ == "__main__":
    evaluate_model()