# collection = single "variable" used to store multiple values
# List    = [] ordered and changeable. Duplicates Ok
# Set     = {} unordered and immutable, but ADD/Remove Ok. NO duplicates
# Tuple   = () ordered and unchangeable .Duplicates Ok. FASTER
#  dictionary = a collection of {key:value} pairs
#                 ordered and changeable. no duplicates


# LIST
#li=[input().strip().strip()]
#l=[map(int,input().strip().strip())]
bw=["dog","cat","cow","bat"]
k=["human"]
#print(bw[0])
#for b in bw:
    #print(b)
#k=bw.__iadd__("h g")
#k=k.__imul__(3)
#o=k.index("moggaa")
#k.insert(0,"puppy")
#k.append("love")
#bw.remove("dog")
#bw.pop(1)
#bw.reverse()
#bw.sort()
#m=bw.count("dog")
#h=len(bw)
#bw.pop() #pop will remove the last element or item in list
#print(bw)

#print("dog" in bw)
# ................................................................................

#SET
#se=set(input().strip().strip())
#s=set(map(int,input().strip().split()))
q={"add","sub","mul","div","add"}
#print(help(q))
#print(len(q))
#print("sub" in q)
#q.remove("add")
#q.add("add")
#q.pop() # Here pop will be removed randomly
#q.clear()
#print(q)
# ..................................................................................

# TUPLE
#tu=(input().strip().strip())
#t=(map(int,input().strip().strip()))
tup=("add","sub","mul","div","add")
#print(help(t))
#print(len(t))
#print(t.count("add"))
#print(t.index("add"))
#print(t)
# .................................................................................

# Dictionary

capitals={"usa": "washington dc",
          "india": "new delhi",
          "russia": "moscow"}
#print(capitals.get("usa"))
#print(dir(capitals))
capitals.update({"Mahi":2050})
#capitals.pop("usa")
#capitals.popitem()
#capitals.clear()
#keys=capitals.keys()
#for keys in capitals.keys():
    #print(keys)
#values=capitals.values()
#print(keys)
#for values in capitals.values():
    #print(values)
#values=capitals.values()
#for key ,value in capitals.items():
    #print(f"{key} : {value}")
#print(values)
#print(capitals)
menu={"mon": 1,
      "tue": 2,
      "wed": 3,
      "thu": 4,
      "fri": 5,
      "sat": 6,
      "sun": 7}
co=0
for keys,value in menu.items():
    co=co+value
print(co)

days=[]
count=0
