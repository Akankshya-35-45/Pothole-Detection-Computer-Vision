import cv2
from pathlib import Path


def preprocess_image(input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(output_path)

    image = cv2.imread(str(input_path))

    if image is None:
        raise FileNotFoundError(
            f"Could not read image: {input_path}"
        )

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise while preserving edges
    processed = cv2.GaussianBlur(gray, (5, 5), 0)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    cv2.imwrite(str(output_path), processed)

    print(f"Preprocessed image saved to: {output_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Preprocess a road image."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to input image"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Path to output image"
    )

    args = parser.parse_args()

    preprocess_image(
        args.input,
        args.output
    )