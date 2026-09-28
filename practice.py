
def blacklist(name):
    """Проверяет имя по черному списку."""
    black_list = ("Ivan", "Petro", "Sergey")
    for bad_name in black_list:
        if name == bad_name:
            return False
    return True

def check_name_characters(name):    
    char_black_list=("0", "1", "2", "3", "4", "5")
    for char in name:
        if char in char_black_list:
            return False 
    return True       

def old(age):
    """Проверяет, попадает ли возраст в разрешенный диапазон."""
    if not (age < 18 or age >= 65):
        return True
    else:
        return False


def handle_ticket_check(name):
    """Оркестратор проверки билета."""
    
    
    if not blacklist(name):
        print("No access.")
        return False

    has_ticket = input("Do you have a ticket? (yes/no): ")
    age = int(input("How old are you? "))

    if not old(age):
        print("No access.")
        return False

    if has_ticket == "yes":
        print("Go!")
        return True

    print("No access.")
    return False
    
def handle_discount():
    """Проверка бонусов."""
    vip = input("Do you have VIP? (yes/no): ")
    promo = input("Do you have promo? (yes/no): ")

    if vip == "yes" or promo == "yes":
        print("You have a discount")
    else:
        print("Full tax")


def main():
    while True:
        name = input("Введите имя для проверки (или 'exit' для выхода): ")
        if name.lower() == 'exit':
            break
            
        # 1. Проверяем символы (цифры и спецсимволы)
        if not check_name_characters(name):
            print("Ошибка: в имени есть запрещенные символы!")
            print("-" * 20)
            continue
            
        # 2. Передаем всё остальное в оркестратор билетов
        if not handle_ticket_check(name):
            print("-" * 20)
            continue

        # 3. Если всё ок — проверяем скидки
        handle_discount()
        print("-" * 20)

if __name__ == "__main__":
    main()