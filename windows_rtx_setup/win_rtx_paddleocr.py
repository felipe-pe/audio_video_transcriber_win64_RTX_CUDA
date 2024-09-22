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
    filename=os.path.join(log_dir, 'install_paddleocr.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_paddleocr():
    """Instala os pacotes paddleocr e paddlepaddle-gpu com logs."""
    logging.info("Iniciando a instalação do paddleocr e paddlepaddle-gpu.")
    
    try:
        # Instala o paddlepaddle-gpu
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'paddlepaddle-gpu'])
        logging.info("paddlepaddle-gpu instalado com sucesso.")
        print("paddlepaddle-gpu instalado com sucesso!")
        
        # Instala o paddleocr
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'paddleocr'])
        logging.info("paddleocr instalado com sucesso.")
        print("paddleocr instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        logging.error("Erro ao instalar paddleocr ou paddlepaddle-gpu: %s", e)
        print(f"Erro ao instalar paddleocr ou paddlepaddle-gpu: {e}")
    except Exception as general_error:
        logging.error("Erro inesperado: %s", general_error)
        print(f"Erro inesperado: {general_error}")

if __name__ == "__main__":
    logging.info("Script de instalação do PaddleOCR iniciado.")
    install_paddleocr()
    logging.info("Script de instalação do PaddleOCR finalizado.")
