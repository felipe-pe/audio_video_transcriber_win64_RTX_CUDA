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

def filter_srt_content(srt_content):
    """
    Filtra as linhas de texto do arquivo SRT, ignorando números de sequência e timestamps.

    Args:
        srt_content (list): Conteúdo do arquivo SRT, linha por linha.

    Returns:
        list: Linhas de texto filtradas.
    """
    txt_content = []
    for line in srt_content:
        line = line.strip()
        if line and not line.isdigit() and '-->' not in line:
            txt_content.append(line)
    return txt_content

def generate_txt(srt_file, txt_output):
    """
    Gera um arquivo de texto (TXT) simples a partir do arquivo SRT.

    Args:
        srt_file (str): Caminho do arquivo SRT de entrada.
        txt_output (str): Caminho do arquivo TXT de saída.
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
        logging.info(f"Lendo conteúdo do arquivo SRT: {srt_file}")
        with open(srt_file, 'r', encoding='utf-8') as f:
            srt_content = f.readlines()

        # Filtra o conteúdo do SRT para texto
        logging.info(f"Filtrando conteúdo do arquivo SRT para gerar o TXT.")
        txt_content = filter_srt_content(srt_content)

        # Escreve o conteúdo filtrado no arquivo TXT
        logging.info(f"Escrevendo conteúdo filtrado no arquivo TXT: {txt_output}")
        with open(txt_output, 'w', encoding='utf-8') as f_out:
            f_out.write("\n".join(txt_content))

        logging.info(f"Arquivo TXT gerado com sucesso: {txt_output}")

    except Exception as e:
        logging.error(f"Erro ao gerar o arquivo TXT: {e}")
        raise e

# Exemplo de uso
if __name__ == "__main__":
    # Configura logging
    logging.basicConfig(level=logging.INFO)

    # Caminhos de entrada e saída
    srt_file = 'transcriptions_samples/sample_audio.srt'
    txt_output = 'transcriptions_samples/sample.txt'

    # Gera o arquivo TXT
    generate_txt(srt_file, txt_output)
