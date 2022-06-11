# Lab 4

# OBJECTIVES :
1) Preparing templates for Django.
2) Creating another templates and extending the base template.

# INTRODUCTION :
A Django template is a text document or a Python string marked-up using the Django template language. Some constructs are recognized and interpreted by the template engine. The main ones are variables and tags.

A template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags. Everything else is output as is.

The syntax of the Django template language involves four constructs.
* Variables
* Tags
* Filters 
* Comments

# PROCEDURES :
1) create a directory named templates and add a base template file named "base.html".

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <link rel="stylesheet"href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.minss"/>
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <scriptsrc="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" />
        <title>{% block title %} Electronics Commerce {% endblock %}</title>
        <style type="text/css">
            .min-h-100 { min-height: 100%; }
        </style>
    </head>
    <body>
    <div class="row">
        <div id="header" class="bg-info col-sm-12 col-md-12 col-lg-12">
            <div class="row">
                <div class="col-sm-4 col-md-4 col-lg-4">
                    <img src="https://img.favpng.com/23/7/24/logo-e-commerce-digital-marketing-brand-trade-png-favpng-xTcxcPuHCYQBUh9P8q30ETQji.jpg" alt="E-commerce Logo" style="height:50px; width:auto;" />
                </div>
                <div class="col-sm-7 col-md-7 col-lg-7">
                    <h2>{% block header %} Electronic Commerce {% endblock %}</h2>
                </div>
                <div class="col-sm-1 col-md-1 col-lg-1">
                    <a class="btn btn-success btn-sm ml-3" href="#cart-model" data-toggle="modal">
                        <span>Cart</span>
                        <span class="badge badge-light">
                            <label id="cart_qty">0</label>
                        </span>
                    </a>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div id="sidebar" class="min-h-100 min-h-800 bg-light border col-sm-3 col-md-3 col-lg-3">
        {% block sidebar %}
            <ul>

                <li><a href="/admin/"><i class="fa fa-user" aria-
                hidden="true"></i> Admin</a></li>

                <li><a href="/"><i class="fa fa-search" aria-hidden="true"></i>
                Product</a></li>

                <li><a href="/cart/"><i class="fa fa-shopping-cart" aria-
                hidden="true"></i> Cart</a></li>

            </ul>
        {% endblock %}
        </div>
        <div id="content" class="min-h-100 bg-light col-sm-9 col-md-9 col-lg-9">
            {% block content %}{% endblock %}
        </div>
    </div>
    </body>
    </html>
    
2) In setting.py add the following code:

        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [BASE_DIR / 'templates'],
                .......
            }
        ]

3) Inside “product_module”, create a directory “templates”. Create a html “index.html” and add the following code:

        {% extends "base.html" %}
        {% block title %} Search {% endblock %}
        {% block header %} Search Product {% endblock %}
        {% block content %}
        
        <!--Navbar-->
        <nav class="navbar navbar-expand-lg">
            <div>
                <!-- Links -->
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active"><a class="nav-link text-dark" href="/ ">All</a></li>
                    {% for category in categories %}
                        <li class="nav-item"><a class="nav-link text-dark"href="/?category={{category.id}}">{{category.name}}</a></li>
                    {% endfor %}
                    {% for brand in brands %}
                        <li class="nav-item">href="/?brand={{brand.id}}">{{brand.name}}</a></li>
                    {% endfor %}
                </ul>
                <!-- Links -->
            </div>
            <div>
                <form class="form-inline" method="POST">
                {% csrf_token %}
                    <div>
                        <input name="query" class="form-control" type="text"placeholder="Search/enter price-range" aria-label="Search"value="{{search_query}}">
                    </div>
                </form>
            </div>
            </nav>
                <!--/.Navbar-->
                {% for product in products %}
                <div class="row border bg-light">
                    <div class="col-md-4">
                        <div class="text-center">
                            <img src="{{ product.image_url }}" style="height:200px; width:auto;" alt="{{ product.name }}">
                        </div>
                    </div>
                    <div class="col-md-3">
                        <span class="btn btn-danger disabled">{{ product.brand.name}}</span>
                        <span class="btn btn-info disabled">{{ product.category.name}}</span>
                        <h3>{{ product.name }}</h3>
                        <h4 class="bold text-secondary">
                            <strong>NRs. {{ product.price }}</strong>
                        </h4>
                        <form class="d-flex" action="/cart" method="GET">
                        <!-- Default input -->
                            <input type="hidden" name="id" value="{{product.id}}" />

                        <input type="number" name="qty" value="1" aria-label="Search" class="form-control" style="width: 100px">

                        <button id="btn-add-to-cart" class="btn btn-primary btn-md" type="submit" data-toggle="modal" data-target="#cart-model"><i class="fa fa-shopping-cart" aria-hidden="true"></i> Add to cart</button>

                    </form>
                </div>
                <div class="col-md-5">
                    <table class="table table-sm">
                    <tr>
                        <td>Available Quantity</td>
                        <td>{{product.quantity}}</td>
                    </tr>
                    <tr>
                        <td>Color Code</td>
                        <td><div style="height: 25px; width: 25px; background-color: {{ product.color_code }};"></div></td>

                    </tr>
                    <tr>
                        <td>Brand</td>
                        <td>{{ product.brand.name }}</td>
                    </tr>
                    <tr>
                        <td>Category</td>
                        <td>{{ product.category.name }}</td>
                    </tr>
                    <tr>
                        <td>Registered On</td>
                        <td>{{ product.registered_on }}</td>
                    </tr>
                    <tr>
                        <td>Is Active</td>
                        <td>
                        {% if product.is_active %}
                            <input type="checkbox" checked />
                        {% else %}
                            <input type="checkbox" />
                        {% endif %}
                        </td>
                    </tr>
                    </table>
                </div>
            </div>
            {% endfor %}
            {% endblock %}

4) In views.py add the follwoing code:

        from django.db.models import Q
        from .models import Product, Brand, Category
        ...
        def index(request):
            if request.method == "GET":
                category_id = request.GET.get("category")
                brand_id = request.GET.get("brand")
                if category_id:
                    filter_query = Q(category__id=category_id)
                products = Product.objects.filter(filter_query)
                elif brand_id:
                    filter_query = Q(brand__id=brand_id)
                products = Product.objects.filter(filter_query)
                else:
                    products = Product.objects.all()
                    categories = Category.objects.all()
                    brands = Brand.objects.all()
                    context = {
                        'products': products,
                        'categories': categories,
                        'brands': brands,
                        'search_query': '',
                    }
                return render(request, 'index.html', context)
            elif request.method == "POST":
                q = request.POST.get("query")
                if "-" in q:
                price_values = q.split("-")
                filter_query = Q(price__gte=price_values[0]) &
                Q(price__lte=price_values[1])
                else:
                    filter_query = Q(name__icontains=q) | Q(price__icontains=q) |Q(brand__name__icontains=q)
                    products = Product.objects.filter(filter_query)
                    categories = Category.objects.all()
                    brands = Brand.objects.all()
                    context = {
                        'products': products,
                        'categories': categories,
                        'brands': brands,
                        'search_query': q,
                    }
                return render(request, 'index.html', context)

5) In urls.py add the path:

        from django.contrib import admin
        from django.urls import path, include
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('product_module.urls')),
        ]

6) Run the server and check the output is correct or not.


# OUTPUT :
![image of product model]()


# CONCLUSION :
Here in this lab session we understood how a base template is extended by another template and how to manupulate data and retrive from database using django