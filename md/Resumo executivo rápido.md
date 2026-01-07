# Resumo executivo rápido

As fontes cobrem três pilares essenciais para o seu projeto:

- **Interfaces e integração** (AXI4-Stream — fonte 1) → como o core vai conversar com o resto do sistema FPGA / host.

- **Algoritmos e arquiteturas de compressão para FPGA** (LZW, Huffman canônico, RLE, preditiva — fontes 2, 6, 9, 10, 4) → opções de implementação, trade-offs área/throughput/energia.

- **Requisitos do domínio de imagens térmicas** (bit depth, full well, dinâmica, processamento TIR — fontes 3, 8) → formatação dos dados, quantização, calibração radiométrica e metadados necessários.  
  Complementos práticos (otimizações FPGA, FIFO, uso de BRAM) aparecem nas fontes 5 e 7.

# Mapeamento direto fonte → uso prático na 1ª semana

1. **AMBA® 4 AXI4-Stream Protocol Specification (Arm)**
   
   - Uso imediato: *definir a interface* do core (sinais TVALID/TREADY, TDATA width, TLAST, TID/TDEST para streams múltiplos).
   
   - Entregável: trecho do Documento de Requisitos que especifica largura de dados TDATA (ex.: 16/24/32 bits), comportamento de handshake, e política de backpressure.
   
   - Risco a checar: compatibilidade com o bus do sistema (se há necessidade de upsizing/downsizing entre sensor e host).

2. **LZW FPGA (artigo de implementação LZW em Virtex-7)**
   
   - Uso imediato: *modelo arquitetural* de dicionário usando BRAM dual-port; técnicas para leit./escr. simultâneas; paralelismo por instâncias replicadas.
   
   - Entregável: lista de blocos lógicos sugeridos (hash table em BRAM, ponteiro-caractere, back-pointer q) e estimativa qualitativa de BRAM/logic para protótipo.
   
   - Observação crítica: LZW é bom para certos padrões; teste com imagens térmicas é necessário (ver atividade de validação).

3. **Teledyne — Bit Depth, Full Well, Dynamic Range**
   
   - Uso imediato: definir **profundidade de bits** alvo (p.ex. 12 bits nativo do sensor vs. armazenamento em 16 bits), impacto em tamanho/throughput e escolha de pre/post-processing (quantização, LUTs).
   
   - Entregável: requisito de formato de entrada (bits por pixel, endianness, signed/unsigned) e recomendações sobre escolha entre 8/12/16 bits para compressão sem perdas.

4. **Wikipedia — Categoria Lossless compression**
   
   - Uso imediato: inventário rápido de algoritmos a considerar (RLE, Huffman, LZW, JPEG-LS, Golomb-Rice) para a matriz de trade-offs.
   
   - Entregável: tabela comparativa (complexidade HW, compressão típica em imagens, memória exigida).

5. **Reddit — Discussão sobre FIFO / axis_fifo.v**
   
   - Uso imediato: referência prática para implementação de FIFO compatível AXI-Stream (usar axis_fifo.v ou adaptar).
   
   - Entregável: decisão de usar FIFO BRAM-based entre sensor → compressão → output AXI-Stream; incluir referência de módulo testado pela comunidade.

6. **Energy Efficient Canonical Huffman Encoding (CHE)**
   
   - Uso imediato: arquitetura para codificação de entropia com ótimo trade-off área/energia; técnicas HLS/dataflow e uso de FIFO para ordenar.
   
   - Entregável: considerar CHE (canonic Huffman) como codificador de entropia preferido quando for necessário balancear memória e energia; fluxograma de blocos (Filter, Sort, Compute BitLen, Canonize, Create Codeword).

7. **FPGA OPTIMIZATIONS**
   
   - Uso imediato: lista de otimizações que orientarão o design RTL (pipelining, retiming, resource sharing, uso de DSP/BRAM).
   
   - Entregável: checklist de implementação/ síntese (onehot vs gray para FSMs, pipeline stages mínimos, inferência de BRAM/DSP).

8. **Image Processing of Thermal Infrared Images**
   
   - Uso imediato: requisitos de pré-processamento (calibração radiométrica, LUTs para conversão contagem → temperatura), correções geométricas e formatos de arquivo.
   
   - Entregável: se o core receberá dados já calibrados ou contagens brutas; se for bruto, documentar algoritmos externos de calibração (não parte do core de compressão).

9. **RLE Verilog HDL**
   
   - Uso imediato: RLE como baseline (simples, baixa latência, pequena lógica) — avaliar ganho em imagens térmicas (muito bom se houver áreas uniformes).
   
   - Entregável: módulo RLE RTL como protótipo rápido para comparação com LZW/Huffman.

10. **Predictive-Based Lossless Compression (alta profundidade de bits)**
    
    - Uso imediato: justificar predição + codificação por contexto + Golomb-Rice para imagens 12–16 bits; técnica com bom custo/benefício para imagens com alto dynamic range.
    
    - Entregável: candidato forte para TIR (onde correlações espaciais são exploráveis): especificar bloco de predição e codificador de entropia (Golomb-Rice).

# Plano de atividades — primeiro *sprint* (dia a dia, entregáveis claros)

(uso criterioso das fontes acima para cada tarefa)

**Dia 1 — Leitura orientada / escopo**

- Ler e extrair: AXI4-Stream (fonte 1) — definir TDATA width options e handshake.

- Ler resumo das técnicas de compressão (fontes 2, 6, 9, 10) para montar matriz comparativa.

- Entregável: 1-página de escopo com opções de algoritmos e interfaces.

**Dia 2 — Caracterização das imagens térmicas**

- Usar fontes 3 e 8 para definir: bit depth alvo, formatos (raw counts vs temperatura), resoluções típicas (ex.: 320×240, 640×480), faixa dinâmica e SNR.

- Entregável: tabela “Características das imagens” (bit depth, frame rate alvo, tamanho por frame).

**Dia 3 — Seleção arquitetural inicial**

- Decidir caminhos a testar: (A) RLE (baseline), (B) LZW (BRAM hash), (C) Predictor + Golomb-Rice (para 12/16 bit). Use fonte 7 para restrições FPGA.

- Entregável: diagrama de blocos do core com interface AXI4-Stream, FIFO de entrada (axis_fifo), módulos de compressão alternativos plugáveis.

**Dia 4 — Requisitos funcionais e de desempenho**

- Documentar requisitos: interface (AXI4-Stream TDATA width, TLAST), latência máxima aceitável, throughput mínimo (frame rate × pixels × bits), memória BRAM disponível, meta de CR mínima (p.ex. baseline objetivo: CR>1.5 em cenários representativos — *nota: valor inicial para validação*, ajustar após testes).

- Entregável: draft do Documento de Especificação de Requisitos (seções iniciais: visão geral, interfaces, métricas).

**Dia 5 — Plano de validação e testes**

- Definir datasets de teste (imagens reais e sintéticas): incluir imagens com gradientes, ruído, pequenos detalhes, áreas homogêneas; preparar formatos 12/16 bit.

- Definir métricas: Compression Ratio (CR), throughput (MB/s), latency (µs/frame), resource use (LUTs, FFs, BRAM, DSP), energia (se medível).

- Entregável: plano de teste + checklist de métricas.

# Checklists acionáveis (o que escrever já nos documentos)

## Documento técnico de referência — conteúdo mínimo

- Introdução e objetivos.

- Sumário das imagens térmicas (bit depth, formato, taxa). — use fontes 3 e 8.

- Tabela comparativa de algoritmos lossless (RLE, LZW, CHE/Huffman canonic, Predictor+GolombRice, JPEG-LS): prós/contras HW — use fontes 2,6,9,10,4.

- Arquitetura proposta (diagrama AXI4-Stream, FIFO, blocos compressão, BRAM map). — base: fonte 1,5,2.

- Estratégia de otimização FPGA (pipelining, BRAM usage). — fonte 7.

- Plano de testes e datasets.

- Requisitos e interfaces (extrair do AXI4-Stream spec).

## Documento de Especificação de Requisitos — mínimo

- Requisitos funcionais (recebe stream raw 12-16bit; produz stream AXI4-Stream comprimido; suporta TLAST semantics; fluxo de controle com TVALID/TREADY). — fonte 1.

- Requisitos não-funcionais (throughput mínimo = sensor_rate × pixel_count × bitdepth; meta CR inicial; resource budget — LUT/BRAM cap a definir com base na FPGA alvo). — use fontes 3,7.

- Métricas de aceitação (CR em cenários representativos; latência por frame; taxa de perda = 0 — lossless). — fontes 4,10.

- Componentes de integração (FIFO axis_fifo, testes com BRAM inferred). — fonte 5.

# Decisões técnicas recomendadas agora (com justificativa)

1. **Usar AXI4-Stream como interface** — interoperabilidade simples com IPs e o restante do SoC. (fonte 1 + 5)

2. **Implementar RLE como protótipo inicial** (muito rápido em Verilog; serve como baseline de latência e área). (fonte 9)

3. **Parallelizar LZW usando BRAM dual-port** se RLE não atingir CR aceitável; aproveitar técnicas do artigo LZW para tabelas hash em BRAM. (fonte 2)

4. **Projetar bloco preditivo (para 12/16 bits) + Golomb-Rice** como candidato para melhor CR em imagens TIR com alta bit depth. (fonte 10)

5. **Usar Canonical Huffman (CHE)** se necessidade de reduzir memória da tabela de códigos/energia for crítica — bom trade-off por throughput/energia. (fonte 6)

# Validação e métricas sugeridas (numéricas → para instrumentar nos testes)

- **Compression Ratio (CR)**: reportar média, mediana e pior caso sobre dataset.

- **Throughput**: MB/s comprimidos e descomprimidos. Medir *sustained* e *burst*.

- **Latency**: tempo desde primeiro pixel do frame até saída do primeiro byte comprimido.

- **Recursos FPGA**: LUTs, FFs, BRAMs, DSPs usados.

- **Corretude**: bit-a-bit equality after decompress (lossless = must be exact).

# Entregáveis ao final da semana

1. Documento técnico de referência (rascunho) com as seções listadas acima.

2. Documento de Especificação de Requisitos (versão 0.1) cobrindo interfaces e métricas.

3. Matriz comparativa de algoritmos (1 página) com recomendações prioritárias.

4. Plano de teste/dataset + scripts sugeridos para gerar imagens sintéticas 12/16bit (descrição e formatos).

5. Diagrama de blocos RTL com AXI4-Stream + axis_fifo + portas para módulos de compressão plugáveis.

# Pontos em aberto que você deverá confirmar (necessários para fechar requisitos)

- **FPGA alvo exato** (família e parte) → para dimensionar BRAM/DSP e definir metas reais de área.

- **Resolução e frame rate do sensor térmico** (ex.: 640×480 @ 30Hz vs 320×240 @ 60Hz) → para calcular throughput mínimo.

- **Se os dados chegam já calibrados (temperatura) ou como contagens brutas** → altera decisão sobre inclusão de LUT/fluxo de calibração no pipeline.

- **Orçamento de recursos (LUTs/BRAM) e energia** do dispositivo alvo.

# Recomendações práticas imediatas (o que eu faria já hoje)

- Extrair e copiar no documento os trechos relevantes do AXI4-Stream (sinais TVALID/TREADY, TLAST, recomendação sobre TDATA widths).

- Implementar um **módulo RLE** simples em Verilog e um *testbench* que leia imagens 12/16bit para obter baseline CR e throughput. (rápido e informativo)

- Preparar 10 imagens de teste (5 reais, 5 sintéticas) em 12/16 bits com histograma diversificado para análise comparativa entre RLE/LZW/Predictive+Golomb.

---

Se quiser, eu já monto:

- a **tabela comparativa** preenchida com prós/cons de RLE, LZW, Predictor+Golomb, Canonical Huffman, JPEG-LS; **ou**

- o **esqueleto em markdown** do Documento de Especificação de Requisitos pronto para você editar.

Diga qual desses dois entregáveis prefere que eu gere agora (faço já — sem esperar).
