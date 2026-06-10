# Desafio 21 - Simulação de Caneta

## Sobre o Projeto

Este projeto foi desenvolvido como parte dos estudos de Programação Orientada a Objetos (POO) em Python.

O sistema simula o funcionamento básico de uma caneta, permitindo controlar seu estado (tampada ou destampada) e realizar escritas no terminal apenas quando a caneta estiver pronta para uso.

A aplicação utiliza a biblioteca Rich para exibir o texto escrito com a cor definida para a caneta.

---

## Conceitos Praticados

* Programação Orientada a Objetos (POO)
* Classes e Objetos
* Método construtor (`__init__`)
* Atributos de instância
* Métodos
* Estruturas condicionais
* Controle de estado de objetos
* Formatação de saída com Rich

---

## Estrutura da Classe

A classe `Caneta` possui os seguintes atributos:

| Atributo  | Descrição                                     |
| --------- | --------------------------------------------- |
| `cor`     | Cor utilizada para exibir o texto             |
| `tampada` | Indica se a caneta está tampada ou destampada |

---

## Métodos Disponíveis

| Método        | Função                                                    |
| ------------- | --------------------------------------------------------- |
| `destampar()` | Remove a tampa da caneta                                  |
| `escrever()`  | Permite escrever um texto caso a caneta esteja destampada |

---

## Regras Implementadas

* A caneta inicia tampada por padrão.
* Não é possível escrever com a caneta tampada.
* O texto é exibido na cor definida para a caneta.
* O sistema informa quando o usuário precisa destampar a caneta antes de escrever.

---

## Exemplo de Uso

```python
c1 = Caneta('red')

c1.destampar()
c1.escrever('Olá, tudo bem?')
```

---

## Tecnologias Utilizadas

* Python 3
* Rich

### Instalação da Biblioteca Rich

```bash
pip install rich
```

---

## Objetivo Educacional

Este exercício foi desenvolvido para praticar o conceito de estado de objetos, demonstrando como métodos podem alterar comportamentos e permitir ou impedir determinadas ações de acordo com as condições definidas na classe.

---

## Autora

**Maria Ivonize**

Estudante de Tecnologia da Informação (T.I.) em formação, dedicada ao desenvolvimento de habilidades em programação e engenharia de software.

Atualmente aprofundando conhecimentos em Python, Programação Orientada a Objetos (POO), Git, GitHub e boas práticas de desenvolvimento através da construção de projetos e resolução de desafios práticos.
