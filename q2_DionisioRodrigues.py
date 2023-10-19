file = open('./q2_credentials.txt', 'r')

get_usr = lambda : input('user: ')
get_password = lambda : input('password: ')

check_account = lambda usr, pwd : print('SUCESSO') if len([True for credential in file if usr == credential.rstrip().split(':')[0] and pwd == credential.rstrip().split(':')[1]]) == 1 else print('FRACASSO')

check_account(get_usr(), get_password())
