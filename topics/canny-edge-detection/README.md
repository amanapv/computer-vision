# Canny Edge Detection

## Overview

Canny edge detection finds places in an image where brightness changes sharply.
These changes often mark the boundaries of objects, shapes, or surfaces. The
algorithm produces a single-channel edge map: detected edges appear bright and
the rest of the image appears dark.

## What is it used for?

Edge maps are a useful starting point for computer-vision tasks that need
object outlines rather than image color. Common uses include:

- finding object or document boundaries
- preparing an image for line detection or contour analysis
- highlighting shapes in inspection and measurement systems
- identifying road markings and scene boundaries

Canny detects intensity boundaries; it does not identify or label the objects
that created them.

## How Canny works

The Canny method processes an image in stages:

1. **Smooth noise** so small brightness variations are less likely to become
   false edges.
2. **Measure intensity gradients** to find where and in which direction
   brightness changes most strongly.
3. **Thin edge responses** so detected edges are approximately one pixel wide.
4. **Apply two thresholds.** Strong responses are accepted as edges, weak
   responses are kept only when connected to strong edges, and very weak
   responses are discarded.

In this example, the color image is first converted to grayscale, then
`cv2.Canny(gray, 100, 200)` runs Canny with lower and upper thresholds of 100
and 200. Thresholds that are too low can keep texture and noise; thresholds
that are too high can miss faint edges. Good values depend on the image.

## Run this example

From the repository root:

```powershell
python topics\canny-edge-detection\canny_edge_detection.py --no-display
```

The script reads `house.jpg` from this folder and saves:

- `grayscale.jpg` — the input converted to grayscale
- `edges.jpg` — the Canny edge map

Omit `--no-display` to open the original, grayscale, and edge images in
OpenCV windows. Press a key while a window is active to close them.
