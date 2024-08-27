import abc
import datetime
class Historico:
    def __init__(self):
        self.transacoes = []
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):
        self.transacoes.append(
            {
                "tipo":transacao.__class__.__name__,
                "valor":transacao.valor,
                "data": datetime.datetime.now()
            }
        )

class Transacao(abc.ABC):
    @property
    @abc.abstractproperty
    def valor(self):
        pass
    
    @abc.abstractmethod
    def registrar(self,conta):
        pass    

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor
    def __str__(self):
        return f"Depósito de {self.valor}"
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
    def __str__(self):
        return f"Saque de {self.valor}"
    @property
    def valor(self):
        return self._valor
    def registrar(self,conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)

class Conta:
    def __init__(self,numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'                                       
        self._cliente = cliente
        self._historico = Historico()
    @property    
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)

    def depositar(self,valor):
        self._saldo += valor
        self.historico.transacoes.append(f"Depósito de {valor}")
        print("Depósito realizado com sucesso")
        return True

    def sacar(self,valor):
        saldo = self._saldo
        if saldo >= valor:
            self._saldo -= valor
            self.historico.transacoes.append(f"Saque de {valor}")
            print("Saque realizado com sucesso")
            return True
        else:
            print("Saldo insuficiente")
            return False

    def transferir(self,valor,destino):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.depositar(valor)

class ContaCorrente(Conta):
    def __init__(self,saldo,numero,cliente,limite=500,limite_de_saques=3,numeros_de_saques=0):
        super().__init__(saldo,numero,cliente)
        self.limite = limite
        self.limite_de_saques = limite_de_saques
        self.numeros_de_saques = numeros_de_saques
    def sacar(self,valor):
        if self.valor > self.saldo:
            print("Saldo insuficiente")
            return False
        elif self.limite_de_saques == self.numeros_de_saques:
            print("Limite de saques diários atingido")
            return False
        elif self.valor > self.limite:
            print("Valor de saque excede o limite")
            return False
        else:
            return super().sacar(valor)
    def __str__(self):
        return f"""
        Agência: {self.agencia}
        Conta Corrente: {self.numero}
        Titular: {self.cliente.nome}
        """
class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)
    def adicionar_conta(self,conta):
        self.contas.append(conta)
class PessoaFisica(Cliente):
    def __init__(self,nome,cpf,data_nascimento,endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
