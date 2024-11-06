from django.db import models
from django.contrib.auth.models import User 

class Pet(models.Model):
    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Other', 'Other'),
    ]
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=25, choices=GENDER_CHOICES)
    size = models.CharField(max_length=25)
    color = models.CharField(max_length=25)
    price = models.PositiveIntegerField() 
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/')

    def __str__(self):
        return self.name

class SuccessStory(models.Model):
    title = models.CharField(max_length=20)
    story = models.TextField()
    image = models.ImageField(upload_to='static/images/')
    date = models.DateField()

    def __str__(self):
        return self.title

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('Veterinary Clinics', 'Veterinary Clinics'),
        ('Pet Training Services', 'Pet Training Services'),
        ('Pet Supply Stores', 'Pet Supply Stores'),
        ('Animal Control and Shelters', 'Animal Control and Shelters'),
        ('Pet-friendly Parks and Trails', 'Pet-friendly Parks and Trails'),
        ('Lost and Found Resources', 'Lost and Found Resources'),
        ('Rehoming Resources','Rehoming Resources'),
        ('Wildlife Resources','Wildlife Resources'),
        ('Human Help','Human Help'),
    ]
    
    
    title = models.CharField(max_length=200)
    link = models.URLField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Veterinary Clinic')
    def __str__(self):
        return self.title

class GetInvolved(models.Model):
    CATEGORY_CHOICES = [
        ('Donate', 'Donate'),
        ('Volunteer', 'Volunteer'),
        ('Events', 'Events'),
        ('Foster', 'Foster'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  

    def __str__(self):
        return self.title

class SignUp(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    mobile_num = models.CharField(max_length=15)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


# models.py
from django.db import models

class Adoption(models.Model):
    animal_species = models.CharField(max_length=100)
    animal_name = models.CharField(max_length=100)
    adoptee_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    phone_type = models.CharField(max_length=50)
    residents = models.TextField()
    current_pets = models.TextField()
    vet_reference = models.CharField(max_length=255)
    moving_soon = models.BooleanField()
    moving_city_state = models.CharField(max_length=255, blank=True)
    ready_to_adopt = models.CharField(max_length=100)
    allergies = models.CharField(max_length=100)
    breed_familiarity = models.CharField(max_length=100)
    housing_type = models.CharField(max_length=100)
    property_ownership = models.CharField(max_length=50)
    yard_details = models.CharField(max_length=100)
    household_discussion = models.CharField(max_length=100)
    children_interaction = models.CharField(max_length=100)
    vet_bill_payment_plan = models.TextField()
    additional_reference = models.TextField(blank=True)
    comments = models.TextField(blank=True)
    rehoming_fee = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    terms_agreement = models.BooleanField()
    adopter_signature = models.CharField(max_length=100)
    signature_date = models.DateField()
    
    def __str__(self):
        return f"{self.adopter_name} - {self.animal_name}"
