import argparse
from pathlib import Path

import cv2


PROJECT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = PROJECT_DIR / "city.jpeg"
KERNEL_SIZES = (3, 5, 7, 9, 11)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare Gaussian smoothing at several kernel sizes."
    )
    parser.add_argument(
        "--no-display",
        action="store_true",
        help="Save the blurred images without opening image windows.",
    )
    args = parser.parse_args()

    image = cv2.imread(str(IMAGE_PATH))
    if image is None:
        raise SystemExit(f"Error: Could not load the image: {IMAGE_PATH}")

    if not args.no_display:
        cv2.imshow("Original Image", image)

    for kernel_size in KERNEL_SIZES:
        blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
        output_path = PROJECT_DIR / f"blur_{kernel_size}x{kernel_size}.jpg"
        if not cv2.imwrite(str(output_path), blurred):
            raise OSError(f"Could not save the blurred image: {output_path}")

        print("Saved:", output_path)
        if not args.no_display:
            cv2.imshow(f"Gaussian Blur - Kernel {kernel_size}x{kernel_size}", blurred)

    if not args.no_display:
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    print("All blurred images have been saved.")


if __name__ == "__main__":
    main()
