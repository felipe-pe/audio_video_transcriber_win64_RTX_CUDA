import subprocess
import logging

def transcribe_audio(model_path, audio_path, output_path):
    """
    Usa o modelo Faster-Whisper-XXL para transcrever o áudio.
    """
    try:
        command = [
            model_path, '--audio', audio_path, '--output', output_path
        ]
        subprocess.run(command, check=True)
        logging.info(f"Transcrição concluída com sucesso. Resultado salvo em: {output_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro durante a transcrição: {e}")
        raise e
