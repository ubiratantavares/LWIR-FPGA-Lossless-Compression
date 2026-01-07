# SPRINT DIA 2 (CONCLUÍDO)



# **SPRINT DIA 2 (CONCLUÍDO)**

### **1. Atividade 1: Análise de Algoritmos Lossless e Seleção da Baseline**

| Componente                                          | Status       | Detalhes e Suporte nas Fontes                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Análise de Trade-offs entre Algoritmos Lossless** | Concluído    | A comparação entre **LZW**, **Huffman Canônica (CHE)**, **RLE** e **Preditiva (DPCM/LOCO-I)** foi realizada considerando desempenho, paralelismo e uso de recursos em FPGA. Dados RAW de 16 bits possuem alta correlação espacial, favorecendo abordagens preditivas e codificação de entropia \cite{23, 47, 285}.                   |
| **Definição da Baseline Rápida**                    | Concluído    | A **Baseline Rápida** prioriza **alto throughput** e **baixa complexidade de hardware** em detrimento da taxa de compressão máxima. O **RLE Modificado (contador de 3 bits)** foi selecionado por equilibrar simplicidade arquitetural (uso mínimo de LUTs/FFs) e eficiência razoável de compressão (CR até 1.93:1) \cite{285, 339}. |
| **Conclusão Técnica**                               | Concluído    | A primeira versão funcional adotará o fluxo **DPCM → RLE Modificado**, atendendo ao throughput de $\approx 37 \text{ MB/s}$ exigido no Dia 1.                                                                                                                                                                                        |
| **Ponto Aberto (CR Mínimo)**                        | Em Definição | Necessário estabelecer a **Taxa de Compressão Mínima (CR)** aceitável como requisito de eficiência. O valor depende da redundância estatística dos dados \cite{259}.                                                                                                                                                                 |

---

### **2. Atividade 2: Arquitetura de Pipeline e Decisão FIFO**

| Componente                             | Status       | Detalhes e Suporte nas Fontes                                                                                                                                                                                                                        |
| -------------------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Desenho da Arquitetura de Pipeline** | Concluído    | A arquitetura foi estruturada com estágios desacoplados por buffers \textbf{FIFO}, assegurando fluxo contínuo e paralelismo interno. Essa decisão garante que o pipeline mantenha throughput constante mesmo diante de módulos de latência variável. |
| **Decisão FIFO**                       | Concluído    | O uso de \textbf{FIFOs implementadas em Block RAM (BRAM)} é uma decisão arquitetural chave \cite{23, 30, 37, 183}. As FIFOs desacoplam módulos, armazenando dados intermediários (ex: entre o DPCM e o codificador RLE).                             |
| **Implementação em FPGA**              | Concluído    | Recomenda-se o uso de *macros* nativas de fabricante (XPM FIFOs, Xilinx) para otimização no dispositivo alvo.                                                                                                                                        |
| **Ponto Aberto (Tamanho do Buffer)**   | Em Definição | Definir a profundidade ideal das FIFOs para garantir desempenho contínuo e uso equilibrado de BRAM \cite{125}.                                                                                                                                       |

---

### **3. Entregável Final e Documentos Associados**

| Componente                                                   | Status       | Detalhes                                                                                                                                              |
| ------------------------------------------------------------ | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Texto Técnico em $\text{\LaTeX}$ (Análise e Arquitetura)** | Concluído    | Produzido para o **Documento Técnico de Referência (DTR)**, incluindo a matriz comparativa, definição da baseline e o diagrama de blocos RTL inicial. |
| **Requisito Não Funcional (CR Mínimo)**                      | Concluído    | Registrado para o **Documento de Especificação de Requisitos (DER)** como **RFN-3.1: Eficiência de Compressão (Baseline)**.                           |
| **Pontos Abertos (CR Mínimo e FIFO Depth)**                  | Em Andamento | Serão fechados na próxima fase de refinamento da arquitetura e caracterização dos dados TIR.                                                          |

---

### **4. Diagrama de Blocos RTL (Baseline Rápida - Draft)**

$$  
\text{Interface AXI4-Stream (16 bits)}  
\xrightarrow{\text{Data Input}}  
\underbrace{\text{Buffer FIFO Entrada (BRAM)}}*{\text{Decisão FIFO}}  
\longrightarrow  
\underbrace{\text{Módulo Preditivo (DPCM)}}*{\text{Remoção de Redundância Espacial}}  
\longrightarrow  
\underbrace{\text{Buffer FIFO Resíduo (BRAM)}}*{\text{Decisão FIFO}}  
\longrightarrow  
\underbrace{\text{Módulo Baseline (RLE Modificado)}}*{\text{Codificação de Entropia}}  
\xrightarrow{\text{Compressed Bits}}  
\text{Interface AXI4-Stream (Output)}  
$$

---

### **5. Alocação de Documentos**

| Conteúdo                                          | Documento | Justificativa                                                                                                   |
| ------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------- |
| **Matriz Comparativa e Trade-offs de Algoritmos** | **DTR**   | Descreve detalhes de desempenho, paralelismo e consumo de recursos em FPGA, justificando as decisões de design. |
| **Decisão Baseline (RLE Modificado)**             | **DTR**   | Escolha fundamentada pela relação entre throughput, simplicidade e eficiência de compressão.                    |
| **Arquitetura e Decisão FIFO**                    | **DTR**   | Parte integrante da microarquitetura do acelerador, descrevendo o fluxo RTL.                                    |
| **Ponto Aberto: CR Mínimo (Requisito NF)**        | **DER**   | Define a eficiência mínima de compressão esperada para validação funcional do sistema.                          |
| **Ponto Aberto: Tamanho da FIFO**                 | **DTR**   | Parâmetro de otimização de projeto, dependente do comportamento dinâmico do pipeline.                           |

---

✅ **Resumo do Dia 2:**  
A Sprint consolidou a base arquitetural do sistema de compressão lossless em FPGA, com ênfase em desempenho, modularidade e simplicidade de hardware. Foram definidas as diretrizes para a primeira versão RTL funcional e estabelecidos os pontos de medição e otimização (CR mínimo e profundidade da FIFO) para a próxima etapa.
