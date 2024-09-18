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
    filename=os.path.join(log_dir, 'install_opencv_python_headless.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_opencv_python_headless():
    """Instala o pacote opencv-python-headless e gera logs detalhados."""
    logging.info("Iniciando a instalação do pacote opencv-python-headless.")
    
    try:
        # Executa o comando recomendado: python -m pip install opencv-python-headless
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python-headless'])
        logging.info("opencv-python-headless instalado com sucesso.")
        print("opencv-python-headless instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        logging.error("Erro ao instalar opencv-python-headless: %s", e)
        print(f"Erro ao instalar opencv-python-headless: {e}")
    except Exception as general_error:
        logging.error("Erro inesperado ao instalar opencv-python-headless: %s", general_error)
        print(f"Erro inesperado: {general_error}")

if __name__ == "__main__":
    logging.info("Script de instalação do opencv-python-headless iniciado.")
    install_opencv_python_headless()
    logging.info("Script de instalação do opencv-python-headless finalizado.")
