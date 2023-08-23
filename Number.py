# Di code ini tentang tipe data Number dan ada conversi tipedata juga.

# Number Integer
varInt = 5
varInt1 = 38483848384384834
varInt2 = -15

print(varInt, type(varInt))
print(varInt1, type(varInt1))
print(varInt2, type(varInt2),"\n")


# Number Float
varFloat = 5.0
varFloat1 = 94.9
varFloat2 = -15.0

print(varFloat, type(varFloat))
print(varFloat1, type(varFloat1))
print(varFloat2, type(varFloat2),"\n")

# Number Complex
varComplex = 5j
varComplex1 = 91.0j
varComplex2 = -10.0j

print(varComplex, type(varComplex))
print(varComplex1, type(varComplex1))
print(varComplex2, type(varComplex2))

# Covert dataType
intToFLoat = float(varInt)
floatToInt = int(varFloat)
intToString = str(varInt)
print("\nConvert\n",intToFLoat,type(intToFLoat))
print(floatToInt, type(floatToInt))
print(intToString, type(intToString))     
