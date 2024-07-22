# Alinhamento de Sequências
Esse projeto foi desenvolvido como trabalho prático da disciplina de "Algoritmos para Bioinformática" da Universidade Federal de Minas Gerais (UFMG).

## Descrição do Projeto
O objetivo deste projeto é implementar o algoritmo de Needleman-Wunsch para realizar alinhamentos globais par-a-par de sequências de proteínas. O algoritmo utiliza a matriz BLOSUM62, que contém penalidades para substituições e manutenção de aminoácidos.

## Integrantes do projeto
Luíza Furuno Machado

Laura de Freitas Pimentel dos Anjos

## Como usar


1. Instale a biblioteca "numpy"

```bash
pip install numpy
```

2. Clone o repositório "align_seq" para sua máquina local e entre no diretório
   
```sh
git@github.com:furunoluiza/align_seq.git && cd align_seq
```

3. Execute o programa

```bash
python3 ./main.py
```

O programa solicitará como entrada as duas sequências de aminoácidos e a penalidade. O resultado será as sequências alinhadas.
