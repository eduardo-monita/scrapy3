# Scrapy3
Este é um simples projeto referente ao um teste de processo seletivo.

## Requirements

- [Python 3.9](https://www.python.org)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- [Git](https://git-scm.com/)

## Rodar o projeto.
- Faça o download para uma pasta do seu computador: `git clone https://github.com/eduardo-monita/scrapy3.git`

### Passos a passo instalar os requirements.
Primeiramente é necesário preparar o ambiente para ser possível verificar os resultados, abaixo segue os comandos referente a instalação das bibliotecas do projeto.
- Atualizar o pip: `pip install --upgrade pip`;
- Criar a virtualenv: `virtualenv venv`;
- Criá-la na pasta raiz do projeto: `source venv/bin/activate`;
- Instalar os pacotes necessários: `pip install -r requirements.txt`.

### Rodar Scrapy.
Para iniciar o script de scrapy rode na raiz do projeto `scrapy crawl main`.
Você pode encontrar os resultados em formato csv do scrapy no seguinte diretório: `countries/countries/data/main/{ultimo_arquivo_gerado}.csv`.

### Rodas Exercícios.
É necessário rodar os seguintes comandos na raiz do projeto e os resultados serão exibidos no terminal.
- Exercício 1: `spython exercicio_1.py`;
- Exercício 2: `python exercicio_2.py`.
