n=int(input())

information=[[],[],[]]

for i in n:

    name=(input('введите имя покупателя '))
    information[0].append(name)

    product = (input('введите имя продукта '))
    information[1].append(product)

    count=float(input('введите цену товара '))
    information[2].append(count)

print(information)


