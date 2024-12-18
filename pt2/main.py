import requests 
import pandas as pd 
import os 
import re


base_url='https://swapi.py4e.com/api/' # url base da api, presente na documentação 
endpoints=['planets','films','people'] # lista que contem os endpoints que será utilizada em uma iteração para percorrer por elas

# biblioteca os que realiza a criação de diretorios e verificar a sua existencia 
os.makedirs('./raw', exist_ok=True) 
os.makedirs('./work', exist_ok=True) 

def tratando_dados(s):
    """
    Esta função tem como finalidade realizar a limpeza dos dados presentes no dataframe

    a variavel "s" presente no parametro, está responsável por percorrer todos os elementos do arquivo 
    e após validação dentro da condicional if, transformar tudo em letra minúscula e após, 
    utilizando regular expressions (expressões regulares)
    fazer a substituição de todos os caracteres especiais, por strings vazias.
    """
    if isinstance(s, str):
        s = s.lower()
        s = re.sub(r'[^a-z0-9\s]', '', s) 
    return s

def ingestao_dados():
    """
    Esta é a função principal, que tem como finalidade realizar todo processo da ingestão dados, 
    desde a requisição para acessar a API até a iteração dos endpoints e as páginas, além do mais, 
    transformando os dados coletados em DataFrames no pandas e transferindo e transformando em 
    arquivo .csv e designando para as pastas criadas no começo do código caso o dado esteja tratado ou não
    """
    for endpoint in endpoints: # estrutura para iterar sobre os endpoints
        dados_coletados=[] # lista que armazena os dicionarios coletados da api

        for pagina in range(1,6): # estrutura de somatorio para que o endpoint possa ser complementado com o numero da pagina
            complete_url=f'{base_url}{endpoint}/{pagina}' # realiza a criação completa do endpoint

            r = requests.get(complete_url) # 

            # estrutura condicional para verificar se o retorno da api está com status 200 (solicitação bem sucedida)
            if r.status_code==200:
                print(f'Coletando dados da seção {endpoint} página {pagina}')
                dados=r.json() # variavel para transformar o conteudo que está em .json em um objeto python
                dados_coletados.append(dados) # metodo de lista utilizado para armazenar os dados coletados na lista
                
            else:
                # indicador de erro caso a requisição seja diferente de 200 
                raise ValueError(f'Dados não coletados na seção {endpoint} pagina {pagina}') 

        
        df_raw = pd.DataFrame(dados_coletados) # com pandas, transforma a lista em um dataframe
        df_raw.to_csv(f'./raw/{endpoint}.csv', index=False) # exporta os dados que estao no dataframe para um csv
        print(f'Dados brutos do endpoint {endpoint} salvos na pasta raw') # informa que os dados foram salvos na pasta correta 
                
        df_work = df_raw.map(tratando_dados)
        df_work.to_csv(f'./work/{endpoint}.csv', index=False)
        print(f'Dados já processados e tratados do endpoint {endpoint} salvos na pasta work')

# invocando a função 
ingestao_dados()



