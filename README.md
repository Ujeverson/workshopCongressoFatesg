# Prompts de sala de aula
## 1. Zero-shot

    Classifique o texto, a seguir, em passado, presente ou futuro.
    
    Texto: Ele foi ao médico.
    
    Resposta:

## 1.2 Zero-shot

    Pessoa 1: Às vezes, parece que a vida é um grande quebra-cabeça, não é?
    Pessoa 2: É verdade. E o curioso é que, mesmo que faltem peças, a gente tenta montar algo que faça sentido.
    Pessoa 1: 

## Few-Shot

    Palavra: Baú
    Letras: 3 letras
    Letras: B-A-Ú

    Palavra: Chinelo
    Letras: 7 letras
    Letras: C-H-I-N-E-L-O

    Palavra: Paralelepípedo



## 📘 Descrição Geral do Projeto: "Calculadora Simples com IA Generativa"

Objetivo:

Construir uma calculadora interativa em Python, capaz de realizar operações matemáticas básicas via terminal. O projeto será guiado com o uso de IAs generativas para automatizar etapas como criação de funções, testes e documentação.

 ## 🧮Funcionalidades da Calculadora
O projeto deve incluir funções para:

| Função        | Operação                         | Entrada Esperada          | Exemplo             |
| ------------- | -------------------------------- | ------------------------- | ------------------- |
| `somar`       | Soma de dois números             | `a`, `b` (floats ou ints) | `somar(5, 3) → 8`   |
| `subtrair`    | Subtração de dois números        | `a`, `b`                  | `subtrair(10, 7)`   |
| `multiplicar` | Multiplicação de dois números    | `a`, `b`                  | `multiplicar(4, 2)` |
| `dividir`     | Divisão (com tratamento de zero) | `a`, `b`                  | `dividir(8, 0)`     |
| `potencia`    | Potência                         | `base`, `expoente`        | `potencia(2, 3)`    |
| `raiz`        | Raiz quadrada (básica)           | `a`                       | `raiz(25)`          |

 ## 📁Estrutura de Diretórios

            calculadora/
            ├── main.py                 # Interface no terminal
            ├── operacoes.py           # Módulo com todas as funções matemáticas
            ├── testes/
            │   └── test_operacoes.py  # Testes unitários com pytest
            ├── utils.py               # Funções auxiliares (ex: entrada de usuário segura)
            ├── README.md              # Documentação do projeto
            └── requirements.txt       # Dependências (opcional: pytest)

## 💡 Extras Possíveis (se houver tempo ou como bônus):
Menu interativo em loop com input() do usuário

# Processo
## 1. Criação da Estrutura do Projeto (10 min)
### 📌 Ferramentas sugeridas: Windsurf ou ChatGPT

Prompt para IA:

            "Crie a estrutura de arquivos para uma calculadora simples em Python com as operações: soma, subtração, multiplicação, divisão, potência e raiz quadrada."

Resultado Esperado:

            calculadora/
            ├── main.py
            ├── operacoes.py
            ├── utils.py
            ├── testes/
            │   └── test_operacoes.py
            └── README.md


## 2. Implementação das Funções

## 3. Construção do Menu de Interface no Terminal (10 min)
### 📌 IDE: Cursor/Windsurf + LLM

### Prompt:

    "Crie um menu interativo em Python para uma calculadora no terminal com opções para cada operação matemática e uma opção para sair."

## 4. Documentação com IA

### 📌 Ferramenta: LLM

### Prompt:

    "Escreva um README.md para uma calculadora de terminal em Python com instruções de uso e exemplos."

### Conteúdo esperado:

* Como executar

* Exemplo de uso

* Créditos ou nome do aluno
