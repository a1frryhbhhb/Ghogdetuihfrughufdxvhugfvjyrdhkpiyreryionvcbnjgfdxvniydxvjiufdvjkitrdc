# homework
def lvl1():
    print('choose:')
    print('  upper (все буквы в старший регистр)')
    print('  lower (все буквы в младший регистр)')
    print('  capitalize (первая буква в старший регистр)')
    
    action=input()
    
    if action=='upper':
        print(text.upper())
    elif action=='lower':
        print(text.lower())
    elif action=='capitalize':
        print(text.capitalize())

def lvl2():
    print('choose:')
    print('  replace (замена подстроки на другую)')
    print('  index (индекс первого вхождения подстроки в строку)')
    print('  find (то же самое; только строки)')
    print('  count (подсчет вхождений строки)')
    
    action=input()
    
    if action=='replace':
        print('enter what to replace')
        a=input()
        print('with what')
        b=input()
        print(text.replace(a,b))
    elif action=='index':
        print('what substring to index')
        substr=input()
        print(f'{substr} is located at {text.index(substr)}')
    elif action=='find':
        print('what substring to find')
        substr=input()
        print(f'{substr} is located at {text.find(substr)}')
    elif action=='count':
        print('what to count')
        substr=input()
        print(f'there is {text.count(substr)} {substr} in {text}')
        
def lvl3():
    print('choose')
    print('  split (деление строки указанным разделителем)')
    print('  join (соед куски строки)')
    
    action=input()
    
    if action=='split':
        print('enter divider')
        divider=input()
        print(text.split(divider))
    elif action=='join':
        print(''.join(text.split()))
    
def lvl4():
    print('choose')
    print('  isdigit (провер число ли строка)')
    print('  isalpha (состоит ли строка из букв)')
    print('  strip (убирает по краям)')
    print('  format (ф строки)')
    
    action=input()
    
    if action=='isdigit':
        print(text.isdigit())
    elif action=='isalpha':
        print(text.isalpha())
    elif action=='strip':
        print('enter chars')
        chars=input()
        print(text.strip(chars))
    elif action=='format':
        print('enter values')
        values=input().split()
        print(text.format(*values))

print('enter text')
text=input()

while True:
    print('choose level 1-4')
    lvl=input()
    if lvl=='1':
        lvl1()
    elif lvl=='2':
        lvl2()
    elif lvl=='3':
        lvl3()
    elif lvl=='4':
        lvl4()
    else:
        print('try again')
        break
