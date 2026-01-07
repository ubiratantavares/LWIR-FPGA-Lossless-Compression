# 📘 Documento Técnico de Referência — Arquitetura LZW e Codificação Canonical Huffman

Para enriquecer o **Documento Técnico de Referência (RTR)** e o **Documento de Requisitos de Sistema (DRS)**, detalha-se abaixo a arquitetura de alto desempenho para **LZW (usando BRAM Dual-Port)** e o **fluxograma do codificador Canonical Huffman (CHE)**, ambos otimizados para FPGA.

---

## 💾 1. Estrutura de Dicionário LZW (Baseada em BRAM Dual-Port)

A compressão **LZW em tempo real** em FPGA exige acesso rápido e paralelo ao dicionário. A solução com **BRAM Dual-Port** (RAM de Bloco de Porta Dupla) — conforme a *Fonte 2* — é ideal, pois permite **leitura e escrita simultâneas**, fundamentais para manter o *throughput* contínuo em *streaming*.

### 🔹 Componentes Arquiteturais

A estrutura central do core LZW é composta por uma **Tabela de Hash** e um **Armazenamento de Dados** (dicionário propriamente dito), ambos mapeados em BRAMs:

1. **Tabela de Hash (Hash Table):**
   
   - **Função:** Acelerar a busca de padrões (sequências de símbolos) no dicionário.  
   - **Implementação:** Mapeada em **BRAM Dual-Port**, permitindo *lookup* (leitura) e inserção (escrita) de novos padrões em ciclos simultâneos ou adjacentes.  
   - **Campos Chave:** Contém a **chave do padrão** e um **ponteiro (endereço)** que referencia o padrão completo no Armazenamento de Dados.

2. **Armazenamento de Dados (Data Storage / Dicionário):**
   
   - **Função:** Armazenar os novos códigos gerados pela concatenação do padrão anterior (`P`) com o novo símbolo (`C`).  
   - **Implementação:** Utiliza uma segunda **BRAM Dual-Port** (ou múltiplas BRAMs *Single-Port*), dependendo da profundidade e largura do dicionário.  
   - **Campos:** Guarda o **código prefixo** e o **símbolo sufixo** que formam cada nova sequência.

### ⚙️ Vantagem do Dual-Port para LZW

Em cada ciclo de clock, o core LZW precisa:

- **Acessar** o dicionário: buscar $\text{Código Antigo} + \text{Próximo Símbolo}$  
- **Atualizar/Gravar** o dicionário: inserir $\text{Código Antigo} + \text{Símbolo Atual}$

O uso de BRAM Dual-Port permite que as operações de **leitura** e **escrita** ocorram em paralelo, com latência mínima, possibilitando:

- Processamento de **1 símbolo por ciclo** (ou mais em arquiteturas paralelas)
- Cumprimento do requisito de *throughput* de **≈ 37 MB/s**
- **Baixo consumo de área** e eficiência no uso de recursos de BRAM/LUT

---

## 📊 2. Fluxograma do Codificador Canonical Huffman (CHE)

O **Canonical Huffman Encoding (CHE)**, conforme a *Fonte 6*, é amplamente utilizado por equilibrar **área, energia e throughput**.  
Diferentemente do Huffman tradicional, o CHE **não armazena a árvore completa**, apenas os **comprimentos dos códigos de bits**, o que reduz drasticamente a complexidade de hardware.

### 🔸 Estrutura do Pipeline CHE

O processo é dividido em **cinco fases** principais, organizadas em *pipeline* para operação eficiente em FPGA:

| Fase                                                   | Descrição                                                                                                         | Objetivo na FPGA                                                                                                         |
|:------------------------------------------------------ |:----------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------ |
| **1. Filtro (Filter)**                                 | Analisa o *stream* de entrada e computa as **frequências** de ocorrência de cada símbolo (ou diferença/resíduo).  | Implementado com **contadores e registradores**, possivelmente BRAMs para armazenar a contagem de até 256/4096 símbolos. |
| **2. Ordenação (Sort)**                                | Ordena os símbolos conforme suas frequências (do mais frequente ao menos frequente). Etapa mais custosa em HW.    | Implementação com **árvores de soma (adder trees)**, **comparadores** ou executada por **processador embarcado**.        |
| **3. Cômputo do Comprimento de Bits (Compute BitLen)** | Constrói implicitamente a árvore de Huffman para determinar o **comprimento mínimo de bits ($L_i$)** por símbolo. | Lógica sequencial que simula a árvore de Huffman baseada em prioridade de frequência.                                    |
| **4. Canonização (Canonize)**                          | Gera o conjunto final de **códigos canônicos**, garantindo que códigos de mesmo comprimento sejam contíguos.      | **Soma acumulada** para gerar códigos consecutivos conforme o comprimento ($L_i$).                                       |
| **5. Codificação (Create Codeword)**                   | Substitui cada símbolo de entrada pelo seu **código binário canônico**.                                           | **BRAM de Codificação (lookup table)** com *pipeline*, garantindo alta taxa de saída.                                    |

### 🔻 Diagrama de Blocos do Pipeline

O fluxo geral do CHE pode ser representado da seguinte forma:

[Input Stream]  
↓  
[Filtro de Frequências]  
↓  
[Ordenação]  
↓  
[Cálculo de BitLen]  
↓  
[Canonização]  
↓  
[Tabela BRAM de Códigos]  
↓  
[Output Stream Comprimido]

Após a geração inicial da **Tabela de Códigos (fases 1–4)** — que pode ser feita a cada quadro ou conjunto de quadros — a **fase 5 (Codificação)** opera em modo *streaming* contínuo, alcançando:

- **Alta eficiência energética**
- **Latência previsível**
- **Throughput compatível com 60 fps**

---

## 🧩 Conclusão

As arquiteturas **LZW com BRAM Dual-Port** e **Canonical Huffman (CHE)** complementam-se no contexto de compressão *lossless* para imagens térmicas (LWIR 16-bit), oferecendo:

- **LZW:** Eficiência para dados estruturados e redundantes.  
- **CHE:** Compressão entropia de alta eficiência pós-predictor.  

Ambas as soluções atendem aos requisitos de **latência < 16.6 ms**, **throughput ≈ 37 MB/s** e **CR > 1.5**, sendo viáveis para implementação FPGA dentro do escopo do projeto.
