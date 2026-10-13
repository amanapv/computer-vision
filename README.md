# Computer Vision with OpenCV

A collection of small computer-vision projects built with Python and OpenCV.
Each topic has its own explanation, runnable example, and sample output.

## Projects

- [Canny edge detection](topics/canny-edge-detection/README.md) — find image boundaries by detecting sharp brightness changes.
- [Hough line detection](topics/hough-line-detection/README.md) — group edge pixels into likely straight-line segments.

### How these topics connect

Canny creates an edge map from an image. The Hough line transform can then use
those edge pixels as evidence to find straight lines. The Hough example in this
repository uses Canny as one of its processing steps.

## Setup

From this repository's folder, create and activate a virtual environment, then install the dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If `py` or `python` is not available in PowerShell, use the full path to your Python executable to create the environment.
