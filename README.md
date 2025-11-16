# Driver Drowsiness & Yawn Detection System  
A real-time driver safety system that uses **Eye Aspect Ratio (EAR)** and **Mouth Aspect Ratio (MAR)** to detect:

- 👁️ Drowsiness (long eye closure)  
- 😮 Yawning  
- 🔊 Audio Alerts (TTS + Beep)  
- 📸 Automatic Snapshot Capture  
- 📊 EAR/MAR Logging into CSV  

Built using **OpenCV, dlib, scipy, and pyttsx3**.

---

## 🚀 Features

### ✔️ Drowsiness Detection  
- Uses EAR from both eyes  
- Detects continuous low EAR for several frames  
- Triggers:
  - Snapshot saved in `drowsy_snaps/`
  - Text-to-speech alert ("Wake up!")
  - Beep alarms

### ✔️ Yawn Detection  
- Uses MAR from mouth landmarks  
- Saves snapshot + activates alert

### ✔️ CSV Logging  
All readings are saved to `ear_log.csv`:
Timestamp | EAR | MAR | Status

yaml
Copy code

### ✔️ Audio Alerts  
- **TTS:** “Wake up!”  
- **Beep Alarm:** 2000Hz continuous warning  

### ✔️ Face Landmark Detection  
Uses `shape_predictor_68_face_landmarks.dat` model.

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/driver-drowsiness-detector.git
cd driver-drowsiness-detector
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Download Landmark Model
Download shape_predictor_68_face_landmarks.dat from:
🔗 https://github.com/davisking/dlib-models

Place it in the project folder.

▶️ Usage
Run the script:

bash
Copy code
python drowsiness_detector.py
Press Q to quit the detection window.

📁 Project Structure
arduino
Copy code
│
├── drowsiness_detector.py
├── requirements.txt
├── README.md
├── shape_predictor_68_face_landmarks.dat
├── ear_log.csv                   # auto-created
└── drowsy_snaps/                 # snapshots saved here
📸 Snapshots
drowsy_<timestamp>.jpg

yawn_<timestamp>.jpg

Saved automatically when detection triggers.

📊 CSV Logging Example
yaml
Copy code
Timestamp,EAR,MAR,Status
2025-11-16 19:10:22,0.19,0.51,DROWSY
2025-11-16 19:10:23,0.18,0.53,DROWSY
2025-11-16 19:10:28,0.30,0.84,YAWNING
🧠 How It Works (Short Summary)
EAR = (vertical eye distances) / (horizontal distance)

MAR = (vertical mouth distances) / (horizontal distance)

If EAR < 0.21 for 20 frames → Drowsy

If MAR > 0.75 → Yawn

🧩 Requirements
Python 3.7+

Webcam

Windows (for winsound)

📜 License
MIT License. Feel free to use and modify.
