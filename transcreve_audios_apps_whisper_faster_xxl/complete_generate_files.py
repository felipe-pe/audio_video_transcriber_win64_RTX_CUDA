import os
import argparse
import sys
from generate_txt import generate_txt
from generate_html import generate_html
from generate_ass import generate_ass

def generate_files(input_srt, output_dir):
    """
    Função que gera arquivos .txt, .html e .ass a partir de um arquivo .srt.
    
    Args:
        input_srt (str): Caminho para o arquivo .srt de entrada.
        output_dir (str): Diretório de saída para os arquivos gerados.
    """
    # Verifica se o arquivo .srt existe
    if not os.path.isfile(input_srt):
        print(f"Erro: O arquivo {input_srt} não existe.")
        sys.exit(1)

    # Verifica se o diretório de saída existe, se não, cria
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"Diretório de saída criado: {output_dir}")
        except OSError as e:
            print(f"Erro ao criar o diretório de saída {output_dir}: {e}")
            sys.exit(1)

    # Geração dos arquivos com os novos caminhos
    txt_file = os.path.join(output_dir, os.path.basename(input_srt).replace('.srt', '.txt'))
    html_file = os.path.join(output_dir, os.path.basename(input_srt).replace('.srt', '.html'))
    ass_file = os.path.join(output_dir, os.path.basename(input_srt).replace('.srt', '.ass'))

    # Geração dos arquivos
    try:
        generate_txt(input_srt, txt_file)
        print(f"Arquivo TXT gerado: {txt_file}")
    except Exception as e:
        print(f"Erro ao gerar o arquivo TXT: {e}")

    try:
        generate_html(input_srt, html_file)
        print(f"Arquivo HTML gerado: {html_file}")
    except Exception as e:
        print(f"Erro ao gerar o arquivo HTML: {e}")

    try:
        generate_ass(input_srt, ass_file)
        print(f"Arquivo ASS gerado: {ass_file}")
    except Exception as e:
        print(f"Erro ao gerar o arquivo ASS: {e}")

    print("Processo de geração concluído.")

if __name__ == '__main__':
    # Configuração do parser de argumentos
    parser = argparse.ArgumentParser(description='Gera arquivos .txt, .html e .ass a partir de um arquivo .srt.')
    parser.add_argument('input_srt', type=str, help='Caminho do arquivo .srt de entrada.')
    parser.add_argument('output_dir', type=str, help='Diretório de saída para os arquivos gerados.')

    # Parse dos argumentos
    args = parser.parse_args()

    # Executa a função para gerar os arquivos
    generate_files(args.input_srt, args.output_dir)
