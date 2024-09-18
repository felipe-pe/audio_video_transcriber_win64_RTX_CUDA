import os
import urllib.request
import logging
import patoolib
import shutil

# Caminho para a pasta de logs
log_dir = os.path.join(os.path.dirname(__file__), 'install_logs')

# Cria a pasta de logs, se ela não existir
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configuração de logging
logging.basicConfig(
    filename=os.path.join(log_dir, 'install_whisper.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# URLs e diretórios de instalação
whisper_url = "https://github.com/Purfview/whisper-standalone-win/releases/download/Faster-Whisper-XXL/Faster-Whisper-XXL_r192.3.4_windows.7z"
install_dir = os.path.join(os.path.dirname(__file__), '..', 'whisper_faster_xxl')
download_path = os.path.join(os.path.dirname(__file__), 'Faster-Whisper-XXL_r192.3.4_windows.7z')

def is_whisper_installed():
    """Verifica se o Faster-Whisper XXL já está instalado e se a pasta contém arquivos válidos, ignorando arquivos do Git."""
    if not os.path.exists(install_dir):
        return False
    
    # Lista de arquivos do Git para ignorar ao verificar se a pasta está vazia
    git_files = {".gitignore", ".gitkeep"}

    # Verifica se há arquivos que não sejam os triviais de Git
    valid_files = [f for f in os.listdir(install_dir) if f not in git_files]
    
    return len(valid_files) > 0

def download_whisper():
    """Faz o download do Faster-Whisper XXL."""
    logging.info("Baixando o Faster-Whisper XXL.")
    try:
        urllib.request.urlretrieve(whisper_url, download_path)
        logging.info("Download concluído.")
    except Exception as e:
        logging.error(f"Erro ao baixar o Faster-Whisper: {e}")
        raise

def extract_whisper():
    """Extrai o arquivo .7z usando patool."""
    logging.info("Extraindo o Faster-Whisper XXL com patool.")
    
    try:
        # Extrai o arquivo usando o patoolib
        patoolib.extract_archive(download_path, outdir=install_dir)
        logging.info("Extração concluída com sucesso.")
        print("Faster-Whisper XXL instalado com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao extrair o Faster-Whisper: {e}")
        print(f"Erro ao extrair o Faster-Whisper: {e}")
        raise

def install_whisper():
    """Instala o Faster-Whisper XXL."""
    logging.info("Iniciando a instalação do Faster-Whisper XXL.")
    
    if is_whisper_installed():
        logging.info("Faster-Whisper XXL já está instalado ou a pasta contém arquivos.")
        print("Faster-Whisper XXL já está instalado ou a pasta contém arquivos.")
        return

    try:
        download_whisper()
        extract_whisper()
        os.remove(download_path)  # Remove o arquivo 7z após a instalação
    except Exception as e:
        logging.error(f"Erro durante a instalação do Faster-Whisper: {e}")
        print(f"Erro durante a instalação do Faster-Whisper: {e}")

def update_whisper():
    """Verifica se o Faster-Whisper precisa ser atualizado e realiza a atualização."""
    logging.info("Verificando se o Faster-Whisper precisa ser atualizado.")
    
    if is_whisper_installed():
        logging.info("Atualizando o Faster-Whisper XXL.")
        shutil.rmtree(install_dir)  # Remove a instalação atual
        install_whisper()  # Reinstala a versão mais recente
        logging.info("Faster-Whisper atualizado com sucesso.")
        print("Faster-Whisper atualizado com sucesso!")
    else:
        install_whisper()

if __name__ == "__main__":  
    logging.info("Script de instalação/atualização do Faster-Whisper iniciado.")
    
    # Verifica se é necessário atualizar ou instalar
    update_whisper()
    
    logging.info("Script de instalação/atualização do Faster-Whisper finalizado.")
