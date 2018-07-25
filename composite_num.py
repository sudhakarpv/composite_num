# composite_num
def main():
    pass
    n=int(input())
    flag=0
    if(n>3):
        for i in range(1,n):
            if(n%i==0):
                flag+=1
    if (flag>1):
        print("yes")
    else:
        print("no")
if __name__ == '__main__':
    main()
