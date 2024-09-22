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

def generate_ass(srt_file, ass_output, options=None):
    """
    Gera um arquivo ASS a partir do arquivo SRT, com opções personalizáveis.

    Args:
        srt_file (str): Caminho do arquivo SRT de entrada.
        ass_output (str): Caminho do arquivo ASS de saída.
        options (dict): Opções de personalização para o arquivo ASS.
            - 'vertical_position': Posição vertical da legenda ('low', 'middle', 'high').
            - 'font_color': Cor da legenda em formato hexadecimal (ex: &H00FFFFFF).
            - 'outline_color': Cor do contorno em formato hexadecimal.
            - 'margin_left': Margem esquerda (em pixels).
            - 'margin_right': Margem direita (em pixels).
            - 'margin_vertical': Margem vertical (em pixels).
    """
    # Define opções padrão
    default_options = {
        'vertical_position': 'low',
        'font_color': '&H00FFFFFF',  # Branco
        'outline_color': '&H00000000',  # Preto
        'margin_left': 10,
        'margin_right': 10,
        'margin_vertical': 10
    }

    if options:
        default_options.update(options)

    try:
        # Verifica se o arquivo SRT existe
        if not os.path.exists(srt_file):
            logging.warning(f"Arquivo SRT {srt_file} não encontrado. Fazendo busca no diretório.")
            directory = os.path.dirname(srt_file)
            srt_file = find_srt_file(directory)
            if not srt_file:
                raise FileNotFoundError(f"Nenhum arquivo SRT encontrado no diretório: {directory}")
            logging.info(f"Arquivo SRT encontrado: {srt_file}")

        # Cabeçalho ASS com as opções de estilo
        ass_header = f"""[Script Info]
Title: Gerado a partir de SRT
ScriptType: v4.00+
Collisions: Normal
PlayDepth: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, BackColour, Bold, Italic, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default, Arial, 20, {default_options['font_color']}, {default_options['outline_color']}, 0, 0, 1, 1.5, 0, {get_alignment(default_options['vertical_position'])}, {default_options['margin_left']}, {default_options['margin_right']}, {default_options['margin_vertical']}, 1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

        # Lê o conteúdo do arquivo SRT
        with open(srt_file, 'r', encoding='utf-8') as f:
            srt_content = f.readlines()

        ass_content = []
        current_dialogue = None
        for line in srt_content:
            line = line.strip()
            if line and '-->' in line:
                # Timestamp da linha SRT (converte para formato ASS)
                start_time, end_time = line.split(' --> ')
                start_time_ass = convert_srt_time_to_ass_time(start_time)
                end_time_ass = convert_srt_time_to_ass_time(end_time)
                current_dialogue = f"Dialogue: 0,{start_time_ass},{end_time_ass},Default,,0,0,0,,"
            elif line and not line.isdigit():
                # Adiciona o texto da legenda à linha do ASS
                if current_dialogue:
                    current_dialogue += line
                    ass_content.append(current_dialogue)
                    current_dialogue = None

        # Escreve o cabeçalho e o conteúdo no arquivo ASS
        with open(ass_output, 'w', encoding='utf-8') as f_out:
            f_out.write(ass_header)
            f_out.write("\n".join(ass_content))

        logging.info(f"Arquivo ASS gerado com sucesso: {ass_output}")

    except Exception as e:
        logging.error(f"Erro ao gerar o arquivo ASS: {e}")
        raise e

def get_alignment(position):
    """
    Retorna o código de alinhamento baseado na posição vertical.
    
    Args:
        position (str): Posição vertical da legenda ('low', 'middle', 'high').
        
    Returns:
        int: Código de alinhamento para o arquivo ASS.
    """
    alignment_map = {
        'low': 2,    # Baixo centralizado
        'middle': 5, # Centro
        'high': 8    # Alto centralizado
    }
    return alignment_map.get(position, 2)  # Retorna baixo como padrão

def convert_srt_time_to_ass_time(srt_time):
    """
    Converte o timestamp do formato SRT (hh:mm:ss,ms) para o formato ASS (h:mm:ss.xx).

    Args:
        srt_time (str): Timestamp no formato SRT.

    Returns:
        str: Timestamp no formato ASS.
    """
    hours, minutes, seconds = srt_time.split(':')
    seconds, milliseconds = seconds.split(',')
    ass_time = f"{int(hours)}:{minutes}:{seconds}.{int(milliseconds[:2])}"  # Usa apenas os dois primeiros dígitos dos milissegundos
    return ass_time

# Exemplo de uso
if __name__ == "__main__":
    # Caminhos de entrada e saída
    srt_file = 'transcriptions_samples/sample_audio.srt'
    ass_output = 'transcriptions_samples/sample.ass'

    # Opções de personalização do arquivo ASS
    options = {
        'vertical_position': 'middle',
        'font_color': '&H00FF00FF',  # Verde
        'outline_color': '&H00000000',  # Preto
        'margin_left': 15,
        'margin_right': 15,
        'margin_vertical': 20
    }

    # Gera o arquivo ASS
    generate_ass(srt_file, ass_output, options)
