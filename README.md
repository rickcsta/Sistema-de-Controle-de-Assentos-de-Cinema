Sistema de Controle de Assentos de Cinema

Este projeto consiste em um sistema de gerenciamento de assentos de uma sala de cinema desenvolvido em Python. O programa permite visualizar os assentos disponíveis e ocupados, realizar a venda de entradas, associando cada assento ao nome do comprador, e armazenar essas informações em um arquivo de texto para que os dados sejam preservados mesmo após o encerramento da aplicação.

A implementação utiliza conceitos de Programação Orientada a Objetos (POO) por meio da classe Assento, responsável por representar cada lugar da sala, armazenando atributos como fileira, número, situação de ocupação e comprador.

Os assentos são organizados utilizando a estrutura de dados dicionário, em que cada chave representa a coordenada do assento (por exemplo, A1, B4) e cada valor corresponde a um objeto da classe Assento. Essa abordagem permite localizar e atualizar assentos de maneira simples e eficiente.

O projeto é dividido em dois arquivos principais que devem permanecer na mesma pasta:

assento.py: contém a classe Assento e seus métodos;
cinema.py: contém a lógica do sistema, incluindo criação dos assentos, menu de interação, exibição do mapa, venda de entradas e salvamento dos dados.

Para executar o sistema, basta manter os arquivos assento.py e cinema.py no mesmo diretório e executar o arquivo principal com o comando:

python cinema.py

O arquivo sala.txt será criado automaticamente pelo sistema e será utilizado para armazenar as informações dos assentos vendidos.
