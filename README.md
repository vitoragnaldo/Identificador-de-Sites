## Identificador de Sites

O Identificador de Sites é uma aplicação desenvolvida em Python que permite identificar automaticamente informações de um site a partir de uma URL fornecida pelo usuário.

A aplicação analisa o endereço informado, identifica o domínio de destino, obtém o título da página, verifica o status da conexão, detecta redirecionamentos e registra um histórico das consultas realizadas.

## Funcionalidades

* Identificação automática do site por meio do título da página.
* Extração e exibição do domínio da URL.
* Exibição da URL final após possíveis redirecionamentos.
* Verificação do código de status HTTP.
* Detecção de conexão segura (HTTPS).
* Contagem de redirecionamentos.
* Registro automático do histórico de consultas em arquivo.
* Menu interativo para múltiplas verificações.
* Tratamento de erros para URLs inválidas e falhas de conexão.

## Tecnologias Utilizadas

* Python
* Requests
* BeautifulSoup4
* urllib.parse
* datetime

## Objetivo

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de programação em Python, incluindo requisições HTTP, manipulação de URLs, extração de informações da web, tratamento de exceções, estruturas de repetição e persistência de dados.

## Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conhecimentos em:

* Consumo de páginas web utilizando Requests.
* Web Scraping básico com BeautifulSoup.
* Manipulação e análise de URLs.
* Estruturas de repetição e menus interativos.
* Tratamento de erros e exceções.
* Leitura e gravação de arquivos.
* Organização e desenvolvimento de projetos em Python.

## Exemplo de Uso

Digite a URL: https://www.google.com

RESULTADO DA CONSULTA

Site identificado : Google
Domínio : [www.google.com](http://www.google.com)
URL final : https://www.google.com
Status HTTP : 200
HTTPS : Sim
Redirecionamentos : 0
Consultas feitas : 1

