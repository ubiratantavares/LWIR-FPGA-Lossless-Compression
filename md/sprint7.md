# Sprint 7: Medição de Latência

Período Estimado: Janeiro, 19 a 23 de 2026

## Objetivo

O objetivo desta Sprint é medir a **latência real** do sistema em hardware, garantindo que o tempo de processamento esteja dentro do limite crítico (< 1 ms) para aplicações em tempo real.

### Passo 1: Instrumentação

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **SignalTap II Logic Analyzer** | Configurar o *SignalTap II* no Quartus para capturar sinais internos (valid_in, valid_out, estados da FSM) em tempo real. | Trigger e captura configurados. |
| **1.2** | **Contadores de Ciclos** | Implementar contadores de performance no HDL para medir o número exato de ciclos entre a entrada do primeiro pixel e a saída do primeiro código válido. | Hardware de medição integrado. |

### Passo 2: Execução e Análise

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **Teste de Latência** | Executar o processamento de frames e capturar os tempos. Calcular a latência em microssegundos ($T = Ciclos \times 10ns$). | Dados de latência coletados. |
| **2.2** | **Otimização (se necessário)** | Se a latência for alta, identificar gargalos no pipeline e reduzir estágios desnecessários ou otimizar a FSM. | Latência otimizada. |

### Meta do Sprint 7

* **Latência Medida:** Valor exato documentado.
* **Requisito Atendido:** Latência comprovada < 1 ms.
