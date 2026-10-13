# Hough Line Detection

This project detects line segments in `road.jpeg` using Canny edge detection and
OpenCV's probabilistic Hough transform (`HoughLinesP`). Detected lines are
drawn in green on the original image.

## Run

From the repository root:

```powershell
python topics\hough-line-detection\hough_transform.py --no-display
```

The processed edge map and detected-line image are saved as `hough_edges.jpg`
and `hough_result.jpg` in this folder. Omit `--no-display` to open the result
windows.

## Example output

![Canny edges](hough_edges.jpg)

![Detected Hough lines](hough_result.jpg)
