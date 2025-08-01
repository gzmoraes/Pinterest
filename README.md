# FakePinterest

Este projeto é uma aplicação web inspirada no Pinterest, desenvolvida com o objetivo de aprendizado em Flask.

## Funcionalidades

- Cadastro de usuários com autenticação segura
- Login e logout de usuários
- Upload de fotos para o perfil do usuário
- Visualização de um feed com todas as fotos postadas
- Perfis individuais com galeria de fotos

## Tecnologias Utilizadas

- Python 3
- Flask
- Flask-WTF
- Flask-Login
- Flask-Bcrypt
- Flask-SQLAlchemy
- SQLite

## Estrutura do Projeto

```
fake_pinterest/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   └── templates/
│
├── instance/
│   └── banco.db
│
│
├── venv/
│
├── .gitignore
├── requirements.txt
└── main.py
```


## Como executar

1. Clone o repositório:
   ```
   git clone https://github.com/gzmoraes/fakepinterest.git
   cd fakepinterest
   

2. Crie um ambiente virtual
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows´
```
4. Instale as dependências
```
pip install -r requirements.txt
```
6. Execute a aplicação:
```
python main.py
```
8. Acesse no navegador:
```
http://127.0.0.1:5000//
```

Licença
Este projeto está licenciado sob a Licença Apache 2.0. Veja o arquivo LICENSE para mais detalhes.
