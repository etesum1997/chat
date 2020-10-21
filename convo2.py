
def read_file(filename): 
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ') # 每行有空格的地方就切一刀，放入清單
        time = s[0]
        name = s[1]
        if name == 'Allen':
            for msg in s[2:]:
                if msg == '貼圖':
                    allen_sticker_count += 1
                elif msg == '圖片':
                    allen_image_count += 1
                else:
                    allen_word_count += len(msg)
        if name == 'Viki':
            for msg in s[2:]:
                if msg == '貼圖':
                    viki_sticker_count += 1
                elif msg == '圖片':
                    viki_image_count += 1
                else:
                    viki_word_count += len(msg)
    print('Allen講了', allen_word_count, '個字 傳了', allen_sticker_count, '個貼圖及', allen_image_count, '張圖片')
    print('Viki講了', viki_word_count, '個字 傳了', viki_sticker_count, '個貼圖及', viki_image_count, '張圖片')


def write_file(filename, lines):
    with open(filename, 'w', encoding= 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-viki.txt')
    lines = convert(lines)


main()