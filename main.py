# python3

def parallel_processing(n, m, data):
    output = []
    a = [(0, i) for i in range(n)]
    for i in range(m):
        time = data[i]
        next_t, threads = min(a)
        output.append((threads, next_t))
        a.remove((next_t, threads))
        a.append((next_t + time, threads))
    
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for pair in result:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()

