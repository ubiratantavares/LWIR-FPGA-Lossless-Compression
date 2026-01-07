# Cronograma

O foco agora se desloca para o uso de blocos dedicados da Altera (Blocos de memória **M9K/M10K** para o dicionário LZW e **Blocos DSP** da Cyclone) e o fluxo de síntese/análise de *timing*
do Quartus II.

## Sprint 0: Fechamento da Simulação e Configuração Altera

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Validação Final da Simulação (SW)** | 3 dias | CR 1.5:1 a 2.5:1 |
| Executar as simulações DPCM-LZW nos *frames* TIFF para definir o modelo de predição ideal. | | |
| **Configuração do Ambiente Quartus II** | 2 dias | Ferramenta de Síntese/Implementação (Quartus II 13.1) |
| Instalar e configurar o Quartus II 13.1 Web Edition e os *kits* Cyclone IV/V. | | |
| **Modelagem HLS/HDL Inicial** | 2 dias | Arquitetura Detalhada |
| Iniciar a modelagem em C/C++ (se usar um *tool* HLS compatível) ou diretamente em VHDL/Verilog, focando nas primitivas da Altera. | | |
| **Meta do Sprint 0:** Modelo preditivo definido e Quartus II 13.1 configurado para o Cyclone. | | |

## Sprint 1: Baseline DPCM-RLE (HDL)

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Implementação em HDL (Verilog) do Preditor DPCM e Codificador RLE** | 5 dias | Baseline DPCM-RLE |
| Implementar o preditor DPCM e o codificador RLE em Verilog, focando nas primitivas da Altera. | | |
| **Síntese e validação de corretude (*lossless*)** | 2 dias | Baseline DPCM-RLE |
| Realizar a síntese do código HDL e validar a corretude do sistema. | | |

## Sprint 2: Otimização II=1 no Quartus

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Otimização II=1 no Quartus** | 5 dias | Otimização II=1 no Quartus |
| Uso de técnicas de *pipelining* e *retiming* no código HDL para atingir o **$II=1$** e maximizar $F_{MAX}$. Análise inicial de *timing* no Quartus II. | | |

## Sprint 3: LZW e Mapeamento de Memória

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **LZW e Mapeamento de Memória** | 5 dias | LZW e Mapeamento de Memória |
| Implementação do dicionário **LZW**, focando no mapeamento dos dicionários para blocos de memória **M9K/M10K** da Cyclone.  | | |

## Sprint 4: LZW (DSP) & Integração

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **LZW (DSP) & Integração** | 5 dias | LZW (DSP) & Integração |
| Otimizar a lógica de busca (*hash* LZW) para usar os blocos **DSP da Cyclone** (em vez dos DSP48 do Xilinx). **Integração DPCM-LZW**. | | |

## Sprint 5: Análise de Temporização Final

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Análise de Temporização Final** | 5 dias | Análise de Temporização Final |
| Realizar a compilação final no Quartus II, analisar o **Relatório de *Timing*** (TimeQuest) para estimar o $F_{MAX}$ e verificar se o *timing* é fechado. | | |

## Sprint 6: Setup e interface

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Setup e Interface** | 5 dias | Setup e Interface |
| **Montagem do Setup de Testes**. Validação do Barramento de *streaming* de dados (simulando AXI4/Avalon-ST) para os *pins* do Cyclone. | | |

## Sprint 7: Medição de Latência

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Medição de Latência** | 5 dias | Medição de Latência |
| **Testes de desempenho** no *hardware*. Medição da **Latência total (\< 1 ms)** usando ferramentas *on-chip* (ex: **SignalTap II** do Quartus II). | | |

## Sprint 8: Throughput & Estresse

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Throughput & Estresse** | 5 dias | Throughput & Estresse |
| Medição do **Throughput** (\> 1 *pixel*/ciclo). Testes de estresse na entrada/saída do *pipeline*. | | |

## Sprint 9: Validação Final de CR

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Validação Final de CR** | 5 dias | Validação Final de CR |
| Testes finais do **CR (1.5:1 a 2.5:1)** no *hardware* com o *dataset* FLIR. | | |

## Sprint 10: Revisão e Orçamento

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Revisão e Orçamento** | 5 dias | Revisão e Orçamento |
| Revisão do código/metodologia. Confirmação do uso de recursos (**LUTs, FFs, DSP, M9K**) e garantia de que a utilização total é otimizada (abaixo do limite para o Cyclone). | | |

## Sprint 11: Entrega Final

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Entrega Final** | 5 dias | Entrega Final |
| Organização do código-fonte HDL, arquivo de configuração Quartus (.qpf/.qsf), Relatórios de *Timing* e **Entrega do Projeto** (até 28/Fev/2026). | | |
