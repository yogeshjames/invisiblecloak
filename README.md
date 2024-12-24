🪄 Features
Real-Time Cloaking of Red Objects: Detects and makes red-colored regions invisible in live video streams.
Custom Background Video: Upload and display your own background video to replace the invisible red areas.
Color Segmentation: Efficiently identifies and processes red color using HSV color space for reliable detection.
Adjustable Parameters: Fine-tune the color range for detection and blending based on lighting conditions.
Lightweight and Easy to Use: Minimal dependencies with a straightforward setup.
🔧 How It Works
Custom Background Video: Users upload a background video that replaces areas where the red color is detected.
Red Color Detection: Utilizes HSV color space to detect red color in the video feed with precise thresholding.
Dynamic Masking: Creates masks to blend the custom background into the red-colored regions in real time.
🖥️ Tech Stack
Programming Language: Python
Libraries:
OpenCV: For video capture, masking, and blending.
NumPy: For efficient numerical operations.
