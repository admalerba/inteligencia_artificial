class SistemaEspecialistaEmprestimo:
    def __init__(self):
        # Defina as regras do sistema especialista
        self.regras = [
            self.regra_renda,
            self.regra_score,
            self.regra_dividas
        ]

    # Regra 1: Verifica a renda mensal
    def regra_renda(self, renda):
        return renda >= 2000

    # Regra 2: Verifica o score de crédito
    def regra_score(self, score):
        return score > 600

    # Regra 3: Verifica se há dívidas ativas
    def regra_dividas(self, tem_dividas):
        return not tem_dividas

    # Função principal que avalia todas as regras
    def avaliar_emprestimo(self, renda, score, tem_dividas):
        # Verifica cada regra
        resultados = [
            self.regra_renda(renda),
            self.regra_score(score),
            self.regra_dividas(tem_dividas)
        ]

        # Se todas as regras forem atendidas, o empréstimo é aprovado
        if all(resultados):
            return "Empréstimo APROVADO!"
        else:
            return "Empréstimo NEGADO."


# Exemplo de uso do sistema especialista
if __name__ == "__main__":
    # Cria uma instância do sistema especialista
    sistema = SistemaEspecialistaEmprestimo()

    # Dados do cliente
    renda_cliente = float(input("Informe a renda mensal do cliente: R$ "))
    score_cliente = int(input("Informe o score de crédito do cliente: "))
    dividas_cliente = input("O cliente tem dívidas ativas? (s/n): ").strip().lower() == 's'

    # Avalia o empréstimo
    resultado = sistema.avaliar_emprestimo(renda_cliente, score_cliente, dividas_cliente)
    print(resultado)