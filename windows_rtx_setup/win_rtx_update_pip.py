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
    filename=os.path.join(log_dir, 'update_pip.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def update_pip():
    """Atualiza o pip usando o comando recomendado via python -m pip."""
    logging.info("Iniciando a atualização do pip.")
    
    try:
        # Executa o comando recomendado: python -m pip install --upgrade pip
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        logging.info("pip atualizado com sucesso.")
        print("pip atualizado com sucesso!")
    except subprocess.CalledProcessError as e:
        logging.error("Erro ao atualizar o pip: %s", e)
        print(f"Erro ao atualizar o pip: {e}")
    except Exception as general_error:
        logging.error("Erro inesperado ao atualizar o pip: %s", general_error)
        print(f"Erro inesperado: {general_error}")

if __name__ == "__main__":
    logging.info("Script de atualização do pip iniciado.")
    update_pip()
    logging.info("Script de atualização do pip finalizado.")
