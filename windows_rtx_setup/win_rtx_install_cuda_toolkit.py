import os
import subprocess
import urllib.request

# Lista de arquivos triviais do Git que não contam como conteúdo "real" da pasta
TRIVIAL_FILES = {".gitignore", ".keep", ".gitattributes"}

def is_directory_empty_or_trivial(directory):
    """
    Verifica se a pasta está vazia ou contém apenas arquivos triviais do Git.
    """
    for filename in os.listdir(directory):
        if filename not in TRIVIAL_FILES:
            return False  # Encontrou um arquivo que não é trivial
    return True  # Só encontrou arquivos triviais ou está vazia

def download_cuda_toolkit(url, download_path):
    # Fazendo o download do CUDA Toolkit
    print(f"Baixando o CUDA Toolkit de {url}...")
    urllib.request.urlretrieve(url, download_path)
    print("Download completo!")

def install_cuda_toolkit(installer_path, cuda_path):
    # Simula a instalação do CUDA Toolkit no caminho especificado
    print(f"Instalando CUDA Toolkit em {cuda_path}...")
    
    # Verifica se a pasta existe e se está "vazia" ou contém apenas arquivos triviais
    if not os.path.exists(cuda_path):
        os.makedirs(cuda_path)
        print(f"Pasta {cuda_path} criada.")
    elif is_directory_empty_or_trivial(cuda_path):
        print(f"Pasta {cuda_path} existente, mas contém apenas arquivos triviais do Git. Prosseguindo com a instalação.")
    else:
        print(f"Pasta {cuda_path} já contém arquivos não triviais. Prosseguindo com a instalação e sobrescrevendo se necessário.")
    
    # Executa o arquivo de instalação do CUDA
    subprocess.run([installer_path, "/S", f"/D={cuda_path}"], check=True)
    print(f"CUDA Toolkit instalado em {cuda_path}.")

def setup_cuda_env(cuda_path):
    # Configura variáveis de ambiente para usar o CUDA
    print(f"Configurando variáveis de ambiente para CUDA no caminho: {cuda_path}")
    os.environ["PATH"] = f"{os.path.join(cuda_path, 'bin')};" + os.environ.get("PATH", "")
    os.environ["CUDA_PATH"] = cuda_path
    os.environ["CUDA_HOME"] = cuda_path
    os.environ["LD_LIBRARY_PATH"] = f"{os.path.join(cuda_path, 'lib64')};" + os.environ.get("LD_LIBRARY_PATH", "")

def main():
    # URL oficial do CUDA Toolkit 12.6 para Windows
    cuda_download_url = "https://developer.download.nvidia.com/compute/cuda/12.6.1/local_installers/cuda_12.6.1_560.94_windows.exe"
    
    # Caminho onde o instalador será baixado
    installer_path = os.path.join(os.getcwd(), "cuda_installer.exe")
    
    # Caminho onde o CUDA será instalado (no repositório do projeto)
    cuda_path = os.path.join(os.getcwd(), "cuda_toolkit")

    # Fazer o download do CUDA Toolkit
    download_cuda_toolkit(cuda_download_url, installer_path)
    
    # Instalar o CUDA Toolkit
    install_cuda_toolkit(installer_path, cuda_path)
    
    # Configurar variáveis de ambiente
    setup_cuda_env(cuda_path)
    
    # Verificar instalação
    result = subprocess.run(["nvcc", "--version"], capture_output=True, text=True)
    if "release 12.6" in result.stdout:
        print("Instalação e configuração do CUDA verificadas com sucesso.")
    else:
        print("Erro ao verificar a instalação do CUDA.")

    # Deletar o arquivo de instalação após a conclusão
    if os.path.exists(installer_path):
        os.remove(installer_path)
        print(f"Arquivo de instalação {installer_path} deletado com sucesso.")

if __name__ == "__main__":
    main()
