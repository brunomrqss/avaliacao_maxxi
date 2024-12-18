## Desafio Ingestão de Dados 

Este projeto tem como propósito realizar uma ingestão de dados de uma API pública (SWAPI - Star Wars API) que contém dados do filme de Star Wars. 

Ao realizar a requisição serão coletados dados de diferentes endpoints e armazená-los em dois diretórios ``raw`` e ``work``. 

Os dados que serão salvos em ``raw``, serão os dados brutos, dados esses sem nenhum tratamento e na pasta ``work`` estarão salvos os dados tratados, onde foi realizado padronização de string (todos em letra minúscula) e remoção de caracteres especiais. Além disso, todos os dados que salvos, foram transformados em arquivos ``.csv`` ao invés de permanecer em ``.json()``.


### Como executar o projeto:

Verifique a estrutura do diretório, onde deve conter as seguintes pastas e arquivos.py:
- pt2
    - main.py
    - requirements.txt
    - README.md


1. Em seu terminal, realize a instalação das dependências necessárias ``pandas`` e ``requests``. 

**Você pode realizar isto de duas maneiras:**

- Instalando de maneira isolada, em seu terminal digite as seguintes instruções e aperte Enter.
```bash
pip install pandas
```

```bash
pip install requests 
```

ou 

realize a instação do arquivo requirements.txt também em seu terminal, pressionando Enter.

```bash
pip install -r requirements.txt
```

2. Após a instalação das dependências, verifique se ambas estão instaladas executando ainda em terminal:
```bash
pip show pandas 

pip show requests
```

3. Execute o script main.py 
```bash
python main.py
```

### Dificuldades no desafio

- A url fornecida não funcionava, então tive que puxar outra URL da API ``'https://swapi.py4e.com/api/'``
- Um dos maiores desafios que tive foi conseguir realizar uma estrutura em que os dados fossem armazenados na lista e "somassem" ao inves de substituir a cada iteração, mesmo usando uma lógica com o metodo append, ainda assim não foi possível.