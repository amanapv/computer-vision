import argparse
from pathlib import Path

import cv2


PROJECT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = PROJECT_DIR / "different_shapes.jpeg"
EDGES_PATH = PROJECT_DIR / "shape_edges.jpg"
RESULT_PATH = PROJECT_DIR / "detected_shapes.jpg"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find and draw shape contours in an image."
    )
    parser.add_argument(
        "--no-display",
        action="store_true",
        help="Save the edge map and detected contours without opening image windows.",
    )
    args = parser.parse_args()

    image = cv2.imread(str(IMAGE_PATH))
    if image is None:
        raise SystemExit(f"Error: Could not load the image: {IMAGE_PATH}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    result = image.copy()
    cv2.drawContours(result, contours, -1, (0, 255, 0), 3)

    if not cv2.imwrite(str(EDGES_PATH), edges):
        raise OSError(f"Could not save the shape edge map: {EDGES_PATH}")
    if not cv2.imwrite(str(RESULT_PATH), result):
        raise OSError(f"Could not save the detected shapes image: {RESULT_PATH}")

    print("Number of contours detected:", len(contours))
    print("Saved:", EDGES_PATH)
    print("Saved:", RESULT_PATH)

    if not args.no_display:
        cv2.imshow("Original Image", image)
        cv2.imshow("Detected Edges", edges)
        cv2.imshow("Detected Shapes", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
