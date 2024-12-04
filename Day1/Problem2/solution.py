from collections import Counter

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
    b_counter = Counter(b_list)
    ans = 0
    for i in range(len(a_list)):
        ans += a_list[i] * b_counter[a_list[i]]
    print(ans)

if __name__ == "__main__":
    main()
