# Desenvolvedor : Felipe Adrian Lourenço Barbisan
# Turma : 4º ADS (AMS) - Fatec
# Disciplina : Tecnicas Avancadas de Programacao
class Veiculo:
    def __init__(self, rodas):
        self.rodas = rodas
    def exibir_quant_rodas(self):
        print(f"Quantidade de rodas: {self.rodas}")
        
class Carro(Veiculo):
    def __init__(self,rodas , marca, modelo, ano, renavam):
        super().__init__(rodas)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__renavam = renavam

    def exibir_informacoes(self):
        Veiculo.exibir_quant_rodas(self)
        print(f"Informações do Carro - Marca: {self.marca}; Modelo: {self.modelo}; Ano: {self.ano}")
        
    def exibir_renavam(self):
        print(f"Renavam do Carro - Renavam: {self.__renavam}")
        
class Moto(Veiculo):
    def __init__(self,rodas , marca, modelo, ano, renavam):
        super().__init__(rodas)
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__renavam = renavam

    def exibir_informacoes(self):
        Veiculo.exibir_quant_rodas(self)
        print(f"Informações da Moto - Marca: {self.marca}; Modelo: {self.modelo}; Ano: {self.ano}")
        
    def exibir_renavam(self):
        print(f"Renavam da Moto - Renavam: {self.__renavam}")

# polimorfismo
def exibir_informacoes(veiculo):
    veiculo.exibir_informacoes()
       
       
# Instanciando um objeto da classe Carro
fusca = Carro(4 ,"Volkswagen", "Fusca", 1970, 1023123)
exibir_informacoes(fusca)
fusca.exibir_renavam()
print("-----------------------------")
# Instanciando um objeto da classe Moto
cb300f = Moto(2 ,"Honda", "Cb300F Twister", 2024, 857454)
exibir_informacoes(cb300f)
cb300f.exibir_renavam()