import cv2
from deepface import DeepFace

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

print("[INFO] Sistem Deteksi Emosi dimulai... Tekan 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        # Analisis wajah (emosi, usia, gender, ras)
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        # Ambil emosi terdeteksi
        dominant_emotion = result[0]['dominant_emotion']

        # Tampilkan teks emosi
        cv2.putText(frame, f"Emosi: {dominant_emotion}", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    except Exception as e:
        print(f"[ERROR] {e}")
        cv2.putText(frame, "Wajah tidak terdeteksi", (50, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Tampilkan frame
    cv2.imshow("Deteksi Emosi FIXCODE", frame)

    # Tombol keluar = 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
