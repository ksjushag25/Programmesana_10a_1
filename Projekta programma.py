a = int(input("Cik daudz cilveku edis pirmo edienu? - "))
i = float(input("Cik maksa sis ediens? (eiro) - "))

b = int(input("Cik cilveku edis otro edienu? - "))
t = float(input("Cik maksa sis ediens? (eiro) - "))

c = int(input("Cik cilveku edis treso edienu? - "))
x = float(input("Cik maksa sis ediens? (eiro) - ")) 

pe = (a*i)+20
oe = (b*t)+20
te = (c*x)+20

allmoney = (pe + oe + te)

print("kopeja summa pirma ediena ir", pe)
print("kopeja summa otra ediena ir", oe)
print("kopeja summa tresa ediena ir", te)

print("kopeja summa par visiem edieniem ir", allmoney)
