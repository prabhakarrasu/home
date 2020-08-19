from django.db import models

class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class House(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)
    STATUS_CHOICES = (('1BHK','1BHK'), ('2BHK','2BHK'),('3BHK','3BHK'),)
    RL = (('Rent','Rent'),('Lease','Lease'),)
    house_type = models.CharField(max_length=50, choices=STATUS_CHOICES)
    floor = models.IntegerField()
    portions = models.CharField(max_length=25)    
    Rent_or_Lease = models.CharField(max_length=20, choices=RL)
    amount = models.IntegerField()
    Water_bill_id = models.CharField(max_length=50)
    Current_bill_id = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}-{}'.format(self.floor,self.portions)

class Teneant(models.Model):        #it is for tenant
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    aadhar_no = models.CharField(max_length=20, null=True)
    previous_address = models.TextField(null=True)
    total_members = models.IntegerField(null=True)
    docs = models.FileField(upload_to="rent_docs",null=True)

    def __str__(self):
        return self.name

class Rent(models.Model):
    teneant = models.ForeignKey(Teneant, on_delete=models.CASCADE,null=True)
    month = models.CharField(max_length=15, null=True)
    paid_date = models.DateField(null=True)
    amount_paid = models.FloatField(null=True)
    balance = models.FloatField(null=True)
    type_of_payment = models.CharField(max_length=12, null=True)
    year = models.DateField(null=True)

    def __str__(self):
        return self.teneant.name



class WaterBill(models.Model):
    teneant = models.ForeignKey(Teneant, on_delete=models.CASCADE,null=True)
    bill_amount = models.IntegerField(null=True)
    amount_paid = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    carry_balance = models.IntegerField(null=True)
    paid_date = models.DateTimeField(null=True)
    month_year = models.DateTimeField(null=True)

    def __str__(self):
        return self.teneant.name

class CurrentBill(models.Model):
    teneant = models.ForeignKey(Teneant, on_delete=models.CASCADE,null=True)
    bill_amount = models.IntegerField(null=True)
    amount_paid = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    carry_balance = models.IntegerField(null=True)
    paid_date = models.DateTimeField(null=True)
    month_year = models.DateTimeField(null=True)

    def __str__(self):
        return self.teneant.name
    



class Maintenance(models.Model):
    maintenance_amt = models.IntegerField(null=True)
    add_maintenance_amt = models.IntegerField(null=True)
    amount_paid = models.IntegerField(null=True)
    paid_date = models.DateTimeField(null=True)
    month_year = models.DateTimeField(null=True)

    def __str__(self):
        return self.teneant.name

