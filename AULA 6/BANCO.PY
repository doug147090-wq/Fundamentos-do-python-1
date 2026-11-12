acesso = input('Deseja acessar o banco? sim ou não >> ').lower()
c = 3
saldo =  5000.0
extrato = []



while acesso == 'sim' or acesso == 'SIM' or acesso == 's' or acesso == 'Sim' :
     senha_acesso = input('Digite sua senha para acessar a conta: ')  
     if senha_acesso == '1234':    

     
   
           
            print('Seja bem vindo ao bando z')
            menu =  input('''

                       1 - saque
                       2 - deposito
                       3 - extrato
                       4 - sair

                       ''')
            if menu == '1':
                saque_ = float(input('R$ >> '))
                if saque_ <=  saldo:
                   senha = input('Senha: ')
                   if senha == '123':
                       saldo = saldo - saque_                      
                       extrato.append(- saque_)
                       print('Em conta', saldo)
                       acesso = input('Deseja continuar? sim ou não >>').lower()
                else:
                    print('Saldo insuficiente ... ')
                    acesso = input('Deseja acessar o banco? sim ou não >> ').lower()
            elif menu == '2':
                deposito_ = float(input('R$ >>'))
                senha = input('Senha: ')
                if senha == '123':
                   
                    saldo = saldo +  deposito_
                    extrato.append(deposito_)
                    print('Em conta', saldo)
                    acesso = input('Deseja continuar? sim ou não >> ')
            elif menu =='3':
                extrato.append(saldo)
                print(extrato)
                acesso = input('Deseja acessar o banco? sim ou não >>')
            else:
                print('OBRIGADA VOLTE SEMPRE... ')
                break
               
               
               

           
     else:
        print('SENHA INCORRETA ... ')
else:
    print('OBRIGADO VOLTE SEMPRE...')