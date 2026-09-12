from pathlib import Path


def generate_report(detections, output_path):
    """
    Generate a text report for detected potholes.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    total = len(detections)

    low = sum(
        1 for item in detections
        if item["severity"] == "Low"
    )

    moderate = sum(
        1 for item in detections
        if item["severity"] == "Moderate"
    )

    high = sum(
        1 for item in detections
        if item["severity"] == "High"
    )

    with open(output_path, "w", encoding="utf-8") as file:

        file.write("========== POTHOLE DETECTION REPORT ==========\n\n")

        file.write(f"Total potholes detected: {total}\n\n")

        for item in detections:
            file.write(
                f"Pothole {item['pothole']}\n"
                f"Confidence : {item['confidence']:.2f}\n"
                f"Severity   : {item['severity']}\n"
                f"Area       : {item['area_percentage']:.2f}%\n\n"
            )

        file.write("---------- Severity Summary ----------\n")
        file.write(f"Low       : {low}\n")
        file.write(f"Moderate  : {moderate}\n")
        file.write(f"High      : {high}\n")

        file.write("\n==============================================\n")

    print(f"Report saved to: {output_path}")