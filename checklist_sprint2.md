# Checklist Sprint 2: Otimização II=1 no Quartus

Este documento rastreia o progresso das atividades definidas para a Sprint 2.

## Passo 1: Otimização de Pipeline (II=1)

- [ ] **1.1 Pipelining Fino (Fine-Grained)**
  - Inserir estágios de pipeline adicionais se necessário.
  - Garantir II=1.

- [ ] **1.2 Retiming e Balanceamento**
  - Aplicar *register retiming* para equilibrar atrasos.
  - Maximizar $F_{MAX}$.

- [ ] **1.3 Otimização de Recursos**
  - Revisar uso de LUTs e FFs.
  - Utilizar primitivas eficientes (Carry Chains).

## Passo 2: Análise de Timing (TimeQuest)

- [x] **2.1 Refinamento das Restrições (SDC)**
  - Atualizar `timing.sdc` com incertezas e delays.
  - Definir restrições de I/O.
  - *Status:* Arquivo `hw/constraints/timing.sdc` atualizado com restrições robustas.

- [ ] **2.2 Análise de Caminho Crítico**
  - Identificar e corrigir violações de Setup/Hold.
  - Garantir Slack Positivo.

- [ ] **2.3 Verificação de Throughput**
  - Confirmar throughput > 100 MPixels/s.
