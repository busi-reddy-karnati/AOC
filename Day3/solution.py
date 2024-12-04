enabled = True

def invalid(num):
    for char in num:
        if not char.isdigit():
            return True
    return False

def process(line, i):
    if line[i] != '(':
        return 0
    for j in range(i+1, len(line)):
        if line[j] == ')':
            focus = line[i+1:j]
            focus_arr = focus.split(',')
            if len(focus_arr) != 2:
                return 0
            if invalid(focus_arr[0]) or invalid(focus_arr[1]):
                return 0
            return int(focus_arr[0]) * int(focus_arr[1])
    return 0
def parse_line(line):
    global enabled
    ans = 0
    for i in range(len(line)-2):
        if line[i] == 'd' and line[i+1] == 'o':
            if len(line) > i+3 and line[i+2] == '(' and line[i+3] == ')':
                enabled = True
            if len(line) > i+6 and line[i+2] == 'n' and line[i+3] == "'" and line[i+4] == 't' and line[i+5] == '(' and line[i+6] == ')':
                enabled = False
        if line[i] == 'm' and line[i+1] == 'u' and line[i+2] == 'l' and enabled:
            ans += process(line, i+3)
    return ans

def main():
    ans = 0
    with open('input.txt', 'r') as file:
        for line in file:
            ans += parse_line(line)
    print(ans)

if __name__ == "__main__":
    main()
