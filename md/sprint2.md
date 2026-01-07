# Sprint 2: Otimização II=1 no Quartus

Período Estimado: Dezembro, 15 a 19 de 2025

## Objetivo

O objetivo principal desta Sprint é **otimizar o pipeline HDL** (DPCM-RLE) para atingir um Intervalo de Iniciação (**II=1**) e maximizar a frequência de operação ($F_{MAX}$), garantindo que o sistema possa processar 1 pixel por ciclo de clock sem *stalls*.

### Passo 1: Otimização de Pipeline (II=1)

Esta atividade foca na inserção de registradores de pipeline e balanceamento de lógica para quebrar caminhos críticos.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **Pipelining Fino (Fine-Grained)** | Inserir estágios de pipeline adicionais dentro do Preditor e do RLE, se necessário, para garantir que nenhuma lógica combinacional exceda o tempo de ciclo alvo (10ns para 100MHz). | Pipeline com **II=1** (1 dado processado por ciclo). |
| **1.2** | **Retiming e Balanceamento** | Utilizar técnicas de *register retiming* (manual ou via diretiva do Quartus) para mover a lógica combinacional através dos registradores, equilibrando os atrasos entre estágios. | Caminhos críticos reduzidos e $F_{MAX}$ maximizada. |
| **1.3** | **Otimização de Recursos** | Revisar o uso de LUTs e FFs. Substituir lógicas complexas por implementações mais eficientes (ex: somadores dedicados, *carry chains*) específicas da arquitetura Cyclone. | Uso eficiente de recursos (< 50% do dispositivo). |

### Passo 2: Análise de Timing (TimeQuest)

Este passo envolve a análise rigorosa das restrições de tempo e a correção de violações.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **Refinamento das Restrições (SDC)** | Atualizar o arquivo `.sdc` com incertezas de clock (*jitter*), *input/output delays* e *multicycle paths* (se houver). | Análise de timing realista e robusta. |
| **2.2** | **Análise de Caminho Crítico** | Identificar os caminhos com pior *slack* de setup e hold no TimeQuest Timing Analyzer. Realizar correções no HDL para resolver violações. | **Slack Positivo** em todos os caminhos para 100 MHz. |
| **2.3** | **Verificação de Throughput** | Confirmar via simulação pós-síntese (Gate-Level) ou análise estática que o *throughput* se mantém em 1 pixel/ciclo sob carga máxima. | Throughput garantido de > 100 MPixels/s. |

### Meta do Sprint 2

* **Pipeline Otimizado:** Sistema operando com II=1 (sem bolhas no pipeline em regime permanente).
* **Timing Fechado:** $F_{MAX} \ge 100 \text{ MHz}$ (com margem de segurança, idealmente > 120 MHz).
* **Relatório de Timing:** Documento comprovando ausência de violações (Slack > 0).
