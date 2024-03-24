class AFD:
    def start(self):
        self.estados = []
        self.alfabeto = []
        self.finais = []
        self.inicial = None
        self.transicoes = {}

    def get_input(self):
        # colocca na lista todas os estados fornecidos pelo usuário
        self.estados = input("Digite cade estado separadamente por espaço! ").split()

        # informa o alfabeto a ser utilizado
        self.alfabeto = input("Digite o alfabeto separadamente por espaço! ").split()

        self.inicial = input("Digite o estado incial: ")
        if not self.inicial in self.estados:
            print("Estado inicial inválido, tente de novo!")
            self.get_input()

        self.finais = input("Digite os estados finais: ").split()
        if not all(estados in self.estados for estados in self.finais):
            print("Estados finais inválidos, tente de novo!")
            self.get_input()

        print("Digite as transições no formato seguinte: estadualAtual símbolo  estadoDestino .")
        print("Para finalizar, precione a tecla Enter.")

        while True:
            transicao = input()
            if not transicao:
                break
            estado_inicial, simbolo, estado_final = transicao.split()

            if estado_inicial not in self.estados or estado_final not in self.estados or simbolo not in self.alfabeto:
                print("Transição não válida, tente novamente!") 
                continue
            self.transicoes[(estado_inicial, simbolo)] = estado_final

    def verificar(self, input):
            estado_atual = self.inicial
            for simboloInput in input:
                if (estado_atual, simboloInput) in self.transicoes:
                    estado_atual = self.transicoes[(estado_atual, simboloInput)]
                else:
                    return False
            return estado_atual in self.finais

        
afd = AFD()
afd.start()
afd.get_input()

while True:
    inputUsuario = input("Digite a String que deseja testar: ")
    if inputUsuario.lower() == "sair":
        break
    if afd.verificar(inputUsuario):
        print("Aceito!")
    else:
        print("Rejeitado!")