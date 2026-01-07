# Análise da Entropia do Resíduo

**Data:** 07/01/2026
**Sprint:** 0
**Atividade:** 1.3

## 1. Objetivo

Confirmar a eficiência do preditor **DPCM Fixo (Left Neighbor)** analisando a entropia dos resíduos gerados. Uma baixa entropia no sinal residual indica que a maior parte da redundância espacial foi removida, deixando para o codificador entrópico (LZW) apenas a tarefa de codificar a "novidade" (erro de predição).

## 2. Metodologia

A entropia de Shannon ($H$) foi calculada para os resíduos de cada um dos 500 frames do dataset FLIR, utilizando a fórmula:

$$ H(X) = - \sum_{i} P(x_i) \log_2 P(x_i) $$

Onde $P(x_i)$ é a probabilidade de ocorrência do valor residual $x_i$.

## 3. Resultados

| Métrica | Valor Original (Estimado) | Valor Residual (DPCM Fixo) | Redução |
| :--- | :--- | :--- | :--- |
| **Bit Depth** | 16 bits | ~5.13 bits (Entropia) | **~68%** |
| **Entropia Média** | N/A (Alta) | **5.1260 bits/pixel** | - |

## 4. Análise

O valor de **5.126 bits/pixel** é significativamente menor que a profundidade original de 16 bits. Isso demonstra que:

1. **Alta Correlação Espacial:** Os pixels vizinhos nas imagens térmicas LWIR possuem valores muito próximos, o que faz com que a diferença (resíduo) seja pequena (próxima de zero).
2. **Distribuição Laplaciana:** A distribuição dos resíduos tende a ser fortemente concentrada em torno de zero (formato Laplaciano/Gaussiano generalizado), o que é ideal para compressores baseados em dicionário ou Huffman.
3. **Eficiência do Preditor:** O preditor simples $P_{i,j} = P_{i,j-1}$ foi capaz de remover a maior parte da informação redundante.

## 5. Conclusão

A entropia residual de ~5.1 bits valida a escolha do DPCM Fixo. O fluxo de dados que chegará ao codificador LZW possui baixa entropia, permitindo que o LZW atinja altas taxas de compressão ao mapear sequências repetitivas de resíduos (que agora são frequentes) em códigos curtos.

O requisito de eficiência do preditor foi **atendido**.
