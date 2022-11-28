# Scrapy3
Um projeto referente ao um teste de processo seletivo.

## Requirements

- [Python 3.9](https://www.python.org)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- [Git](https://git-scm.com/)

## Rodar o projeto.
- Faça o download para uma pasta do seu computador: `git clone https://github.com/eduardo-monita/scrapy3.git`

### Passos a passo instalar os requirements.
Primeiramente é necesário preparar o ambiente para ser possível verificar os resultados, abaixo segue os comandos referente a instalação das bibliotecas do projeto.
- Entrar na pasta do projeto: `cd scrapy3`;
- Atualizar o pip: `pip install --upgrade pip`;
- Criar a virtualenv: `virtualenv venv`;
- Criá-la na pasta raiz do projeto: `source venv/bin/activate`;
- Instalar os pacotes necessários: `pip install -r requirements.txt`.

### Rodar Scrapy.
Para iniciar o script de scrapy rode no diretório `scrapy3/countries/` do projeto `scrapy crawl main`.
Você pode encontrar os resultados em formato csv do scrapy no seguinte diretório: `countries/countries/data/main/{ultimo_arquivo_gerado}.csv`.

### Rodas Exercícios.
É necessário rodar os seguintes comandos na raiz(`scrapy3/`) do projeto e os resultados serão exibidos no terminal.
Obs: É importante citar que ao rodar o arquivo aparecerá um terminal interativo para preencher os valores.
- Exercício: `python exercise.py`;
