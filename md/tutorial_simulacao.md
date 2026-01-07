# Tutorial: Simulação Funcional (ModelSim & Icarus Verilog)

Este guia descreve como executar a simulação do testbench `tb_LWIR_Lossless_Compression.v` para validar o funcionamento do hardware.

## Pré-requisitos

* **Arquivos HDL:** `DPCM_Predictor.v`, `RLE_Encoder.v`, `LWIR_Lossless_Compression.v` (em `hw/hdl/`).
* **Testbench:** `tb_LWIR_Lossless_Compression.v` (em `hw/sim/`).
* **Vetor de Teste:** `input.hex` (gerado em `hw/sim/` pelo script Python).

---

## Opção A: Usando Icarus Verilog (Open Source)

O Icarus Verilog é uma ferramenta leve e de linha de comando, ideal para verificações rápidas.

### 1. Instalação (Ubuntu)

```bash
sudo apt-get install iverilog
```

### 2. Compilação

Navegue até a pasta de simulação e compile o projeto:

```bash
cd hw/sim
iverilog -o sim_output \
    ../hdl/DPCM_Predictor.v \
    ../hdl/RLE_Encoder.v \
    ../hdl/LWIR_Lossless_Compression.v \
    tb_LWIR_Lossless_Compression.v
```

### 3. Execução

Execute o arquivo compilado:

```bash
vvp sim_output
```

**Resultado Esperado:**
O terminal deve exibir:

```text
Starting Simulation...
Simulation Finished.
```

E um arquivo `output.hex` será criado no diretório atual.

---

## Opção B: Usando ModelSim (Intel/Altera Starter Edition)

O ModelSim oferece uma interface gráfica poderosa para visualização de formas de onda.

### 1. Criar Projeto

1. Abra o ModelSim.
2. **File > New > Project...**
3. Nome: `LWIR_Sim`. Local: `.../hw/sim`.
4. Clique em **OK**.

### 2. Adicionar Arquivos

1. Clique com o botão direito na janela "Project".
2. **Add to Project > Existing File...**
3. Adicione os arquivos `.v` de `hw/hdl/` e o testbench de `hw/sim/`.

### 3. Compilar

1. **Compile > Compile All**.
2. Verifique se não há erros (check verde).

### 4. Simular

1. **Simulate > Start Simulation...**
2. Expanda a biblioteca `work` e selecione `tb_LWIR_Lossless_Compression`.
3. Clique em **OK**.

### 5. Executar

1. No console (Transcript), digite:

    ```tcl
    run -all
    ```

2. A simulação deve rodar até encontrar o comando `$finish`.
3. Verifique se o arquivo `output.hex` foi gerado na pasta do projeto.

---

## Verificação dos Resultados

Após gerar o `output.hex`, você deve compará-lo com o resultado esperado (gerado pelo modelo Python).

* O arquivo `output.hex` contém os dados de saída do pipeline (formato RLE/Stream).
* Use o script de validação (a ser criado) para confirmar se a compressão foi *lossless* (revertendo o processo ou comparando com a saída do modelo de referência).
