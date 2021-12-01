def main():
    inputnum = int(input())
    if inputnum == 0 or inputnum == 1:
        return inputnum
    fibnum = []
    fibnum.append(0)
    fibnum.append(1)
    i = 1
    while fibnum[i] < inputnum:
        i += 1
        tmpnum = fibnum[i-1] + fibnum[i-2]
        fibnum.append(tmpnum)
    
    return fibnum

if __name__=='__main__':
    print(main())