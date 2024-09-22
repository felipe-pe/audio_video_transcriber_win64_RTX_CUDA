import os
import logging
import subprocess
import time

def find_any_srt(output_dir):
    """
    Busca por qualquer arquivo SRT no diretório de saída.

    Args:
        output_dir (str): Diretório onde o arquivo SRT deve estar.

    Returns:
        str: Caminho completo para o arquivo SRT, ou None se não for encontrado.
    """
    for file in os.listdir(output_dir):
        if file.endswith(".srt"):
            return file  # Retorna apenas o nome do arquivo SRT
    return None

def transcribe_audio(input_audio, output_dir, config):
    """
    Transcreve o áudio utilizando o Whisper e gera o arquivo SRT.

    Args:
        input_audio (str): Caminho do arquivo de áudio a ser transcrito.
        output_dir (str): Diretório onde os arquivos de transcrição serão salvos.
        config (dict): Configurações adicionais para a transcrição.

    Returns:
        bool: Retorna True se bem-sucedido, False caso contrário.
    """
    start_time = time.perf_counter()

    # Verifica se o arquivo de áudio é válido
    if not os.path.exists(input_audio) or os.path.getsize(input_audio) == 0:
        logging.error(f"Arquivo de áudio {input_audio} está vazio ou inválido. Pulando transcrição.")
        return False

    try:
        logging.info("Iniciando transcrição...")

        # Comando de transcrição
        command = [
            "C:/Users/felipe/GitHub/audio_video_transcriber/transcreve_audios_apps_whisper_faster_xxl/Faster-Whisper-XXL/faster-whisper-xxl.exe",
            input_audio,
            '--language', 'Portuguese',
            '--model', config.get('model', 'large-v3'),
            '--output_dir', output_dir,
            '--device', 'cuda',
            '--beam_size', str(config['beam_size']),
            '--chunk_length', str(config['chunk_length'])
        ]

        logging.info(f"Executando comando de transcrição: {' '.join(command)}")

        # Executa a transcrição
        result = subprocess.run(command, check=False)
        logging.info(f"Transcrição concluída. Verificando o diretório de saída {output_dir}.")

        # Busca qualquer arquivo SRT no diretório de saída
        srt_file = find_any_srt(output_dir)

        # Se encontrar o arquivo SRT, mostrar os resultados e não gerar erro
        if srt_file:
            print(f"SRT Gerado: {os.path.basename(input_audio).replace('.wav', '.srt')}")
            print(f"SRT Encontrado: {srt_file}")
            logging.info(f"Arquivo SRT encontrado: {srt_file}")
        else:
            logging.warning(f"Nenhum arquivo SRT encontrado no diretório {output_dir}.")
            return False

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        logging.info(f"Tempo total de transcrição e geração do SRT: {elapsed_time:.2f} segundos")

        return True

    except Exception as e:
        logging.error(f"Erro inesperado durante a transcrição de {input_audio}: {e}")
        return False


if __name__ == "__main__":
    import argparse

    # Configuração de parâmetros
    parser = argparse.ArgumentParser(description="Transcreve áudio usando Whisper e gera arquivo SRT.")
    parser.add_argument("input_audio", type=str, help="Caminho para o arquivo de áudio.")
    parser.add_argument("output_dir", type=str, help="Diretório onde os arquivos de transcrição serão salvos.")
    parser.add_argument("--beam_size", type=int, default=5, help="Tamanho do beam para a transcrição.")
    parser.add_argument("--chunk_length", type=int, default=30, help="Comprimento máximo de chunks de áudio.")
    parser.add_argument("--model", type=str, default='large-v2', help="Modelo a ser usado pelo Faster-Whisper.")

    args = parser.parse_args()

    # Configuração para transcrição
    config = {
        'model': args.model,
        'beam_size': args.beam_size,
        'chunk_length': args.chunk_length
    }

    # Executar a transcrição e gerar o arquivo SRT
    success = transcribe_audio(args.input_audio, args.output_dir, config)
    if success:
        logging.info("Transcrição e geração de arquivos finalizada com sucesso!")
    else:
        logging.error("Falha na transcrição ou na geração dos arquivos.")
