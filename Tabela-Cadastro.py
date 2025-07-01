people = {}
counter = 1
while True:
    name = str(input('Nome: ')).title()
    while True:
        sex = input('Sexo [F/M]:').lower()[0]
        if sex not in 'fm':
            print('ERRO! Por favor, digite F para Feminino e M para masculino!')
        else:
            break
    while True:
        try:
            age = int(input('Idade: '))
            break
        except ValueError:
            print('Por favor, digite apenas números na opção idade!!')
    user_date = {
        'name': name,
        'sex': sex,
        'age': age
    }
    people[f'registration_{counter}'] = user_date
    counter += 1
    opt_continue = input('Deseja continuar? [S/N]').lower()[0]
    if opt_continue == 'n':
        break
print('-=' * 50)
name_counter = len(people)
print(f'A) Ao todo temos {name_counter} pessoas cadastradas.')
average_age = sum([dates['age'] for dates in people.values()]) / len(people)
print(f'B) A média de idade é de {average_age:.2f} anos.')
women = [sex['name'] for sex in people.values() if sex['sex'] == 'f']
print(f'C) As mulheres cadastradas foram:', ', '.join(women))
above_average = [(dates['name'], dates['sex'], dates['age']) for dates in people.values() if dates['age'] >= average_age]
print(f'D) Informações de pessoas acima da média:')
for people in above_average:
    print(f'    -  Nome {people[0]}; Sexo {people[1].upper()}; Idade {people[2]}.')
print('FINALIZADO')