import turtle
import time
from typing import Tuple

class SSDrawer:
    def __init__(self) -> None:
        self.canva = turtle.Turtle()
        self.ROOF_COL = '#FFA07A'

    def run(self) -> None:
        self.house2d()
        self.block(100, 200)
        time.sleep(5)

    def wrap_goto(self, goto_func: callable, *goto_args: Tuple[int, int]) -> None:
        self.canva.penup()
        goto_func(*goto_args)
        self.canva.pendown()

    # Geom
    def square(self, inner_dim: int = 25):
        for _ in range(4):
            self.canva.forward(inner_dim)
            self.canva.right(90)
    
    def poly(self, lat: int = 100, lon: int = 200) -> None:
        for _ in range(2):
            self.canva.forward(lat)
            self.canva.left(90)
            self.canva.forward(lon)
            self.canva.left(90)


    # Drawable
    def house2d(self, dim: int = 100) -> None:
        # pereti patrati
        self.square(dim)
        self.wrap_goto(self.canva.goto, (20*dim/100, -(dim/5))) # 20%
        self.square(dim/5)
        self.wrap_goto(self.canva.goto, (60*dim/100, -(dim/5))) # 60%
        self.square(dim/5)
        
        # usa

        self.wrap_goto(self.canva.goto, (45*dim/100, -dim)) # 20% inaltime, 45 latime
        self.canva.left(90)
        self.canva.forward(20*dim/100)
        self.canva.right(90)
        self.canva.forward(15*dim/100)
        self.canva.right(90)
        self.canva.forward(20*dim/100)


        #acoperis
        self.wrap_goto(self.canva.goto, 0, 0)
        self.canva.fillcolor(self.ROOF_COL)
        self.canva.begin_fill()
        self.canva.goto(dim/2, dim)
        self.canva.right(45)
        self.canva.goto(dim, 0)
        self.canva.end_fill()


    def mountain() -> None:
        pass

    def block(self, dim_x: int, dim_y) -> None:
        self.poly(lat=dim_x, lon=dim_y)

    def person() -> None:
        pass

    def __del__(self) -> None:
        pass


if __name__ == "__main__":
    obj = SSDrawer()
    obj.run()