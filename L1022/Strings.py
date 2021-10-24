str1 = r"Tolga' \n \t \\\ Ovatman"
#print(str1)
str2 = r'''
Tolga Ovatman


sdfsdf
\n
sdf
"""" ' '
'''
# print(str2)

str3 = "Tolga\nOvatman"
print(len(str3))

print(str3[4])
print(str3[2:5])
print(str3[6:])
print(str3[:5])
str3 = "Tolga"
print(str3[1:-2])
print(str3[-3])

str4 = "Ovatman"
print(str3+" "+str4)
print(str3*5)
print("ol" in str3)

str5 = "\n"
print(str5.isdigit())
print(str5.isalpha())
print(str4.upper())

str6 = "   Tolga O\tvatman   "
print(str6.strip().replace("\t", "X"))
print(str6.rfind("a"))
str7 = "Tolga Ovatman"
print(str7.split("a"))
strspl = str7.split("a")
print(".".join(strspl))