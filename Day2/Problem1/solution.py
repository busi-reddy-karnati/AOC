def safe(report):
    if report[0] > report[1]:
        for i in range(len(report)-1):
            if report[i] <= report[i+1] or report[i]-report[i+1] > 3:
                return False
        return True
    else:
        for i in range(len(report)-1):
            if report[i] >= report[i+1] or report[i+1]-report[i] > 3:
                return False
        return True

def safe_helper(report):
    for i in range(len(report)):
        if safe(report[:i]+report[i+1:]):
            return True
    return False

def main():
    ans = 0
    # Read input from file
    with open('input.txt', 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if safe_helper(report):
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
