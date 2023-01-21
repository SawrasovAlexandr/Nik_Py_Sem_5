# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# на семинаре Николай говорил, что ищем 'абв' независимо от регистра


def main():
    text = 'АБВ ылоажы фыыдлх абв Зщышф вабвв ффлжв абвин'
    print(text)
    text = ' '.join([item for item in text.split() if 'абв' not in item.lower()])
    print(text)


if __name__ == '__main__':
    main()