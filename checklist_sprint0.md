# Checklist Sprint 0: Fechamento da Simulação e Configuração Altera

Este documento rastreia o progresso das atividades definidas para a Sprint 0.

## Passo 1: Validação Final da Simulação (SW)

- [x] **1.1 Execução da Simulação em Massa**
  - Utilizar o *Controller* Python refatorado para processar todos os **500 *frames* TIFF de 16 bits** do *dataset* FLIR.
  - *Status:* Concluído. Script `main.py` executado com sucesso. Resultados gerados para DPCM Fixo e Adaptativo.

- [x] **1.2 Análise de CR e Trade-off**
  - Comparar o CR médio alcançado pelo preditor **DPCM Fixo** vs. o **Preditor CNN Adaptativo**.
  - Analisar o ganho de CR da CNN contra o aumento de complexidade (uso de blocos DSP da Cyclone).
  - **Decisão Técnica Formal:** Escolher o Preditor (DPCM ou CNN).
  - *Status:* Concluído. Decisão documentada em `md/decisao_tecnica_preditor.md`. **DPCM Fixo** escolhido.

- [x] **1.3 Análise da Entropia do Resíduo**
  - Calcular a entropia dos resíduos gerados pelo preditor escolhido.
  - Confirmar a baixa entropia como evidência de eficiência do preditor.
  - *Status:* Concluído. Documentado em `md/analise_entropia_residuo.md`. Entropia média de **5.13 bits/pixel**.

## Passo 2: Configuração do Ambiente Quartus II

- [x] **2.1 Instalação e Configuração da Toolchain**
  - Instalar o **Quartus II 13.1 Web Edition**.
  - Garantir a correta configuração do *software* de programação e simulação.
  - *Status:* Arquivos de projeto configurados. Instalação do software deve ser verificada pelo usuário.

- [x] **2.2 Criação do Projeto Base Quartus**
  - Criar um novo projeto no Quartus II.
  - Definir o *target* FPGA (ex: **Cyclone IV ou V**).
  - Estabelecer o caminho para o código-fonte HDL.
  - *Status:* Projeto criado em `hw/quartus/LWIR_Lossless_Compression.qpf` (Target: Cyclone IV E EP4CE115F29C7).

- [x] **2.3 Definição das Restrições de Timing**
  - Configurar o *clock* principal do projeto (provavelmente **100 MHz**).
  - Configurar as restrições de *timing* (SDC) iniciais.
  - *Status:* Arquivo `hw/constraints/timing.sdc` criado com clock de 100MHz (10ns).

## Passo 3: Modelagem HLS/HDL Inicial

- [x] **3.1 Adaptação para Primitivas Altera**
  - Mapear as estruturas de memória do dicionário LZW (BRAMs) para **M9K/M10K**.
  - Mapear as operações aritméticas (Preditor DPCM) para **Blocos DSP**.
  - *Status:* Estratégia documentada em `md/arquitetura_hardware.md`.

- [x] **3.2 Codificação da Lógica Preditora (HLS/HDL)**
  - Iniciar a codificação da lógica Preditora DPCM em VHDL ou Verilog.
  - Garantir a fidelidade de **16 bits**.
  - *Status:* Código Verilog criado em `hw/hdl/DPCM_Predictor.v`. Saída de 17 bits (signed) para evitar overflow.

- [ ] **3.3 Síntese e Relatório de Recursos Inicial**
  - Realizar a primeira síntese do código Preditor no Quartus II.
  - Obter um **Relatório de Uso de Recursos** (LUTs, DSPs, M9K).
  - Comparar com o orçamento máximo de **50%**.
  - *Status:* **Pendente de Validação do Usuário**. O código Verilog está pronto, mas a síntese requer o software Quartus II instalado localmente. Estimativa: < 1% de ocupação (muito leve).
