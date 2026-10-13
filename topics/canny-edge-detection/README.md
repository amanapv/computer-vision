# Canny Edge Detection

This project loads `house.jpg`, creates a grayscale version, detects edges with
the Canny algorithm, saves both processed images next to the script, and opens
the original and processed images in separate windows.

## Run

From the repository root:

```powershell
python topics\canny-edge-detection\canny_edge_detection.py --no-display
```

The output files are `grayscale.jpg` and `edges.jpg` in this folder. Press any
key while an OpenCV image window is active to close the windows. Omit
`--no-display` to open the image windows.
