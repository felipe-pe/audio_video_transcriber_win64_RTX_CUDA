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
    filename=os.path.join(log_dir, 'install_pytesseract.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_pytesseract():
    """Instala o pacote pytesseract e gera logs detalhados."""
    logging.info("Iniciando a instalação do pacote pytesseract.")
    
    try:
        # Executa o comando recomendado: python -m pip install pytesseract
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pytesseract'])
        logging.info("pytesseract instalado com sucesso.")
        print("pytesseract instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        logging.error("Erro ao instalar pytesseract: %s", e)
        print(f"Erro ao instalar pytesseract: {e}")
    except Exception as general_error:
        logging.error("Erro inesperado ao instalar pytesseract: %s", general_error)
        print(f"Erro inesperado: {general_error}")

if __name__ == "__main__":
    logging.info("Script de instalação do pytesseract iniciado.")
    install_pytesseract()
    logging.info("Script de instalação do pytesseract finalizado.")
