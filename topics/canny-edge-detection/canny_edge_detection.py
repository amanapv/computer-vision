import argparse
from pathlib import Path

import cv2


PROJECT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = PROJECT_DIR / "house.jpg"
GRAYSCALE_PATH = PROJECT_DIR / "grayscale.jpg"
EDGES_PATH = PROJECT_DIR / "edges.jpg"


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert an image to grayscale and detect its edges.")
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
    edges = cv2.Canny(gray, 100, 200)

    if not cv2.imwrite(str(GRAYSCALE_PATH), gray):
        raise OSError(f"Could not save the grayscale image: {GRAYSCALE_PATH}")
    if not cv2.imwrite(str(EDGES_PATH), edges):
        raise OSError(f"Could not save the edge image: {EDGES_PATH}")

    print("Original image shape:", image.shape)
    print("Grayscale image shape:", gray.shape)
    print("Saved:", GRAYSCALE_PATH)
    print("Saved:", EDGES_PATH)

    if not args.no_display:
        cv2.imshow("Original Image", image)
        cv2.imshow("Grayscale Image", gray)
        cv2.imshow("Detected Edges", edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
