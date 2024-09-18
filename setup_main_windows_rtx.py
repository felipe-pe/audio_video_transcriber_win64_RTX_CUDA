import os
import subprocess

def run_script(script_name):
    """Função para executar um script Python localizado na pasta windows_rtx_setup."""
    script_path = os.path.join(os.getcwd(), 'windows_rtx_setup', script_name)
    
    if os.path.exists(script_path):
        print(f"Executando {script_name}...")
        try:
            subprocess.run(['python', script_path], check=True)
            print(f"{script_name} executado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar {script_name}: {e}")
    else:
        print(f"Script {script_name} não encontrado em {script_path}.")

def main():
    # Lista dos scripts a serem executados
    scripts = [
        'win_rtx_update_pip.py',
        'win_rtx_install_pkg_resources.py',
        'win_rtx_install_cuda_toolkit.py',
        'win_rtx_flask_cors.py',
        'win_rtx_moviepy.py',
        'win_rtx_opencv_python_headless.py',
        'win_rtx_pytesseract.py',
        'win_rtx_patool.py',
        'win_rtx_Faster-Whisper-XXL.py'
    ]
    
    # Executar cada script na ordem especificada
    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()
