from collections import Counter


class Report:
    def __init__(self):
        self.emotions = []
        self.anomalies = 0
        self.activities = []

    def log(self, track_id, emotion, activity, anomaly):
        self.emotions.append(emotion)
        self.activities.append(activity)
        if anomaly:
            self.anomalies += 1

    def generate(self, total_frames, output_path):
        emotion_count = Counter(self.emotions)
        activity_count = Counter(self.activities)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("TECH CHALLENGE – RELATÓRIO FINAL\n")
            f.write("=" * 40 + "\n\n")

            f.write(f"Total de frames analisados: {total_frames}\n")
            f.write(f"Número de anomalias detectadas: {self.anomalies}\n\n")

            f.write("Distribuição de Emoções:\n")
            for emo, count in emotion_count.items():
                f.write(f"- {emo}: {count}\n")

            f.write("\nDistribuição de Atividades:\n")
            for act, count in activity_count.items():
                f.write(f"- {act}: {count}\n")

            f.write("\nResumo Automático:\n")
            f.write(
                "O sistema analisou o vídeo identificando rostos, "
                "inferindo emoções por meio de modelos de deep learning "
                "e classificando atividades. Movimentos que não seguiram "
                "o padrão geral foram classificados como anômalos.\n"
            )
        print(f"✅ Relatório salvo em: {output_path}")