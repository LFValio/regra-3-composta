pro = []            # processos
proEqui = []        # processos equivalentes
mult = 1            # multiplicação dos processos
multEqui = 1        # multiplicação dos processos equivalentes

c = 0
x = False
while not x:
    pro.append(int(input(f"Processo: ")))       # os processos serão adicionados ao vetor pro
    c += 1                                      # c += 1 tem a finalidade de definir o range final do for logo abaixo
    user = str(input("[P]arar"))                # utilizado para o usuário informar quando os processos acabam
    if user == "P":
        x = True
proEqui.append(int(input(f"Produto: ")))        # o produto é adicionado ao proEqui pois a multiplicação do mesmo é invertida

print("----------EQUIVALENCIA----------")
for x in range(1, c+1):
    proEqui.append(int(input(f"Processo {x}: ")))       # aqui onde os valores serão os equivalentes aos processos iniciais
pro.append(int(input(f"Produto: ")))                    # o produto é adicionado ao pro pois a multiplicação do mesmo é invertida

for x in pro:       # multiplicará todos os números dentro do vetor pro
    mult *= x

for x in proEqui:   # multiplicará todos os números dentro do vetor proEqui
    multEqui *= x

if mult > multEqui:                 # se mult for maior que multEqui, mult é numerador e multEqui denominador
    resultado = mult / multEqui
else:                               # caso contrário, o inverso ocorre
    resultado = multEqui / mult

print(resultado)        # mostra o resultado
