# SPRINT DIA 3 (CONCLUIDO)



Excelente — a consolidação do **Sprint 1 / Dia 3** ficou metodologicamente consistente e totalmente alinhada à lógica de separação entre **requisitos (DRS)** e **decisões de design (DTR)**. Abaixo está a estrutura final revisada e padronizada em \LaTeX, seguindo o mesmo padrão de formatação e hierarquia já adotado nos dias anteriores do sprint.

---

## ✅ **SPRINT 1 / DIA 3 — CONSOLIDAÇÃO ESTRUTURADA EM \LaTeX**

### **1. Avaliação e Alocação de Documentos**

| Conteúdo                                       | Documento Recomendado | Justificativa                                                                                          |
| ---------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------ |
| **RFN-4 — Latência Máxima**                    | **DRS**               | Requisito não funcional de tempo real que define limite de latência tolerável \cite{256, 76}.          |
| **RFN-5 — Orçamento de Recursos**              | **DRS**               | Define restrições de utilização de BRAM, LUTs e FFs, a serem validadas após escolha do FPGA alvo.      |
| **Design LZW — Hash Table com BRAM Dual Port** | **DTR**               | Representa decisão técnica sobre implementação do dicionário e arquitetura paralela \cite{11, 14}.     |
| **Pontos Abertos — Detalhes LZW**              | **DTR**               | Itens de otimização e parametrização de hardware a definir na fase de design detalhado \cite{19, 263}. |

---

### **2. Entregável do Dia 3 — Draft DRS v0.1**

```latex
\section{REQUISITOS DE DESEMPENHO E ARQUITETURA (DRS V0.1)}
\label{sec:requisitos_desempenho}

\subsection{RFN-4 — Requisitos de Latência e Tempo}
\label{req:latencia}
A arquitetura deve assegurar o processamento contínuo dos dados de imagem \gls{TIR} de 16 bits, minimizando a latência de ponta a ponta para suportar aplicações em tempo real.

\subsubsection*{RFN-4.1 — Latência de Processamento}
A latência de processamento (\textit{throughput latency}) do sistema de compressão em \gls{FPGA} — desde a entrada \gls{AXI4-Stream} até o primeiro bit compactado — deve permanecer mínima.

\begin{itemize}
    \item \textbf{Meta Técnica:} Latência \< 1 ms por frame \cite{256}.
    \item \textbf{Abordagem:} Arquitetura \textit{fully pipelined} operando entre 163,35 MHz e 250 MHz \cite{14, 22, 76}.
\end{itemize}

\subsection{RFN-5 — Orçamento de Recursos e Utilização de Hardware}
\label{req:recursos}
O design deve empregar eficientemente os recursos lógicos e de memória do \gls{FPGA}, permitindo instâncias paralelas suficientes para garantir o \textit{throughput} mínimo de $37\,\text{MB/s}$ (RFN-1.1).

\begin{itemize}
    \item \textbf{Ponto Aberto:} Definição do orçamento máximo de LUTs, FFs, \gls{BRAMs} e \gls{DSPs} após escolha do dispositivo.
    \item \textbf{Observação:} Implementações LZW eficientes utilizam \gls{BRAMs} para o dicionário, com exemplos de uso de 18 \gls{BRAMs} de 18 kbit e 346 \gls{LUTs} por instância \cite{22}.
\end{itemize}

\subsection{RF-2 — Algoritmo de Compressão LZW (Requisito de Design)}
O codificador deve seguir a arquitetura \gls{LZW} otimizada para \gls{FPGA}, explorando paralelismo e uso de memória eficiente \cite{12, 11}.

\begin{itemize}
    \item \textbf{Decisão Técnica:} Implementação em \textbf{\gls{BRAMs} de porta dupla}, permitindo leituras e escritas simultâneas na tabela \textit{hash} em um único ciclo de \textit{clock} \cite{11, 14, 18}.
\end{itemize}
```

---

### **3. Texto Complementar em \LaTeX para DTR (Seção 3.5)**

```latex
\subsection{3.5 Estrutura Detalhada do Acelerador LZW}
\label{sec:estrutura_lzw}

Conforme a decisão técnica do Dia 3, o acelerador baseia-se no algoritmo \gls{LZW}, amplamente reconhecido por sua eficiência em compressão \textit{lossless} \cite{1}.

\subsubsection*{Design LZW Otimizado para FPGA}
O \gls{LZW} é inerentemente sequencial \cite{12, 29, 260}. A arquitetura proposta mitiga essa característica por meio de otimizações de memória e paralelismo em nível de circuito \cite{14}:

\begin{itemize}
    \item \textbf{Dicionário Baseado em Hash:} Estrutura de busca e inserção implementada em \textbf{tabela \textit{hash}}, substituindo listas lineares para redução do tempo de acesso \cite{16}.
    \item \textbf{Uso de BRAMs Dual Port:} Permitem leituras e escritas simultâneas, explorando as duas portas independentes da memória para maximizar o desempenho \cite{11, 14, 18, 43}.
    \item \textbf{Estrutura Pointer-Character:} Utiliza tabelas \textit{pointer-character} e \textit{back-pointer} ($q$), seguindo o Algoritmo 2 (LZW modificado) para eficiência de acesso \cite{17}.
\end{itemize}

\subsubsection*{Pontos Abertos de Implementação LZW}
\begin{itemize}
    \item \textbf{Tamanho do Dicionário:} Fixar em 4096 entradas; definir política de \textit{ClearCode} \cite{42, 263}.
    \item \textbf{Paralelismo em Nível de Circuito:} Avaliar uso de múltiplas instâncias LZW (idênticas) em paralelo, visando aceleração de até $\times 23{,}5$ em \gls{FPGA} Virtex-7 \cite{11, 22, 23}.
    \item \textbf{Função Hash e Conflitos:} Detalhar função $h(j, x)$ e método de mitigação de colisões (p. ex., busca sequencial em \textit{buckets} adjacentes) \cite{19}.
\end{itemize}
```

---

### 🧩 **Resumo de Consolidação**

- **DRS v0.1** agora contém todos os **requisitos de desempenho e de arquitetura** definidos no Sprint 1 (Dia 3).

- **DTR** avança o detalhamento do **núcleo LZW**, com decisões de engenharia e pontos abertos para a fase de design detalhado.

- A estrutura mantém coerência entre as seções de requisitos (o “o quê”) e as seções técnicas (o “como”).

Deseja que eu siga para o **Sprint 1 / Dia 4**, com a mesma sistemática (avaliação, alocação e blocos \LaTeX para DRS e DTR)?
