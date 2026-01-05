from openai import OpenAI
from pathlib import Path

client = OpenAI()

# Arquivos que serão usados como contexto
ARQUIVOS = [
    "activity_detector.txt",
    "emotion_detector.txt",
    "face_detector_dnn.txt",
    "face_tracker.txt",
    "main.txt",
    "report.txt",
    "output\relatorio_final.txt"
]

contexto = ""
for arquivo in ARQUIVOS:
    conteudo = Path(arquivo).read_text(encoding="utf-8")
    contexto += f"\n\n### {arquivo}\n{conteudo}"

prompt = f"""
Você é um narrador técnico acadêmico.

Crie um roteiro de podcast para um vídeo de demonstração do Tech Challenge – Fase 4.

Regras:
- Use SOMENTE as informações fornecidas
- Linguagem técnica, clara e objetiva
- Voz única masculina
- Duração aproximada: 5 a 7 minutos
- Explique o objetivo do projeto, o funcionamento do código e os resultados

Contexto do projeto:
{contexto}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.3
)

roteiro = response.choices[0].message.content

Path("roteiro_podcast.txt").write_text(roteiro, encoding="utf-8")

print("📝 Roteiro gerado com sucesso: roteiro_podcast.txt")
