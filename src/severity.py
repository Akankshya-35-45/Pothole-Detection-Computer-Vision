def calculate_severity(width, height, image_width, image_height):
    """
    Estimate pothole severity based on the percentage
    of the image occupied by the detected bounding box.
    """

    image_area = image_width * image_height
    pothole_area = width * height

    area_percentage = (pothole_area / image_area) * 100

    if area_percentage < 2:
        severity = "Low"
    elif area_percentage < 6:
        severity = "Moderate"
    else:
        severity = "High"

    return severity, area_percentage


def analyze_detections(boxes, image_width, image_height):
    """
    Analyze all detected potholes and assign a severity level.
    """

    results = []

    for index, box in enumerate(boxes, start=1):
        x1, y1, x2, y2 = box

        width = x2 - x1
        height = y2 - y1

        severity, percentage = calculate_severity(
            width,
            height,
            image_width,
            image_height
        )

        results.append({
            "pothole": index,
            "severity": severity,
            "area_percentage": round(percentage, 2)
        })

    return results


if __name__ == "__main__":
    print("Pothole Severity Analysis Module")
    print("Severity levels: Low, Moderate, High")