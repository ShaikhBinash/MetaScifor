from django.db import models

class MenuItem(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly defining primary key
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly defining primary key
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly defining primary key
    created_on = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)  # Fixed incorrect field type
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I:%M %p")}'
