import argparse
from pathlib import Path

import cv2
import numpy as np


PROJECT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = PROJECT_DIR / "nature.jpeg"
MASK_PATH = PROJECT_DIR / "roi_mask.jpg"
ROI_PATH = PROJECT_DIR / "road_roi.jpg"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Select a triangular road region from an image."
    )
    parser.add_argument(
        "--no-display",
        action="store_true",
        help="Save the mask and selected region without opening image windows.",
    )
    args = parser.parse_args()

    image = cv2.imread(str(IMAGE_PATH))
    if image is None:
        raise SystemExit(f"Error: Could not load the image: {IMAGE_PATH}")

    height, width = image.shape[:2]
    mask = np.zeros((height, width), dtype=np.uint8)
    polygon = np.array(
        [
            [
                (int(width * 0.10), height - 1),
                (int(width * 0.90), height - 1),
                (int(width * 0.55), int(height * 0.55)),
                (int(width * 0.45), int(height * 0.55)),
            ]
        ],
        dtype=np.int32,
    )

    cv2.fillPoly(mask, polygon, 255)
    roi = cv2.bitwise_and(image, image, mask=mask)

    if not cv2.imwrite(str(MASK_PATH), mask):
        raise OSError(f"Could not save the ROI mask: {MASK_PATH}")
    if not cv2.imwrite(str(ROI_PATH), roi):
        raise OSError(f"Could not save the selected region: {ROI_PATH}")

    print("Image shape:", image.shape)
    print("Saved:", MASK_PATH)
    print("Saved:", ROI_PATH)

    if not args.no_display:
        cv2.imshow("Original Image", image)
        cv2.imshow("ROI Mask", mask)
        cv2.imshow("Road Region Only", roi)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
