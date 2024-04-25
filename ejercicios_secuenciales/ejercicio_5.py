costoproducto=int(input("digite el valor de la compra : "))
oferta=int(input("digite la oferta : "))

descuentocompra=oferta / 100

oferta=oferta * costoproducto
valorfinal=costoproducto-descuentocompra
print("la compra fue", costoproducto,"oferta",descuentocompra,"%","valor final es" , valorfinal)