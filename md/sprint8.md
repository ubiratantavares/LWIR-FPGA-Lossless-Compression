# Sprint 8: Throughput & Estresse

Período Estimado: Janeiro, 26 a 30 de 2026

## Objetivo

O objetivo desta Sprint é validar a capacidade do sistema de manter o **throughput** alvo (> 1 pixel/ciclo ou > 100 MPixels/s) sob condições de carga máxima e estresse contínuo.

### Passo 1: Testes de Throughput

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **Injeção de Tráfego Máximo** | Alimentar o sistema com dados na velocidade máxima do clock (back-to-back) sem pausas. | Teste de saturação de entrada. |
| **1.2** | **Verificação de Stalls** | Monitorar o sinal de *ready* ou *stall* interno. Garantir que o pipeline não engasgue (exceto por backpressure da saída). | Ausência de *stalls* internos indesejados. |

### Passo 2: Testes de Estresse

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **Padrões de Pior Caso** | Testar com imagens sintéticas projetadas para causar colisões máximas no LZW ou expansão de dados. | Robustez verificada. |
| **2.2** | **Estabilidade Térmica/Longa Duração** | Deixar o sistema rodando em loop por um período estendido para verificar estabilidade. | Sistema estável sob estresse. |

### Meta do Sprint 8

* **Throughput Validado:** > 100 MPixels/s sustentado.
* **Robustez Comprovada:** Sistema opera sem falhas sob carga máxima.
