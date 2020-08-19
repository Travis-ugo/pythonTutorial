is_hot = False
is_cold = False

print ('take off your jacket')
if is_hot:
    print('ok i will after all its a hot day')
elif is_cold:
     print('mans not hot')
else:
    print('enjoy the weather')


price = 100
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
     down_payment = 0.2 * price
print(f'Down payment: #{down_payment}')
