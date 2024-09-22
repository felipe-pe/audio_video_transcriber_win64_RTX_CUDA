import os
import logging

def generate_srt(transcription_file, output_file):
    """
    Gera um arquivo SRT a partir da transcrição.

    Args:
        transcription_file (str): Caminho completo do arquivo de transcrição.
        output_file (str): Caminho do arquivo SRT de saída.
    """
    try:
        if not os.path.exists(transcription_file):
            raise FileNotFoundError(f"Arquivo de transcrição não encontrado: {transcription_file}")
        
        with open(transcription_file, 'r') as f:
            transcript_lines = f.readlines()

        srt_content = []
        timestamp = 0
        time_per_line = 5  # Define o tempo de duração de cada linha em segundos

        for index, line in enumerate(transcript_lines):
            start_time = convert_seconds_to_srt_time(timestamp)
            end_time = convert_seconds_to_srt_time(timestamp + time_per_line)

            srt_content.append(f"{index + 1}")
            srt_content.append(f"{start_time} --> {end_time}")
            srt_content.append(line.strip())
            srt_content.append("")  # Linha em branco para separar blocos

            timestamp += time_per_line

        # Escreve o conteúdo gerado no arquivo SRT
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write("\n".join(srt_content))

        logging.info(f"Arquivo SRT gerado com sucesso: {output_file}")

    except Exception as e:
        logging.error(f"Erro ao gerar o arquivo SRT: {e}")
        raise e

def convert_seconds_to_srt_time(seconds):
    """
    Converte tempo em segundos para o formato de tempo do SRT (hh:mm:ss,ms).
    
    Args:
        seconds (int): Tempo em segundos.

    Returns:
        str: Tempo no formato SRT (hh:mm:ss,ms).
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = 0
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{milliseconds:03}"

# Exemplo de uso
if __name__ == "__main__":
    # Caminhos de entrada e saída
    transcription_file = 'transcriptions_samples/sample_transcript.txt'  # Arquivo de transcrição
    output_file = 'transcriptions_samples/sample_audio.srt'  # Arquivo SRT de saída

    # Gera o arquivo SRT
    generate_srt(transcription_file, output_file)
