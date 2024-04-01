name_1 = input("enter 1st name :")
name_2 = input("enter 2nd name :")


t = name_1.count('t')
r = name_1.count('r')
u = name_1.count('u')
e = name_1.count('e')
t_2 = name_2.count('t')
r_2 = name_2.count('r')
u_2 = name_2.count('u')
e_2 = name_2.count('e')
true = t+r+u+e+t_2+r_2+u_2+e_2

l = name_1.count('l')
o = name_1.count('o')
v = name_1.count('v')
e = name_1.count('e')
l_2 = name_2.count('l')
o_2 = name_2.count('o')
v_2 = name_2.count('v')
e_2 = name_2.count('e')
love = l+o+v+e+l_2+o_2+v_2+e_2

love_score = int(str(true) + str(love))

if love_score > 10 or love_score > 90:
    print(f"Your love score is {love_score} and you go togather like coke and mentos ")