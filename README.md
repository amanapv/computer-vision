# Computer Vision with OpenCV

A collection of small computer-vision projects built with Python and OpenCV.

## Projects

- [Canny edge detection](topics/canny-edge-detection/README.md) — load an image, convert it to grayscale, detect edges, and save the results.

Future topics, such as the Hough transform, can be added as separate folders under `topics/`.

## Setup

From this repository's folder, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If `py` or `python` is not available in PowerShell, use the full path to your Python executable to create the environment.
