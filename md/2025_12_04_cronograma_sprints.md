## 🛠️  Cronograma

O foco agora se desloca para o uso de blocos dedicados da Altera (Blocos de memória **M9K/M10K** para o dicionário LZW e **Blocos DSP** da Cyclone) e o fluxo de síntese/análise de *timing* 
do Quartus II.

### 💻 Sprint 0 (Dezembro - Semana 1): Fechamento da Simulação e Configuração Altera

| Atividade (User Story) | Duração Estimada | Requisitos Relacionados |
| :--- | :--- | :--- |
| **Validação Final da Simulação (SW)** | 3 dias | CR 1.5:1 a 2.5:1 |
| Executar as simulações DPCM-LZW nos *frames* TIFF para definir o modelo de predição ideal. | | |
| **Configuração do Ambiente Quartus II** | 2 dias | Ferramenta de Síntese/Implementação (Quartus II 13.1) |
| Instalar e configurar o Quartus II 13.1 Web Edition e os *kits* Cyclone IV/V. | | |
| **Modelagem HLS/HDL Inicial** | 2 dias | Arquitetura Detalhada |
| Iniciar a modelagem em C/C++ (se usar um *tool* HLS compatível) ou diretamente em VHDL/Verilog, focando nas primitivas da Altera. | | |
| **Meta do Sprint 0:** Modelo preditivo definido e Quartus II 13.1 configurado para o Cyclone. | | |

\<hr\>

### Fase 2: Implementação e Otimização de Hardware (Dezembro - Jan)

O foco é a implementação e otimização de *timing* usando os relatórios e *tools* do Quartus II.

| Sprint | Período (Aprox.) | Foco Principal | Atividades Chave |
| :--- | :--- | :--- | :--- |
| **Sprint 1** | Dez/Sem 2 | **Baseline DPCM-RLE (HDL)** | Implementação em HDL (VHDL/Verilog) do Preditor DPCM e Codificador RLE. Síntese e validação de corretude (*lossless*). |
| **Sprint 2** | Dez/Sem 3 | **Otimização II=1 no Quartus** | Uso de técnicas de *pipelining* e *retiming* no código HDL para atingir o **$II=1$** e maximizar $F_{MAX}$. Análise inicial de *timing* no Quartus II. |
| **Sprint 3** | Dez/Sem 4 | **LZW e Mapeamento de Memória** | Implementação do dicionário **LZW**, focando no mapeamento dos dicionários para blocos de memória **M9K/M10K** da Cyclone.  |
| **Sprint 4** | Jan/Sem 1 | **LZW (DSP) & Integração** | Otimizar a lógica de busca (*hash* LZW) para usar os blocos **DSP da Cyclone** (em vez dos DSP48 do Xilinx). **Integração DPCM-LZW**. |
| **Sprint 5** | Jan/Sem 2 | **Análise de Temporização Final** | Realizar a compilação final no Quartus II, analisar o **Relatório de *Timing*** (TimeQuest) para estimar o $F_{MAX}$ e verificar se o *timing* é fechado. |

\<hr\>

### Fase 3: Validação, Testes e Entrega (Jan - Fev)

O foco é na medição das métricas (CR, Latência) no *hardware* real.

| Sprint | Período (Aprox.) | Foco Principal | Atividades Chave |
| :--- | :--- | :--- | :--- |
| **Sprint 6** | Jan/Sem 3 | **Setup e Interface** | **Montagem do Setup de Testes**. Validação do Barramento de *streaming* de dados (simulando AXI4/Avalon-ST) para os *pins* do Cyclone. |
| **Sprint 7** | Jan/Sem 4 | **Medição de Latência** | **Testes de desempenho** no *hardware*. Medição da **Latência total (\< 1 ms)** usando ferramentas *on-chip* (ex: **SignalTap II** do Quartus II). |
| **Sprint 8** | Fev/Sem 1 | **Throughput & Estresse** | Medição do **Throughput** (\> 1 *pixel*/ciclo). Testes de estresse na entrada/saída do *pipeline*. |
| **Sprint 9** | Fev/Sem 2 | **Validação Final de CR** | Testes finais do **CR (1.5:1 a 2.5:1)** no *hardware* com o *dataset* FLIR. |
| **Sprint 10** | Fev/Sem 3 | **Revisão e Orçamento** | Revisão do código/metodologia. Confirmação do uso de recursos (**LUTs, FFs, DSP, M9K**) e garantia de que a utilização total é otimizada (abaixo do limite para o Cyclone). |
| **Sprint 11** | Fev/Sem 4 | **Entrega Final** | Organização do código-fonte HDL, arquivo de configuração Quartus (.qpf/.qsf), Relatórios de *Timing* e **Entrega do Projeto** (até 28/Fev/2026). |
