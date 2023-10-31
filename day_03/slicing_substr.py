text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
substr1 = text[2:5]
substr2 = text[:5]
substr3 = text[3:20:3]  # char jumping
substr4 = text[::-1]  # reverse
substr5 = text[::-4]  # reverse n char jumps

print(substr1)
print(substr2)
print(substr3)
print(substr4)
print(substr5)

# testing
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase[9::3])

