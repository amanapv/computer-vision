import argparse
from pathlib import Path

import cv2
import numpy as np


PROJECT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = PROJECT_DIR / "road.jpeg"
EDGES_PATH = PROJECT_DIR / "hough_edges.jpg"
RESULT_PATH = PROJECT_DIR / "hough_result.jpg"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Detect and draw line segments with the probabilistic Hough transform."
    )
    parser.add_argument(
        "--no-display",
        action="store_true",
        help="Save the processed images without opening image windows.",
    )
    args = parser.parse_args()

    image = cv2.imread(str(IMAGE_PATH))
    if image is None:
        raise SystemExit(f"Error: Could not load the image: {IMAGE_PATH}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    lines = cv2.HoughLinesP(
        edges,
        rho=1,
        theta=np.pi / 180,
        threshold=50,
        minLineLength=50,
        maxLineGap=20,
    )

    result = image.copy()
    line_count = 0 if lines is None else len(lines)
    if lines is not None:
        for x1, y1, x2, y2 in np.asarray(lines).reshape(-1, 4):
            cv2.line(
                result,
                (int(x1), int(y1)),
                (int(x2), int(y2)),
                (0, 255, 0),
                2,
            )

    if not cv2.imwrite(str(EDGES_PATH), edges):
        raise OSError(f"Could not save the edge image: {EDGES_PATH}")
    if not cv2.imwrite(str(RESULT_PATH), result):
        raise OSError(f"Could not save the Hough result image: {RESULT_PATH}")

    print("Number of detected line segments:", line_count)
    print("Saved:", EDGES_PATH)
    print("Saved:", RESULT_PATH)

    if not args.no_display:
        cv2.imshow("Canny Edges", edges)
        cv2.imshow("Hough Line Detection", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
