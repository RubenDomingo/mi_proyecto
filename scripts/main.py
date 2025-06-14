from mi_proyecto import (
    burla_A,
    burla_E,
    burla_I,
    burla_O,
    burla_U,
    get_binario,
    num_romanos,
)

print(burla_A('No me gustan los macarrones'))
print(burla_E('No me gustan los macarrones'))
print(burla_I('No me gustan los macarrones'))
print(burla_O('No me gustan los macarrones'))
print(burla_U('No me gustan los macarrones\n'))

print(get_binario(5))
print(get_binario(10))
print(f'{get_binario(15)}\n')

for i in range(1, 21):
    if i == 20:
        print(f'{num_romanos(i)}\n')
    else:
        print(num_romanos(i), end = ' - ')

for i in range(40, 201, 10):
    if i == 200:
        print(f'{num_romanos(i)}\n')
    else:
        print(num_romanos(i), end=' - ')

for i in range(900, 2001, 50):
    if i == 2000:
        print(f'{num_romanos(i)}\n')
    else:
        print(num_romanos(i), end=' - ')