class DescobrirSenha:
    def __init__(self, senha):
        self._senha = senha
        self.descobrir_senha()

    def descobrir_senha(self):

        caracteres_validos = [  # alfabeto lower
                              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                              'u', 'v', 'w', 'x', 'y', 'z',
                                # alfabeto upper
                              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                              'U', 'V', 'W', 'X', 'Y', 'Z',
                                # ç/Ç
                              'ç', 'Ç',
                                # numeros
                              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        resultado = []
        tentativas = 0

        for index in range(0, len(self._senha)):
            for caracter in caracteres_validos:
                if ''.join(resultado) == self._senha:
                    break

                print(''.join(resultado) + caracter)

                if caracter == self._senha[index]:
                    resultado.append(caracter)

                tentativas += 1

        print('='*10)
        print(f'A senha foi descoberta após {tentativas} tentativas de combinação.')
        print('A senha descoberta foi: {}.'.format(''.join(resultado)))
