import random
print("*****************************")
print("***WELCOME TO BOUNTY HUNT****")
print("*****************************")
def spin():
    x = ['❤️', '🤡', '😍', '😊', '🔅']
    return [random.choice(x) for i in range(3)]
def printing(k):
    print(" | ".join(k))
def bounty(k,head):
    if k[0]==k[1]==k[2]:
        print("****************************")
        print("you win the hunt")
        print("****************************")
        if k[0]=='❤️':
            return 100*head
        elif k[0]=='🤡':
            return 80*head
        elif k[0]=='😍':
            return head*60
        elif k[0]=='😊':
            return head*40
        elif k[0]=='🔅':
            return head*20
        else:
            return 0
    else:
        return 0
def main():
    bal = 100
    while bal>0:
        print("symbols are ❤️ 🤡 😍 😊 🔅 ")
        print(f"balance is : ${bal}")
        head=int(input("enter the head : $"))
        if head>0:
            k=spin()
            printing(k)
            v=bounty(k,head)
            if v>=0:
                bal=bal+v
                v=0
            else:
                continue
        elif head==0 and head>=bal:
            print("head must be grater than 0")
            continue
        elif head>bal:
            print("out of balance")
            continue
        else:
            print("give the valid value")
            continue
        bal=bal-head
if __name__ == '__main__':
    main()


