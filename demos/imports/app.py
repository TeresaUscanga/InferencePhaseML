from utils.math_boy import MathBoy, Logger
from operadores.operador_yee import OperadorYee

logger = Logger()
operadorYee = OperadorYee(logger)
math_boy = MathBoy(logger, operadorYee)

math_boy.greetings('Tere')
math_boy.jump()