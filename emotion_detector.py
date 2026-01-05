import cv2
import numpy as np
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class EmotionDetector:
    def __init__(self):
        base_options = python.BaseOptions(
            model_asset_path="models/face_landmarker.task"
        )

        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            output_face_blendshapes=True,
            num_faces=1
        )

        self.detector = vision.FaceLandmarker.create_from_options(options)

    def detect_emotion(self, face_img, track_id=None):
        if face_img.size == 0:
            return "neutral"

        rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)

        # ✅ CLASSE CORRETA NA VERSÃO 0.10.31
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = self.detector.detect(mp_image)

        if not result.face_blendshapes:
            return "neutral"

        blendshapes = result.face_blendshapes[0]
        scores = {b.category_name: b.score for b in blendshapes}

        # 🎭 Inferência de emoção baseada em ML pesado (blendshapes)
        if scores.get("jawOpen", 0) > 0.4:
            return "surprise"
        if scores.get("mouthSmileLeft", 0) + scores.get("mouthSmileRight", 0) > 0.6:
            return "happy"
        if scores.get("browDownLeft", 0) + scores.get("browDownRight", 0) > 0.6:
            return "angry"
        if scores.get("eyeBlinkLeft", 0) + scores.get("eyeBlinkRight", 0) > 0.7:
            return "sad"

        return "neutral"
