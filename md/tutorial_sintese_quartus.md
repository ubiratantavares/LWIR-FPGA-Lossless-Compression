# Tutorial: Executando a Síntese no Quartus II 13.1

Este guia descreve como abrir o projeto criado e realizar a síntese lógica para validar o código Verilog e obter o relatório de uso de recursos.

## 1. Abrindo o Projeto

1. Inicie o Quartus II:

    ```bash
    quartus
    ```

2. No menu principal, vá em **File > Open Project...**
3. Navegue até a pasta do projeto:
    `.../LWIR-FPGA-Lossless-Compression/hw/quartus/`
4. Selecione o arquivo **`LWIR_Lossless_Compression.qpf`** e clique em **Open**.

## 2. Adicionando o Código Verilog ao Projeto

O projeto base foi criado, mas precisamos garantir que o arquivo Verilog do preditor esteja incluído como o *Top-Level* ou parte dele.

1. No menu, vá em **Project > Add/Remove Files in Project...**
2. Clique no botão **...** (browse) e navegue até `../hdl/`.
3. Selecione **`DPCM_Predictor.v`**.
4. Clique em **Add** e depois em **OK**.

### 2.1 Definindo o Top-Level Entity

Como queremos sintetizar apenas o Preditor agora (para validar a atividade 3.3):

1. Vá em **Project > Set as Top-Level Entity...** (ou pressione `Ctrl+Shift+J` para abrir o Project Navigator, clique com o botão direito no arquivo `DPCM_Predictor.v` e selecione **Set as Top-Level Entity**).
2. Alternativamente, vá em **Assignments > Settings > General** e em "Top-level entity name", digite: `DPCM_Predictor`.

## 3. Executando a Síntese (Analysis & Synthesis)

1. Localize a janela **Tasks** (geralmente à esquerda).
2. Dê um duplo clique em **Analysis & Synthesis**.
    * *Atalho:* Pressione o botão "Play" azul na barra de ferramentas (Start Compilation) para rodar o fluxo completo, ou apenas o ícone com um "check" sobre um papel para rodar apenas a síntese.
3. Aguarde o processo terminar. A janela de mensagens inferior mostrará o progresso.
    * Se houver erros (texto vermelho), revise o código Verilog.
    * Avisos (Warnings) sobre "pins not driven" são normais nesta etapa, pois não atribuímos pinos físicos ainda.

## 4. Analisando o Relatório de Recursos

Após a síntese ser concluída com sucesso (ícone verde):

1. Vá para a janela **Compilation Report**.
2. Navegue para **Analysis & Synthesis > Summary**.
3. Verifique os seguintes campos:
    * **Total logic elements:** Quantidade de LEs usados (esperado: < 50 para este módulo).
    * **Total registers:** Quantidade de Flip-Flops.
    * **Total memory bits:** Uso de BRAM (deve ser 0 por enquanto).
    * **Embedded Multiplier 9-bit elements:** Uso de DSPs (deve ser 0).

## 5. Verificando o Timing (Opcional nesta fase)

Para uma análise preliminar de frequência máxima ($F_{MAX}$):

1. Na janela **Tasks**, execute **TimeQuest Timing Analysis**.
2. Abra o relatório gerado (TimeQuest Timing Analyzer).
3. Verifique a seção **Slow 1200mV 85C Model > Fmax Summary**.
    * O valor deve ser bem superior a 100 MHz para este bloco simples.

---
**Próximos Passos:** Se a síntese passar e o uso de recursos for baixo, a Atividade 3.3 pode ser marcada como concluída.
