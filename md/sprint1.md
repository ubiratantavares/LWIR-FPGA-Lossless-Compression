# Sprint 1: Baseline DPCM-RLE (Verilog)

Período Estimado: Dezembro, 08 a 14 de 2025

## Objetivo

O objetivo principal desta Sprint é **implementar o pipeline baseline** composto pelo Preditor DPCM e o Codificador RLE em hardware (HDL), garantindo a **corretude funcional (lossless)** e a viabilidade de síntese no FPGA Altera.

### Passo 1: Implementação HDL (Verilog)

Esta atividade foca na codificação dos módulos de hardware que compõem a primeira versão funcional do sistema.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **Codificação do Preditor DPCM** | Refinar o módulo `DPCM_Predictor` (iniciado na Sprint 0) para integração completa. Garantir tratamento correto de reset e sinalização de validade (*valid/ready*). | Módulo DPCM finalizado e pronto para integração. |
| **1.2** | **Codificação do Codificador RLE** | Implementar o módulo RLE (*Run-Length Encoding*) para comprimir sequências de valores repetidos (focando em zeros do resíduo). Utilizar contadores otimizados para LUTs. | Módulo RLE funcional implementado em Verilog. |
| **1.3** | **Integração do Pipeline DPCM-RLE** | Criar o módulo *Top-Level* conectando DPCM e RLE. Estabelecer o fluxo de dados contínuo (*streaming*) entre os estágios. | Pipeline DPCM-RLE integrado e sintetizável. |

### Passo 2: Validação e Síntese

Este passo garante que o hardware descrito funciona como esperado (bit-perfect) e atende aos requisitos de temporização e área.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **Criação do Testbench (RTL)** | Desenvolver um *testbench* Verilog que leia vetores de teste (imagens convertidas para texto/hex) e estimule o DUT (*Device Under Test*). | Ambiente de verificação funcional (Testbench) criado. |
| **2.2** | **Simulação Funcional e Validação Lossless** | Executar a simulação do pipeline com frames reais do dataset FLIR. Comparar a saída do hardware com o modelo de referência (Python) para garantir integridade bit a bit. | **Corretude (*Lossless*)** validada. |
| **2.3** | **Síntese e Análise de Timing** | Sintetizar o projeto completo no Quartus II. Analisar o relatório de *Timing* (TimeQuest) para garantir $F_{MAX} \ge 100 \text{ MHz}$ e verificar o uso de recursos. | Relatório de Síntese e Timing aprovado. |

### Meta do Sprint 1

* **Pipeline Funcional:** DPCM + RLE operando em hardware (simulação).
* **Corretude Garantida:** Saída do hardware idêntica ao modelo de software (Bit-perfect).
* **Baseline Estabelecido:** Dados reais de ocupação e frequência máxima para o sistema inicial.
