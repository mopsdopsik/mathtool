import sys
import math

MAX_VALUE = 10000

def print_help():
    help_text = """mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000."""
    print(help_text)

def main():
    # Получаем аргументы командной строки (исключая имя самого скрипта)
    args = sys.argv[1:]
    
    # Если параметров нет или первый из них --help, выводим справку
    if len(args) == 0 or args[0] == "--help":
        print_help()
        sys.exit(0)
        
    # Если первым параметром идет не solve, сообщаем об ошибке
    if args[0] != "solve":
        print("ОШИБКА: неизвестная команда. Используйте --help для справки.", file=sys.stderr)
        sys.exit(1)
        
    a_str, b_str, c_str = "", "", ""
    
    if len(args) == 1:
        # Вариант: python mathtool.py solve (ввод с клавиатуры)
        a_str = input("Введите A: ")
        b_str = input("Введите B: ")
        c_str = input("Введите C: ")
    elif len(args) == 7:
        # Вариант: python mathtool.py solve -a 1 -b -3 -c 2
        try:
            idx_a = args.index("-a")
            idx_b = args.index("-b")
            idx_c = args.index("-c")
            a_str = args[idx_a + 1]
            b_str = args[idx_b + 1]
            c_str = args[idx_c + 1]
        except (ValueError, IndexError):
            print("ОШИБКА: неверный формат параметров командной строки.", file=sys.stderr)
            sys.exit(1)
    else:
        print("ОШИБКА: неверное количество параметров.", file=sys.stderr)
        sys.exit(1)
        
    # 2. Получение и преобразование исходных данных
    try:
        A = int(a_str)
        B = int(b_str)
        C = int(c_str)
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом.", file=sys.stderr)
        sys.exit(1)
        
    # 3. Проверка ограничений диапазона
    if abs(A) > MAX_VALUE or abs(B) > MAX_VALUE or abs(C) > MAX_VALUE:
        print("ОШИБКА: значение вне допустимого диапазона (макс. 10000).", file=sys.stderr)
        sys.exit(1)
        
    # 4. Определение вида уравнения и решение
    if A == 0:
        if B != 0:
            print("Уравнение линейное")
            x = -C / B
            print(f"x = {x:.3f}")
        else:
            print("ОШИБКА: это не уравнение, неизвестное отсутствует.", file=sys.stderr)
            sys.exit(1)
    else:
        print("Уравнение квадратное")
        D = B * B - 4 * A * C
        print(f"D = {D}")
        
        if D > 0:
            x1 = (-B + math.sqrt(D)) / (2 * A)
            x2 = (-B - math.sqrt(D)) / (2 * A)
            print(f"x1 = {x1:.3f}")
            print(f"x2 = {x2:.3f}")
        elif D == 0:
            x = -B / (2 * A)
            print(f"x = {x:.3f}")
        else:
            print("Действительных корней нет")

if __name__ == "__main__":
    main()

