import numpy as np

class FaceTracker:
    def __init__(self, max_frames_missing=10):
        self.tracks = {}
        self.next_id = 0
        self.max_frames_missing = max_frames_missing

    def _iou(self, a, b):
        xA = max(a[0], b[0])
        yA = max(a[1], b[1])
        xB = min(a[2], b[2])
        yB = min(a[3], b[3])

        inter = max(0, xB - xA) * max(0, yB - yA)
        areaA = (a[2]-a[0]) * (a[3]-a[1])
        areaB = (b[2]-b[0]) * (b[3]-b[1])

        return inter / float(areaA + areaB - inter + 1e-6)

    def update(self, boxes):
        updated = {}

        for box in boxes:
            matched = False
            for tid, track in self.tracks.items():
                if self._iou(box, track["box"]) > 0.3:
                    updated[tid] = {
                        "box": box,
                        "missed": 0
                    }
                    matched = True
                    break

            if not matched:
                updated[self.next_id] = {
                    "box": box,
                    "missed": 0
                }
                self.next_id += 1

        for tid, track in self.tracks.items():
            if tid not in updated:
                track["missed"] += 1
                if track["missed"] <= self.max_frames_missing:
                    updated[tid] = track

        self.tracks = updated
        return self.tracks
