import hashlib

class Usuario: # Programa da última entrega
    def __init__(self, nome, senha, tipo):
        self.nome = nome
        self.__senha_hash = self.__encriptografar(senha)
        self.tipo = tipo

    def __encriptografar(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    @property
    def senha_hash(self):
        return self.__senha_hash

    def verificar_senha(self, senha):
        return self.__senha_hash == self.__encriptografar(senha)
    
def test_funcao() -> None:
    # Criando usuário correto
    usuario = Usuario("Gabriel", "admin123", "administrador")

    # Pegando a senha digitada do arquivo senha.txt
    with open("senha.txt", "r") as file:
        senha_digitada = file.read().strip()

    # Realizando a encriptografia da senha digitada e colocando no arquivo senha_encriptada.txt
    senha_digitada_hash = hashlib.sha256(senha_digitada.encode()).hexdigest()

    with open("senha_encriptada.txt", "w") as file:
        file.write(senha_digitada_hash)

    # Comparando a senha digitada com a senha correta e o hash da senha digitada com o hash da senha correta
    senhas_conferem = False
    if senha_digitada_hash == usuario.senha_hash:
        senhas_conferem = True
    else:
        pass

