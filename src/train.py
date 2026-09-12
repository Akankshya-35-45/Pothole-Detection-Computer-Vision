from ultralytics import YOLO
from pathlib import Path


# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Path to dataset configuration
DATA_YAML = BASE_DIR / "data.yaml"

# Path to pretrained YOLO model
PRETRAINED_MODEL = BASE_DIR / "yolo11n.pt"

# Directory where training results will be stored
RESULTS_DIR = BASE_DIR / "results"


def train_model():
    """
    Train a YOLO model for pothole detection.
    """

    # Check whether dataset configuration exists
    if not DATA_YAML.exists():
        raise FileNotFoundError(
            f"Dataset configuration not found: {DATA_YAML}"
        )

    # Check whether pretrained model exists
    if not PRETRAINED_MODEL.exists():
        raise FileNotFoundError(
            f"Pretrained model not found: {PRETRAINED_MODEL}"
        )

    # Load pretrained YOLO model
    model = YOLO(str(PRETRAINED_MODEL))

    # Train the model
    results = model.train(
        data=str(DATA_YAML),
        epochs=30,
        imgsz=640,
        batch=8,
        project=str(RESULTS_DIR),
        name="pothole_model",
        exist_ok=True
    )

    print("\nTraining completed successfully!")

    print(
        f"Training results saved in: "
        f"{RESULTS_DIR / 'pothole_model'}"
    )

    return results


if __name__ == "__main__":
    train_model()