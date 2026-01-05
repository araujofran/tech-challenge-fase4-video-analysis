import cv2
import os

from face_detector_dnn import FaceDetectorDNN
from face_tracker import FaceTracker
from emotion_detector import EmotionDetector
from activity_detector import ActivityDetector
from report import Report


# ===============================
# CONFIGURAÇÕES
# ===============================
VIDEO_PATH = r"C:\Users\fferr\Desktop\Pos_Fase4_Constructor\Unlocking Facial Recognition_ Diverse Activities Analysis.mp4"

OUTPUT_DIR = "output"
OUTPUT_VIDEO = os.path.join(OUTPUT_DIR, "video_processado.mp4")

os.makedirs(OUTPUT_DIR, exist_ok=True)


EMOCOES_PT = {
    "happy": "feliz",
    "sad": "triste",
    "surprise": "surpreso",
    "angry": "raiva",
    "neutral": "neutro",
    "fear": "medo",
    "disgust": "nojo"
}


# ===============================
# INICIALIZAÇÃO
# ===============================
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise RuntimeError("Erro ao abrir o vídeo.")

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))


face_detector = FaceDetectorDNN()
tracker = FaceTracker(max_frames_missing=10)
emotion_detector = EmotionDetector()
activity_detector = ActivityDetector()
report = Report()

total_frames = 0


# ===============================
# LOOP PRINCIPAL
# ===============================
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    total_frames += 1

    boxes = face_detector.detect(frame)
    tracks = tracker.update(boxes)

    for track_id, track in tracks.items():
        x1, y1, x2, y2 = track["box"]
        face_roi = frame[y1:y2, x1:x2]

        emotion = emotion_detector.detect_emotion(face_roi, track_id)
        emotion_pt = EMOCOES_PT.get(emotion, emotion)

        activity, anomaly = activity_detector.detect((x1, y1, x2, y2), track_id)

        report.log(
            track_id=track_id,
            emotion=emotion,
            activity=activity,
            anomaly=anomaly
        )

        label = f"Pessoa {track_id} | {emotion} ({emotion_pt}) | {activity}"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(
            frame,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    video_writer.write(frame)
    cv2.imshow("Tech Challenge - Analise Facial", frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break


# ===============================
# FINALIZAÇÃO
# ===============================
cap.release()
video_writer.release()
cv2.destroyAllWindows()

report.generate(
    total_frames=total_frames,
    output_path=os.path.join(OUTPUT_DIR, "relatorio_final.txt")
)

print("✅ Vídeo salvo em:", OUTPUT_VIDEO)
print("✅ Relatório salvo em:", os.path.join(OUTPUT_DIR, "relatorio_final.txt"))
