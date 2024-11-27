import time
k = int(input("enter the timer in seconds :"))
for i in range(k,0,-1):
    s=i%60
    m=int(i/60)%60
    h=int(i/3600)
    print(f"{h:02}:{m:02}:{s:02}")
    time.sleep(1)
print("HAPPY NEW YEAR")
