from django.db import models


class ImageDB(models.Model):
    category_options = [('unknown', 'unknown'), ('Animal', 'Animal'), ('Fruit', 'Fruit'), ('Nature', 'Nature'), ('Art', 'Art')]

    name = models.CharField(max_length=500)
    image_file = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=10, default='unknown', choices=category_options)

    def __str__(self):
        return self.name + " : " + str(self.image_file)
