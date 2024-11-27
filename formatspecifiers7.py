# format specifiers = {:flags} format a value based on what
#                                  flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# = : (number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, =comma separator

p1=3.14159
p2=-9965.65
p3=1254456.345
#print(f" price1 is ${p1:.2f}")
#print(f" price1 is ${p1:.6f}")
#print(f" price1 is ${p1:10}")
#print(f" price1 is ${p2:10}")
#print(f" price1 is ${p3:10}")
#print(f" price1 is ${p1:>10}")
#print(f" price1 is ${p1:<10}")
#print(f" price1 is ${p1:^10}")
#print(f" price1 is ${p2:.2f}")
print(f" price1 is ${p3:,}")
print(f" price1 is ${p2:+,.2f}")

