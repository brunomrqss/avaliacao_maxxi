## Part 2 - Ingestão de dados

Realização da parte 2 do desafio

1. Iniciei criando a pasta pt2 dentro do repositório 
2. Após, criei um ambiente virtual .venv para que eu pudesse segregar as libs das outras bibliotecas globais presentes no meu pc
```python
python -m venv .venv
```

inicializei o ambiente virtual com:
```bash
source .venv/bin/activate
```

3. criei o arquivo .gitignore para colocar dentro dele o .venv para não subi-lo ao repositorio 
4. dentro do .venv instalei as dependencias ``requests`` e ``pandas``
5. criei o arquivo requirements.txt com as dependencias que estavam instaladas, utilizei:
```python
pip freeze >> requirements.txt
```
6. criei meu arquivo main.py para começar o projeto e testar a primeira requisição da api, para ver o que era retornado 
```python
import requests
import pandas as pd

url = "https://swapi.dev/api/people/"

response = requests.get(url)
print(response) # Saída <Response [404]>
```

Verifiquei que não estava conseguindo realizar as requisições da API do desafio, tentei entrar na URL e na documentação e todas me deram retorno 404 not found. Até que depois de algumas horas, consegui verificar que a URL mudou e agora é: https://swapi.bry.com.br/documentation#start e para solicitar a requisição da API, precisaria mudar para ``url = "https://swapi.co/api/people/"``

Obtive o response <200>

