🛠️ Mini-Projeto: Sistema de Cadastro de Peças com FastAPI + IA Generativa (sem banco de dados)
🔍 Descrição:
Vamos construir um sistema simples de cadastro e gerenciamento de peças utilizando Python com FastAPI, armazenando os dados em um arquivo .txt local (formato JSON por linha). O projeto será guiado com o auxílio de LLMs como ChatGPT, Copilot, Gemini e IDEs inteligentes como Cursor, Windsurf e VSCode.
    cadastro_pecas/
    ├── app/
    │   ├── main.py               # Ponto de entrada da API
    │   ├── models.py             # Definição da classe Peca com Pydantic
    │   ├── storage.py            # Funções de leitura/gravação no .txt
    │   └── utils.py              # Funções auxiliares (ex: validação, formatação)
    ├── data/
    │   └── pecas.txt             # Arquivo de armazenamento das peças (JSON por linha)
    ├── tests/
    │   └── test_api.py           # Testes básicos da API
    ├── README.md                 # Documentação do projeto
    └── requirements.txt          # Dependências (FastAPI, Uvicorn, etc.)

