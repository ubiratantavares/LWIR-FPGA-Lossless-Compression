# Sprint 6: Setup e Interface

Período Estimado: Janeiro, 12 a 16 de 2026

## Objetivo

O objetivo desta Sprint é preparar o **ambiente físico de teste** e implementar as interfaces de comunicação necessárias para injetar dados na FPGA e coletar os resultados comprimidos.

### Passo 1: Interface de Dados

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **Protocolo de Entrada** | Implementar/Validar a interface de entrada (ex: Avalon-ST, UART rápida ou interface paralela GPIO) para receber os pixels brutos. | Interface de entrada funcional. |
| **1.2** | **Protocolo de Saída** | Implementar a interface de saída para transmitir o *bitstream* comprimido para o PC ou memória externa. | Interface de saída funcional. |

### Passo 2: Montagem do Setup

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **Configuração do Kit FPGA** | Configurar a placa de desenvolvimento (DE2-115 ou similar). Conectar cabos e verificar drivers USB-Blaster. | Hardware pronto para teste. |
| **2.2** | **Software de Host** | Desenvolver ou configurar um software no PC (Python/C) para enviar imagens e receber dados binários da FPGA. | Loopback de dados PC-FPGA-PC funcionando. |

### Meta do Sprint 6

* **Interfaces Operacionais:** Comunicação estável entre PC e FPGA.
* **Setup Pronto:** Ambiente físico montado para os testes de desempenho.
