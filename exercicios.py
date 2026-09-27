print("1. Ler um nome e idade e exibi-los")
print("2. Ler dois numeros e soma-los")
print("3. Ler dois numeros e subtrai-los")
print("4. Ler dois numeros e multiplica-los")
print("5. Ler dois numeros e dividi-los")
print("6. Leia uma idade e diga se é criança, adulta ou idosa")
print("7. Leia três números e exiba o maior")
print("8. Leia um valor e se o valor for maior que 100.00 aplique desconto de 10%")
print("9. Leia o usuário e senha e confirme o login")
print("10. Exiba uma vetor de 5 números")
print("11. Leia 5 números e exiba em forma de vetor")
print("12. Leia 5 números e exiba a soma deles em forma de vetor")
print("13. Leia 100 números e exiba a soma deles em forma de vetor")
print("14. Exiba uma matriz 3X3")
print("15. Leia uma matriz 3X3")
print("16. Receber um número com parâmetro e exibir o dobro")
print("17. Receba dois números com parâmetros e exiba o maior")
print("18. Receba três números com parâmetros e calcule a média")
print("19. Faça a contagem de 5 até 1 com recursiva")
print("20. Receba um número e calcule o seu fatorial com fatorial")
print("21. Receba um número e some ele pelos números seguintes dele 10 vezes")
print("22. Sair")
opcao = int(input(("Escolha uma das opções acima!\n")))
match opcao:
    case 1:
        idade = int;
        nome = str;
        print("\n")
        print("Vcê escolher ler o nome e a idade e mostra-lo!\n")
        idade = int(input(("Informe sua idade..: ")))
        while idade < 0:
            print("Idade informada é NEGATIVA!\n")
            idade = int(input("Informe uma idade maior que zero..: "))
        nome = input(("Informe seu nome..: "))
        print("Seu nome é:", nome, "e tem", idade, "anos")
        print("\n")
    case 2:
        num1 = float;
        num2 = float;
        print("\n")
        print("Você escolheu ler dois números e exibir a soma deles!\n")
        num1 = float(input("Informe o primeiro número..: "))
        while num1 < 0:
            print("NEGATIVO!\n")
            num1 = float(input("Informe o primeiro número que seja positivo..: "))
        num2 = float(input("Informe o segundo número..: "))
        while num2 < 0:
            print("NEGATIVO!\n")
            num2 = float(input("Informe o segundo número que seja positivo..: "))
        resultado = num1 + num2;
        print("A soma de", num1, "+", num2, " é:", resultado)
        print("\n")
    case 3:
        num1 = float;
        num2 = float;
        print("\n")
        print("Você escolheu ler dois números e exibir a subtração deles!\n")
        num1 = float(input("Informe o primeiro número..: "))
        while num1 < 0:
            print("NEGATIVO\n")
            num1 = float(input("Informe o primeior número que seja positivo..: "))
        num2 = float(input("Informe o segundo número..: "))
        while num2 < 0:
            print("NEGATIVO!\n")
            num2 = float(input("Informe o segundo número que seja positivo..: "))
        resultado = num1 - num2;
        print("A subtração de", num1, "-", num2, " é:", resultado)
        print("\n")
    case 4:
        num1 = float;
        num2 = float;
        print("\n")
        print("Você escolheu ler dois números e exibir a multiplicação deles!\n")
        num1 = float(input("Informe o primeiro número..: "))
        while num1 < 0:
            print("NEGATIVO!\n")
            num1 = float(input("Informe o primeiro número que seja positivo..: "))
        num2 = float(input("Informe o segundo número..: "))
        while num2 < 0:
            print("NEGATIVO!\n")
            num2 = float(input("Informe o segundo número que seja positivo..: "))
        resultado = num1 * num2;
        print("A multiplicação de", num1, "x", num2, " é:", resultado)
        print("\n")
    case 5:
        num1 = float;
        num2 = float;
        print("\n")
        print("Você escolheu ler dois números e exibir a divisão deles!\n")
        num1 = float(input("Informe o primeiro número..: "))
        while num1 < 0:
            print("NEGATIVO!\n")
            num1 = float(input("Informe o primerio número que seja positivo..: "))
        num2 = float(input("Informe o segundo número..: "))
        while num2 < 0:
            print("NEGATIVO!\n")
            num2 = float(input("Informe o segundo número que seja positivo..: "))
        resultado = num1 / num2;
        print("A divisão de", num1, "%", num2, " é:", resultado)
        print("\n")    
    case 6:
        idade = int;
        print("\n")
        print("Você escolheu ler uma idade e dizer se a pessoa é criança, adulta ou idosa!\n")
        idade = int(input("Informe a idade..: "))
        while idade < 0:
            print("NEGATIVO!\n")
            idade = int(input("Informe outra idade que seja positiva..: "))
        if idade < 12:
            print("Com a idade de", idade, "você é uma criança!")
        if idade >= 13 and idade < 18:
            print("Com a idade de", idade, "você é um adolescente!")
        if idade >= 18 and idade < 50:
            print("Com a idade de", idade, "você é um adulto!")
        if idade >= 50:
            print("Com a idade de", idade, "você é um idoso")
        print("\n")
    case 7:
        num1 = float;
        num2 = float;
        num3 = float;
        print("\n")
        print("Você escolheu ler três numeros e exibir o maior!\n")

        num1 = float(input("Informe o primeiro número..: "))
        while num1 < 0:
            print("NEGATIVO!\n")
            num1 = float(input("Informe o primeiro número que seja positivo..: "))
        num2 = float(input("Informe o segundo número..: "))
        while num2 < 0:
            print("NEGATIVO!\n")
            num2 = float(input("Informe o segundo número que seja positivo..: "))
        num3 = float(input("Informe o terceiro número..: "))
        while num3 < 0:
            print("NEGATIVO!\n")
            num3 = float(input("Informe o terceiro número que seja positivo..: "))
        if num1 > num2 and num1 > num3:
            print("O número:", num1, "é o maior entre os três")
        if num2 > num1 and num2 > num3:
            print("O número:", num2, "é o maior entre os três")
        if num3 > num1 and num3 > num2:
            print("O número", num3, "é o maior entre os três")
        if num1 == num2 and num1 == num3:
            print("Os números:", num1, num2, num3, "são iguais")
        print("\n")
    case 8:
        num1 = float;
        resultado = float;
        desconto = float;
        print("\n")
        print("Você escolheu ver um valor e aplicar desconto caso o valor seja acima de 100.00R$\n")
        num1 = float(input("Informe o valor..: "))
        while num1 < 0:
            print("NEGATIVO!\n")
            num1 = float(input("Informe um valor que seja positivo..: "))
        if num1 >= 100.01:
            desconto = num1 / 10
            resultado = num1 - desconto
            print("O valor informado é válido para aplicar o desconto, valor sem desconto:", num1, "| com desconto:", resultado, "| desconto aplicado:", desconto)
        else:
            print("O valor informado não é válido para aplicar o desconto, valor informado:", num1)
        print("\n")
    case 9:
        usuario = "user";
        senha = "senha";
        print("\n")
        print("Você escolheu ler usuario e senha e efetuar o login!\n")
        usuario = input("Informe o usuário..: ")
        while usuario != "user":
            print("Usuário incorreto!\n")
            usuario = str(input("Informe o usuário correto..: "))
        senha = input("Informe a senha..: ")
        while senha != "senha":
            print("Senha incorreta!\n")
            senha = str(input("Informe a senha correta..: "))
        if usuario == "user" and senha == "senha":
            print("Login efetuado com sucesso, Bem vindo!")
        print("\n")
    case 10:
        vetor = [1,2,3,4,5];
        print("\n")
        print("Você escolheu a exibição de uma matriz de 5 números!\n")
        print("Mostrando os números de uma vez:", vetor, "\n")
        print("Mostrando um de cada vez:\n")
        print("Primeiro número:", vetor[0])
        print("Segundo número:", vetor[1])
        print("Terceiro número:", vetor[2])
        print("Quarto número:", vetor[3])
        print("Quinto número:", vetor[4])
        print("\n")
    case 11:
        vetor = [];
        print("\n")
        print("Você escolheu ler 5 números e exibi-los em forma de vetor!\n")
        vetor.append(input("Informe o primeiro número:"))
        vetor.append(input("Informe o segundo número:"))
        vetor.append(input("Informe o terceiro número:"))
        vetor.append(input("Informe o quarto número:"))
        vetor.append(input("Informe o quinto número:"))
        print("\n")
        print("Os números informados em forma de vetor:", vetor)
        print("\n")
        print("Mostrando em forma de lista:")
        for vetor in vetor:
            print(vetor)
        print("\n")
    case 12:
        vetor = [];
        soma = 0;
        print("\n")
        print("Você escolheu ler 5 números e exibir a soma em forma de vetor!\n")
        vetor.append(int(input("Informe o primeiro número:")))
        vetor.append(int(input("Informe o segundo número:")))
        vetor.append(int(input("Informe o terceiro número:")))
        vetor.append(int(input("Informe o quarto número:")))
        vetor.append(int(input("Informe o quinto número:")))
        print("\n")
        print("Os números informados em forma de vetor:", vetor)
        for vetor in vetor:
            soma = soma + vetor
        print("Soma dos valores:", soma)
        print("\n")
    case 13:
        vetor = [];
        soma = 0;
        print("\n")
        print("Você escolheu ler 100 números e exibir a soma em forma de vetor!\n")
        for i in range(10):
            numero = int(input(f"Informe o {i + 1}° número:"))
            vetor.append(numero)
        print("\n")
        for numero in vetor:
            soma = soma + numero
        print("Os números informados em forma de vetor:", vetor)
        print(f"Soma dos números informados:{soma}")
        print("\n")
    case 14:
        matriz = [[1,2,3], [4,5,6], [7,8,9]];
        print("\n")
        print("Você escolheu exibir uma matriz 3X3!\n")
        print("Matriz reta:", matriz, "\n")
        print("Matriz em linhas:")
        for linha in matriz:
            print(linha)
        print("\n")
    case 15:
        matriz = [];
        print("\n")
        print("Você escolheu ler uma matriz 3X3!\n")
        for i in range(3):
            linha = []
            for j in range(3):
                numero = int(input("Informe um número..:"))
                linha.append(numero)
            matriz.append(linha)
        for linha in matriz:
            print("Valores informados em matriz 3X3:", linha)
        print("\n")
    case 16:
        valor = 5;
        print("\n")
        print("Você escolheu receber dois números com parâmetro e exibir o dobro!\n")
        def dobro(numero):
            print("O dobro de 5 é:", numero * 2)
        dobro(valor)
        print("\n")
    case 17:
        num1 = int;
        num2 = int;
        print("\n")
        print("Você escolheu ler dois números com parâmetros e exibir o maior!\n")
        num1 = int(input("Informe o primeiro número..:"))
        num2 = int(input("Informe o segundo número..:"))
        def maior(num1, num2):
            if num1 > num2:
                print("O maior número é o primeiro:", num1)
            else:
                print("O maior número é o segundo:", num2)
            if num1 == num2:
                print("Os dois números são iguais:", num1, "e", num2)
        maior(num1, num2)
        print("\n")
    case 18:
        num1 = int;
        num2 = int;
        num3 = int;
        print("\n")
        print("Você escolheu receber três números com parâmetros e exibir o dobro!\n")
        num1 = int(input("Informe o primeiro número..:"))
        num2 = int(input("Informe o primeiro número..:"))
        num3 = int(input("Informe o primeiro número..:"))
        print("\n")
        def media(num1 , num2, num3):
            print("A média entre esses três números é:", (num1 + num2 + num3) / 3)
        media(num1, num2, num3)
        print("\n")
    case 19:
        numero = 5;
        print("\n")
        print("Você escolheu exibir a contagem de 5 até 1 com recursiva!\n")
        def contagem(n):
            print(n)
            contagem(n - 1)
        def contagem(n):
            if n == 1:
                print(n)
                return
            print(n)
            contagem(n - 1)
        contagem(numero)
        print("\n")
    case 20:
        numero = int;
        print("\n")
        print("Você escolheu receber um número e exibir o seu fatorial com recursiva\n")
        numero = int(input("Informe um número..:"))
        def fatorial(n):
            if n == 1:
                print(n)
                return 1
            return n * fatorial(n - 1)
        print("O fatorial de:", numero, "é:", fatorial(numero))
        print("\n")
    case 21:
        numero = int;
        print("\n")
        print("Você escolheu ler um número e somar com os seguintes dele 10 vezes!\n")
        numero = int(input("Informe um número..:"))
        def soma(n):
            if n == 10:
                print(n)
                return 10
            return n + soma(n + 1)
        print("A soma de:", numero, "com os 10 seguintes números é:", soma(numero))
        print("\n")
    case 22:    
        print("Até Logo...")
    case _:
        print("Informe uma opção válida!")