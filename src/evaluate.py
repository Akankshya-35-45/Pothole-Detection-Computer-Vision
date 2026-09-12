from ultralytics import YOLO
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "results" / "pothole_model-2" / "weights" / "best.pt"
DATA_YAML = BASE_DIR / "data.yaml"


def evaluate_model():
    model = YOLO(str(MODEL_PATH))

    metrics = model.val(
        data=str(DATA_YAML),
        split="test",
        imgsz=640
    )

    print("\n===== Pothole Detection Evaluation =====")
    print(f"Precision : {metrics.box.mp:.4f}")
    print(f"Recall    : {metrics.box.mr:.4f}")
    print(f"mAP50     : {metrics.box.map50:.4f}")
    print(f"mAP50-95  : {metrics.box.map:.4f}")


if __name__ == "__main__":
    evaluate_model()