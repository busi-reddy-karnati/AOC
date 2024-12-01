def main():
    a_list = []
    b_list = []
    
    # Read input from file
    with open('input.txt', 'r') as file:
        for line in file:
            # Split each line into two numbers and convert to integers
            a, b = map(int, line.strip().split())
            a_list.append(a)
            b_list.append(b)
    a_list.sort()
    b_list.sort()
    ans = 0
    for i in range(len(a_list)):
        ans += abs(a_list[i] - b_list[i])
    print(ans)

if __name__ == "__main__":
    main()
