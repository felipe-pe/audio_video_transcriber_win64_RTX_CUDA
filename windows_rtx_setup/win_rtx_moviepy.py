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
    filename=os.path.join(log_dir, 'install_moviepy.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_moviepy():
    """Instala o pacote moviepy e gera logs detalhados."""
    logging.info("Iniciando a instalação do pacote moviepy.")
    
    try:
        # Executa o comando recomendado: python -m pip install moviepy
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'moviepy'])
        logging.info("moviepy instalado com sucesso.")
        print("moviepy instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        logging.error("Erro ao instalar moviepy: %s", e)
        print(f"Erro ao instalar moviepy: {e}")
    except Exception as general_error:
        logging.error("Erro inesperado ao instalar moviepy: %s", general_error)
        print(f"Erro inesperado: {general_error}")

if __name__ == "__main__":
    logging.info("Script de instalação do moviepy iniciado.")
    install_moviepy()
    logging.info("Script de instalação do moviepy finalizado.")
