# 🚗 Driver Drowsiness & Yawn Detection System

> Real-time computer vision safety system that detects driver fatigue from a webcam feed and raises instant voice + audio alerts - before drowsiness becomes a road hazard.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8.svg)](https://opencv.org/)
[![dlib](https://img.shields.io/badge/dlib-Facial%20Landmarks-orange.svg)](http://dlib.net/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📖 Overview

Drowsy driving is a leading cause of road accidents worldwide, yet it's often invisible to the driver until it's too late. This project is a **real-time driver safety system** that continuously monitors a driver's eyes and mouth through a webcam, using **Eye Aspect Ratio (EAR)** and **Mouth Aspect Ratio (MAR)** - well-established computer vision metrics - to detect early signs of **drowsiness** and **yawning**, then immediately alerts the driver through **voice and audio alarms**.

The system runs entirely on local video processing (no cloud, no internet dependency), making it lightweight, privacy-respecting, and deployable on low-cost hardware such as an in-car Raspberry Pi or laptop setup.

## ✨ Key Features

| Feature | Description |
|---|---|
| 👁️ **Drowsiness Detection** | Flags sustained eye closure using EAR, tracked across consecutive frames to avoid false positives from normal blinking |
| 😮 **Yawn Detection** | Flags wide mouth-opening events using MAR from mouth landmarks |
| 🔊 **Dual Alert System** | Text-to-speech voice warning ("Wake up!") + a continuous audible beep alarm, running on separate background threads |
| 📸 **Automatic Snapshot Capture** | Saves a timestamped image to `drowsy_snaps/` the moment drowsiness or yawning is detected |
| 📊 **CSV Data Logging** | Logs every frame's timestamp, EAR, MAR, and status to `ear_log.csv` for later analysis |
| 🎯 **68-Point Facial Landmark Tracking** | Uses dlib's pretrained facial landmark predictor for precise eye and mouth geometry |

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Face & Landmark Detection | [dlib](http://dlib.net/) (frontal face detector + 68-point shape predictor) |
| Video Capture / Image Processing | [OpenCV](https://opencv.org/) |
| Geometric Distance Calculations | [SciPy](https://scipy.org/) (`scipy.spatial.distance`) |
| Text-to-Speech Alerts | [pyttsx3](https://pypi.org/project/pyttsx3/) |
| Audio Beep Alarm | `winsound` (Windows built-in) |
| Concurrency | Python `threading` (runs voice + beep alerts without blocking the video loop) |
| Data Logging | Python `csv` |

## ⚙️ How It Works

```
Webcam Frame
    │
    ▼
Detect face (dlib frontal face detector)
    │
    ▼
Extract 68 facial landmarks (eyes: pts 36–47, mouth: pts 48–67)
    │
    ▼
Compute EAR (both eyes, averaged) & MAR (mouth)
    │
    ├── EAR < 0.21 for 20 consecutive frames → DROWSY
    └── MAR > 0.75                            → YAWNING
    │
    ▼
Trigger: snapshot + voice alert + beep alarm + CSV log entry
```

**Eye Aspect Ratio (EAR)** and **Mouth Aspect Ratio (MAR)** are both computed as a ratio of vertical-to-horizontal distances between specific landmark points:

```
EAR = (‖p2−p6‖ + ‖p3−p5‖) / (2 × ‖p1−p4‖)
MAR = (‖p14−p20‖ + ‖p15−p19‖) / (2 × ‖p13−p17‖)
```

- A consistently **low EAR** means the eyes are closing - sustained for 20+ frames, this signals drowsiness rather than a normal blink.
- A **high MAR** means the mouth is wide open - indicating a yawn.

When either condition triggers, the system fires a snapshot, starts a background voice alert ("Wake up! Wake up! Wake up!") and a 2000Hz beep alarm simultaneously, and logs the event to CSV - all without freezing the live video feed, thanks to threading.

## 📂 Project Structure

```
Drowsiness_detection/
├── Drowsiness detection.py            # Main real-time detection script
├── Drowsiness Detection.ipynb         # Notebook version / development workspace
├── requirements.txt                    # Python dependencies
├── ear_log.csv                         # Auto-generated EAR/MAR/status log
├── drowsy_snaps/                       # Auto-created folder for triggered snapshots
└── README.md
```

> ⚠️ **Not included in the repo:** `shape_predictor_68_face_landmarks.dat` - dlib's pretrained facial landmark model. You'll need to download it separately (see setup below); it's excluded here due to its large file size.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- A working **webcam**
- **Windows OS** (the beep alarm uses `winsound`, a Windows-only module - see [Limitations](#-limitations--notes))

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Gayathri-Reddy874/Drowsiness_detection.git
cd Drowsiness_detection

# 2. Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

### Download the Facial Landmark Model

1. Download `shape_predictor_68_face_landmarks.dat` from [davisking/dlib-models](https://github.com/davisking/dlib-models).
2. Extract it (it's distributed as a `.bz2` archive) and place the `.dat` file in the project's root folder, alongside the script.

### Run the Detector

```bash
python "Drowsiness detection.py"
```

Press **`Q`** at any time to stop the detection and close the window.

## 💡 Usage

1. Launch the script — your webcam feed opens in a window titled **"Driver Alert System"**.
2. Live **EAR** and **MAR** values are displayed on-screen in real time.
3. If your eyes stay closed (EAR < 0.21) for 20+ consecutive frames → a **"DROWSINESS ALERT!"** banner appears, a snapshot is saved, and voice + beep alerts start.
4. If your mouth opens wide (MAR > 0.75) → a **"YAWN DETECTED!"** banner appears, with the same snapshot + alert behavior.
5. Every frame's readings are appended to `ear_log.csv` for later review.
6. Press **`Q`** to exit cleanly.

## 📊 Sample CSV Log Output

| Timestamp | EAR | MAR | Status |
|---|---|---|---|
| 2025-11-16 19:10:22 | 0.19 | 0.51 | DROWSY |
| 2025-11-16 19:10:23 | 0.18 | 0.53 | DROWSY |
| 2025-11-16 19:10:28 | 0.30 | 0.84 | YAWNING |

## ⚠️ Limitations & Notes

- **Windows-only beep alarm** — `winsound` is a Windows standard-library module, so the audible beep won't work on macOS/Linux without swapping in a cross-platform alternative (e.g. `playsound` or `simpleaudio`).
- Requires reasonably good, even lighting and a front-facing view for reliable face/landmark detection.
- Designed for a **single driver/face** in frame; behavior with multiple faces is not explicitly handled.
- Thresholds (`EAR_THRESH = 0.21`, frame limit = 20, `MAR > 0.75`) are general-purpose defaults — for production use, these would benefit from per-user calibration.

## 🔭 Future Improvements

- [ ] Cross-platform audio alerts (replace `winsound` with `playsound`/`simpleaudio`)
- [ ] Per-user EAR/MAR calibration at startup for higher accuracy
- [ ] Head-pose / nodding-off detection as an additional fatigue signal
- [ ] Lightweight deployment on Raspberry Pi for real in-car use
- [ ] Dashboard to visualize `ear_log.csv` trends over a driving session
- [ ] Replace dlib's HOG-based detector with a faster deep-learning face detector for better low-light performance

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/Gayathri-Reddy874/Drowsiness_detection/issues) or open a pull request.

## 📄 License

MIT License. Feel free to use and modify.

## 👩‍💻 Author

**Mallareddygari Gayathri**
GitHub: [@Gayathri-Reddy874](https://github.com/Gayathri-Reddy874)

---
⭐ If you found this project useful, consider giving it a star!
