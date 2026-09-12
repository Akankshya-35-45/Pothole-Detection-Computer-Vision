from pathlib import Path


def generate_report(detections, output_path):
    """
    Generate a text report containing:
    - Total number of detected potholes
    - Confidence score of each pothole
    - Severity level of each pothole
    - Area percentage of each pothole
    - Severity summary
    """

    # Convert output path to Path object
    output_path = Path(output_path)

    # Create parent directory if it does not exist
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Count total detections
    total = len(detections)

    # Count potholes by severity
    low = sum(
        1
        for item in detections
        if item["severity"] == "Low"
    )

    moderate = sum(
        1
        for item in detections
        if item["severity"] == "Moderate"
    )

    high = sum(
        1
        for item in detections
        if item["severity"] == "High"
    )

    # Create the report file
    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "========== POTHOLE DETECTION REPORT ==========\n\n"
        )

        # Write total number of potholes
        file.write(
            f"Total potholes detected: {total}\n\n"
        )

        # Handle the case where no potholes are detected
        if total == 0:

            file.write(
                "No potholes were detected in the input image.\n\n"
            )

        else:

            # Write details of every detected pothole
            for item in detections:

                file.write(
                    f"Pothole {item['pothole']}\n"
                    f"Confidence : "
                    f"{item['confidence']:.2f}\n"
                    f"Severity   : "
                    f"{item['severity']}\n"
                    f"Area       : "
                    f"{item['area_percentage']:.2f}%\n\n"
                )

        # Write severity summary
        file.write(
            "---------- Severity Summary ----------\n"
        )

        file.write(
            f"Low       : {low}\n"
        )

        file.write(
            f"Moderate  : {moderate}\n"
        )

        file.write(
            f"High      : {high}\n"
        )

        file.write(
            "\n==============================================\n"
        )

    # Confirm report location
    print(
        f"Report saved to: {output_path}"
    )


if __name__ == "__main__":

    # Basic standalone test
    sample_detections = [
        {
            "pothole": 1,
            "confidence": 0.89,
            "severity": "Moderate",
            "area_percentage": 3.70
        },
        {
            "pothole": 2,
            "confidence": 0.70,
            "severity": "Moderate",
            "area_percentage": 2.66
        }
    ]

    generate_report(
        sample_detections,
        "results/test_report.txt"
    )

    print("Report module test completed.")