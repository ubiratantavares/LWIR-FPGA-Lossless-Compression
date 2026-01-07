# Sprint 0: Fechamento da Simulação e Configuração Altera

Período Estimado: Dezembro, 01 a 07 de 2025

## Objetivo

O objetivo principal desta Sprint é **definir o modelo preditivo final** para o *hardware* e **validar o ambiente de síntese** Altera.

### Passo 1: Validação Final da Simulação (SW)

Esta atividade visa determinar qual preditor (DPCM Fixo ou CNN) oferece o melhor equilíbrio entre desempenho (*CR*) e complexidade para a próxima fase.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **Execução da Simulação em Massa** | Utilizar o *Controller* Python refatorado para processar todos os **500 *frames* TIFF de 16 bits** do *dataset* FLIR. | *Dataset* validado e **Taxas de Compressão (CR) Médias** para os *pipelines* DPCM-LZW e CNN-LZW calculadas. |
| **1.2** | **Análise de CR e Trade-off** | Comparar o CR médio alcançado pelo preditor **DPCM Fixo** vs. o **Preditor CNN Adaptativo**. Analisar o ganho de CR da CNN contra o aumento de complexidade (uso de blocos DSP da Cyclone). | **Decisão Técnica Formal:** Escolher o **Preditor (DPCM ou CNN)** que atinge o requisito CR ($1.5:1$ a $2.5:1$) com o menor *overhead* de *hardware*. |
| **1.3** | **Análise da Entropia do Resíduo** | Calcular a entropia dos resíduos gerados pelo preditor escolhido para confirmar a baixa redundância dos dados que serão alimentados ao codificador LZW. | Confirmar a baixa entropia como evidência de eficiência do preditor. |

### Passo 2: Configuração do Ambiente Quartus II

Este passo realiza a transição de *toolchain*, garantindo que o ambiente de *hardware* esteja pronto.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **Instalação e Configuração da Toolchain** | Instalar o **Quartus II 13.1 Web Edition** e garantir a correta configuração do *software* de programação e simulação. | Ambiente de desenvolvimento Altera operacional. |
| **2.2** | **Criação do Projeto Base Quartus** | Criar um novo projeto no Quartus II, definindo o *target* FPGA (ex: **Cyclone IV ou V**) e estabelecendo o caminho para o código-fonte HDL. | Projeto Quartus criado com o dispositivo alvo configurado. |
| **2.3** | **Definição das Restrições de Timing** | Configurar o *clock* principal do projeto (provavelmente **100 MHz**) e as restrições de *timing* (SDC) iniciais para que o Quartus possa realizar a análise de temporização. | Arquivo SDC de *timing* configurado. |

### Passo 3: Modelagem HLS/HDL Inicial

Este passo transforma a lógica de *software* (Python/C/C++) na arquitetura de *hardware* específica para a família Cyclone.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **3.1** | **Adaptação para Primitivas Altera** | Mapear as estruturas de memória do dicionário LZW (BRAMs) e as operações aritméticas (Preditor DPCM) para os blocos dedicados da Altera (**M9K/M10K** e **Blocos DSP**). | Estrutura de memória e aritmética definida em termos de blocos Cyclone. |
| **3.2** | **Codificação da Lógica Preditora (HLS/HDL)** | Iniciar a codificação da lógica Preditora DPCM em VHDL ou Verilog (ou C/C++ se usar *tool* HLS compatível com Quartus 13.1), garantindo a fidelidade de **16 bits**. | Código HDL/HLS inicial para o Preditor. |
| **3.3** | **Síntese e Relatório de Recursos Inicial** | Realizar a primeira síntese do código Preditor no Quartus II para obter um **Relatório de Uso de Recursos** (LUTs, DSPs, M9K) e compará-lo com o orçamento máximo de **50%**. | Relatório de Recursos inicial validado contra o RNF005. |

### Meta do Sprint 0

* **Decisão Algorítmica:** O Preditor ideal (DPCM Fixo vs. CNN) para o *hardware* foi escolhido.
* **Toolchain Pronta:** Quartus II 13.1 configurado para síntese.
* **Protótipo Imediato:** Código DPCM inicial sintetizado com Relatório de Recursos da Cyclone.
