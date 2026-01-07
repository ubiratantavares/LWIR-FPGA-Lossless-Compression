# Sprint 3: LZW e Mapeamento de Memória

Período Estimado: Dezembro, 22 a 26 de 2025

## Objetivo

O objetivo principal desta Sprint é **implementar o núcleo do algoritmo LZW**, focando no mapeamento eficiente do dicionário para os blocos de memória embarcada (**M9K/M10K**) da FPGA Cyclone, garantindo acesso rápido para leitura e escrita.

### Passo 1: Arquitetura de Memória LZW

Esta atividade define e implementa a estrutura de armazenamento do dicionário LZW.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **Mapeamento M9K/M10K** | Instanciar blocos de memória RAM Dual-Port (usando *MegaWizard* ou inferência HDL) para o dicionário. Configurar portas de Leitura (Lookup) e Escrita (Update) independentes. | Dicionário LZW mapeado em BRAMs (M9K). |
| **1.2** | **Gerenciamento de Endereços** | Implementar a lógica de controle para indexação da tabela Hash (ou CAM simulada). Definir estratégia de resolução de colisões (ex: *Linear Probing* ou *Cuckoo Hashing* simplificado). | Acesso ao dicionário em 1 ciclo (idealmente). |
| **1.3** | **Inicialização do Dicionário** | Criar a máquina de estados (FSM) para inicializar o dicionário com os 256 símbolos base (ou alfabeto do resíduo) no reset. | Dicionário pronto para operação após reset. |

### Passo 2: Lógica de Compressão LZW

Este passo implementa o algoritmo LZW propriamente dito, conectado à memória.

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **FSM de Controle LZW** | Implementar a Máquina de Estados Finitos que controla o fluxo: Ler Prefixo + Char -> Buscar no Dicionário -> (Existe? Atualiza Prefixo : Emite Código + Adiciona Novo). | Lógica de controle LZW funcional. |
| **2.2** | **Integração com DPCM** | Conectar a saída do Preditor DPCM (Sprint 1/2) à entrada do Codificador LZW. Adaptar o RLE (se mantido) ou substituí-lo pelo LZW conforme arquitetura híbrida definida. | Pipeline DPCM -> LZW integrado. |
| **2.3** | **Validação Funcional (Simulação)** | Simular o bloco LZW isoladamente e integrado. Verificar a corretude da emissão de códigos e atualização do dicionário. | LZW validado em simulação (*Lossless*). |

### Meta do Sprint 3

* **Dicionário em Hardware:** Memória M9K instanciada e operante.
* **LZW Funcional:** Algoritmo comprimindo dados corretamente em simulação.
* **Uso de Memória:** Relatório de uso de BRAMs dentro do orçamento do dispositivo.
