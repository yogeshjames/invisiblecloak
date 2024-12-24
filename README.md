# 🪄 Invisible Cloak with Custom Background Video

Transform your live video feed into a magical experience by cloaking red-colored objects in real-time! Replace these regions with a custom background video of your choice. 

---

## ✨ Features

- **Real-Time Cloaking of Red Objects:** Detects and makes red-colored regions invisible in live video streams.
- **Custom Background Video:** Upload and display your own background video to replace the invisible red areas.
- **Color Segmentation:** Efficiently identifies and processes red color using HSV color space for reliable detection.
- **Adjustable Parameters:** Fine-tune the color range for detection and blending based on lighting conditions.
- **Lightweight and Easy to Use:** Minimal dependencies with a straightforward setup.

---

## 🔧 How It Works

1. **Custom Background Video:** Users upload a background video that replaces areas where the red color is detected.
2. **Red Color Detection:** Utilizes HSV color space to detect red color in the video feed with precise thresholding.
3. **Dynamic Masking:** Creates masks to blend the custom background into the red-colored regions in real-time.

---

## 🖥️ Tech Stack

- **Programming Language:** Python
- **Libraries:**
  - **OpenCV:** For video capture, masking, and blending.
  - **NumPy:** For efficient numerical operations.

---

## 🚀 Getting Started

Follow these steps to use the Invisible Cloak:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/invisible-cloak.git
   cd invisible-cloak
