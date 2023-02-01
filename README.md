# Bem-vindo ao Projeto Inventory Report!

Este é um projeto da [Trybe](https://www.betrybe.com/) que foi desenvolvido no módulo de Ciência da Computação.
Trata-se de um gerador de relatórios que recebe como entrada arquivos com dados de um estoque, estes arquivos podem estar no formato CSV, JSON ou XML, e gera como saída, um relatório sobre estes dados, podendo este relatório ser do tipo simples ou completo.

## Tecnologias utilizadas

Em seu desenvolvimento foi utilizada linguagem ***Python*** para escrever os códigos e aplicados os conceitos da ***Programação Orientada a Objetos***, e alguns padrões de projeto, como ***Strategy***, ***Iterator*** e ***Decorator***.

Fora isso, foi utilizado o framework ***pytest***, para testar classes que já haviam sido implementadas pela Trybe.

## Habilidades que foram trabalhadas:

  - Aplicação de conceitos de Orientação a Objetos em Python; 
  - Aplicação de padrões de projeto;
  - Leitura de arquivos XML, CSV e JSON.

## Como rodar o projeto na sua máquina:

1. Navegue até o local onde deseja clonar o repositório e utilize o **git clone**:
```
git clone git@github.com:Tayna-Silva-Macedo/
project-inventory-report.git
```

2. Acesse o diretório do projeto **
project-inventory-report**:
```
cd 
project-inventory-report
```

3. Crie e ative um ambiente virtual para o projeto:
```
python3 -m venv .venv && source .venv/bin/activate
```

4. Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```

5. Instale o próprio projeto:
```
pip install .
```

6. Execute o projeto utilizando o comando:
```
inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
```
Exemplo: ```inventory_report inventory_report/data/inventory.csv simples```

7. Para rodar os testes é utilizado o seguinte comando:

```
python3 -m pytest
```
