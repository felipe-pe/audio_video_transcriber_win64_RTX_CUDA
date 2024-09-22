

O FFmpeg é uma ferramenta poderosa para transcodificação de vídeos e
pode ser configurado tanto para usar a CPU quanto a GPU para melhorar o
desempenho, especialmente na codificação de vídeos. A seguir, vamos
explicar detalhadamente como você pode parametrizar comandos usando
FFmpeg, tanto para uso com a GPU (Nvidia CUDA) quanto com a CPU.

# Usando a GPU (CUDA) com FFmpeg

Para aproveitar a aceleração por hardware, o FFmpeg oferece suporte a
vários codecs otimizados para GPU, como o `h264_nvenc` para H.264 e o
`hevc_nvenc` para H.265, que usam a tecnologia NVENC das GPUs Nvidia.

## Parâmetros Principais para GPU

-   `-hwaccel cuda`: Ativa a aceleração por hardware CUDA. Isso indica
    ao FFmpeg que ele deve usar a GPU para decodificação ou
    processamento do vídeo.

-   `-c:v h264_nvenc` ou `-c:v hevc_nvenc`: Define o codec de vídeo
    NVENC para H.264 ou H.265, que utiliza a GPU para codificação. O
    NVENC é uma tecnologia de codificação de vídeo acelerada por
    hardware nas GPUs Nvidia.

-   `-preset`: Define a velocidade e qualidade da codificação. Com GPUs
    Nvidia, os valores variam de `p1` a `p7` (em versões mais recentes
    do FFmpeg), sendo:

    -   `p1`: Mais rápido (menor qualidade).

    -   `p7`: Mais lento (maior qualidade).

-   `-b:v`: Taxa de bits de vídeo. Controla a quantidade de dados
    alocados para o vídeo por segundo. Um valor mais alto significa
    melhor qualidade, mas arquivos maiores. Exemplo: `-b:v 5M` define 5
    Mbps.

-   `-gpu N`: Se você tem várias GPUs, pode especificar qual GPU usar.
    `N` é o índice da GPU (começando do zero). Exemplo: `-gpu 0`.

## Exemplo de Comando Usando GPU

Este comando usa o codec `h264_nvenc` (para H.264), com aceleração CUDA,
para codificar um vídeo com legendas:

    & "C:\caminho\para\ffmpeg.exe" -hwaccel cuda -i "C:\caminho\para\video_input.mp4" -vf "subtitles='C\:\\caminho\\para\\subtitulo.srt'" -c:v h264_nvenc -preset fast -b:v 5M -c:a aac -b:a 192k "C:\caminho\para\video_output.mp4"

## Detalhes

-   `-i "C:_input.mp4"`: Arquivo de entrada (vídeo).

-   `-vf "subtitles=’C:`\
    `caminho`\
    `para`\
    `subtitulo.srt’"`: Adiciona legendas ao vídeo.

-   `-c:v h264_nvenc`: Usa o codec NVENC para H.264.

-   `-preset fast`: Usa o preset \"rápido\" para codificação balanceada
    entre qualidade e velocidade.

-   `-b:v 5M`: Define a taxa de bits de vídeo em 5 Mbps.

-   `-c:a aac`: Usa o codec de áudio AAC.

-   `-b:a 192k`: Define a taxa de bits do áudio em 192 kbps.

-   `-hwaccel cuda`: Ativa a aceleração por hardware CUDA.

# Usando a CPU com FFmpeg

Se você deseja usar a CPU para codificação de vídeo, você não precisará
de aceleração por hardware. O FFmpeg fornece codecs otimizados para CPU,
como o `libx264` para H.264 e `libx265` para H.265.

## Parâmetros Principais para CPU

-   `-c:v libx264` ou `-c:v libx265`: Define o codec de vídeo que será
    usado pela CPU. O `libx264` é amplamente usado para H.264, enquanto
    o `libx265` oferece melhor compressão, mas é mais lento.

-   `-preset`: Semelhante ao uso com GPU, o preset também pode ser
    aplicado para a CPU. No entanto, os valores de preset para `libx264`
    e `libx265` são diferentes. Eles variam de:

    -   `ultrafast`: Codificação mais rápida, menor qualidade.

    -   `veryfast`, `faster`, `fast`: Boa combinação de velocidade e
        qualidade.

    -   `medium`: Valor padrão.

    -   `slow`, `slower`: Melhor qualidade, mais lento.

    -   `veryslow`: Máxima qualidade, extremamente lento.

-   `-crf`: Controle de taxa constante (*Constant Rate Factor*). Um
    valor mais baixo significa melhor qualidade. O valor recomendado
    para H.264 é entre `18` e `23`. Para H.265, entre `22` e `28`.

-   `-threads N`: Define o número de threads a serem usados pela CPU.
    Exemplo: `-threads 8` para usar 8 threads do processador.

## Exemplo de Comando Usando CPU

Aqui está um comando para codificar um vídeo usando a CPU com o codec
`libx264` (H.264):

    & "C:\caminho\para\ffmpeg.exe" -i "C:\caminho\para\video_input.mp4" -vf "subtitles='C\:\\caminho\\para\\subtitulo.srt'" -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 192k "C:\caminho\para\video_output.mp4"

## Detalhes

-   `-c:v libx264`: Usa o codec `libx264` para H.264, que roda na CPU.

-   `-preset medium`: Usa o preset \"medium\", que é o valor padrão,
    balanceando qualidade e velocidade.

-   `-crf 23`: Define a qualidade de vídeo. O valor 23 é considerado boa
    qualidade com tamanho de arquivo razoável. Para uma qualidade
    melhor, você pode usar `-crf 18`, mas o arquivo será maior.

-   `-c:a aac` e `-b:a 192k`: Mesma configuração de áudio usada
    anteriormente.

# Principais Diferenças entre GPU e CPU

-   **Desempenho**: Usar a GPU pode ser consideravelmente mais rápido
    para a codificação de vídeo, especialmente com NVENC. No entanto, o
    controle fino sobre a qualidade (como com `-crf`) é mais detalhado
    ao usar a CPU com `libx264` ou `libx265`.

-   **Qualidade vs. Velocidade**: A GPU é ideal para transcodificação
    rápida, mas a CPU pode oferecer mais flexibilidade e controle sobre
    a qualidade do vídeo final, especialmente em casos onde a compressão
    é uma preocupação maior do que o tempo de processamento.

-   **Taxa de bits (`-b:v`) vs. CRF (`-crf`)**: Ao usar NVENC (GPU),
    você geralmente define a taxa de bits manualmente (`-b:v`), enquanto
    com a CPU (`libx264` ou `libx265`), você pode usar o `-crf` para
    ajustar automaticamente a qualidade com base no conteúdo do vídeo.

# Considerações Adicionais

-   **Tamanho do Arquivo**: Usar `-crf` em vez de `-b:v` em codificações
    com CPU permite que o FFmpeg ajuste a taxa de bits dinamicamente,
    resultando em tamanhos de arquivo menores sem sacrificar qualidade
    visível.

-   **Compatibilidade de Hardware**: Nem todos os sistemas possuem GPUs
    compatíveis com NVENC. Se o seu hardware não suporta, você precisará
    usar a CPU.

-   **Controlando a Resolução**: Você pode redimensionar o vídeo durante
    a codificação, seja com CPU ou GPU, adicionando o filtro `scale`.
    Exemplo para redimensionar para 1280x720:

            -vf "scale=1280:720"

# Conclusão

-   **Com GPU (CUDA)**: Use a aceleração de hardware para ganhos de
    desempenho significativos, principalmente em transcodificações
    frequentes ou de longa duração.

-   **Com CPU**: Obtenha maior controle sobre a qualidade de vídeo, mas
    a custo de tempos de processamento mais longos.

Ambas as opções têm seus pontos fortes, e a escolha entre GPU e CPU
dependerá das necessidades específicas do projeto e do hardware
disponível.
