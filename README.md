# Active Directory API

API desenvolvida em Python, através do framework [FastAPI](https://fastapi.tiangolo.com/) e da biblioteca [pyad](https://pypi.org/project/pyad/), para realização de ações no Active Directory.

A ideia de desenvolver esta API veio do projeto [Active Directory Explorer](https://github.com/vpess/Active-Directory-Explorer), visando proporcionar a execução de mais ações no Active Directory, e com maior praticidade.

**‼️ OBSERVAÇÃO**: A API funciona apenas no ambiente Windows, pois a biblioteca pyad funciona apenas neste ambiente. Pretendo fazer futuramente uma API que funcione nos demais ambientes, consequentemente, usando outra biblioteca.

## 💡 Orientações

As dependências do projeto estão especificadas no arquivo `requirements.txt`. Para instalar todas as dependências do projeto, execute o comando:

```py
pip install -r .\requirements.txt
```

Para executar o projeto, execute:

```py
uvicorn main:app --reload
```

## 📃 Documentação

O framework FastAPI cria automaticamente a documentação no Swagger e no Redoc. A documentação do Swagger fica em `/docs`, e a do Redoc fica em `/redoc`.

## 🗂️ Pastas do Projeto

| **Nome** | **Escopo** |
| ------ | ------ |
| _app_ | Especificações da API, além de exceções de erro e modelos de resposta |
| _controllers_ | Ações realizadas no Active Directory |
| _models_ | Criação de conexão com o Active Directory |
