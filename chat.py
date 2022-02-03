from fileinput import filename
from mailbox import linesep
from pdb import line_prefix


def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='UTF-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open('output.txt', 'w') as f:
        for line in lines:
            f.write(line + '\n')

            
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)


main()