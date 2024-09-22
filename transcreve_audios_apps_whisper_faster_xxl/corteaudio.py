from pydub import AudioSegment

# Caminho para o arquivo de áudio original
input_audio = "C:/Users/felipe/GitHub/audio_video_transcriber/download_videos_apps/temporary_downloads/samples_standalone_downloads/user123/video_XbgfkeV2_Cc/video_XbgfkeV2_Cc_audio.wav"

# Caminho para salvar o áudio fatiado (especificar o nome do arquivo)
output_audio = "C:/Users/felipe/GitHub/audio_video_transcriber/transcreve_audios_apps_whisper_faster_xxl/transcriptions_samples/video_XbgfkeV2_Cc_audio_slice.wav"

# Carregar o arquivo de áudio
audio = AudioSegment.from_file(input_audio)

# Definir a duração do slice (30 segundos em milissegundos)
duration_ms = 30 * 1000  # 30 segundos

# Fatia o áudio
sliced_audio = audio[:duration_ms]

# Exporta o áudio fatiado com o nome do arquivo correto
sliced_audio.export(output_audio, format="wav")

print(f"Áudio fatiado salvo em: {output_audio}")
