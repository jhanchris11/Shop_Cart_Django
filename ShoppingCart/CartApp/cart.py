class Cart :
  def __init__(self,request):
    # Llevar una solicitud porque nos va a permitir a mantener la sesion
    self.request= request
    self.session = request.session
    cart = self.session.get('cart')
    if not cart:
      #diccionario vacio
      self.session['cart']={}
      self.cart=self.session['cart']
    else:
      self.cart=cart

  def add(self, product):
    id = str(product.id)
    print('Product',product)
    if id not in self.cart.keys():
      self.cart[id] = {
        'product_id':product.id,
        'name':product.name,
        'price_unit':product.price,
        'accumulated':product.price,
        'amount':1
      }
    else:
      #si el producto ya existe
      self.cart[id]['price_unit']=product.price
      self.cart[id]['amount']+=1
      self.cart[id]['accumulated']+=product.price
    self.save_cart()

  def save_cart(self):
    # va ser igual al carrito que actualizamos
    self.session['cart'] = self.cart
    self.session.modified = True

  def delete(self,product):
    id = str(product.id)
    if id in self.cart:
      del self.cart[id]
      self.save_cart()

  def subtract(self , product):
    id = str(product.id)
    print(id)
    if id in self.cart.keys():
       self.cart[id]['amount']-=1
       self.cart[id]['accumulated']-=product.price
       if self.cart[id]['amount'] <=0 :self.delete(product)
       self.save_cart()

  def clean(self):
     self.session['cart']={}
     self.session.modified = True
