import unittest
from Game_TDD.Tdd_game import Personagem


class TestPersonagem(unittest.TestCase):

    def personagemrecebedanoretornavida(self):
        personagem = Personagem()
        personagem.vida = 50
        personagem.receber_dano(10)

        self.assertEqual(personagem.vida, 4000)


if __name__ == '__main__':
    unittest.main()
