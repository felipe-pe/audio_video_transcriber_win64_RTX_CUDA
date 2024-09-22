import os
import re
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

def format_srt(srt_file, output_file=None):
    """
    Formata o arquivo SRT para corrigir possíveis problemas específicos do modelo large-v3.
    
    Args:
        srt_file (str): Caminho do arquivo SRT a ser formatado.
        output_file (str): Caminho do arquivo de saída SRT formatado (opcional).
                           Se não for fornecido, sobrescreve o arquivo original.
    """
    try:
        # Se não for fornecido um arquivo de saída, usa o mesmo arquivo de entrada
        if output_file is None:
            output_file = srt_file
        
        # Verifica se o arquivo SRT existe
        if not os.path.exists(srt_file):
            raise FileNotFoundError(f"Arquivo SRT não encontrado: {srt_file}")

        logging.info(f"Lendo e formatando o arquivo SRT: {srt_file}")

        # Lê o conteúdo do arquivo SRT
        with open(srt_file, 'r', encoding='utf-8') as f:
            srt_content = f.readlines()

        # Formatação do conteúdo SRT (Exemplo de normalização de linhas)
        formatted_content = []
        buffer_text = ""

        for line in srt_content:
            line = line.strip()

            # Verifica se é um timestamp
            if re.match(r"^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$", line):
                # Se houver texto armazenado no buffer, adiciona ao conteúdo
                if buffer_text:
                    formatted_content.append(buffer_text)
                    buffer_text = ""
                formatted_content.append(line)  # Adiciona o timestamp
                
            # Verifica se é uma linha de número de sequência
            elif line.isdigit():
                # Adiciona o número de sequência
                formatted_content.append(line)

            else:
                # Concatena linhas de texto fragmentadas (frases quebradas)
                if buffer_text:
                    buffer_text += " " + line
                else:
                    buffer_text = line

        # Adiciona o último buffer de texto, se houver
        if buffer_text:
            formatted_content.append(buffer_text)

        # Escreve o conteúdo formatado no arquivo de saída
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write("\n".join(formatted_content) + "\n")

        logging.info(f"Arquivo SRT formatado e salvo: {output_file}")

    except Exception as e:
        logging.error(f"Erro ao formatar o arquivo SRT: {e}")
        raise e

# Exemplo de uso
if __name__ == "__main__":
    import argparse
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Formata um arquivo SRT para corrigir problemas de formatação.")
    parser.add_argument('--srt_file', required=True, help="Caminho do arquivo SRT a ser formatado")
    parser.add_argument('--output_file', help="Caminho do arquivo SRT formatado de saída (opcional)")

    args = parser.parse_args()

    # Executa a formatação
    format_srt(args.srt_file, args.output_file)
