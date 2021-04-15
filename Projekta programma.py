a = int(input("Cik daudz cilveku edis pirmo edienu? - "))
i = float(input("Cik maksa sis ediens? (eiro) - "))
q = int(input("Ievadiet skaitli - " ))
if q>1:
    print ("kopeja summa ir", (a*i)+20)
else:
    b = int(input("Cik cilveku edis otro edienu? - "))
    t = float(input("Cik maksa sis ediens? (eiro) - "))
    q = int(input("Ievadiet skaitli - " ))
if q>1:
    print ("kopeja summa ir", (a*i)+(b*t)+20)
else:
    c = int(input("Cik cilveku edis treso edienu? - "))
    x = float(input("Cik maksa sis ediens? (eiro) - ")) 
    q = int(input("Ievadiet skaitli - " ))
if q>1:
    print ("kopeja summa ir", (a*i)+(b*t)+(c*x)+20)
else:
    d = int(input("Cik cilveku edis cetro edienu? - "))
    z = float(input("Cik maksa sis ediens? (eiro) - ")) 
    q = int(input("Ievadiet skaitli - " ))
if q>1:
    print ("kopeja summa ir", (a*i)+(b*t)+(c*x)+(d*z)+20)
else:
    v = int(input("Cik cilveku edis piekto edienu? - "))
    m = float(input("Cik maksa sis ediens? (eiro) - ")) 
    q = int(input("Ievadiet skaitli - " ))
if q>1:
    print ("kopeja summa ir", (a*i)+(b*t)+(c*x)+(d*z)+(v*m)+20)