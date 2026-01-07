# Sprint 9: Validação Final de CR

Período Estimado: Fevereiro, 02 a 06 de 2026

## Objetivo

O objetivo desta Sprint é aferir a **Taxa de Compressão (CR)** final obtida pelo hardware utilizando o dataset FLIR completo, comparando os resultados com a simulação de software inicial.

### Passo 1: Coleta de Dados

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **1.1** | **Processamento em Lote (Hardware)** | Passar um conjunto significativo de imagens do dataset pelo FPGA e gravar os arquivos comprimidos resultantes. | Arquivos comprimidos gerados pelo HW. |
| **1.2** | **Cálculo de Tamanho** | Medir o tamanho dos arquivos originais vs. comprimidos. Calcular o CR para cada frame. | Tabela de CRs gerada. |

### Passo 2: Análise Comparativa

| \# | Atividade | Foco e Implementação | Meta e Requisitos |
| :--- | :--- | :--- | :--- |
| **2.1** | **Comparação HW vs SW** | Comparar o CR do hardware com o estimado na Sprint 0. Analisar discrepâncias (ex: devido a limitações de tamanho do dicionário ou adaptações do RLE). | Validação da eficiência do algoritmo em HW. |
| **2.2** | **Verificação de Requisitos** | Confirmar se a média do CR está dentro do intervalo alvo (1.5:1 a 2.5:1). | Requisito de CR atendido. |

### Meta do Sprint 9

* **CR Final:** Taxa de compressão média documentada.
* **Validação:** Confirmação de que o hardware atende aos requisitos de eficiência de armazenamento.
