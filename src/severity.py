def calculate_severity(width, height, image_width, image_height):
    """
    Estimate pothole severity based on the percentage
    of the image occupied by the detected bounding box.

    Severity thresholds:
        Less than 2%  -> Low
        2% to <6%     -> Moderate
        6% or more    -> High
    """

    # Validate image dimensions
    if image_width <= 0 or image_height <= 0:
        raise ValueError(
            "Image width and height must be greater than zero."
        )

    # Validate bounding-box dimensions
    if width < 0 or height < 0:
        raise ValueError(
            "Pothole width and height cannot be negative."
        )

    # Calculate image area
    image_area = image_width * image_height

    # Calculate detected pothole bounding-box area
    pothole_area = width * height

    # Calculate percentage of image occupied by pothole
    area_percentage = (
        pothole_area / image_area
    ) * 100

    # Assign severity level
    if area_percentage < 2:
        severity = "Low"

    elif area_percentage < 6:
        severity = "Moderate"

    else:
        severity = "High"

    return severity, area_percentage


def analyze_detections(boxes, image_width, image_height):
    """
    Analyze all detected potholes and assign a severity level
    based on their bounding-box area.
    """

    results = []

    # Process every detected pothole
    for index, box in enumerate(boxes, start=1):

        # Extract bounding-box coordinates
        x1, y1, x2, y2 = box

        # Calculate bounding-box width and height
        width = x2 - x1
        height = y2 - y1

        # Calculate severity and area percentage
        severity, percentage = calculate_severity(
            width,
            height,
            image_width,
            image_height
        )

        # Store result
        results.append({
            "pothole": index,
            "severity": severity,
            "area_percentage": round(
                percentage,
                2
            )
        })

    return results


if __name__ == "__main__":

    print("Pothole Severity Analysis Module")
    print("Severity levels: Low, Moderate, High")
    print("Severity is estimated using bounding-box area.")