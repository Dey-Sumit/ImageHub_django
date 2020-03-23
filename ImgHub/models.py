from django.db import models


class ImageDB(models.Model):
    u_ctg_options = [('unknown', 'unknown'), ('Animal', 'Animal'), ('Fruit', 'Fruit'), ('Nature', 'Nature'), ('Art', 'Art')]

    name = models.CharField(max_length=500)
    image_file = models.ImageField(upload_to='images/')
    u_ctg = models.CharField(max_length=10, default='unknown', choices=u_ctg_options)
    v_ctg = models.CharField(max_length=10, default="unknown")
    hash_val = models.CharField(max_length=100, null=True)
    #hash_val max length <=36

    def __str__(self):
        return self.name + " : " + str(self.image_file)
