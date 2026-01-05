import subprocess
from pathlib import Path

# Caminhos dos arquivos
audio_path = Path(
    r"C:\Users\fferr\Desktop\Pos_Fase4_Constructor\output\Nova pasta\Anatomia_da_IA_que_Analisa_Vídeos.m4a"
)

video_path = Path(
    r"C:\Users\fferr\Desktop\Pos_Fase4_Constructor\output\video_processado.mp4"
)

output_path = Path(
    r"C:\Users\fferr\Desktop\Pos_Fase4_Constructor\output\video_final_completo_com_podcast.mp4"
)

# Validações
if not audio_path.exists():
    raise FileNotFoundError(f"Áudio não encontrado: {audio_path}")

if not video_path.exists():
    raise FileNotFoundError(f"Vídeo não encontrado: {video_path}")

print("🎧 Áudio encontrado:", audio_path.name)
print("🎬 Vídeo encontrado:", video_path.name)
print("🔁 Repetindo o vídeo até o áudio terminar...")
print("⚙️ Gerando vídeo final...")

# Comando FFmpeg com LOOP DE VÍDEO
cmd = [
    "ffmpeg",
    "-y",
    "-stream_loop", "-1",            # 🔁 loop infinito do vídeo
    "-i", str(video_path),            # vídeo
    "-i", str(audio_path),            # áudio
    "-map", "0:v:0",                  # vídeo do input 0
    "-map", "1:a:0",                  # áudio do input 1
    "-c:v", "copy",                   # não reencoda vídeo
    "-c:a", "aac",                    # áudio compatível
    "-shortest",                      # agora o áudio é o limitador
    str(output_path)
]

subprocess.run(cmd, check=True)

print("✅ VÍDEO FINAL COMPLETO GERADO COM SUCESSO!")
print("📁 Arquivo:", output_path)
