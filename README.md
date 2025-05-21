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

