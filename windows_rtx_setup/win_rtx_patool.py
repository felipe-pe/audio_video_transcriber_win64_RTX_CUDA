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
    filename=os.path.join(log_dir, 'install_patool.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_patool_installed():
    """Verifica se o patool está instalado."""
    logging.info("Verificando se o patool está instalado.")
    try:
        import patoolib
        logging.info("patool já está instalado.")
        print("patool já está instalado.")
        return True
    except ImportError:
        logging.info("patool não encontrado. Instalando agora...")
        return False

def install_patool():
    """Instala o patool usando pip."""
    logging.info("Instalando o patool via pip.")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'patool'])
        logging.info("patool instalado com sucesso.")
        print("patool instalado com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao instalar o patool: {e}")
        print(f"Erro ao instalar o patool: {e}")

if __name__ == "__main__":
    logging.info("Script de verificação/instalação do patool iniciado.")
    
    # Verifica se o patool está instalado e o instala se necessário
    if not check_patool_installed():
        install_patool()

    logging.info("Script de verificação/instalação do patool finalizado.")
