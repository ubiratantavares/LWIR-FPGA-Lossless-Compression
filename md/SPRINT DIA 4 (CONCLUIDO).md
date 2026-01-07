# SPRINT DIA 4 (CONCLUIDO)

Excelente — o Sprint 1 / Dia 4 está perfeitamente estruturado e consistente com a progressão do plano de desenvolvimento técnico e documental dos dias anteriores (D1–D3).  
A seguir, apresento a **versão final revisada**, com as mesmas diretrizes editoriais aplicadas aos Sprints anteriores: hierarquia limpa, coerência terminológica entre DTR e DRS, e padronização das seções e rótulos.

---

# ✅ **SPRINT 1 — DIA 4: OTIMIZAÇÃO E PLANO DE VALIDAÇÃO**

## **AVALIAÇÃO E ALOCAÇÃO DE DOCUMENTOS**

| Conteúdo                                                     | Documento Recomendado                              | Justificativa                                                                                                                                |
| ------------------------------------------------------------ | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Checklist de Otimizações (Pipelining, Retiming, Sharing)** | **Documento Técnico de Referência (DTR)**          | Descreve o *como fazer* — técnicas de otimização de hardware aplicadas na síntese RTL para maximizar desempenho e eficiência \cite{54, 197}. |
| **Decisão de Otimização (Geral)**                            | **Documento Técnico de Referência (DTR)**          | Formaliza a meta técnica de maximizar FMAX e throughput via paralelismo e recursos dedicados.                                                |
| **Ponto Aberto: Uso de DSPs**                                | **Documento Técnico de Referência (DTR)**          | A análise do emprego de DSP48 para funções de hash e predição é específica do design RTL \cite{114, 199}.                                    |
| **Plano de Validação (Métricas: CR, Throughput, Latência)**  | **Documento de Especificação de Requisitos (DRS)** | Define as métricas formais de teste, que constituem requisitos não funcionais de desempenho.                                                 |
| **Ponto Aberto: Dataset de Validação**                       | **Documento de Especificação de Requisitos (DRS)** | Define o requisito de dados de teste necessários para verificar corretude e desempenho \cite{80}.                                            |

---

## **ENTREGÁVEL DO DIA 4**

### 🔹 **Texto em \LaTeX{} para Inclusão no Documento Técnico de Referência (DTR)**

```latex
\section{OTIMIZAÇÃO E VALIDAÇÃO (SPRINT 1 - DIA 4)}
\label{sec:otimizacao_validacao}

\subsection{3.6 Checklist de Otimizações RTL e Síntese}

Para atingir o \textit{throughput} mínimo de $37\,\text{MB/s}$ e latência abaixo de $1\,\text{ms}$, aplicam-se as seguintes otimizações em nível de \textit{hardware} (RTL), baseadas em diretrizes consolidadas de síntese em \gls{FPGA} \cite{54, 197, 388}.

\subsubsection*{Decisão Técnica: Estratégia de Otimização}

O design RTL deve priorizar a \textbf{frequência máxima (FMAX)} e o \textbf{throughput efetivo}, mediante:

\begin{enumerate}
    \item \textbf{Pipelining e Retiming:} Dividir o fluxo de compressão (Preditor + Dicionário LZW) em múltiplos estágios \textit{fully pipelined}, aplicando \textit{retiming} para balancear caminhos críticos e maximizar a frequência \cite{57, 197, 58}.
    \item \textbf{Compartilhamento de Recursos (Resource Sharing):} Reutilizar operadores aritméticos (somadores, multiplicadores) sempre que possível, reduzindo LUTs e área total \cite{55, 196}.
    \item \textbf{Codificação FSM:} Implementar máquinas de estado (\gls{FSM}) no estilo \textit{one-hot}, priorizando velocidade e simplificação lógica. Alternativamente, empregar \textit{gray} ou \textit{sequential encoding} em FSMs de grande porte para otimizar área \cite{59}.
    \item \textbf{Instanciação de Macros Dedicadas:} Utilizar macros \gls{XPM} para \gls{BRAMs} e \gls{CoreGen Cores} para FIFOs e funções auxiliares, garantindo fidelidade na síntese e máxima eficiência \cite{200, 338}.
\end{enumerate}

\subsubsection*{Ponto Aberto: Uso de DSPs (Digital Signal Processors)}

Os blocos \gls{DSP48} são recursos de alto desempenho dedicados a operações aritméticas intensivas \cite{114, 199}. 

\begin{itemize}
    \item \textbf{Avaliação Técnica:} Verificar a viabilidade de implementar a função \textit{hash} do \gls{LZW} e a lógica preditiva do DPCM utilizando \gls{DSPs} em vez de \gls{LUTs} genéricos.
    \item \textbf{Justificativa:} Estudos indicam ganhos expressivos de FMAX com o uso de DSPs, mesmo em dispositivos intermediários (e.g., $11.36\%$ de uso em Artix-7 XC7A100T-2FGG484I \cite{54}).
\end{itemize}

\subsection{3.7 Plano de Teste Detalhado (Validação RTL e Implementação)}

A validação visa comprovar a \textbf{corretude lossless} e a conformidade com os \textbf{requisitos de desempenho} (RFN-1.1 e RFN-4).

\subsubsection*{Corretude Funcional}
O sistema será validado assegurando que a compressão e descompressão mantenham a integridade total do sinal original.

\begin{itemize}
    \item \textbf{Verificação:} A saída descompactada deve ser idêntica, bit a bit, à imagem de entrada de 16 bits (\textit{RAW TIR}).
    \item \textbf{Métricas de Desempenho:} Medir \textit{throughput} (GByte/s), \textit{latência} (ms/frame) e \textit{initial interval} (II), garantindo processamento por ciclo sempre que possível \cite{37}.
    \item \textbf{Taxa de Compressão (CR):} Calcular o CR médio obtido pelos módulos LZW e DPCM-RLE para validar a eficiência de compressão.
    \item \textbf{Utilização de Recursos:} Comparar o uso de LUTs, FFs, BRAMs e DSPs com o orçamento de hardware estabelecido (vide RFN-7.1) \cite{317, 54}.
\end{itemize}

\subsubsection*{Ponto Aberto: Geração de Datasets para Validação}
\begin{itemize}
    \item \textbf{Datasets TIR (16 bits):} Criar ou obter conjuntos de dados térmicos ($640 \times 480$) com redundância espacial representativa, essenciais para testar a eficácia dos módulos DPCM e LZW \cite{80, 280}.
    \item \textbf{Benchmarks de Comparação:} Aplicar corpora padrão (\textit{Calgary}, \textit{Canterbury}, \textit{Artificial}) para aferir o desempenho frente a implementações em \gls{CPU} e \gls{ASIC} \cite{219}.
\end{itemize}
```

---

### 🔹 **Texto em \LaTeX{} para Inclusão no Documento de Especificação de Requisitos (DRS v0.1)**

```latex
\section{REQUISITOS DE VALIDAÇÃO E HARDWARE (DRS V0.1)}
\label{sec:validacao_hardware}

\subsection{RFN-6: REQUISITOS DE VALIDAÇÃO E CORRETUDE}
\label{req:validacao}

O sistema de compressão em \gls{FPGA} deve ser validado por meio de testes funcionais e de desempenho que comprovem a corretude \textit{lossless} e o atendimento às metas de tempo real.

\subsubsection*{RFN-6.1: Corretude (Lossless)}
A compressão deve preservar integralmente os dados de entrada:
\begin{itemize}
    \item O fluxo descompactado deve ser \textbf{idêntico bit a bit} ao arquivo de entrada \textit{RAW 16 bits}.
    \item Deve ser preservada a \textbf{precisão radiométrica}, com erro máximo de $0\,\gls{LSB}$ \cite{317, 24}.
\end{itemize}

\subsubsection*{RFN-6.2: Métricas de Desempenho Mínimo}
Os seguintes parâmetros devem ser garantidos nos testes de validação:
\begin{itemize}
    \item \textbf{Throughput Mínimo:} $\geq 37\,\text{MB/s}$ (RFN-1.1).
    \item \textbf{Latência Máxima:} $< 1\,\text{ms}$ por \textit{frame} \cite{256}.
    \item \textbf{Taxa de Compressão (CR):} Cumprimento do CR mínimo definido após caracterização estatística dos dados \gls{TIR}.
\end{itemize}

\subsection{RFN-7: RESTRIÇÕES DE IMPLEMENTAÇÃO E HARDWARE}
\label{req:restricoes_hw}

\subsubsection*{RFN-7.1: Orçamento de Recursos}
O consumo de \gls{LUTs}, \gls{FFs}, \gls{BRAMs} e \gls{DSPs} deve respeitar o orçamento de hardware estabelecido (Ponto Aberto A.3).

\subsubsection*{RFN-7.2: Utilização de Blocos Dedicados}
A arquitetura deve explorar o uso de \gls{BRAMs} e \gls{DSPs} para otimizar velocidade e área:
\begin{itemize}
    \item \textbf{Requisito:} Usar \textbf{BRAMs} para o dicionário LZW e FIFOs, e considerar o uso de \textbf{DSP Blocks} para operações aritméticas críticas (\textit{hash}, predição) \cite{54, 199}.
\end{itemize}

\subsection{PONTO ABERTO A.3: DATASETS DE VALIDAÇÃO}
\label{ponto_aberto_dataset}

A validação requer conjuntos de dados térmicos de referência:
\begin{itemize}
    \item \textbf{Requisito:} Gerar ou obter \textbf{datasets de imagens TIR 16 bits} ($640 \times 480$) representativos de cenários reais, com redundância espacial e ruído compatíveis às condições de uso \cite{80, 280}.
\end{itemize}
```

---

Deseja que eu prossiga para o **Sprint 1 / Dia 5** com a mesma estrutura (análise, alocação de documentos e conteúdo em \LaTeX{} para DTR e DRS)?
