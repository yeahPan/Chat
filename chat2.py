from fileinput import filename
from mailbox import linesep
from pdb import line_prefix

#讀出檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='UTF-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

#轉換(計算)
def convert(lines):
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0

    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            for m in s[2:]:
                if '貼圖' in line:
                    allen_sticker_count += 1
                elif '圖片' in line:
                    allen_image_count += 1
                else:
                    allen_word_count += len(m)

        if name == 'Viki':
            for m in s[2:]:
                if s[2] == '貼圖':
                    viki_sticker_count += 1
                elif s[2] == '圖片':
                    viki_image_count += 1
                else:
                    viki_word_count += len(m)

    print('Allen講了', allen_word_count, '個字')
    print('Allen傳了', allen_sticker_count, '個貼圖')
    print('Allen傳了', allen_image_count, '張照片')
    
    print('Viki講了', viki_word_count, '個字')
    print('Viki傳了', viki_sticker_count, '個貼圖')
    print('Viki傳了', viki_image_count, '張照片')



            
def main():
    lines = read_file('LINE-Viki.txt')
    convert(lines)
#    write_file('output.txt', lines)


main()