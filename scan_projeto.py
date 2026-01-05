import os
from pathlib import Path

ROOT_DIR = Path(r"C:\Users\fferr\Desktop\Pos_Fase4_Constructor")
OUTPUT_FILE = ROOT_DIR / "estrutura_projeto.txt"

EXTENSOES_INTERESSE = {".py", ".txt", ".md", ".mp4", ".m4a", ".pdf"}

def tamanho_humano(bytes_size):
    for unidade in ["B", "KB", "MB", "GB"]:
        if bytes_size < 1024:
            return f"{bytes_size:.2f}{unidade}"
        bytes_size /= 1024
    return f"{bytes_size:.2f}TB"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("ESTRUTURA COMPLETA DO PROJETO\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"Diretório raiz: {ROOT_DIR}\n\n")

    for root, dirs, files in os.walk(ROOT_DIR):
        nivel = root.replace(str(ROOT_DIR), "").count(os.sep)
        indent = "  " * nivel

        f.write(f"{indent}📁 {os.path.basename(root)}\n")

        for file in files:
            caminho = Path(root) / file
            ext = caminho.suffix.lower()
            tamanho = tamanho_humano(caminho.stat().st_size)

            marcador = "📄"
            if ext in {".mp4", ".m4a"}:
                marcador = "🎬"
            elif ext == ".py":
                marcador = "🐍"
            elif ext == ".pdf":
                marcador = "📘"

            f.write(f"{indent}  {marcador} {file} ({tamanho})\n")

        f.write("\n")

print("✅ Varredura concluída com sucesso!")
print(f"📁 Arquivo gerado: {OUTPUT_FILE}")
