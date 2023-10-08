from enum import Enum

class OPERATION(Enum):
    WITHDRAWAL = 1
    DEPOSIT = 2

users_db = {
    'usr1':'pwd1',
    'usr2':'pwd2',
    'usr3':'pwd3',
}

accounts_db = {
    'usr1':2000,
    'usr2':5000,
    'usr3':100,
}

get_user = lambda : input('User: ')
get_pwd = lambda : input('Password: ')
get_operation = lambda : int(input(f'Operation:\n   {OPERATION.DEPOSIT.value} --> Deposit\n   {OPERATION.WITHDRAWAL.value} --> Withdrawal\n'))
get_value = lambda : int(input('Value (R$): '))

deposit = lambda usr, value : accounts_db.update({usr: accounts_db[usr]+value}) or print(f'R${value} successfully deposited.\nNew balance: R${accounts_db[usr]}\n')
withdrawal = lambda usr, value: accounts_db.update({usr: accounts_db[usr]-value}) or print(f'R${value} successfully withdrawn.\nNew balance: R${accounts_db[usr]}\n') if accounts_db[usr] >= value else print('Error when withdrawing\n')
account_manager = lambda usr, op : deposit(usr, get_value()) if op == OPERATION.DEPOSIT.value else withdrawal(usr, get_value()) if op == OPERATION.WITHDRAWAL.value else print('Invalid Operation. Try again.\n') or account_manager(usr, get_operation())
check_account = lambda usr, pwd : print('Login successfully.\n') or account_manager(usr, get_operation()) if usr in users_db.keys() and users_db[usr] == pwd else print('\nUser or Password invalid.\nTry again.\n') or check_account(get_user(), get_pwd())
enter_bank = lambda : check_account(get_user(), get_pwd())

enter_bank()
