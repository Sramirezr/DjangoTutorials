from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })
        return context


class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = [
            {"id": 1, "name": "TV Samsung", "price": 1000, "image": "https://example.com/tv.jpg"},
            {"id": 2, "name": "iPhone", "price": 2000, "image": "https://example.com/iphone.jpg"},
            {"id": 3, "name": "Chromecast", "price": 50, "image": "https://example.com/chromecast.jpg"},
            {"id": 4, "name": "Nintendo Switch", "price": 300, "image": "https://example.com/switch.jpg"},
        ]
        return render(request, self.template_name, viewData)


class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        products = [
            {"id": 1, "name": "TV Samsung", "price": 1000, "description": "A high-quality smart TV", "image": "https://example.com/tv.jpg"},
            {"id": 2, "name": "iPhone", "price": 2000, "description": "Latest model iPhone", "image": "https://example.com/iphone.jpg"},
            {"id": 3, "name": "Chromecast", "price": 50, "description": "Stream from your devices", "image": "https://example.com/chromecast.jpg"},
            {"id": 4, "name": "Nintendo Switch", "price": 300, "description": "Portable and home gaming console", "image": "https://example.com/switch.jpg"},
        ]

        product = next((p for p in products if p["id"] == id), None)
        if product is None:
            return redirect('products.index')

        viewData = {}
        viewData["title"] = f"{product['name']} - Online Store"
        viewData["subtitle"] = f"{product['name']} - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)


class CartView(View):
    template_name = 'cart/index.html'

    def get(self, request):
        products = {
            1: {'name': 'TV Samsung', 'price': '1000'},
            2: {'name': 'iPhone', 'price': '2000'}
        }

        cart_products = {}
        cart_product_data = request.session.get('cart_product_data', {})

        for key, product in products.items():
            if str(key) in cart_product_data.keys():
                cart_products[key] = product

        view_data = {
            'title': 'Cart - Online Store',
            'subtitle': 'Shopping Cart',
            'products': products,
            'cart_products': cart_products
        }
        return render(request, self.template_name, view_data)

    def post(self, request, product_id):
        cart_product_data = request.session.get('cart_product_data', {})
        cart_product_data[str(product_id)] = product_id
        request.session['cart_product_data'] = cart_product_data

        return redirect('cart_index')


class CartRemoveAllView(View):
    def post(self, request):
        if 'cart_product_data' in request.session:
            del request.session['cart_product_data']
        return redirect('cart_index')
    
class CartAddView(View):
    def post(self, request, product_id):
        cart_product_data = request.session.get('cart_product_data', {})
        cart_product_data[str(product_id)] = product_id
        request.session['cart_product_data'] = cart_product_data
        return redirect('cart_index')
