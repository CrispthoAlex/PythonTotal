from pathlib import Path

guide = Path("Cali", "La_Ermita.txt")
print(guide)
# Cali\La_Ermita.txt

guide = Path("Cali", "La_Ermita")
print(guide)
# Cali\La_Ermita

base = Path.home()
print(base)
# C:\Users\Home

guide = Path("Cali", "La_Ermita.txt")
print(guide)
# Cali\La_Ermita.txt

guide = Path(base, "Cali", "La_Ermita.txt")
print(guide)
# C:\Users\Home\Cali\La_Ermita.txt

guide = Path(base, "America", "Colombia", Path("Cali", "La_Ermita.txt"))
print(guide)
# C:\Users\Home\America\Colombia\Cali\La_Ermita.txt

guide2 = guide.with_name("Avenida_El_Rio.txt")
print(guide2)
# C:\Users\Home\America\Colombia\Cali\Avenida_El_Rio.txt

# Parent property
print(guide.parent)
# C:\Users\Home\America\Colombia\Cali
print(guide.parent.parent)
# C:\Users\Home\America\Colombia
print(guide.parent.parent.parent)
# C:\Users\Home\America
print([p for p in guide.parents])
"""
[
    WindowsPath('C:/Users/Home/America/Colombia/Cali'),
    WindowsPath('C:/Users/Home/America/Colombia'),
    WindowsPath('C:/Users/Home/America'),
    WindowsPath('C:/Users/Home'),
    WindowsPath('C:/Users'),
    WindowsPath('C:/')]
"""
ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
print(ruta)
print([f"{ruta.parents.index(p)} - {p}" for p in ruta.parents])
carpeta = ruta.parents[3]
print(f"ruta.parents[3] = {carpeta}")
print(ruta.stem)

guide3 = Path(Path.home(), "America")

for txt in Path(guide3).glob("*.txt"):
    print(f"Loop path => {txt}")
# C:\Users\Home\America\test_1.txt
# C:\Users\Home\America\test_2.txt

for txt in Path(guide).glob("**/*.txt"):
    print(f"Loop path => {txt}")
# C:\Users\Home\America\test_1.txt
# C:\Users\Home\America\test_2.txt
# C:\Users\Home\America\Colombia\Cali\La_Ermita.txt
# C:\Users\Home\America\Colombia\Cali\Avenida_El_Rio.txt

guide4 = Path("America", "Colombia", "Cali", "La_Ermita.txt")
print("guide4 => ", guide4)
in_America = guide4.relative_to(Path("America"))
in_Colombia = guide4.relative_to(Path("America", "Colombia"))

print("Relative path in in_America => ", in_America)
# Colombia\Cali\La_Ermita.txt
print("Relative path in in_Colombia => ", in_Colombia)
# Cali\La_Ermita.txt
