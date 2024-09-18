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
    filename=os.path.join(log_dir, 'install_flask_cors.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def install_flask_cors():
    """Instala o pacote flask-cors, gerando logs detalhados e verificando se o pacote já está instalado."""
    logging.info("Iniciando a instalação do pacote flask-cors.")
    
    try:
        # Executa o comando recomendado: python -m pip install flask-cors
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'flask-cors'])
        logging.info("flask-cors instalado com sucesso.")
        print("flask-cors instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        logging.error("Erro ao instalar flask-cors: %s", e)
        print(f"Erro ao instalar flask-cors: {e}")
    except Exception as general_error:
        logging.error("Erro inesperado ao instalar flask-cors: %s", general_error)
        print(f"Erro inesperado: {general_error}")

if __name__ == "__main__":
    logging.info("Script de instalação do flask-cors iniciado.")
    install_flask_cors()
    logging.info("Script de instalação do flask-cors finalizado.")
