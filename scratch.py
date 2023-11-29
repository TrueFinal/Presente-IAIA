import arcade

largura = 800
altura = 600

class MeuTeste(arcade.Window):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)

        arcade.set_background_color(arcade.color.LIGHT_CYAN)

    def setup(self):
        pass
    def on_draw(self):
        arcade.start_render()

    # Desenhando a aba e rendereizando
    largura = 800
    altura = 600
    arcade.open_window(altura, largura)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()

    # Desenhando o perssonagem (face)
    x = 300
    y = 300
    radius = 200
    arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

    # Desenhando o olho (direito)
    x = 370
    y = 350
    radius = 20
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

    # Desenhando o olho (esquerdo)
    x = 230
    y = 350
    arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

    # Desenhando o sorriso
    x = 305
    y = 290
    width = 120
    height = 100
    arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle=170, end_angle=350)

    # Terminando desenho e renderizando
    arcade.finish_render()

    # Manter rodando
    arcade.run()

    # Desenhando o cenário
    def draw_triangle_filled(x, y):
        arcade.draw_triangle_filled(x + 40, y,
                                    x, y - 100,
                                    x + 80, y - 100,
                                    arcade.color.DARK_GREEN)
        arcade.draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140,
                                          arcade.color.DARK_BROWN)
    def update(self, delta_time):
        pass
    def main(self):
        game = MeuTeste(largura, altura)
        game.setup()
        arcade.run()
    if __name__ == "__main__":
        main()

arcade.finish_render()

arcade.run()