import rclpy
import time
import typer
import inquirer
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill
from collections import deque

app = typer.Typer()

# Criação de um deque vazio
dq = deque()

# Adicionando elementos no final
dq.append('')
print(f"Deque após append: {dq}")

@app.command()
def comando():
    coordenada = str(typer.prompt("Defina: x(0.0) y(0.0) theta(0.0) tempo(1000)"))
    dq.append(coordenada)
    escolha(coordenada)

class DesenhoTartaruga(Node):
    def __init__(self):
        super().__init__('desenho_tartaruga')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.spawn_client = self.create_client(Spawn, 'spawn')
        self.kill_client = self.create_client(Kill, 'kill')
        self.pen_down = True 

        self.spawn_turtle()

    def spawn_turtle(self):
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        request = Spawn.Request()
        request.x = 5.0
        request.y = 5.0
        request.theta = 0.0
        request.name = 'tartaruga'
        future = self.spawn_client.call_async(request)

    def kill_turtle(self):
        while not self.kill_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')
        request = Kill.Request()
        request.name = 'tartaruga'
        future = self.kill_client.call_async(request)
        self.get_logger().info(f'It is over')

    def set_pen(self, pen_down):
        self.pen_down = pen_down

def escolha(coordenada, self):
    twist = Twist()
    (x,y,theta, tempo,_,_,_,_) = Twist()
    if coordenada == "x":
        twist.linear.x = x
    elif coordenada == "y":
        twist.angular.y = y
    elif coordenada == "theta":
        twist.angular.z = theta
    elif coordenada == "tempo":
        time.sleep(tempo)
    else:
        print("Erro: coordenada inválida")
    
    moves = [
            [x, y, theta]
        ]

    for linear_x in moves:
        twist.linear.x = linear_x[0]*3
        twist.linear.y = linear_x[1]*3 
        twist.linear.z = linear_x[1]*3 

        self.publisher_.publish(twist)
        time.sleep(1)

@app.command()
def comandos():
    # realiza lista de perguntas para o usuário
    pergunta = [
        inquirer.List("escolha", message="Qual movimento deseja realizar?", choices=["escolha"])
    ]

def main(args=None):
    rclpy.init(args=args)

    desenho_tartaruga = DesenhoTartaruga()

    desenho_tartaruga.escolha()

    desenho_tartaruga.kill_turtle()

    rclpy.shutdown()

if __name__ == '__main__':
    main()