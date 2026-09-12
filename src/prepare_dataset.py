import random
import shutil
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent

SOURCE_DIR = BASE_DIR / "data" / "raw" / "Pothole Dataset"
IMAGES_DIR = BASE_DIR / "data" / "images"
LABELS_DIR = BASE_DIR / "data" / "labels"

# Split ratios
TRAIN_RATIO = 0.70
VAL_RATIO = 0.20
TEST_RATIO = 0.10

random.seed(42)

# Get all images
images = list(SOURCE_DIR.glob("*.jpg"))

if not images:
    raise FileNotFoundError(
        f"No .jpg images found in: {SOURCE_DIR}"
    )

# Shuffle images
random.shuffle(images)

# Calculate split sizes
total = len(images)
train_end = int(total * TRAIN_RATIO)
val_end = train_end + int(total * VAL_RATIO)

train_images = images[:train_end]
val_images = images[train_end:val_end]
test_images = images[val_end:]


def copy_files(image_list, split):
    for image_path in image_list:
        label_path = image_path.with_suffix(".txt")

        if not label_path.exists():
            print(f"Warning: Label not found for {image_path.name}")
            continue

        # Copy image
        shutil.copy2(
            image_path,
            IMAGES_DIR / split / image_path.name
        )

        # Copy label
        shutil.copy2(
            label_path,
            LABELS_DIR / split / label_path.name
        )


# Copy each split
copy_files(train_images, "train")
copy_files(val_images, "val")
copy_files(test_images, "test")

print("Dataset preparation completed!")
print(f"Total images : {total}")
print(f"Training     : {len(train_images)}")
print(f"Validation   : {len(val_images)}")
print(f"Testing      : {len(test_images)}")