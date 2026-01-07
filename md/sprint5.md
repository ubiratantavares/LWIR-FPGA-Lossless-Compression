# Sprint 5: Análise de Temporização Final

Período Estimado: Janeiro, 05 a 09 de 2026

## Objetivo

O objetivo desta Sprint é realizar o **fechamento de timing** do projeto completo, garantindo que a frequência alvo ($F_{MAX} \ge 100 \text{ MHz}$) seja atingida em todas as condições de operação (Worst-Case Corner).

### Passo 1: Compilação e Análise

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **Compilação Full** | Executar o fluxo completo de compilação no Quartus II (Synthesis, Fitter, Assembler, TimeQuest) com o design integrado. | Bitstream gerado. |
| **1.2** | **Análise de Setup/Hold** | Analisar os relatórios de *Setup* e *Hold* para os modelos *Slow* e *Fast*. Identificar os caminhos críticos remanescentes. | Relatório de violações detalhado. |

### Passo 2: Otimização de Timing

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **Correção de Violações** | Aplicar técnicas de otimização física (*Physical Synthesis*), duplicar registradores de alto *fan-out*, ou ajustar o código HDL para quebrar caminhos longos. | Slack de Setup positivo (> 0ns). |
| **2.2** | **Restrições Finais** | Congelar as restrições de *timing* e pinagem (se definida). Garantir que as interfaces de I/O também atendam aos requisitos. | SDC final validado. |
| **2.3** | **Validação de Estabilidade** | Verificar se o design é estável sob variações de processo, tensão e temperatura (PVT) suportadas pelo dispositivo. | Design robusto e aprovado. |

### Meta do Sprint 5

* **Timing Fechado:** $F_{MAX} \ge 100 \text{ MHz}$ (Slack > 0).
* **Relatório TimeQuest:** Aprovado e documentado.
* **Bitstream:** Arquivo `.sof` pronto para gravação.
