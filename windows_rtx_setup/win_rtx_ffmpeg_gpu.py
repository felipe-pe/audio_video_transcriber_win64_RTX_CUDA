import os
import urllib.request
import logging
import patoolib
import zipfile

# Caminho para a pasta de logs
log_dir = os.path.join(os.path.dirname(__file__), 'install_logs')

# Cria a pasta de logs, se ela não existir
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configuração de logging
logging.basicConfig(
    filename=os.path.join(log_dir, 'install_ffmpeg.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# URLs do FFmpeg compatível com GPU
ffmpeg_7z_url = "https://github.com/GyanD/codexffmpeg/releases/download/2024-09-16-git-76ff97cef5/ffmpeg-2024-09-16-git-76ff97cef5-full_build.7z"
ffmpeg_zip_url = "https://github.com/GyanD/codexffmpeg/releases/download/2024-09-16-git-76ff97cef5/ffmpeg-2024-09-16-git-76ff97cef5-full_build.zip"

# Diretório de instalação no ambiente virtual
venv_bin_path = os.path.join(os.path.dirname(__file__), '..', 'transcribe_env', 'Scripts')

# Caminho do arquivo baixado
download_path = os.path.join(os.path.dirname(__file__), 'ffmpeg-download')

def download_ffmpeg(url):
    """Faz o download do FFmpeg a partir da URL fornecida."""
    logging.info("Baixando o FFmpeg a partir da URL: %s", url)
    try:
        urllib.request.urlretrieve(url, download_path)
        logging.info("Download do FFmpeg concluído com sucesso.")
        return True
    except Exception as e:
        logging.error(f"Erro ao baixar o FFmpeg da URL {url}: {e}")
        return False

def validate_download():
    """Valida se o arquivo baixado é um arquivo 7z ou zip."""
    if os.path.exists(download_path):
        if download_path.endswith('.7z') or download_path.endswith('.zip'):
            return download_path.endswith('.7z'), download_path.endswith('.zip')
        else:
            logging.error("O arquivo baixado não tem a extensão 7z ou zip.")
            return None, None
    logging.error("Arquivo de download não encontrado.")
    return None, None

def extract_ffmpeg(file_type):
    """Extrai o arquivo FFmpeg dentro do ambiente virtual."""
    logging.info("Extraindo o FFmpeg com patool na pasta: %s", venv_bin_path)
    try:
        if not os.path.exists(venv_bin_path):
            os.makedirs(venv_bin_path)

        if file_type:
            if file_type[0]:  # Se for 7z
                patoolib.extract_archive(download_path, outdir=venv_bin_path)
            elif file_type[1]:  # Se for zip
                with zipfile.ZipFile(download_path, 'r') as zip_ref:
                    zip_ref.extractall(venv_bin_path)

            logging.info("FFmpeg extraído com sucesso na pasta: %s", venv_bin_path)
        else:
            logging.error("Formato de arquivo desconhecido. Não é possível extrair.")
            raise Exception("Formato de arquivo desconhecido.")
    except Exception as e:
        logging.error(f"Erro ao extrair o FFmpeg: {e}")
        raise

def set_ffmpeg_as_default():
    """Configura FFmpeg, FFprobe e FFplay para serem usados por padrão no ambiente virtual."""
    logging.info("Configurando FFmpeg como padrão no virtualenv.")
    try:
        os.environ['PATH'] = venv_bin_path + os.pathsep + os.environ['PATH']
        logging.info("FFmpeg configurado como padrão. O novo PATH é: %s", os.environ['PATH'])
        print("FFmpeg configurado como padrão no ambiente virtual!")
    except Exception as e:
        logging.error(f"Erro ao configurar o FFmpeg como padrão: {e}")
        raise

def install_ffmpeg():
    """Realiza o processo completo de instalação do FFmpeg no ambiente virtual."""
    logging.info("Iniciando instalação do FFmpeg.")

    # Tenta baixar o arquivo 7z primeiro
    if download_ffmpeg(ffmpeg_7z_url):
        logging.info("Usando a URL 7z para o download do FFmpeg.")
    else:
        logging.info("Tentando usar a URL zip para o download do FFmpeg.")
        if not download_ffmpeg(ffmpeg_zip_url):
            logging.error("Falha ao baixar o FFmpeg de ambas as URLs.")
            print("Erro durante a instalação do FFmpeg: Falha ao baixar de ambas as URLs.")
            return

    file_type = validate_download()
    if file_type is None:
        print("Erro: O arquivo baixado não é válido. Verifique os logs.")
        return

    extract_ffmpeg(file_type)
    set_ffmpeg_as_default()
    os.remove(download_path)  # Remover o arquivo de instalação após a extração
    logging.info("FFmpeg instalado e configurado com sucesso.")

if __name__ == "__main__":
    install_ffmpeg()
