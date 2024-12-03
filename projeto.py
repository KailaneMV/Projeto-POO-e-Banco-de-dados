import random

class ContaCorrente:
    def __init__(self, titular, senha, saldoC, conta=random.randint(100,999)):
        self.titular = titular
        self.__senha = senha
        self.__saldoC = saldoC  
        self.conta = conta 

    def get_saldoC(self):
        return self.__saldoC

    def set_saldoC(self, saldoC):
        self.__saldoC = saldoC

    def verificar_senha(self, senha):
        return senha == self.__senha

    def sacar(self, valor, senha):
        if self.verificar_senha(senha):
            if valor <= self.__saldoC:
                self.__saldoC -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("Senha incorreta.")

    def depositar(self, valor):
        if valor > 0:
            self.__saldoC += valor 
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def aplicar(self, valor, conta_poupanca, senha):
        if self.verificar_senha(senha):
            if valor <= self.__saldoC:
                self.__saldoC -= valor
                conta_poupanca.saldoP += valor
                print(f"Aplicação de R$ {valor:.2f} realizada com sucesso!")
            else:
                print("Saldo insuficiente para aplicar.")
        else:
            print("Senha incorreta.")

class ContaPoupanca(ContaCorrente):
    def __init__(self, titular, senha, saldoC, saldoP=0, conta=None):
        super().__init__(titular, senha, saldoC, conta)
        self.saldoP = saldoP 

    def resgatar(self, valor, senha):
        if self.verificar_senha(senha):
            if valor <= self.saldoP:
                self.saldoP -= valor
                self.set_saldoC(self.set_saldoC() + valor)
                print(f"Resgate de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente na poupança.")
        else:
            print("Senha incorreta.")

    def extrato(self):
        print("Banco Futuro")
        print("+--------------------------------------------+")
        print(f"| Titular: {self.titular}")
        print(f"| Número da conta: {self.conta}")
        print(f"| Saldo da Conta Corrente: R$ {self.get_saldoC():.2f}")
        print(f"| Saldo da Conta Poupança: R$ {self.saldoP:.2f}")
        print("+--------------------------------------------+")

def main():
    print("Bem-vindo ao Banco Futuro!")
    print("Cadastrar Conta")
    nome = input("Digite o nome completo do titular: ")
    print("Saldo: R$")
    senha = input("Digite uma senha numérica de 4 dígitos: ")

    while len(senha) != 4 or not senha.isdigit():
        print("A senha deve conter exatamente 4 dígitos.")
        senha = input("Digite uma senha válida: ")

    depositoInicial = float(input("Valor do depósito inicial de no mínimo R$ 10,00: R$ "))

    while depositoInicial < 10:
        print("O depósito inicial deve ser no mínimo R$ 10,00.")
        depositoInicial = float(input("Digite o valor do depósito inicial: R$ "))

    conta_corrente = ContaCorrente(nome, senha, depositoInicial)
    conta_poupanca = ContaPoupanca(nome, senha, depositoInicial)

    print(f"Número da conta gerado: {conta_corrente.conta}")
    print("Conta criada com sucesso!")
    conta_poupanca.extrato()

    while True:
        print("\nOperações disponíveis:")
        print("1. Extrato")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Aplicar na poupança")
        print("5. Resgatar da poupança")
        print("6. Finalizar Atendimento")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conta_poupanca.extrato()

        elif opcao == "2":
            valor = float(input("Digite o valor para depósito: R$ "))
            conta_corrente.depositar(valor)

        elif opcao == "3":
            valor = float(input("Digite o valor para saque: R$ "))
            senha = input("Digite sua senha: ")
            conta_corrente.sacar(valor, senha)

        elif opcao == "4":
            valor = float(input("Digite o valor para aplicar na poupança: R$ "))
            senha = input("Digite sua senha: ")
            conta_corrente.aplicar(valor, conta_poupanca, senha)

        elif opcao == "5":
            valor = float(input("Digite o valor para resgatar da poupança: R$ "))
            senha = input("Digite sua senha: ")
            conta_poupanca.resgatar(valor, senha)

        elif opcao == "6":
            print("Obrigado por usar o Banco Futuro. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
