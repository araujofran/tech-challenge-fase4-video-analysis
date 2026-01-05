import cv2

class FaceDetectorDNN:
    def __init__(self):
        self.net = cv2.dnn.readNetFromCaffe(
            r"models\deploy.prototxt",
            r"models\res10_300x300_ssd_iter_140000.caffemodel"
        )

    def detect(self, frame, conf_threshold=0.3):
        h, w = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(
            cv2.resize(frame, (300, 300)),
            1.0,
            (300, 300),
            (104.0, 177.0, 123.0)
        )

        self.net.setInput(blob)
        detections = self.net.forward()

        boxes = []

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > conf_threshold:
                box = detections[0, 0, i, 3:7] * [w, h, w, h]
                x1, y1, x2, y2 = box.astype("int")

                # garante que não saia da imagem
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(w, x2), min(h, y2)

                boxes.append((x1, y1, x2, y2))

        return boxes
