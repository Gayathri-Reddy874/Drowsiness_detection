import cv2
import dlib
import numpy as np
from scipy.spatial import distance
import winsound
import threading
import time
import csv
import os
from datetime import datetime
import pyttsx3

# -----------------------------
# 1. TEXT-TO-SPEECH ENGINE
# -----------------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

alert_on = False

def voice_alert():
    while alert_on:
        engine.say("Wake up! Wake up! Wake up!")
        engine.runAndWait()
        time.sleep(0.3)

def beep_alarm():
    while alert_on:
        winsound.Beep(2000, 500)
        time.sleep(0.1)

# -----------------------------
# 2. FACE DETECTOR + LANDMARKS
# -----------------------------
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# -----------------------------
# 3. CSV LOGGING
# -----------------------------
log_file = "ear_log.csv"
if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "EAR", "MAR", "Status"])

# -----------------------------
# 4. SNAPSHOT FOLDER
# -----------------------------
os.makedirs("drowsy_snaps", exist_ok=True)

# -----------------------------
# 5. EAR & MAR FUNCTIONS
# -----------------------------
def ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def mar(mouth):
    A = distance.euclidean(mouth[13], mouth[19])
    B = distance.euclidean(mouth[14], mouth[18])
    C = distance.euclidean(mouth[12], mouth[16])
    return (A + B) / (2.0 * C)

# -----------------------------
# 6. VIDEO CAPTURE
# -----------------------------
cap = cv2.VideoCapture(0)

EAR_THRESH = 0.21
MAR_THRESH = 0.65
FRAME_LIMIT = 20
ear_count = 0

print("🚀 Driver Safety System Running... Press 'q' to exit.")

# -----------------------------
# 7. MAIN LOOP
# -----------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    for face in faces:
        lm = landmark_predictor(gray, face)

        left_eye = np.array([(lm.part(i).x, lm.part(i).y) for i in range(36, 42)])
        right_eye = np.array([(lm.part(i).x, lm.part(i).y) for i in range(42, 48)])
        mouth = np.array([(lm.part(i).x, lm.part(i).y) for i in range(48, 68)])

        EAR = (ear(left_eye) + ear(right_eye)) / 2
        MAR = mar(mouth)

        status = "Normal"

        # -----------------------------
        # DROWSINESS DETECTION
        # -----------------------------
        if EAR < EAR_THRESH:
            ear_count += 1

            if ear_count >= FRAME_LIMIT:
                status = "DROWSY"

                cv2.putText(frame, "DROWSINESS ALERT!", (20, 150),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                snap = f"drowsy_snaps/drowsy_{time.time()}.jpg"
                cv2.imwrite(snap, frame)

                if not alert_on:
                    alert_on = True
                    threading.Thread(target=voice_alert, daemon=True).start()
                    threading.Thread(target=beep_alarm, daemon=True).start()

        else:
            ear_count = 0
            alert_on = False

        # -----------------------------
        # YAWN DETECTION
        # -----------------------------
        if MAR > 0.75:
            status = "YAWNING"
            cv2.putText(frame, "YAWN DETECTED!", (20, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

            snap = f"drowsy_snaps/yawn_{time.time()}.jpg"
            cv2.imwrite(snap, frame)

            if not alert_on:
                alert_on = True
                threading.Thread(target=voice_alert, daemon=True).start()
                threading.Thread(target=beep_alarm, daemon=True).start()

        # -----------------------------
        # LOG DATA
        # -----------------------------
        with open(log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), EAR, MAR, status])

        # Display values
        cv2.putText(frame, f"EAR: {EAR:.2f}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        cv2.putText(frame, f"MAR: {MAR:.2f}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow("Driver Alert System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        alert_on = False
        break

cap.release()
cv2.destroyAllWindows()
