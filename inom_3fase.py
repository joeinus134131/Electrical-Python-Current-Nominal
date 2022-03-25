# Program I nominal

daya = float(input('Daya motor : '))
v = float(input('Tegangan : '))

cosphi = 0.85
i = float(input('Arus Standar :'))

inom = float(daya/(v*cosphi*1.73))
print("Arus Nominal = ", inom)

#istandar = float()
istandar = float(i*1.25)


if inom > istandar:
    print("Kondisi motor : Overload")
else:
    print("Kondisi motor : Aman")
