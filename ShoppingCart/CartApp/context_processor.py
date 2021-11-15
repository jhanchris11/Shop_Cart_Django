#nos va  a permitir guardar el carrito de forma global
def total_cart(request):
  total=0
  if request.user.is_authenticated:
    if 'cart' in request.session.keys():
      #todos los objetos que tiene el carrito que son objetos
      for key, value in request.session['cart'].items():
        total += int(value['accumulated'])
  return {"total_cart":total}
