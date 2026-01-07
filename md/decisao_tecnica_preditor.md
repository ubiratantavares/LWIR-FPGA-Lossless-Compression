# Decisão Técnica 001: Seleção do Algoritmo Preditor

**Data:** 07/01/2026
**Sprint:** 0
**Responsável:** Antigravity (AI Assistant)

## 1. Contexto

O objetivo desta análise é selecionar o algoritmo preditor ideal para o sistema de compressão *lossless* em FPGA. A escolha deve equilibrar a **Taxa de Compressão (CR)** obtida com a **Complexidade de Hardware** (uso de recursos lógicos e memória).

Os requisitos do projeto estipulam uma meta de CR entre **1.5:1 e 2.5:1**.

## 2. Dados da Simulação (500 Frames - FLIR Dataset)

Foram simulados dois modelos:

1. **DPCM Fixo (Left Neighbor):** Predição baseada apenas no pixel imediatamente à esquerda.
2. **Adaptativo (MED - Median Edge Detection):** Proxy para preditores mais complexos, utilizando vizinhos da esquerda, cima e cima-esquerda.

| Métrica | DPCM Fixo (Left Neighbor) | Adaptativo (MED) | Diferença |
| :--- | :--- | :--- | :--- |
| **Entropia Média** | 5.1260 bits/pixel | 4.9004 bits/pixel | -0.2256 |
| **CR Estimado (Deflate)** | **2.4303:1** | **2.5127:1** | +0.0824 (+3.4%) |

## 3. Análise de Trade-off

### 3.1 Desempenho (CR)

Ambos os algoritmos atingiram a meta de projeto.

- O **DPCM Fixo** atingiu 2.43:1, ficando muito próximo do limite superior da meta (2.5:1).
- O **Adaptativo** superou ligeiramente a meta (2.51:1), oferecendo um ganho marginal de ~3.4% sobre o fixo.

### 3.2 Complexidade de Hardware (FPGA - Cyclone)

**DPCM Fixo (Left Neighbor):**

- **Lógica:** Requer apenas 1 subtrator de 16 bits.
- **Memória:** Requer apenas **1 Registrador** de 16 bits para armazenar o pixel anterior ($P_{i, j-1}$).
- **Latência:** Mínima (combinacional + 1 ciclo).

**Adaptativo (MED):**

- **Lógica:** Requer comparadores, multiplexadores e somadores/subtratores para calcular `min(A,B)`, `max(A,B)` e `A+B-C`.
- **Memória:** Requer acesso aos pixels da linha anterior ($P_{i-1, j}$ e $P_{i-1, j-1}$). Isso exige um **Line Buffer** (Buffer de Linha) capaz de armazenar uma linha inteira da imagem (ex: 640 pixels $\times$ 16 bits $\approx$ 10 Kbits). Isso consumiria blocos de memória **M9K** adicionais.
- **Latência:** Introduz complexidade no controle de fluxo para gerenciar o buffer de linha.

## 4. Veredito e Recomendação

**Decisão:** Recomenda-se a utilização do **DPCM Fixo (Left Neighbor)**.

**Justificativa:**

1. **Suficiência:** O DPCM Fixo já atende confortavelmente aos requisitos de compressão (2.43:1), inserindo-se na faixa alvo de 1.5:1 a 2.5:1.
2. **Eficiência de Recursos:** O ganho de 3.4% do preditor Adaptativo **não justifica** o custo de hardware adicional, especificamente a necessidade de um *Line Buffer* (M9K). Economizar recursos de memória no estágio de predição deixa mais BRAMs livres para o dicionário LZW, que é crítico para o desempenho global.
3. **Simplicidade:** A implementação do DPCM Fixo é trivial, reduzindo o risco de *bugs*, facilitando o fechamento de *timing* ($F_{MAX}$) e acelerando o desenvolvimento (Time-to-Market).

## 5. Próximos Passos

1. Atualizar a especificação para confirmar o DPCM Fixo como o preditor oficial.
2. Proceder para a análise de entropia do resíduo (formalização).
3. Iniciar a implementação em HDL focada na arquitetura "Left Neighbor".
