pitajCenu=True
zbir_cena=0
while pitajCenu:
    cena = int(input("kolko kosta bato"))
    if(cena==0):
        pitajCenu=False
    else:
        zbir_cena=zbir_cena+cena
lova=int(input("koliko love dajes"))
print("kusur je",lova - zbir_cena,"din.")
