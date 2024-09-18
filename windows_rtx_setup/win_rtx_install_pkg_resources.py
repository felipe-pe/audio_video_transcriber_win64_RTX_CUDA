import subprocess
import logging
import sys
import pkgutil

# Configuração de logging
logging.basicConfig(
    filename='install_pkg_resources.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def is_pkg_resources_available():
    """Verifica se o pkg_resources (parte do setuptools) está disponível."""
    logging.info("Verificando se o pkg_resources está disponível.")
    if pkgutil.find_loader('pkg_resources'):
        logging.info("pkg_resources já está disponível.")
        return True
    else:
        logging.info("pkg_resources não foi encontrado.")
        return False

def install_pkg_resources():
    """Instala o pacote setuptools para garantir que pkg_resources esteja disponível."""
    logging.info("Iniciando a instalação do setuptools (pkg_resources).")

    try:
        # Executa o comando recomendado: python -m pip install setuptools
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'setuptools'])
        logging.info("setuptools (pkg_resources) instalado com sucesso.")
        print("setuptools (pkg_resources) instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        logging.error("Erro ao instalar setuptools (pkg_resources): %s", e)
        print(f"Erro ao instalar setuptools (pkg_resources): {e}")
    except Exception as general_error:
        logging.error("Erro inesperado ao instalar setuptools (pkg_resources): %s", general_error)
        print(f"Erro inesperado: {general_error}")

if __name__ == "__main__":
    logging.info("Script de instalação do pkg_resources iniciado.")
    
    # Verifica se o pkg_resources já está disponível antes de tentar instalar
    if is_pkg_resources_available():
        print("pkg_resources já está instalado. Nenhuma ação necessária.")
    else:
        print("pkg_resources não foi encontrado. Iniciando a instalação.")
        install_pkg_resources()

    logging.info("Script de instalação do pkg_resources finalizado.")
