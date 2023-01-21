# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode_rle(file):
    with open(file, 'r', encoding = 'UTF-8') as r_rle:
        data = r_rle.read()
    with open(f'rle_{file}', 'w', encoding = 'UTF-8') as w_rle:
        temp = ''
        length = 1
        for item in data:
            if item != temp:
                w_rle.write(f'|{length}^{temp}' if length > 4 else temp * length)
                temp = item
                length = 1
            else: length += 1
        w_rle.write(f'|{length}^{temp}' if length > 4 else temp * length)
                        
def decode_rle(file):
    with open(file, 'r', encoding = 'UTF-8') as r_rle:
        data = r_rle.read()
        # print(len(data))
        data = data.split('|')
    with open(f'new_{file}', 'w', encoding = 'UTF-8') as a_rle:
        for item in data:
            if '^' in item:
                item = item.split('^')
                item = int(item[0]) * item[1][0] + item[1][1:]
            a_rle.write(item)
    
def main():
    encode_rle('test.txt')
    decode_rle('rle_test.txt')

if __name__ == '__main__':
    main()