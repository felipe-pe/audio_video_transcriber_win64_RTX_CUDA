import subprocess
import logging
import os

def process_audio(input_audio_path, output_audio_path):
    """
    Processa o áudio para prepará-lo para transcrição. Isso pode incluir normalização ou resampling.
    """
    try:
        if not os.path.exists(input_audio_path):
            raise FileNotFoundError(f"Arquivo de áudio não encontrado: {input_audio_path}")

        # Exemplo de processamento com ffmpeg (resampling para 16kHz)
        command = [
            'ffmpeg', '-i', input_audio_path, '-ar', '16000', '-ac', '1', output_audio_path
        ]
        subprocess.run(command, check=True)
        logging.info(f"Áudio processado com sucesso e salvo em: {output_audio_path}")
        return output_audio_path
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao processar o áudio: {e}")
        raise e
