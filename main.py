dict = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return f'Будь ласка введіть ім`я та номер телефону'
        except IndexError:
            return f'Будь ласка введіть ім`я та номер телефону'
        except KeyError:
            return f'Неіснуючий контакт'

    return wrapper

def input_exit(*args):
    return 'Допобачення, хорошого дня'

def input_hello(*args):
    return "Чим я можу вам допомогти?"

def input_help(*args):
   return """ Ви можете скористатися наступними командами:
                add - Додати ім'я та номер телефону
                change - змінити контакт
                all - показати всі контакти"""

@input_error
def input_add(name: str, phone: str):
    dict[name] = phone
    return f'Контакт {name} успішно добавлено'
#
#
@input_error
def input_change(name: str, phone: str):
    for i in dict.keys():
        if i != name:
            print('такого контакту неіснує')
            raise KeyError
        else:
            dict[name] = phone
    return f'Контакт {name} успішно змінено'

@input_error
def input_phone(name: str):
    return dict[name]

def input_show(*args):
    list = ['{:^10}:{:>15}'.format(k,v) for k,v in dict.items()]
    return "\n".join(list)


COMMANDS = {
    input_exit:["good bye", 'Допобачення', '.', 'exit'],
    input_hello:['hello', 'Привіт'],
    input_help:['help', 'Допомога'],
    input_add:['add', 'Додати'],
    input_change:["change", 'змінити'],
    input_phone:["phone"],
    input_show:["all"]
}


def parse_command(user_input: str):
    for k,v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(' ')


def main():
    while True:
        user_input = input('>>>')
        result, data = parse_command(user_input)
        print(result(*data))
        if result is input_exit:
            break


if __name__ == "__main__":
    main()
