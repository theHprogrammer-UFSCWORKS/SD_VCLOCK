# Simulador de Vetor de Relógio

O simulador de vetor de relógio é uma aplicação GUI que simula o funcionamento de um algoritmo de vetor de relógio em um sistema distribuído. O simulador foi desenvolvido como trabalho prático da disciplina de Sistemas Distribuídos do curso de Engenharia de Computação da Universidade Federal de Santa Catarina (UFSC), campus Araranguá.

O simulador foi desenvolvido utilizando a linguagem Python e a biblioteca tkinter para a interface gráfica. O gráfico do vetor de relógio foi implementado utilizando a biblioteca matplotlib.

-   [Simulador de Vetor de Relógio](#simulador-de-vetor-de-relógio)
    -   [Como executar](#como-executar)
    -   [Como utilizar](#como-utilizar)

## Como executar

Para executar o simulador, é necessário ter o Python 3 instalado. Em seguida, instale as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```

Para executar o simulador, execute o arquivo main.py:

```bash
python main.py
```

## Como utilizar

Ao executar o simulador, uma janela será aberta com a interface gráfica do simulador. A interface possui os seguintes elementos:

-   Dropdown: Permite selecionar o número de processos da simulação.
-   Botão "Criar simulação de relógio vetorial": Cria a simulação com base no número de processos selecionado.
    -   Núrmero máximo de processos: 5

Após criar a simulação, a interface gráfica será reorganizada para exibir os botões e labels correspondentes a cada processo. Além disso, o gráfico será atualizado para exibir o vetor de relógio de cada processo.

-   Botão "Evento Local": Executa um evento local no processo correspondente.
-   Botão "Enviar Mensagem": Envia uma mensagem do processo correspondente para outro processo.
-   Botão "Encerrar simulação": Encerra a simulação atual e reorganiza a interface para permitir a criação de uma nova simulação.

## Cloning this Repository

1. On GitHub.com, navigate to the repository's main page.
2. Above the list of files, click code.
3. To clone the repository using HTTPS, under "Clone with HTTPS", click 📋. To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click 📋. To clone a repository using GitHub CLI, click Use GitHub CLI, then click 📋.
4. Open Git Bash.
5. Type git clone (clone git) and paste the URL you copied earlier.

```c
$ git clone
```

6. Press Enter to create your local clone.

<br>

## 👨‍💻 Author

<table align="center">
    <tr>
        <td align="center">
            <a href="https://github.com/theHprogrammer">
                <img src="https://avatars.githubusercontent.com/u/79870881?v=4" width="150px;" alt="Helder's Image" />
                <br />
                <sub><b>Helder Henrique</b></sub>
            </a>
        </td>    
    </tr>
</table>
<h4 align="center">
   By: <a href="https://www.linkedin.com/in/theHprogrammer/" target="_blank"> Helder Henrique </a>
</h4>
