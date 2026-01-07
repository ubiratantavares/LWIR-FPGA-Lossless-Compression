## 🔹 **Desafio 2 — Compressão sem perdas para imagens térmicas**

### **Resumo técnico**

Compressão sem perdas (lossless) envolve transformar os dados de imagem em uma representação compactada que possa ser revertida integralmente.  
Para imagens térmicas (normalmente 14–16 bits/pixel, monocromáticas), os algoritmos típicos são **Run-Length Encoding (RLE)**, **Huffman**, ou **Predictive Coding** simples.

### **Principais etapas**

- Estudo do algoritmo de compressão mais apropriado (pode-se usar RLE + Huffman);

- Definição da arquitetura sequencial/pipeline;

- Implementação de blocos combinacionais e FSMs em Verilog;

- Integração com interface de memória e entrada de dados de imagem térmica;

- Validação funcional e testes de taxa de compressão.

### **Grau de dificuldade:** **6 / 10**

### **Risco de prazo (4 meses):** **moderado**

### **Motivo:**

Apesar de envolver conceitos matemáticos de compressão, os algoritmos são bem documentados e implementáveis com arquitetura sequencial, sem necessidade de throughput muito alto (não necessariamente tempo real). Pode ser validado com imagens armazenadas, sem fluxo contínuo.

## ✅ **Recomendação final**

O **Desafio 2 — Compressão sem perdas para imagens térmicas** é o **mais adequado** para execução dentro do prazo de **4 meses (≈ 320 horas)**, com um equilíbrio razoável entre:

- complexidade técnica (nível intermediário);

- viabilidade prática em FPGA com Verilog;

- possibilidade de validação realista (sem necessidade de alta taxa de quadros);

- bom aprendizado em design digital e otimização de lógica sequencial.

---

## 💡 **Proposta de cronograma (exemplo)**

| Mês   | Etapa                        | Atividades principais                                                                                                |
| ----- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **1** | **Pesquisa e planejamento**  | Estudo de algoritmos de compressão (RLE, Huffman, LZ), análise de imagens térmicas, definição da arquitetura do core |
| **2** | **Modelagem e prototipagem** | Implementação em Python/MATLAB para validação teórica + desenho do pipeline lógico                                   |
| **3** | **Implementação em Verilog** | Codificação do core, FSM de controle, interfaces, simulação funcional                                                |
| **4** | **Integração e validação**   | Testes com imagens reais, medição de taxa de compressão, desempenho e consumo de recursos                            |

# Plano completo de execução em FPGA (Verilog)** para o **Desafio 2 – Compressão sem perdas para imagens térmicas**, considerando:

- **Duração:** 4 meses (≈ 16 semanas)

- **Carga diária:** 4 h/dia, de segunda a sexta (≈ 80 h/mês, total ≈ 320 h)

- **Objetivo final:** Core funcional em FPGA capaz de comprimir e descomprimir imagens térmicas sem perdas, com testes de desempenho e validação experimental.

---

## 🧩 **Visão geral técnica**

### **Escopo do core**

- Implementação de compressão **sem perdas** para imagens térmicas monocromáticas (12 a 16 bits/pixel).

- Algoritmo-alvo: **RLE (Run-Length Encoding)** com possível extensão para **Huffman**.

- Operação em **fluxo sequencial** (não é necessário tempo real).

- Interface simples de entrada e saída (por exemplo: AXI-Stream, FIFO ou barramento local).

### **Principais blocos**

1. **Pré-processamento e leitura de pixels**

2. **Detecção de repetições (RLE Encoder)**

3. **Codificação Huffman (opcional)**

4. **Armazenamento temporário / buffer**

5. **Controle FSM principal**

6. **Módulo de descompressão (Decoder)**

7. **Testbench e validação com imagens reais**

---

## 📅 **Cronograma detalhado (16 semanas)**

| **Mês / Semana**                                   | **Etapa / Entregas**                              | **Atividades principais**                                                                                                             | **Resultados esperados**                 |
| -------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Mês 1 – Pesquisa e especificação (Semanas 1–4)** |                                                   |                                                                                                                                       |                                          |
| Semana 1                                           | **Estudo da base teórica**                        | - Estudar algoritmos lossless (RLE, Huffman, LZW) - Levantar requisitos das imagens térmicas (bit depth, resolução, formato de dados) | Documento técnico de referência          |
| Semana 2                                           | **Análise de complexidade e arquitetura inicial** | - Escolher algoritmo-base (RLE) - Definir formato de dados, fluxo e interfaces                                                        | Especificação funcional e fluxograma     |
| Semana 3                                           | **Prototipagem em alto nível (Python/MATLAB)**    | - Implementar RLE/Huffman e medir taxas de compressão em imagens reais                                                                | Resultados teóricos e parâmetros alvo    |
| Semana 4                                           | **Definição da arquitetura em FPGA**              | - Desenhar diagrama de blocos - Definir tamanho de buffers, FSMs e interconexões                                                      | Arquitetura final e plano de verificação |

---

| **Mês 2 – Implementação em Verilog (Semanas 5–8)** | | | |  
| Semana 5 | **Desenvolvimento do módulo de leitura** | - Módulo de entrada (stream ou FIFO) - Conversão de dados de imagem em palavras de pixel | Bloco de leitura testado em simulação |  
| Semana 6 | **Implementação do RLE Encoder** | - FSM de detecção de repetições e escrita de pares (valor, contagem) - Validação unitária em simulação | Core RLE funcional |  
| Semana 7 | **Implementação do Huffman Encoder (opcional)** | - Codificação simbólica e geração de código binário variável - Testes em vetor reduzido | Bloco Huffman validado |  
| Semana 8 | **Integração Encoder completo** | - Integração leitura + compressão - Verificação de sincronismo e controle FSM principal | Pipeline de compressão integrado |

---

| **Mês 3 – Validação e otimização (Semanas 9–12)** | | | |  
| Semana 9 | **Implementação do Decoder (descompressão)** | - FSM inversa para reconstruir a imagem - Teste de reversibilidade bit a bit | Core decoder funcional |  
| Semana 10 | **Simulação fim a fim** | - Compressão → Descompressão → Comparação de pixels | Validação 100 % sem perdas |  
| Semana 11 | **Avaliação de desempenho** | - Medição de throughput, uso de LUTs/FFs, tempo de clock | Relatório técnico de desempenho |  
| Semana 12 | **Otimizações** | - Ajuste de pipeline, redução de latência - Melhoria de controle de buffer e FSM | Core otimizado e estável |

---

| **Mês 4 – Integração em hardware e testes físicos (Semanas 13–16)** | | | |  
| Semana 13 | **Síntese e implementação no kit FPGA** | - Escolha e configuração do kit (Zynq, Cyclone, Artix etc.) - Geração de bitstream | Core sintetizado e programado |  
| Semana 14 | **Montagem do setup de teste** | - Integração com memória local / interface USB / UART - Preparação de ambiente com equipe Invent Vision | Sistema pronto para validação |  
| Semana 15 | **Testes reais com imagens térmicas** | - Envio de imagens reais e coleta de resultados - Comparação com compressão via software | Relatório de validação experimental |  
| Semana 16 | **Documentação e entrega final** | - Documentar arquitetura, FSMs, códigos e resultados | Relatório final + código Verilog revisado |

---

## ⚙️ **Ferramentas e recursos recomendados**

| Tipo                        | Opção sugerida                                                          |
| --------------------------- | ----------------------------------------------------------------------- |
| **FPGA**                    | Intel Cyclone V ou Xilinx Artix-7 (com interface de memória acessível)  |
| **Linguagem HDL**           | Verilog 2001                                                            |
| **Ambiente de simulação**   | ModelSim / Vivado Simulator / Questa                                    |
| **Síntese e place & route** | Quartus Prime / Vivado                                                  |
| **Testbench**               | Verificação automatizada com `$fopen`, `$fread`, `$fwrite` para imagens |
| **Ferramentas auxiliares**  | Python + NumPy para gerar vetores de teste e validar resultados         |

---

## 🔍 **Critérios de sucesso**

1. **Compressão sem perdas comprovada** (imagem reconstruída idêntica bit a bit).

2. **Taxa de compressão ≥ 1.5×** para imagens térmicas típicas.

3. **Clock operacional ≥ 50 MHz** com pipeline estável.

4. **Relatório técnico** completo: arquitetura, recursos usados, desempenho, validação.

---
