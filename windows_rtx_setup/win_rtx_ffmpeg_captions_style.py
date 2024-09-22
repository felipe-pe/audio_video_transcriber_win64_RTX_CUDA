import subprocess
import logging
import sys
import os

# Caminho para a pasta de logs
log_dir = os.path.join(os.path.dirname(__file__), 'install_logs')

# Cria a pasta de logs, se ela não existir
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configuração de logging
logging.basicConfig(
    filename=os.path.join(log_dir, 'install_visual_effects.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_visual_effects():
    """Instala pacotes para manipulação de legendas e efeitos visuais."""
    logging.info("Iniciando a instalação dos pacotes de manipulação de legendas e efeitos visuais.")
    
    try:
        # Instala o ffmpeg-python para manipulação do FFmpeg via Python (mantendo por redundância)
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ffmpeg-python'])
        logging.info("ffmpeg-python instalado com sucesso.")
        print("ffmpeg-python instalado com sucesso!")
        
        # Outros pacotes como Pillow, MoviePy, Tesseract já estão instalados em outros scripts, então não precisamos repetir aqui
        
    except subprocess.CalledProcessError as e:
        logging.error("Erro ao instalar pacotes: %s", e)
        print(f"Erro ao instalar pacotes: {e}")
    except Exception as general_error:
        logging.error("Erro inesperado: %s", general_error)
        print(f"Erro inesperado: {general_error}")

if __name__ == "__main__":
    logging.info("Script de instalação dos pacotes de manipulação de legendas e efeitos visuais iniciado.")
    install_visual_effects()
    logging.info("Script de instalação dos pacotes de manipulação de legendas e efeitos visuais finalizado.")
