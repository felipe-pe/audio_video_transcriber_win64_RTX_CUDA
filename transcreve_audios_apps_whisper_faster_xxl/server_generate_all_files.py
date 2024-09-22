from flask import Flask, request, jsonify
import subprocess
import os
import logging
import time

app = Flask(__name__)

# Função para rodar a transcrição
def run_transcription(input_audio, output_dir):
    try:
        command = [
            "python", "main_standalone_faster_xxl_transcribe_audio.py",
            input_audio,
            output_dir,
            "--model", "large-v3"
        ]
        logging.info(f"Executando comando de transcrição: {' '.join(command)}")
        result = subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro na transcrição: {e}")
        return False

# Função para rodar a geração de arquivos (HTML, TXT, ASS)
def run_generate_files(srt_file, output_dir):
    try:
        command = [
            "python", "complete_generate_files.py",
            srt_file,
            output_dir
        ]
        logging.info(f"Executando comando de geração de arquivos: {' '.join(command)}")
        result = subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro na geração dos arquivos: {e}")
        return False

@app.route('/process', methods=['POST'])
def process_files():
    # Obtém os parâmetros da requisição
    data = request.get_json()
    input_audio = data.get('input_audio')
    output_dir = data.get('output_dir')

    if not input_audio or not output_dir:
        return jsonify({"error": "Parâmetros 'input_audio' e 'output_dir' são obrigatórios"}), 400

    # Rodar a transcrição
    if run_transcription(input_audio, output_dir):
        # Após a transcrição, encontrar o arquivo .srt gerado
        srt_file = None
        for file in os.listdir(output_dir):
            if file.endswith('.srt'):
                srt_file = os.path.join(output_dir, file)
                break

        if srt_file:
            # Rodar a geração de arquivos com o SRT gerado
            if run_generate_files(srt_file, output_dir):
                return jsonify({"message": "Transcrição e geração de arquivos concluídas com sucesso."}), 200
            else:
                return jsonify({"error": "Erro ao gerar os arquivos (HTML, TXT, ASS)."}), 500
        else:
            return jsonify({"error": "Arquivo SRT não encontrado."}), 500
    else:
        return jsonify({"error": "Erro ao transcrever o áudio."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6226)
