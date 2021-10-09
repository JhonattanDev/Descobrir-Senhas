from descobrir_senha import DescobrirSenha


class DescobreSenha:
    def __init__(self):
        self._senha = self.pedir_senha()
        self._senha_valida = self.verifica_senha()
        self.descobre_senha()

    @staticmethod
    def pedir_senha():
        senha = input('Por favor, insira a senha do cadeado (letras de A-Z e números): ')
        return senha.strip()

    def verifica_senha(self):
        if self._senha.isalnum():
            print('Senha válida.')
            return True
        else:
            return False

    def descobre_senha(self):  # def descobre_senha(self, senha_valida)
        if self._senha_valida:
            DescobrirSenha(self._senha)  # função importada de 'descobrir_senha.py'
        if not self._senha_valida:
            print('Sua senha não é válida, tente novamente.')
            print('Sua senha é inválida, por favor, insira uma senha válida.')
            DescobreSenha()


DescobreSenha()
