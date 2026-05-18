print("---Programu ya Matokeo  ya Wanafunzi (PCM)---")

jina = input("Jina la Mwanafunzi: ")
shule = input("Jina la Shule : ")
darasa = input("Kidatu cha Mwanafunzi(Advance level) : ")
alama1 = int(input("Alama ya Somo la Mathematics: "))
alama2 = int(input("Alama ya Somo la Physics: "))
alama3 = int(input("Alama ya Somo la Chemistry: "))
alama4 = int(input("Alama ya Somo la General study: "))
mwalimu = input("Jina la Mwalimu Mkuu: ")

jumla = alama1 + alama2 + alama3 + alama4

wastani = jumla/4

if jumla >= 200 :
    print("Umefaulu")
else:
    print("Jitihada inahitajika zaidi usivunjike moyo")
    
print("\n~~~RIPOTI YA MATOKEO YA MWANAFUNZI 2026~~~")
print(f"Jina la Mwanafunzi: {jina}")
print(f"Shule ya Mwanafunzi: {shule}")
print(f"Darasa la Mwanafunzi (kidatu cha 5-6): {darasa}")
print(f"Jumla ya Alama: {jumla}")
print(f"Wastani wa Mwanafunzi: {wastani}")
print(f"Jina la Mwalimu Mkuu: {mwalimu}")


with open("takwimu.tex", "w") as file:
    file.write(f"{jina} , {shule} , {darasa} , {jumla} , {wastani} , {mwalimu}")