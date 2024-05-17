# EC - Prova Regular - Parte 2 - Isabelle Oliveira

# Como executar a aplicação

O projeto desenvolvido utilizando Python, ROS 2, Typer, Inquirer e Turtlesim no arquivo main.py, utilizando apenas uma tartaruga para realizar a atividade.

Para executar o projeto corretamente, o usuário deve ter os seguintes pré-requisitos: ROS 2, Typer, Inquirer Turtlesim e Python3 instalados.

O segundo passo é clonar o repositório utilizando ferramentas do Git para que você possa executar localmente: git clone [https://github.com/IsabelleVOliveira/ponderada-S1-M6/](https://github.com/IsabelleVOliveira/prova1-M6-P2-IsabelleOliveira/)

Também é necessário que o usuário utilize dois terminais (PowerShell, Bash ou algum similar) e acesse a pasta correta ao executar o programa pelo seguinte comando: cd workspace-prova/src/prova-P2

Execute os seguintes comandos para baixar e construir os pacotes necessários: colcon build e source install/local_setup.bash

Execute o Turtlesim pelo primeiro terminal com o seguinte comando: ros2 run turtlesim turtlesim_node Mantenha a tela com a tartaruga aberta para executar o próximo comando!

Em outro terminal (mas no mesmo diretório) execute o código em Python que controla a tartaruga e movimenta a mesma para formar um triângulo com o seguinte comando: python3 main.py


