# Sprint 4: LZW (DSP) & Integração

Período Estimado: Dezembro, 29 de 2025 a 02 de Janeiro de 2026

## Objetivo

O objetivo desta Sprint é **otimizar a função de Hash** do dicionário LZW utilizando os **Blocos DSP** da FPGA Cyclone para acelerar o cálculo de índices e realizar a **integração final** entre os estágios de Predição (DPCM) e Codificação Entrópica (LZW).

### Passo 1: Otimização com DSP

Esta atividade foca no uso eficiente dos recursos aritméticos dedicados.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **Hash Function em DSP** | Implementar a função de hash (ex: `(Prefix << 4) ^ Char`) utilizando os multiplicadores/acumuladores dos blocos DSP para reduzir a latência e liberar LEs. | Cálculo de Hash mapeado em DSPs. |
| **1.2** | **Tratamento de Colisões** | Refinar a lógica de colisão para operar em conjunto com o hash rápido. Avaliar o impacto no caminho crítico. | Colisões resolvidas sem degradar $F_{MAX}$. |

### Passo 2: Integração do Sistema

Este passo une todos os módulos desenvolvidos até o momento.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **Top-Level Completo** | Integrar `DPCM_Predictor`, `RLE_Encoder` (opcional/adaptado) e `LZW_Encoder` em um único módulo. | Sistema completo instanciado. |
| **2.2** | **Controle de Fluxo Global** | Implementar sinais de *backpressure* (ready/valid) robustos entre todos os estágios para evitar perda de dados se o LZW demorar mais que 1 ciclo (ex: em colisões). | Fluxo de dados seguro e sem perdas. |
| **2.3** | **Validação Integrada** | Simular o sistema completo com imagens reais. Verificar a integridade dos dados do início ao fim. | Sistema validado *Bit-Perfect*. |

### Meta do Sprint 4

* **Aceleração DSP:** Função de Hash otimizada.
* **Sistema Integrado:** Pipeline DPCM -> LZW operando em conjunto.
* **Robustez:** Controle de fluxo lidando corretamente com variações de taxa.
