from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    partnership_logo =models.ImageField(upload_to='Banner_photo/')
    image = models.ImageField(upload_to='Banner/')

    def __str__(self):
        return self.title


class Recomendation(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Recomendation_photo/')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user_name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    user_photo = models.ImageField(upload_to='user_photo/')
    CHOICES_TAG = (
        ('popular', 'popular'),
        ('new house', 'new house'),
        ('best deals', 'best deals'),
    )
    tag = models.CharField(max_length=25, choices=CHOICES_TAG)
    CHOICES_TYPE = (
        ('house', 'house'),
        ('villa', 'villa'),
        ('apartment', 'apartment'),
    )
    type = models.CharField(max_length=25, choices=CHOICES_TYPE)

    def __str__(self):
        return self.name


class Sell(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    detail = models.ManyToManyField(to='Detail')
    user_photo = models.ImageField(upload_to='user_photo/')
    user_name = models.CharField(max_length=255)
    user_job = models.CharField(max_length=255)
    presintation = models.ManyToManyField(to='Presintaiton')

    def __str__(self):
        return self.title


class Detail(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Presintaiton(models.Model):
    img = models.FileField(upload_to='video_img/')


class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='Testimonial/')
    user_title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user_photo = models.ImageField(upload_to='Test_photo/')
    user_job = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    reting = models.FloatField()

    def __str__(self):
        return self.user_name


class About_us(models.Model):
    title = models.CharField(max_length=255)
    user_fullname = models.CharField(max_length=255)
    house_img = models.ImageField(upload_to='image_house/')
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_fullname


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Info(models.Model):
    my_logo = models.ImageField(upload_to='my_logo/')
    description = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagramm = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=255)
