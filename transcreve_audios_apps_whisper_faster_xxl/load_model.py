import os
import logging

def load_faster_whisper_xxl(model_dir):
    """
    Carrega o modelo Faster-Whisper-XXL do diretório fornecido.
    """
    try:
        model_path = os.path.join(model_dir, 'faster-whisper-xxl.exe')
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Modelo não encontrado em {model_path}")
        
        logging.info(f"Modelo carregado com sucesso de {model_path}")
        return model_path
    except Exception as e:
        logging.error(f"Erro ao carregar o modelo: {e}")
        raise e
