# Lab 2

# OBJECTIVES:
    1) Initializing the product_module.

    2) Making different modules suitable as per needs and registering to database.

# INTRODUCTION:


# PROCEDURES:
1) In models.py, create a model for brands

        code:
            class Brand(models.Model):
                name = models.CharField(max_length=200)
                is_active = models.BooleanField()

2) Add the brand table to the database by python manage.py makemigartions and pyhton manage.py maigrate

3) In the 'admin.py', add the content at the admin panel using following code:

        from.models import Brand
        admin.site.register(Brand)

4) Run the server and verify the table by performing the CRUD operation.

            python manage.py runserver

5) In the 'model.py', edit the code for the brand model with following code:

        class Brand(models.Model):
            name = models.CharField(max_length=200)
            is_active = models.BooleanField()

6) In the same file, edit the code for the category model

        class Category(models.Model):
            name = models.CharField(max_length=200)
            is_active = models.BooleanField()
            class Meta:
                verbose_name_plural = "Categories"

7) Add the necessary fields to the product model

        code:
            class Product(models.Model):
                name = models.CharField(max_length=200)
                price = models.FloatField()
                quantity = models.IntegerField()
                image_url = models.CharField(max_length=500)
                color_code = models.CharField(max_length=20)
                brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
                category = models.ForeignKey(Category, on_delete=models.CASCADE)
                registered_on = models.DateTimeField()
                is_active = models.BooleanField()

8) Save the changes to the database.

9) To enable the category and product models in the admin, add the following code:

        from .models import Brand, Category, Product
        admin.site.register(Brand)
        admin.site.register(Category)
        admin.site.register(Product)

10) Run the project server and verify the CRUD operations for brand, category and product respectively

        python manage.py runserver



# OUTPUT: 

![image of category model] 

# CONCLUSION:
