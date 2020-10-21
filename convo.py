
def read_file(filename): 
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines
def convert(lines):
    new = []
    person = None # 為了避免第一行不是person而出現bug
    for line in lines: 
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: # 如果person是有值的話，在執行下面這行
            new.append(person + ': ' + line)
    return new
def write_file(filename, lines):
    with open(filename, 'w', encoding= 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)
main()

