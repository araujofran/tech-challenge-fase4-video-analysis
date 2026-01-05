# 🎥 Tech Challenge – Fase 4

## Análise Automatizada de Vídeo com Reconhecimento Facial, Emoções e Detecção de Atividades

---

## 📌 Visão Geral do Projeto

Este projeto foi desenvolvido como entrega do **Tech Challenge – Fase 4 (IADT)** e tem como objetivo a **análise automatizada de vídeos**, aplicando técnicas de **Visão Computacional e Inteligência Artificial** para:

* Reconhecimento facial
* Análise de expressões emocionais
* Detecção de atividades e anomalias comportamentais
* Geração automática de relatório estatístico
* Produção de vídeo demonstrativo com **narração em formato de podcast**

Todo o pipeline foi implementado em **Python**, utilizando bibliotecas consolidadas de visão computacional e processamento multimídia.

---

## 🎯 Objetivo do Projeto (conforme o desafio)

De acordo com o enunciado oficial do Tech Challenge – Fase 4 , o objetivo principal é:

> Desenvolver uma aplicação capaz de analisar vídeos de forma automatizada, identificando rostos, inferindo emoções, classificando atividades e gerando relatórios que auxiliem na interpretação dos dados extraídos.

Este projeto atende integralmente aos requisitos propostos, incluindo **demonstração em vídeo**.

---

## 🧠 Funcionalidades Implementadas

### 1️⃣ Reconhecimento Facial

* Detecção de múltiplos rostos em tempo real
* Delimitação visual por bounding boxes
* Baseado em **DNN (Deep Neural Network)** com modelos pré-treinados

📄 Arquivo principal:

```
face_detector_dnn.py
face_tracker.py
```

---

### 2️⃣ Análise de Expressões Emocionais

* Classificação emocional por frame
* Emoções detectadas incluem:

  * Neutro
  * Felicidade
  * Tristeza
  * Outras variações conforme o modelo FER

📄 Arquivo:

```
emotion_detector.py
```

---

### 3️⃣ Detecção de Atividades e Anomalias

* Classificação de movimento em:

  * Parado
  * Movimento leve
  * Movimento brusco
* Identificação de **anomalias comportamentais**
* Contabilização automática dos eventos detectados

📄 Arquivo:

```
activity_detector.py
```

---

### 4️⃣ Pipeline Principal de Processamento

* Leitura do vídeo de entrada
* Processamento frame a frame
* Integração entre:

  * Detecção facial
  * Emoções
  * Atividades
* Geração do vídeo processado com overlays visuais

📄 Arquivo:

```
main.py
```

---

### 5️⃣ Geração Automática de Relatório

* Consolidação estatística dos dados analisados:

  * Total de frames processados
  * Distribuição de emoções
  * Número de anomalias detectadas
* Exportação para arquivo `.txt`

📄 Arquivo:

```
report.py
```

📄 Saída:

```
output/relatorio_final.txt
```

---

### 6️⃣ Narração em Formato de Podcast (IA)

* Geração de roteiro automatizado com base:

  * Nos códigos `.py`
  * No relatório final
  * Nos requisitos do desafio
* Conversão do roteiro em áudio narrado (voz masculina estilo podcast)

📄 Arquivo:

```
gerar_audio.py
```

📄 Saída:

```
output/Nova pasta/Anatomia_da_IA_que_Analisa_Vídeos.m4a
```

---

### 7️⃣ Vídeo Final com Podcast Integrado

* O vídeo processado é **repetido automaticamente** para cobrir toda a duração do podcast
* O áudio é sincronizado e incorporado ao vídeo final
* Resultado pronto para entrega

📄 Arquivo:

```
unir_audio_video.py
```

📄 Saída final:

```
output/video_final_completo_com_podcast.mp4
```

---

## 🗂️ Estrutura do Projeto

```text
Pos_Fase4_Constructor/
│
├── activity_detector.py
├── emotion_detector.py
├── face_detector_dnn.py
├── face_tracker.py
├── main.py
├── report.py
├── gerar_audio.py
├── unir_audio_video.py
├── scan_projeto.py
├── requirements.txt
├── Tech Challenge - IADT - Fase 4.pdf
│
├── models/
│   ├── deploy.prototxt
│   ├── res10_300x300_ssd_iter_140000.caffemodel
│   ├── face_landmarker.task
│   └── ffmpeg/
│
├── output/
│   ├── video_processado.mp4
│   ├── video_final_completo_com_podcast.mp4
│   ├── relatorio_final.txt
│   └── Nova pasta/
│       └── Anatomia_da_IA_que_Analisa_Vídeos.m4a
│
└── venv/
```

---

## ⚙️ Tecnologias Utilizadas

* **Python 3.12+**
* **OpenCV**
* **FER (Facial Expression Recognition)**
* **MediaPipe**
* **FFmpeg**
* **NumPy**
* **IA Generativa (Text-to-Speech)**

---

## ▶️ Como Executar o Projeto

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Processar o vídeo

```bash
python main.py
```

### 4️⃣ Gerar relatório

```bash
python report.py
```

### 5️⃣ Gerar áudio (podcast)

```bash
python gerar_audio.py
```

### 6️⃣ Gerar vídeo final com podcast

```bash
python unir_audio_video.py
```

---

## 🎬 Demonstração em Vídeo

O vídeo final demonstra:

* Reconhecimento facial em tempo real
* Inferência emocional
* Detecção de atividades e anomalias
* Relatório consolidado
* Narração explicativa em formato de podcast

📁 Arquivo:

```
video_final_completo_com_podcast.mp4
```

---

## ✅ Status do Projeto

✔ Todos os requisitos do Tech Challenge – Fase 4 atendidos
✔ Código funcional e documentado
✔ Demonstração em vídeo dentro do limite de tempo
✔ Pipeline completo de análise automatizada

---

## 👤 Autor(es)

***Francisco Ferreira de Araujo*** /fferreira.araujo@hotmail.com - RM361133
***Diego Silva Prado***/ prado.dis@gmail.com - RM362655
***Ricardo Almeida da Rocha***/ricardoalmeida.for@gmail.com - RM364919


Projeto desenvolvido para fins acadêmicos – Pós-graduação / IADT

---

