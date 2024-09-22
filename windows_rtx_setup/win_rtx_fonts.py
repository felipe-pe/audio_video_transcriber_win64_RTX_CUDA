import os
import requests

def download_font(url, font_name, save_dir):
    """Baixa uma fonte de um URL e a salva no diretório especificado"""
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    font_path = os.path.join(save_dir, font_name)

    # Baixa o arquivo da fonte
    response = requests.get(url)
    if response.status_code == 200:
        with open(font_path, 'wb') as f:
            f.write(response.content)
        print(f"Fonte {font_name} baixada com sucesso em {save_dir}")
    else:
        print(f"Falha ao baixar a fonte {font_name}")

if __name__ == "__main__":
    font_url = "https://example.com/path/to/font.ttf"  # Insira a URL correta para a fonte
    font_name = "custom_font.ttf"
    save_directory = os.path.join(os.getcwd(), "fonts")  # Diretório onde as fontes serão salvas

    download_font(font_url, font_name, save_directory)
