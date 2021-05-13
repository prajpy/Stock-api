from django.db import models

class Stocks(models.Model):
    ticker = models.CharField(max_length=10)
    volume = models.IntegerField()
    open = models.FloatField()
    close = models.FloatField()
    test = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.ticker


