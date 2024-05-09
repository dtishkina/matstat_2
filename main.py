from discrete_distributions import uniform as u
from discrete_distributions import geometric as g
from discrete_distributions import binomial as b
from discrete_distributions import poisson as p


def main():
    while True:
        print("Меню:")
        print("1. Равномерное распределение>")
        print("2. Геометрическое распределение>")
        print("3. Биномиальное распределение>")
        print("4. Пуассоновское распределение>")
        print("5. Выход")
        choice = input("Выберите опцию: ")

        if choice == "1":
            u.modeling_accuracy()
        elif choice == "2":
            g.modeling_accuracy()
        elif choice == "3":
            b.modeling_accuracy()
        elif choice == "4":
            p.modeling_accuracy()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Ошибка: Некорректный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()
