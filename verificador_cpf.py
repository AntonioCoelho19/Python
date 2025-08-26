import sys

def consulta(cpf_enviado):
    lista = []
    if len(cpf_enviado) == 11:
        multiplo = 10
        for x in range(0,9):
            numero_mult = int(cpf_enviado[x])*multiplo
            lista.append(numero_mult)
            multiplo-=1
        soma_lista = sum(lista)
        soma_lista = soma_lista*10
        resultado = soma_lista%11
        resultado = resultado if resultado <= 9 else 0
        multiplo = 11
        dez_digitos = str(cpf_enviado[:9])+str(resultado)
        soma_digito2 = 0
        for digito in dez_digitos:
            soma_digito2 += int(digito)*int(multiplo)
            multiplo-=1
        resultado_digito2 = (soma_digito2*10) % 11
        resultado_digito2 = resultado_digito2 if resultado_digito2 <=9 else 0
        cpf_gerado = dez_digitos+str(resultado_digito2)
        if cpf_gerado == cpf_enviado:
            print(f'O {cpf_enviado} é válido')
        else:
            print(f'O {cpf_enviado} não é válido')

    else:
        print('O cpf precisa ter 11 digitos')
        return

cpf = input('Digite um cpf completo: ').replace('.', '').replace('-', '').replace(',', '')
teste_cpf_sequencial = cpf == cpf[0]*len(cpf)
if teste_cpf_sequencial is True:
    print('Você enviou dados repetidos')
    sys.exit()
else:
    consulta(cpf)
