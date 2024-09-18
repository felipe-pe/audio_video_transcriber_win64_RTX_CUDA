from faster_whisper import WhisperModel

# Caminho para o arquivo de áudio extraído
audio_file = "C:/Users/felipe/GitHub/audio_video_transcriber/output_audio.aac"

# Carregue o modelo 'large-v2'
model = WhisperModel("large-v2", device="cuda", compute_type="float16")

# Transcrever o áudio
segments, info = model.transcribe(audio_file)

print(f"Language: {info.language}, Duration: {info.duration}s")

# Salvar a transcrição em um arquivo SRT
with open("transcription.srt", "w", encoding="utf-8") as srt_file:
    for segment in segments:
        # Formatar no estilo SRT
        start = segment.start
        end = segment.end
        text = segment.text
        srt_file.write(f"{start} --> {end}\n{text}\n\n")

print("Transcrição finalizada e salva como transcription.srt.")
