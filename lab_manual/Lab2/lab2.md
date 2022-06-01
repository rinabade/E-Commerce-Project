# Lab 2

# OBJECTIVES:
    1) Initializing the product_module.

    2) Making different modules suitable as per needs and registering to database.

# INTRODUCTION:

A model is the single, definitive source of information about data. It contains the essential fields and behaviors of the data that is being stored. Generally, each model maps to a single database table.

The basics:
* Each model is a Python class that subclasses django.db.models.Model.
* Each attribute of the model represents a database field.
* With all of this, Django gives an automatically-generated database-access API


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

![image of product model](https://github.com/rinabade/E-Commerce-Project/blob/master/lab_manual/Lab2/284382751_723579082221058_2103099558406711841_n.png) 

![image of category model](https://github.com/rinabade/E-Commerce-Project/blob/master/lab_manual/Lab2/284837814_490152009532384_7957260564952937221_n.png)

![image of view product](https://github.com/rinabade/E-Commerce-Project/blob/master/lab_manual/Lab2/285010121_1991098547747591_8730209762865238535_n.png)


# CONCLUSION:

Here we got to know about how to create a model, edit the model in an appropriate manner, and enter and evaluate the entered data in the django server database.