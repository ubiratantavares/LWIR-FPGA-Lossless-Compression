Estou desenvolvendo um projeto de Compressão sem perdas para imagens térmicas considerando que:

* complexidade técnica (nível intermediário);
* viabilidade prática em FPGA com Verilog;
* possibilidade de validação realista (sem necessidade de alta taxa de quadros);
* bom aprendizado em design digital e otimização de lógica sequencial.

Objetivo final: Core funcional em FPGA capaz de comprimir e descomprimir imagens térmicas sem perdas, com testes de desempenho e validação experimental.

Visão geral técnica

Escopo do core

Implementação de compressão sem perdas para imagens térmicas monocromáticas (12 a 16 bits/pixel).

Algoritmo-alvo: RLE (Run-Length Encoding) com possível extensão para Huffman.

Operação em fluxo sequencial (não é necessário tempo real).

Interface simples de entrada e saída (por exemplo: AXI-Stream, FIFO ou barramento local).

Principais blocos

Pré-processamento e leitura de pixels

Detecção de repetições (RLE Encoder)

Codificação Huffman (opcional)

Armazenamento temporário / buffer

Controle FSM principal

Módulo de descompressão (Decoder)

Testbench e validação com imagens reais

Critérios de sucesso

Compressão sem perdas comprovada (imagem reconstruída idêntica bit a bit).

Taxa de compressão ≥ 1.5× para imagens térmicas típicas.

Clock operacional ≥ 50 MHz com pipeline estável.

Relatório técnico completo: arquitetura, recursos usados, desempenho, validação.

Neste momento estou na primeira semana de desenvolvimento projeto realizando estudo da base teórica visando a compreensão e requisitos do problema contendo as seguintes atividades principais:

* Estudo dos princípios de compressão sem perdas (RLE, Huffman, LZW) e studar algoritmos lossless (RLE, Huffman, LZW)

* Levantar requisitos das imagens térmicas, Análise das características das imagens térmicas (bit depth, dinâmica térmica, resolução, formato de dados)

* Definição dos requisitos funcionais e de desempenho do core FPGA

Visando produzir documento técnico de referência e Documento de especificação de requisitos


Pesquise na web livros técnicos, artigos científicos, documentos em PDF que me auxilie no estudo da base teórica visando a compreensão e requisitos do problema contendo as seguintes atividades principais descritas.
