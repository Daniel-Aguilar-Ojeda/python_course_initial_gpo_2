#Funciones

def saludar(name:str) -> str:
    '''Retorna un salud cordial'''
    return f"Hola, {name}. Bienvenido al curso. \n"

students = ["Jona", "Daniel", "Luis"]

for student in students:
    print(saludar(student))

# Lambda, maps y filtes

mask_string = lambda s, mask_char='#': len(s)*mask_char
filter_d = lambda s: s[0] == "D"

name_masked = list(map(mask_string, students))
name_filtered = list(filter(filter_d, students))

print(name_masked)
print(name_filtered)


# Ejercicio IVA
print("\n")
print("***** Ejercicio IVA *****\n")

apply_iva = lambda price, iva: round(price * (iva + 1), 2)

apply_iva_to_products = lambda product, iva = 0.16: {"product": product["product"], "price": apply_iva(product["price"], iva)}


products = [{"product": "apple", "price": 2.6}, {"product": "pineple", "price": 3.4}, {"product":"orange", "price": 5.4}]

print("Products without iva: ", products)


products_with_iva = [apply_iva_to_products(p) for p in products]

print("Products with iva: ", products_with_iva)


""" iva: float = 1.16

products_with_iva = [{
    "product": p["product"],
    "price": p["price"] * iva
} for p in products]

print("Products with iva: ", products_with_iva) """

print("\n")
print("***** Ejercicio IVA *****\n")

