# CP5-DynamicProgramming
# Desafio: Troca de Moedas — Checkpoint 05

**Integrantes:**
* Athos Rodrigues Alves
* Luiz Felipe Coelho Ramos
* Gabriel Escobosa Vallejo

## 1. Introdução e Contextualização

**Problema:** Dado um conjunto de moedas (valores inteiros positivos, quantidade ilimitada) e um montante `M`, determinar a **menor quantidade de moedas** cuja soma seja exatamente `M`.

* **Objetivo:** Minimizar o número de moedas usadas.
* **Premissas:** Moedas ilimitadas; valores inteiros positivos; se não for possível formar `M`, a função retorna `-1`.
* **Natureza:** Problema de otimização combinatória — buscar a melhor solução entre muitas combinações possíveis.

## 2. Programação Dinâmica (PD) — Conceito Rápido

**PD** é uma técnica que resolve problemas decompondo-os em subproblemas menores e reutilizando soluções de subproblemas sobrepostos.

* **Subestrutura ótima:** A solução ótima para `M` pode ser construída a partir das soluções ótimas para valores menores.
* **Subproblemas sobrepostos:** Vários caminhos da recursão resolvem os mesmos subproblemas; memoização/DP evita recomputações.

## 3. Abordagens Implementadas

As quatro funções estão no arquivo `main.py`:

#### `qtdeMoedas(M, moedas)` — Gulosa (iterativa)
* **Conceito:** Escolhe sempre a maior moeda possível.
* **Limitação:** Não garante solução ótima para todas as moedas (ex.: `M=6`, `moedas=[1,3,4]` => gulosa dá 3, ótimo é 2).
* **Complexidade:** O(n log n) pelo sort, depois O(n) na passagem.

#### `qtdeMoedasRec(M, moedas)` — Recursiva pura
* **Conceito:** Tenta todas as combinações recursivamente.
* **Performance:** Árvore de recursão com muitos reprocessamentos; tempo exponencial.
* **Complexidade:** Exponencial no pior caso.

#### `qtdeMoedasRecMemo(M, moedas)` — Recursiva com memoização (Top-Down)
* **Conceito:** Mesma recursão, mas armazena resultados em `memo` para evitar recalcular.
* **Ligação com PD:** É PD Top-Down (memoização).
* **Complexidade:** O(M * n) tempo, O(M) espaço.

#### `qtdeMoedasPD(M, moedas)` — Programação Dinâmica (Bottom-Up)
* **Conceito:** Constrói vetor `dp[0..M]` com `dp[i]` = mínimo de moedas para `i`.
* **Fluxo:** Para cada `i` calcula `dp[i]` a partir de `dp[i - moeda]`.
* **Vantagem:** Evita overhead de chamadas recursivas; também O(M * n) tempo.
* **Resultado:** Esta é a solução ótima e eficiente.

## 4. Demonstração / Exemplos

Exemplo simples usado no código:
```python
M = 6
moedas = [1, 3, 4]

# Gulosa -> 3 (4+1+1) [não ótima]
print(f"Gulosa: {qtdeMoedas(M, moedas)}")

# Recursiva Pura -> 2 (3+3) [ótima, mas lenta]
print(f"Recursiva Pura: {qtdeMoedasRec(M, moedas)}")

# Recursiva com Memoização (PD Top-Down) -> 2 [ótima]
print(f"Memoization (Top-Down): {qtdeMoedasRecMemo(M, moedas)}")

# Programação Dinâmica (PD Bottom-Up) -> 2 [ótima]
print(f"PD (Bottom-Up): {qtdeMoedasPD(M, moedas)}")
