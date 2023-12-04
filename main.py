with open('pium.txt', 'r', encoding = "UTF-8") as file:
    for line in file:
        print(line)


author = input('Хто написвв ці рядки?')
with open('pium.txt', 'a', encoding= "UTF-8") as file:
    file.write(f'({author})\n')
while True:
    answer = input("Бажаєте додати ще одну цитату? (так / ні))")
    answer = answer.lower()
    if answer == 'так':
        quote = input('Введіть цитату: ')
        author = input("Введіть автора:")
        file = open("pium.txt", 'a', encoding= "UTF-8")
        file.write(f"{quote}\n({author})\n")
    else:
        break
with open('pium.txt', 'r', encoding= "UTF-8") as file:
    for line in file:
        print(line)
