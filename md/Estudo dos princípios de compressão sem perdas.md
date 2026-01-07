Perfeito. Com essas novas informações — **imagens LWIR (Long Wave InfraRed)** com **faixa espectral de 7–14 µm** e resolução inicial **640×480 @ 60 fps** — podemos refinar a análise e contextualizar as fontes dentro do escopo **da primeira semana do projeto**, que busca construir uma **base teórica sólida** para definir **requisitos de compressão sem perdas em imagens térmicas** e **parâmetros de hardware FPGA**.

A seguir está uma **análise detalhada, integrando as fontes e os dados de imagem fornecidos**, segmentada por atividade principal:

---

## 🧩 1. Estudo dos princípios de compressão sem perdas (RLE, Huffman, LZW)

### Fontes-chave:

- **(2) An Efficient Implementation of LZW Compression in FPGA**

- **(6) Energy Efficient Canonical Huffman Encoding**

- **(9) Implementation of Run Length Encoding Using Verilog HDL**

- **(4) Categoria: Lossless Compression Algorithms – Wikipedia**

### Análise e contribuição:

Essas fontes estabelecem o **núcleo conceitual e prático** do estudo de algoritmos *lossless*.  
Na primeira semana, elas fornecem:

- **Compreensão comparativa** entre os três principais métodos — **RLE (redundância de runs)**, **Huffman (entropia)** e **LZW (dicionário adaptativo)**.

- **Mapeamento de complexidade vs. eficiência**:
  
  - *RLE*: simples, ideal para dados com repetições contíguas — útil em regiões homogêneas das imagens térmicas.
  
  - *Huffman*: ótimo para compressão de dados com distribuição de probabilidade não uniforme — relevante para imagens com gradientes térmicos sutis.
  
  - *LZW*: gera compactação melhor em padrões repetitivos complexos — pode capturar redundância entre linhas (variações térmicas espaciais suaves).

- **Visão prática em FPGA**:
  
  - O artigo de **LZW** mostra como **implementar um dicionário em BRAM dual-port** (relevante para paralelização e *throughput*).
  
  - O de **Huffman Canônico** apresenta **arquitetura otimizada por energia e paralelismo**, útil para comparar *design trade-offs* em implementações reais.
  
  - O de **RLE** demonstra a importância de ajustes simples na arquitetura (uso de contador reduzido) para **melhorar razão de compressão e área lógica**.

**Resultado esperado para a semana:**  
Um quadro comparativo (técnico) entre RLE, Huffman e LZW, destacando:

- Complexidade de hardware (nível lógico e de memória);

- Ganho de compressão teórico;

- Potencial de paralelização e integração em *pipeline* AXI4-Stream.

Esse estudo fundamentará a **escolha preliminar do algoritmo de compressão para prototipagem**.

---

## 🌡️ 2. Levantar requisitos das imagens térmicas

### Fontes-chave:

- **(3) Bit Depth, Full Well, and Dynamic Range | Teledyne Vision Solutions**

- **(8) Image Processing of Thermal Infrared Images**

- **Dados fornecidos: LWIR 7–14 µm, 640×480 @ 60 fps**

### Análise e contribuição:

Essas fontes e especificações definem o **contexto físico e digital** das imagens a serem tratadas.

1. **Faixa espectral (7–14 µm, LWIR)** → implica uso de sensores microbolométricos **não resfriados**, com **resposta lenta e ruído térmico elevado**, exigindo compressão sem perdas para evitar distorções radiométricas.

2. **Resolução e taxa de quadros (640×480 @ 60 fps)** → fluxo bruto ≈  
   [  
   640 \times 480 \times 16\text{ bits/pixel} \times 60 \text{ fps} = 294.9 \text{ Mbit/s}  
   ]  
   Ou seja, **≈37 MB/s**, reforçando a necessidade de **compressão leve e em tempo real**.

3. **Profundidade de bits** (12–16 bits típicos, conforme Teledyne) → alta **resolução radiométrica** e **faixa dinâmica ampla**, importante para distinguir pequenas variações térmicas.

4. **Artigo de processamento TIR** → aborda:
   
   - **Conversão LUT** (para linearização da resposta do sensor);
   
   - **Correção geométrica e radiométrica**, que podem alterar a estrutura estatística dos dados;
   
   - Portanto, o **compressor deve operar antes dessas transformações**, atuando diretamente sobre os dados brutos.

**Resultado esperado para a semana:**  
Um **perfil técnico das imagens LWIR**, incluindo:

- Resolução, profundidade de bits e formato de dados de entrada (provável 16-bit RAW);

- Características estatísticas (homogeneidade espacial e gradientes suaves);

- Taxa de dados alvo e requisitos de latência máxima permitida;

- Implicações na escolha do algoritmo (RLE e LZW se destacam).

---

## ⚙️ 3. Definição dos requisitos funcionais e de desempenho do core FPGA

### Fontes-chave:

- **(1) AMBA 4 AXI4-Stream Specification**

- **(5) r/FPGA FIFO discussion**

- **(7) FPGA Optimizations**

- **Resultados e métricas das fontes 2, 6 e 9**

### Análise e contribuição:

Essas referências estabelecem a base para a **arquitetura de integração e otimização do core de compressão**:

1. **AXI4-Stream Protocol** → define o **padrão de interface** para troca de dados entre o módulo de compressão e outros blocos (p. ex. captura, memória, transmissor).
   
   - Uso de sinais **TVALID**, **TREADY** e **TLAST** garante compatibilidade e controle de fluxo entre blocos.
   
   - Permite fácil integração com **FIFOs AXIS**, DMA e periféricos de vídeo (VDMA).

2. **FIFO Implementation (Reddit discussion)** →
   
   - Fornece insights sobre **implementações portáteis e eficientes em BRAM**, sem dependência de IPs proprietários.
   
   - Recomenda integração direta com **AXI-Stream**, crucial para pipeline contínuo entre captura e compressão.

3. **FPGA Optimizations** →
   
   - Fundamenta a **escolha de estratégias de síntese** (pipelining, retiming, resource sharing) para atingir as metas de frequência (>150 MHz).
   
   - Reforça boas práticas de codificação FSM (*one-hot* para velocidade, *gray* para área).

4. **Benchmarks das implementações LZW e Huffman** →
   
   - Servem como **referência de throughput esperado**: LZW paralelo atingiu 163 MHz e ganho ×23 sobre CPU; Huffman Canônico apresentou 230 codificações/Watt.

**Resultado esperado para a semana:**  
Documento preliminar de **Requisitos do Core FPGA**, incluindo:

- Interfaces padrão (AXI4-Stream);

- Frequência alvo (~150 MHz);

- Largura de dados (16 bits);

- Suporte a fluxo contínuo (TVALID/TREADY);

- Capacidade de processar **640×480×60 fps** em *streaming real-time*;

- Compatibilidade com buffer AXIS FIFO e BRAM dual-port.

---

## 📘 Entregáveis da Semana 1

| Documento                                          | Conteúdo principal                                                                                                       | Fontes base                    |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| **Documento Técnico de Referência**                | Revisão teórica sobre compressão sem perdas (RLE, Huffman, LZW) e análise de aplicabilidade em imagens térmicas LWIR     | 2, 4, 6, 8, 9                  |
| **Documento de Especificação de Requisitos (DRS)** | Requisitos funcionais e de desempenho do core FPGA; interfaces AXI4-Stream; parâmetros das imagens e metas de throughput | 1, 3, 5, 7, + dados fornecidos |

---

Se desejar, posso montar o **modelo inicial dos dois documentos (Técnico e DRS)** — com seções e estrutura profissional — para que você comece a preenchê-los durante o estudo.  
Quer que eu gere o esqueleto deles em formato técnico (Markdown ou DOCX)?
