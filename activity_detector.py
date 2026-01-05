import math


class ActivityDetector:
    def __init__(self, movement_threshold=15):
        self.last_positions = {}
        self.movement_threshold = movement_threshold

    def _center(self, box):
        x1, y1, x2, y2 = box
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        return cx, cy

    def detect(self, box, track_id):
        """
        Retorna:
        - activity: str
        - anomaly: bool
        """
        cx, cy = self._center(box)

        # Primeira aparição da pessoa
        if track_id not in self.last_positions:
            self.last_positions[track_id] = (cx, cy)
            return "parado", False

        px, py = self.last_positions[track_id]
        distance = math.hypot(cx - px, cy - py)

        self.last_positions[track_id] = (cx, cy)

        if distance > self.movement_threshold:
            return "movimento brusco", True
        elif distance > 3:
            return "movimento leve", False
        else:
            return "parado", False
