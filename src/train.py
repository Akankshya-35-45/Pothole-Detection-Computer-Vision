from ultralytics import YOLO
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset configuration
DATA_YAML = BASE_DIR / "data.yaml"

# Load a small pretrained YOLO model
model = YOLO("yolo11n.pt")

# Train the model
results = model.train(
    data=str(DATA_YAML),
    epochs=30,
    imgsz=640,
    batch=8,
    project=str(BASE_DIR / "results"),
    name="pothole_model",
)

print("\nTraining completed successfully!")
print(f"Results saved in: {BASE_DIR / 'results' / 'pothole_model'}")