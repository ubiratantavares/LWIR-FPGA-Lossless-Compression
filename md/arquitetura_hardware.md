# Arquitetura de Hardware e Mapeamento de Primitivas

**Sprint:** 0
**Atividade:** 3.1 - Adaptação para Primitivas Altera

Este documento define a estratégia de mapeamento dos algoritmos de compressão para os recursos dedicados da FPGA Altera (Intel) Cyclone IV/V.

## 1. Preditor DPCM (Left Neighbor)

O preditor selecionado é o **DPCM Fixo (Left Neighbor)**.

### Lógica

$$ R_i = P_i - P_{i-1} $$

### Mapeamento de Hardware

* **Operação Aritmética (Subtração):**
  * Como a subtração é de 16 bits, ela pode ser implementada eficientemente usando **Logic Elements (LEs)** em modo aritmético (Carry Chain).
  * **Opção DSP:** Embora possível, o uso de blocos DSP para uma subtração simples pode ser um desperdício, a menos que se deseje economizar LEs ou alcançar frequências muito altas (> 200 MHz).
  * **Decisão:** Inicialmente, permitir que o sintetizador infira LEs. Se o timing for crítico, forçar o uso de DSP via atributo `use_dsp`.
* **Armazenamento ($P_{i-1}$):**
  * Requer um registrador de 16 bits.
  * Mapeado para **Flip-Flops (FFs)** nos Logic Elements.

## 2. Dicionário LZW (Futuro - Sprint 3)

O dicionário LZW é o componente mais crítico em termos de memória.

### Estrutura

* **Tabela Hash:** Necessária para verificar rapidamente se uma sequência `Prefix + Char` já existe.
* **Memória de Códigos:** Armazena os códigos gerados.

### Mapeamento de Hardware (M9K/M10K)

* **Recurso Alvo:** Blocos de Memória Embarcada **M9K** (Cyclone IV) ou **M10K** (Cyclone V).
* **Configuração:** **Dual-Port RAM**.
  * *Porta A:* Leitura (Lookup) para verificar existência.
  * *Porta B:* Escrita (Update) para adicionar novas entradas.
  * Isso permite processar 1 símbolo por ciclo de clock (Throughput de 100%).
* **Capacidade:** O Cyclone IV E (EP4CE115) possui 432 blocos M9K (~3.8 Mbits). Um dicionário LZW típico (4K entradas x 20-30 bits) cabe confortavelmente.

## 3. Estratégia de Pipeline

O pipeline será dividido em estágios para garantir $F_{MAX} \ge 100 \text{ MHz}$.

1. **Estágio 1 (Fetch/Predict):** Busca do pixel e cálculo do resíduo (DPCM).
2. **Estágio 2 (Map/Encode):** Mapeamento para inteiros positivos (ZigZag) e Codificação (RLE/LZW).
3. **Estágio 3 (Pack):** Empacotamento do bitstream.

---
**Status:** Estratégia definida. Código VHDL inicial focará no Estágio 1 (DPCM).
