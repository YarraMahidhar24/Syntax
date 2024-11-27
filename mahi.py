if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        l1=list(input().strip().split())

        if l1[0]=="insert":
            l.insert(int(l1[1]),int(l1[2]))
    print(l)
