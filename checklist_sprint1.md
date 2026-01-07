# Checklist Sprint 1: Baseline DPCM-RLE (Verilog)

Este documento rastreia o progresso das atividades definidas para a Sprint 1.

## Passo 1: Implementação HDL (Verilog)

- [x] **1.1 Codificação do Preditor DPCM**
  - Refinar o módulo `DPCM_Predictor` para integração completa.
  - Garantir tratamento correto de reset e sinalização de validade (*valid*).
  - *Status:* Implementado em `hw/hdl/DPCM_Predictor.v`.

- [x] **1.2 Codificação do Codificador RLE**
  - Implementar o módulo RLE (*Run-Length Encoding*).
  - Focar na compressão de sequências de zeros (Zero-Run).
  - Utilizar contadores otimizados.
  - *Status:* Estrutura inicial implementada em `hw/hdl/RLE_Encoder.v`.

- [x] **1.3 Integração do Pipeline DPCM-RLE**
  - Criar o módulo *Top-Level* conectando DPCM e RLE.
  - Estabelecer o fluxo de dados contínuo (*streaming*).
  - *Status:* Integrado em `hw/hdl/LWIR_Lossless_Compression.v`.

## Passo 2: Validação e Síntese

- [x] **2.1 Criação do Testbench (RTL)**
  - Desenvolver um *testbench* Verilog.
  - Implementar leitura de arquivos de entrada (hex/txt).
  - Implementar escrita de arquivos de saída para verificação.
  - *Status:* Testbench criado em `hw/sim/tb_LWIR_Lossless_Compression.v`. Script gerador de vetores `generate_vectors.py` criado e executado.

- [ ] **2.2 Simulação Funcional e Validação Lossless**
  - Gerar vetores de teste a partir do dataset FLIR (Python).
  - Executar a simulação (ModelSim/Icarus Verilog).
  - Comparar saída do HW com modelo SW (Bit-perfect).

- [ ] **2.3 Síntese e Análise de Timing**
  - Sintetizar o projeto no Quartus II.
  - Verificar $F_{MAX} \ge 100 \text{ MHz}$.
  - Verificar uso de recursos (LUTs/FFs).
