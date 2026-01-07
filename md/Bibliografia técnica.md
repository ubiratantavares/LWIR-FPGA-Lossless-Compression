# Bibliografia técnica selecionada, com livros, artigos e documentos em PDF que abrem excelentes caminhos teóricos e práticos — levando em conta os três tópicos que você levantou (algoritmos de compressão sem perdas, características de imagens térmicas, requisitos para implementação em FPGA)

---

### 1. Algoritmos de compressão sem perdas (RLE, Huffman, LZW e outros)

**Referências recomendadas:**

- Lossless compression algorithm for use in … – artigo PDF de 2022 que trata de métodos básicos de compressão sem perdas, revisando RLE, Huffman, codificação aritmética e implementações em FPGA. ([HSE University](https://www.hse.ru/data/2022/03/24/1810369790/7.pdf?utm_source=chatgpt.com "Lossless compression algorithm for use in ..."))
  
  - **Por que útil**: bom para fundamentar a parte teórica (“estado da arte”) dos algoritmos que você pretende usar (RLE + Huffman).
  
  - **Pontos de atenção**: não necessariamente focado em imagens térmicas, mas mostra hardware+FPGA.
  
  - **Como usar no seu documento**: no capítulo “Requisitos e estudo de algoritmos”, cite esse artigo para justificar por que RLE e Huffman são boas opções, e porque alternativas mais complexas (como aritmética) poderiam ficar fora do escopo intermediário.

- FPGA Realization of RLE Scheme for High Speed Data Transmission with Improved Compression Rate – estudo de 2017 que implementa RLE em FPGA/VHDL, com “fator de tolerância” para melhorar taxa de compressão. ([IJERT](https://www.ijert.org/research/fpga-realization-of-rle-scheme-for-highspeed-data-transmission-with-improved-compression-rate-IJERTV2IS110900.pdf?utm_source=chatgpt.com "fpga-realization-of-rle-scheme-for-highspeed-data- ..."))
  
  - **Por que útil**: exatamente RLE + FPGA, o que conecta diretamente ao bloco encoder de RLE que você planeja.
  
  - **Ponto de atenção**: adaptado para dados genéricos; você vai precisar verificar se os “runs” em imagens térmicas se comportam de forma similar aos dados que esse artigo trata.

- Data Compression Algorithms in FPGAs – trabalho de Ribeiro (2017) que trata de compressão em hardware FPGA (LZ77, stream interface, etc). ([Fénix Técnico](https://fenix.tecnico.ulisboa.pt/downloadFile/1689244997257479/bare_conf.pdf?utm_source=chatgpt.com "Data Compression Algorithms in FPGAs"))
  
  - **Por que útil**: contexto de como integrar a compressão em fluxo (“stream‐based interface”) que você mencionou (AXI-Stream/FIFO).
  
  - **Uso prático**: pode ajudar a pensar nos requisitos de interface e como o módulo pode ligar ao sistema FPGA.

- The Impact of State‑of‑the‑Art Techniques for Lossless Still Image Compression – artigo de 2021 que analisa diversos algoritmos lossless para imagens fixas. ([MDPI](https://www.mdpi.com/2079-9292/10/3/360?utm_source=chatgpt.com "The Impact of State-of-the-Art Techniques for Lossless Still ..."))
  
  - **Por que útil**: embora não FPGA‐focado, ele traz comparações entre algoritmos, taxas de compressão alcançáveis, trade-offs de tempo de codificação/decodificação, o que é útil para definir metas de taxa (≥1.5×) e latência.
  
  - **Como usar**: você pode usar para justificar a escolha de algoritmo simples (como RLE) versus mais complexos, dado seu nível intermediário.

---

### 2. Características de imagens térmicas e requisitos de dados

- Real‑time compression of high‑bandwidth measurement data of thermographic cameras with high temporal and spatial resolution – artigo que trata de compressão (embora focado em banda alta/tempo real) para câmeras termográficas, com 14 bits por pixel, >1.3 Megapixels, >100 fps. ([ndt.net](https://www.ndt.net/article/qirt2016/papers/148.pdf?utm_source=chatgpt.com "Real-time compression of high-bandwidth measurement ..."))
  
  - **Por que útil**: ajuda você a entender as especificidades de imagens térmicas: bit depth (14 bits no estudo), requisitos de banda, latência, padrões de repetição ou não repetição de dados térmicos.
  
  - **Como usar**: na seção de “levantamento de requisitos das imagens térmicas” do seu documento, extraia dados como profundidade de bits, possíveis repetitividades, e desafios de compressão (ex: pouca repetição se cada pixel varia).
  
  - **Ponto de atenção**: esse trabalho é para compressão possivelmente com perdas ou pesquisa de banda; seu foco é sem perdas, assim vai haver diferenças.

- Consultative Committee for Space Data Systems (CCSDS) – documento “Lossless multispectral and hyperspectral image compression” (2022) aborda compressão de imagens multiespectrais/hiperespectrais, que têm similaridades com imagens térmicas em termos de altos bit-depths e necessidade de compressão sem perdas. ([ccsds.org](https://ccsds.org/Pubs/120x2g2.pdf?utm_source=chatgpt.com "Lossless Multispectral and Hyperspectral Image ..."))
  
  - **Por que útil**: fornece padrões, requisitos de hardware, contexto “on‐board/in‐FPGA” para dados de sensor (próximo do seu caso).
  
  - **Como usar**: na parte de “análise das características das imagens térmicas”, use esse documento para comparar e extrair boas práticas: pipelines, bufferização, taxa de compressão esperada para dados similares.

---

### 3. Hardware / implementação em FPGA / design digital

- O artigo **Lossless compression algorithm for use in …** (já citado acima) menciona FPGA como implementação. (turn0search8)

- A revisão sistemática A Systematic Review of Hardware‑Accelerated Image Compression Techniques – cobre “hardware‐accelerated image compression” em FPGA, com foco em imagens remotas, compressão sem perdas, e especifica métricas de hardware (throughput, frequência, recursos). ([Semantic Scholar](https://pdfs.semanticscholar.org/0dd4/2607c003ee1079f302f9b4cb5b64179bf02b.pdf?utm_source=chatgpt.com "A Systematic Review of Hardware-Accelerated ..."))
  
  - **Por que útil**: ajuda você a definir critérios de desempenho (por exemplo: “clock operacional ≥ 50 MHz”, “pipeline estável”) baseado em literatura de FPGA.
  
  - **Como usar**: na definição dos requisitos de desempenho, consulte essa revisão para ver o que outros implementadores conseguiram em termos de frequência, recursos, throughput e latência.

- A tese A Resource Efficient, High Speed FPGA Implementation of Lossless Image Compression System (2019) – trata de implementação FPGA de compressor sem perdas de imagem. ([liu.diva-portal.org](https://liu.diva-portal.org/smash/get/diva2%3A1426363/FULLTEXT01.pdf?utm_source=chatgpt.com "A Resource Efficient, High Speed FPGA Implementation of ..."))
  
  - **Por que útil**: mais “hands-on” e pode dar ideias de arquitetura, blocos de controle FSM, bufferização, trade‐offs de lógica sequencial vs. recursos.
  
  - **Como usar**: no seu documento de especificação de requisitos, pode extrair que tipo de interface foi usada, quantos ciclos de latência, que tamanho de buffer, etc.

---

### 4. Especificamente sobre RLE e sua adequação

- A página da Wikipedia sobre RLE (“Codificação run-length”) oferece uma introdução rápida. ([Wikipédia](https://pt.wikipedia.org/wiki/Codifica%C3%A7%C3%A3o_run-length?utm_source=chatgpt.com "Codificação run-length"))
  
  - **Nota de ceticismo**: sendo Wikipedia, use apenas para introdução, não como fonte primária.

- O artigo “FPGA Realization of RLE Scheme…” (turn0search11) já citado é mais técnico e mostra modificações (fator tolerância) para melhorar a compressão, o que pode inspirar extensões ao seu RLE para imagens térmicas (ex: permitir pequenas variações térmicas serem consideradas “repetições”).
  
  - **Reflexão para você**: imagens térmicas monocromáticas com 12-16 bits/pixel podem ter “runs” de valores próximos (não exatamente iguais) — talvez considerar “quase igual” ou tolerância pode aumentar taxa de compressão. Isso entra na parte de “pré‐processamento e leitura de pixels”.

---

## Sugestão de estrutura para o seu documento de base teórica / especificação de requisitos

Com base nessas referências, você pode estruturar da seguinte forma:

1. Introdução à compressão sem perdas
   
   - Definição, por que “sem perdas”.
   
   - Principais algoritmos: RLE, Huffman, LZW, etc. Use as referências acima.
   
   - Critérios de seleção para seu projeto (simplicidade, implementação FPGA, taxa de compressão alvo, throughput alvo).

2. Caracterização das imagens térmicas
   
   - Bit‐depth típico (12‐16 bits, 14 bits citados no artigo de thermographic cameras) ([ndt.net](https://www.ndt.net/article/qirt2016/papers/148.pdf?utm_source=chatgpt.com "Real-time compression of high-bandwidth measurement ..."))
   
   - Dinâmica térmica: como os valores variam entre pixels, quais padrões de repetição ou gradientes podem existir.
   
   - Resolução, formato de dados (por exemplo, fluxo sequencial, pixel por pixel, linha por linha) — use também a literatura de multispectrais (CCSDS) para analogia.
   
   - Implicações para compressão: se há muitos valores iguais ou zonas de repetição, RLE pode dar bom ganho; se não, talvez RLE + Huffman ou outro esquema.

3. Definição de requisitos funcionais e de desempenho para seu core FPGA
   
   - Interface: por exemplo AXI-Stream, FIFO, barramento local. Pense em bit-width, fluxo de entrada/saída, controle de start/stop, flags de fim de transmissão.
   
   - Requisitos de compressão: “sem perdas” (bit à bit idêntico). Taxa alvo ≥ 1.5× (você já definiu).
   
   - Requisitos de desempenho: frequência do clock ≥50 MHz (você já definiu), pipeline estável, latência aceitável (já que “não é necessário tempo real de alta taxa de quadros”).
   
   - Requisitos de implementação lógica: recurso FPGA (flip-flops, LUTs, BRAMs), buffer interno para runs ou dicionário, FSM de controle. Use os artigos FPGA para ver que faixas de recursos são razoáveis (ex: revisão sistemática).
   
   - Validação: teste com imagens reais térmicas (por exemplo gravadas, ou de dataset público), medir taxa de compressão alcançada, medir lógica utilizada (síntese FPGA), medir frequência alcançada, verificar bit-à-bit igualdade.

4. Arquitetura proposta (visão geral)
   
   - Pré‐processamento/leitura de pixels: leitura de pixel de N bits (12-16 bits), possivelmente adaptação (por exemplo, se dados vêm em 16 bits mas só 12 úteis, etc).
   
   - Detecção de repetições (RLE Encoder): como definir “repetição” para valores térmicos, faixa de tolerância, contagem, codificação do run (“valor + comprimento”).
   
   - (Opcional) Codificação Huffman: se você quiser extenso para melhorar taxa, como construir árvore static/dinâmica, como armazenar tabela de códigos, decoder correspondente. Use a literatura de Huffman em FPGA.
   
   - Armazenamento temporário / Buffer: para runs e/ou códigos Huffman, como FIFO ou BRAM local.
   
   - Controle FSM principal: iniciar, ler pixel, comparar com pixel anterior, contar run, quando valor muda, emitir código, etc. E módulo de decodificação simétrico.
   
   - Interface de saída: empacotamento do fluxo comprimido, flags de fim, possivelmente contagem original/comprimido para relatório.
   
   - Decodificador: ler o fluxo comprimido, reconstruir pixel a pixel, verificar igualdade.

5. Plano de teste e validação
   
   - Escolha de imagens térmicas: faixa de bit‐depth, resolução, exemplo de dataset ou captura própria.
   
   - Métricas: taxa de compressão (tamanho original / tamanho comprimido), tempo (ou número de ciclos) para compressão/descompressão, uso de recursos do FPGA, frequência alcançada, latência de pipeline.
   
   - Verificação bit‐a‐bit de reconstrução (sem perdas).
   
   - Experimentos: variação de parâmetros (por ex. tolerância do run, se aplicar Huffman ou não) e impacto na taxa de compressão e recursos.

6. Conclusões da especificação e próximos passos
   
   - Sumário dos requisitos, restrições, trade-offs.
   
   - Decisão de que algoritmo(s) usarão (ex: primeiro apenas RLE, depois extensão para Huffman se sobrar recursos).
   
   - Cronograma de implementação (primeira versão: RLE encoder/decoder funcional; segunda versão: otimização + Huffman).
   
   - Possíveis extensões além do escopo (ex: compressão em linha, tempo real, compressão com perdas toleradas, etc).

---

### 5. Considerações específicas para o seu caso

- Como você está lidando com imagens térmicas monocromáticas de **12 a 16 bits/pixel**, convém verificar se há muitos *runs* (valores repetidos) nesse tipo de imagem — se não, a RLE simples pode não atingir a taxa de compressão alvo (≥1.5×). Pode valer a pena fazer uma **análise exploratória de dados térmicos** antes: extrair histogramas de valores, contagem de repetições consecutivas, quantas vezes o mesmo valor se repete, ou quantas vezes um valor se mantém igual entre pixels adjacentes.

- A interface FPGA: embora você não precise de tempo real de alta taxa de quadros, ainda é importante pipeline e fluxo contínuo para não gerar gargalo. Pense em operar com um buffer de linha na FPGA (por exemplo, armazenar a linha de pixels, ou contar runs enquanto lê).

- Sobre o uso de Huffman: se fizer Huffman além do RLE, há custo de lógica (árvore, tabela, lookup) e complexidade de decodificador. Se o objetivo é “nível intermediário” e “bom aprendizado”, talvez comece só com RLE e documente que Huffman é extensão futura.

- Na definição de taxa de compressão ≥1.5×: é razoável, mas convém documentar que isso depende muito da característica da imagem (valor repetido ou não). Use o artigo de “The Impact …” (turn0search17) para embasar que diferentes algoritmos têm diferentes taxas dependendo da imagem tipo.

- Frequência alvo ≥50 MHz: verifique nos artigos de FPGA quais frequências foram alcançadas para módulos similares (por exemplo, em revisão sistemática) para viabilizar essa meta.

---
