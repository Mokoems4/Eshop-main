from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False
    
    def isExists(self):
        return Customer.objects.filter(email=self.email).exists()

# This will make the object representation more meaningful
def __str__(self):
    return f"{self.first_name} {self.last_name} - {self.email}"

class Meta:
    verbose_name = "Customer"
verbose_name_plural = "Customers"

