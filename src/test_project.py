from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODEL_PATH = BASE_DIR / "results" / "pothole_model-2" / "weights" / "best.pt"


def check_dataset():
    print("Checking dataset...")

    for split in ["train", "val", "test"]:
        image_dir = DATA_DIR / "images" / split
        label_dir = DATA_DIR / "labels" / split

        images = list(image_dir.glob("*.jpg"))
        labels = list(label_dir.glob("*.txt"))

        print(
            f"{split}: {len(images)} images, "
            f"{len(labels)} labels"
        )

        if len(images) != len(labels):
            return False

    return True


def check_model():
    print("\nChecking trained model...")

    if MODEL_PATH.exists():
        print(f"Model found: {MODEL_PATH}")
        return True

    print("Trained model not found.")
    return False


def run_tests():
    dataset_ok = check_dataset()
    model_ok = check_model()

    print("\n===== Project Validation =====")

    if dataset_ok and model_ok:
        print("All validation checks passed!")
    else:
        print("Some validation checks failed.")


if __name__ == "__main__":
    run_tests()