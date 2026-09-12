from pathlib import Path


# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset directory
DATA_DIR = BASE_DIR / "data"

# Trained model path
MODEL_PATH = (
    BASE_DIR
    / "results"
    / "pothole_model-2"
    / "weights"
    / "best.pt"
)


def check_dataset():
    """
    Check whether the train, validation, and test datasets
    contain matching image and label files.
    """

    print("Checking dataset...")

    all_checks_passed = True

    # Check all dataset splits
    for split in ["train", "val", "test"]:

        image_dir = DATA_DIR / "images" / split
        label_dir = DATA_DIR / "labels" / split

        # Check whether directories exist
        if not image_dir.exists():
            print(
                f"{split}: Image directory not found - "
                f"{image_dir}"
            )
            all_checks_passed = False
            continue

        if not label_dir.exists():
            print(
                f"{split}: Label directory not found - "
                f"{label_dir}"
            )
            all_checks_passed = False
            continue

        # Find supported image formats
        images = []

        for extension in ["*.jpg", "*.jpeg", "*.png"]:
            images.extend(image_dir.glob(extension))

        # Find YOLO label files
        labels = list(label_dir.glob("*.txt"))

        print(
            f"{split}: "
            f"{len(images)} images, "
            f"{len(labels)} labels"
        )

        # Check whether every image has a label
        if len(images) != len(labels):
            print(
                f"Warning: {split} has mismatched "
                "image and label counts."
            )
            all_checks_passed = False

        # Check that the split is not empty
        if len(images) == 0:
            print(
                f"Warning: {split} contains no images."
            )
            all_checks_passed = False

    return all_checks_passed


def check_model():
    """
    Check whether the trained YOLO model exists.
    """

    print("\nChecking trained model...")

    if MODEL_PATH.exists():

        print(
            f"Model found: {MODEL_PATH}"
        )

        # Display model size
        model_size_mb = MODEL_PATH.stat().st_size / (
            1024 * 1024
        )

        print(
            f"Model size: {model_size_mb:.2f} MB"
        )

        return True

    print(
        f"Trained model not found: {MODEL_PATH}"
    )

    return False


def run_tests():
    """
    Run all project validation checks.
    """

    dataset_ok = check_dataset()
    model_ok = check_model()

    print("\n===== Project Validation =====")

    if dataset_ok and model_ok:

        print("All validation checks passed!")
        return True

    print("Some validation checks failed.")
    return False


if __name__ == "__main__":

    success = run_tests()

    # Return an appropriate exit status
    if not success:
        raise SystemExit(1)