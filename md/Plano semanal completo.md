# Plano semanal completo (16 semanas, 4 meses)** para o **Desafio 2 — Compressão sem perdas para imagens térmicas**, considerando:

- 4h/dia × 5 dias/semana → **20 horas semanais**

- Total de **320 horas úteis**

- Divisão equilibrada entre **pesquisa**, **prototipagem orientada a objetos (Python)**, **implementação em FPGA (Verilog)** e **validação final**.

---

# 🧭 PLANO DE EXECUÇÃO SEMANAL (4 MESES – 16 SEMANAS)

---

## 🔹 **Mês 1 — Fase de Pesquisa, Modelagem e Prototipagem (80h)**

| Semana | Objetivo principal                                     | Atividades (POO + SOLID + Clean Code)                                                                                                                                                                                             | Entregáveis                                      |
| ------ | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| **1**  | Compreensão e requisitos do problema                   | - Estudo dos princípios de compressão sem perdas (RLE, Huffman, LZW) - Análise das características das imagens térmicas (bit depth, dinâmica térmica) - Definição dos requisitos funcionais e de desempenho do core FPGA          | Documento de especificação de requisitos         |
| **2**  | Arquitetura orientada a objetos da compressão          | - Definir classes principais: `ImageLoader`, `Compressor`, `Decompressor`, `MetricsEvaluator` - Criar interfaces e abstrações (interface de compressor genérico) - Aplicar SRP e OCP (responsabilidade única e abertura/extensão) | Diagrama UML e estrutura de pacotes Python       |
| **3**  | Implementar protótipo RLE modular                      | - Implementar `RLECompressor` e `RLEDecompressor` - Escrever testes unitários com `pytest` - Garantir cobertura de código e clareza seguindo Clean Code                                                                           | Protótipo funcional RLE com testes automatizados |
| **4**  | Implementar compressão Huffman (opcional) + integração | - Implementar `HuffmanEncoder` / `HuffmanDecoder` - Integrar em `CompressorFactory` para seleção dinâmica de algoritmo - Avaliar taxa de compressão e tempo de execução                                                           | Protótipo híbrido RLE+Huffman validado           |

---

## 🔹 **Mês 2 — Arquitetura FPGA e Implementação Inicial (80h)**

| Semana | Objetivo principal                            | Atividades                                                                                                                                                                  | Entregáveis                                   |
| ------ | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **5**  | Definição da arquitetura em FPGA              | - Transpor a estrutura POO para blocos Verilog modulares (cada classe → módulo HDL) - Criar diagrama de blocos HDL (Entrada, RLE Encoder, Huffman Encoder, Controle, Saída) | Arquitetura HDL e especificação de interfaces |
| **6**  | Módulo de leitura e controle de fluxo         | - Implementar `input_interface.v` (leitura sequencial de pixels) - FSM de controle de entrada - Simulação de leitura de imagem (vetor `.mem` ou `.txt`)                     | Bloco de entrada validado em simulação        |
| **7**  | Implementação do **RLE Encoder (Verilog)**    | - FSM de detecção de repetições - Armazenamento de pares `(valor, contagem)` - Verificação de overflow e flush                                                              | `rle_encoder.v` testado unitariamente         |
| **8**  | Integração parcial e testbench Python↔Verilog | - Conectar blocos de entrada e RLE - Simular fluxo de compressão via ModelSim e comparar com saída Python                                                                   | Simulação integrada e validação funcional     |

---

## 🔹 **Mês 3 — Implementação Completa, Decodificação e Testes (80h)**

| Semana | Objetivo principal                            | Atividades                                                                                                                        | Entregáveis                             |
| ------ | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **9**  | Implementação do **Decoder (RLE e Huffman)**  | - Criar `rle_decoder.v` e `huffman_decoder.v` - FSM inversa para reconstrução de dados - Testbench para verificar reversibilidade | Módulo decoder funcional                |
| **10** | Simulação completa Compressão → Descompressão | - Geração automática de vetores de teste com Python - Simulação fim-a-fim e comparação binária (bitwise)                          | Pipeline completo validado em simulação |
| **11** | Otimização de pipeline e buffers              | - Inserção de registros pipeline para clock > 50 MHz - Análise de temporização (timing analysis) - Ajuste de FSM principal        | Core otimizado e estável                |
| **12** | Avaliação de desempenho e uso de recursos     | - Síntese em FPGA (Vivado/Quartus) - Relatório de LUTs, FFs, uso de memória - Benchmark comparativo com modelo Python             | Relatório técnico de desempenho         |

---

## 🔹 **Mês 4 — Integração, Validação Real e Documentação (80h)**

| Semana | Objetivo principal                             | Atividades                                                                                                                                           | Entregáveis                             |
| ------ | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **13** | Integração no kit FPGA                         | - Implementar interface de comunicação (UART, AXI ou SPI) - Gerar bitstream e carregar no kit                                                        | Sistema FPGA programado                 |
| **14** | Montagem do setup de teste (com Invent Vision) | - Configuração do ambiente físico - Envio/recebimento de imagens reais - Coleta de resultados e logs                                                 | Setup validado                          |
| **15** | Testes de validação e comparação real          | - Compressão e descompressão de imagens térmicas reais - Comparar desempenho com software Python                                                     | Relatório de validação experimental     |
| **16** | Documentação final e apresentação              | - Documentar arquitetura HDL + modelo Python - Explicar design patterns aplicados (Strategy, Factory, etc.) - Relatório técnico e apresentação final | Documentação e entrega final do projeto |

---

## 🧱 **Estrutura de diretórios sugerida**

```
fpga_compression_project/
├── docs/
│   ├── requisitos.md
│   ├── arquitetura_fpga.pdf
│   └── relatorio_final.pdf
├── python_model/
│   ├── core/
│   │   ├── compressor_base.py
│   │   ├── rle_compressor.py
│   │   ├── huffman_compressor.py
│   │   └── decompressor.py
│   ├── utils/
│   │   ├── image_loader.py
│   │   └── metrics.py
│   ├── tests/
│   │   ├── test_rle.py
│   │   └── test_huffman.py
│   └── main.py
├── verilog_core/
│   ├── input_interface.v
│   ├── rle_encoder.v
│   ├── rle_decoder.v
│   ├── top_module.v
│   ├── tb_top.v
│   └── defines.vh
└── simulations/
    ├── test_vectors/
    └── results/
```

---

## 🧩 **Boas práticas de POO e Clean Code aplicadas à prototipagem Python**

| Princípio                                 | Aplicação prática                                                                                 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **SRP (Single Responsibility Principle)** | Cada classe faz uma única função clara (por exemplo, `Compressor` apenas comprime).               |
| **OCP (Open-Closed Principle)**           | Adicionar novos algoritmos de compressão sem alterar os existentes (uso de herança/polimorfismo). |
| **LSP (Liskov Substitution)**             | Todos os compressores respeitam a mesma interface (`compress`, `decompress`).                     |
| **ISP (Interface Segregation)**           | Interfaces enxutas e específicas para cada tipo de componente.                                    |
| **DIP (Dependency Inversion)**            | Uso de `CompressorFactory` e injeção de dependência.                                              |
| **Clean Code**                            | Nomes descritivos, funções curtas, testes unitários, tipagem com hints (`typing`), docstrings.    |

---

## ⚙️ **Métricas de acompanhamento**

| Tipo                                  | Indicador                          | Meta |
| ------------------------------------- | ---------------------------------- | ---- |
| **Produtividade semanal**             | ≥ 18h/20h efetivamente registradas | ✅    |
| **Cobertura de testes Python**        | ≥ 90%                              | ✅    |
| **Validação bit a bit FPGA ↔ Python** | 100% de equivalência               | ✅    |
| **Clock FPGA estável**                | ≥ 50 MHz                           | ✅    |
| **Documentação atualizada**           | Revisão semanal                    | ✅    |

---
