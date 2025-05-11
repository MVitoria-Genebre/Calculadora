import sympy as sp

def calcular_derivada():
    # Define a variável simbólica
    x = sp.Symbol('x')

    # Recebe a função do usuário
    expressao_str = input("Digite a função f(x) para derivar (ex: x**2 + 3*x + 1): ")
    
    try:
        # Converte a string em expressão simbólica
        expressao = sp.sympify(expressao_str)

        # Calcula a derivada
        derivada = sp.diff(expressao, x)

        # Mostra o resultado
        print(f"A derivada de f(x) = {expressao} é:\nf'(x) = {derivada}")

    except (sp.SympifyError, SyntaxError):
        print("Erro: função inválida. Tente novamente com uma expressão como 'x**2 + 3*x'.")

if __name__ == "__main__":
    calcular_derivada()
