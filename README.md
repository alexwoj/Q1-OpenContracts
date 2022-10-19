# Open Contracts

O projeto **Open Contracts** implementa classes e métodos para gerar uma lista com os maiores devedores que ainda 
não possuem débitos renegociados com a instituição.

# Instalação

O projeto encontra-se disponível em repositório privado no Github. É necessário solicitar acesso ao proprietário 
do repositório.

**Instruções para instalação:**

- Clonar o repositório
    
   `git clone https://github.com/alexwoj/Q1-OpenContracts`

- Criar um ambiente virtual no diretório base do projeto:

    `python3 -m venv venv`

 - Ativar o ambiente virtual:
 
    `source venv/bin/activate`    
    
 - Instalar os pacotes necessários
 
    `pip install -r requirements.txt`
  
  
  # Modo de Uso
  
  Disponibilizamos o arquivo _example.py_ com um caso de uso hipotético.
  
  Devemos chamar o método  _get_top_N_open_contracts_ da classe _Contracts_ passando os seguintes parâmetros:
  
  - open_contracts: uma lista em que cada elemento é uma instância de _Contract_ 
  
  - renegotiated_contracts: Uma lista de inteiros representando o ID dos asssociados que já renegociaram seus contratos.
  
  - top_n: Um inteiro com a quantidade de devedores que deve ser retornado pelo método.
  
  O método irá retornar uma lista contento os _top_n_ inteiros representando o ID do associado, ordenado do maior para
  o menor de acordo com o valor em aberto com a instituição.
  
  
  # Testes
  
  O projeto utiliza a biblioteca de testes Unittest do Pyhon. Para rodar os testes, execute o seguinte comando:
      
  `python3 -m unittest discover -v -s . -p "*test*.py"`
  
 