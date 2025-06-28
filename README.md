# Calculadora-ipv6
Calculadora IPv6 feita em `python` que utiliza os conceitos de rightmost e leftmost 

### Regras e instruções para construção da calculadora 
1. A calculadora não deve conter bibliotecas já prontas;
2. Crie sua própria biblioteca, ou suas próprias funções;
3. A calculadora, deve utilizar as abreviações corretamente para o IPv6;
4. Informando o valor do IPv6 deve retornar qual seu endereço com prefixo
    1. Ex: 2801:0390:0080:0000:0100:0000:0000:ff00 /64
    Deve retornar: 2801:390:80:0:100::ff00 /64
    2. Gerar IPv6 aleatórios com /54 e /48 que está especificado na RFC.

## Organização dos arquivos
A calculadora foi modulada da seguinte forma para melhor visualização e organização pessoal:

calculadora-ipv6/

├── calculadora_ipv6.py

├── main.py

├── gitignore

└── README.md

### Explicação das funções
O arquivo `calculadora_ipv6.py` possui as seguintes funções

1. `normalizar_ipv6(endereco_ipv6)`: É uma função de "preparação", isto é, utilizamos ela para termos um endereço consistente que esteja no formato padrão e completo. Aqui, lidamos com a expansão das abreviações **::** e fazemos o preenchimento dos blocos.

2. ``abreviar_ipv6(partes_normalizadas)``: Após a normalização do endereço, aplica as regras de abreviação. Ao encontrar a maior sequência de zeros, fazemos sua remoção considerando os zeros à esquerda (*leftmost*) e aplicamos a compreensão utilizando **::** .Para esse projeto, podemos tê-la como a **função principal**.

3. ``gerar_ipv6_aleatorio()``: Um dos requisitos era a geração de endereços IPv6 aleatórios. É uma função simples e direta que faz a geração usando a biblioteca built-in `random` e segue a formatação padrão do IPv6.

4. `apresentar_calculadora()`: comandos no cli que permitem a interação usuário-sistema. Ela é executada no arquivo **main** para melhor modulação. 

## Rodando o código
O código foi feito para rodar em versões iguais ou superiores a **3.11**. Logo, sua corretude em versões anteriores pode não ser garantida 

Ao baixar o arquivo, acesse-o usando seu terminal de preferência (PowerShell, Linux...) e rode o comando 

> py main.py

Caso você esteja no diretório correto, o programa deve abrir um cli que o instruirá quanto ao uso da calculadora e suas funcionalidades.



