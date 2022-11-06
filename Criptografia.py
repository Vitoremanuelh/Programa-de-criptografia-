def Opcao():
    ## Função para determinar a opcão (c ou d) escolhida pelo usuário.
    while True: ## Loop até o usuário digitar "c" ou "d". 
        opcao = input('Digite c para criptografia e d para descriptografia \n')
        if opcao in 'c d':
            return opcao
        else:
            return Opcao()
def Chave():
    ## função que determina a chave da criptografia(9 chaves).
    chave = 0
    while True: ## Loop até o usuário digitar um número dentro do intervalo exigido.
        chave = int(input('entre com uma chave (1-9): \n'))
        if  chave >= 1 and chave <=9: ##intervalo.
            return chave
        else:
            print('apenas números no intervalo 1-9!')
            return Chave()            
def crip(opcao, mensagem, chave):
    ## função que rodará o processo de criptografia.
    list=[]
    teste =""
    if opcao == "c":
      if len(mensagem)<128:
        for letra in mensagem: ## um for para cada caractere da mensagem digitada.
            n = ord(letra)
            if n>=0 and n<=255:
                  list.append(chr(n+chave)) 
            else:
              print("Não está na tabela ASCII!")       
      else:
              print("apenas menos de 128 caracteres:)") 
    return ''.join(list)
def descrip(opcao, mensagem, chave):
    ## função que rodará o processo de descriptografia.
    resultado = ""
    if opcao == 'd':
      for letra in mensagem: ## um for para cada caractere da mensagem digitada.
              n = ord(letra)
              resultado = resultado+chr(n-chave) ## conta matemática inversa.
    return resultado
opcao = Opcao()
mensagem = input('Digite a mensagem: \n')
chave = Chave()
print('Sua frase traduzida é:')
if opcao=='c':
      print(crip(opcao, mensagem, chave))
else:
    print(descrip(opcao, mensagem, chave))
