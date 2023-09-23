import time
from colorama import init, Fore

init(autoreset=True)

def banner():
    banner_text = """
DDoS Tool
    """
    print(banner_text)

def udp_flood():
    print("Запуск UDP flood атаки...")
    time.sleep(2)
    print(Fore.CYAN + "Атака запущена...")
    time.sleep(3)
    print(Fore.GREEN + "Атака завершена!")

def tcp_flood():
    print("Запуск TCP flood атаки...")
    time.sleep(2)
    print(Fore.CYAN + "Атака запущена...")
    time.sleep(3)
    print(Fore.GREEN + "Атака завершена!")

def syn_flood():
    print("Запуск SYN flood атаки...")
    time.sleep(2)
    print(Fore.CYAN + "Атака запущена...")
    time.sleep(3)
    print(Fore.GREEN + "Атака завершена!")

def send_command():
    command = input(Fore.LIGHTWHITE_EX + "> ")

    if command == 'help':
        print("Доступные команды: ddos, exit")
    elif command == 'ddos':
        ip = input("Введите адрес сайта для атаки: ")
        port = input("Введите порт для атаки: ")
        print("Выберите метод атаки:")
        print("1. UDP flood")
        print("2. TCP flood")
        print("3. SYN flood")
        
        attack_type = input()
        
        if attack_type == "1":
            udp_flood()
        elif attack_type == "2":
            tcp_flood()
        elif attack_type == "3":
            syn_flood()
        else:
            print(Fore.RED + "Неизвестный тип атаки!")
    elif command == 'exit':
        print(Fore.YELLOW + "Выход...")
        exit()
    else:
        print(Fore.RED + "Неизвестная команда")

if __name__ == "__main__":
    banner()
    while True:
        send_command()
