from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Guilherme ouviu falar de uma aplicação online interessante
        #para listas de tarefas. Logo, decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        #Guilherme percebe que o titulo da página que se encontra e o cabeçalho mencionam 
        #listas de tarefas (to-do)
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')

        #Guilherme é convidado a inserir um item de tarefa imediatamente




        #Guilherme digita "Comprar ingressos para o cinema" em uma caixa de texto (Guilherme
        # costuma sair bastante com seus amigos e sua namorada Julia)


        #Quando Guilherme tecla enter, a página é atualizada, e agora a página lista "1:Comprar 
        # ingressos para o cinema" como um item em uma lista de tarefas


        #Ainda continua havendo uma caixa de texto convidando-o a acrescentar outro item 
        #dentro da lista de tarefas. Guilherme insere "encontrar-me com Julia" - Guilherme é um
        #namorado bem atensioso

        #A pagina é atualizada novamente e agora mostra os dois itens em sua lista


        #Guilherme se pergunta se, após fechar o navegador, o site se lembrará de sua lista. Então, ele
        #nota que o site gerou um URL único para ele *há um pequeno texto explicativo para isso


        #Guilherme acessa esse URL. Sua lista de tarefas continua lá


        #Satisfeito, Guilherme retorna a jogar em seu video-game.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
