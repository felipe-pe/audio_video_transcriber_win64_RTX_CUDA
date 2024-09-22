import os
import logging

def find_srt_file(directory):
    """
    Procura por qualquer arquivo SRT no diretório especificado.

    Args:
        directory (str): Caminho do diretório onde procurar o arquivo SRT.

    Returns:
        str: Caminho do arquivo SRT encontrado ou None se nenhum for encontrado.
    """
    for file in os.listdir(directory):
        if file.endswith('.srt'):
            return os.path.join(directory, file)
    return None

def is_timestamp(line):
    """
    Verifica se uma linha é um timestamp no formato SRT.

    Args:
        line (str): Linha a ser verificada.

    Returns:
        bool: True se a linha for um timestamp, False caso contrário.
    """
    return '-->' in line

def generate_html(srt_file, html_output):
    """
    Gera um arquivo HTML a partir do arquivo SRT, formatando todo o texto como um único parágrafo.

    Args:
        srt_file (str): Caminho do arquivo SRT de entrada.
        html_output (str): Caminho do arquivo HTML de saída.
    """
    try:
        # Verifica se o arquivo SRT existe
        if not os.path.exists(srt_file):
            logging.warning(f"Arquivo SRT {srt_file} não encontrado. Fazendo busca no diretório.")
            directory = os.path.dirname(srt_file)
            srt_file = find_srt_file(directory)
            if not srt_file:
                raise FileNotFoundError(f"Nenhum arquivo SRT encontrado no diretório: {directory}")
            logging.info(f"Arquivo SRT encontrado: {srt_file}")

        # Lê o conteúdo do arquivo SRT
        with open(srt_file, 'r', encoding='utf-8') as f:
            srt_content = f.readlines()

        # Filtra as linhas de texto (ignorando números e timestamps)
        paragraph_content = []
        for line in srt_content:
            line = line.strip()
            # Ignora números e timestamps
            if line and not line.isdigit() and not is_timestamp(line):
                paragraph_content.append(line)

        # Transforma o conteúdo em um único parágrafo, unindo as frases
        paragraph = ' '.join(paragraph_content)

        # Estrutura básica do arquivo HTML
        html_content = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Transcrição</title>
        </head>
        <body>
            <p>{paragraph}</p>
        </body>
        </html>
        """

        # Escreve o conteúdo no arquivo HTML
        with open(html_output, 'w', encoding='utf-8') as f_out:
            f_out.write(html_content)

        logging.info(f"Arquivo HTML gerado com sucesso: {html_output}")

    except Exception as e:
        logging.error(f"Erro ao gerar o arquivo HTML: {e}")
        raise e

# Exemplo de uso
if __name__ == "__main__":
    # Caminhos de entrada e saída
    srt_file = 'transcriptions_samples/sample_audio.srt'
    html_output = 'transcriptions_samples/sample.html'

    # Gera o arquivo HTML
    generate_html(srt_file, html_output)
