from django.db import models

class MyTable(models.Model):
    id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=255)
    result = models.BooleanField()

    def __str__(self) -> str:
        text = f"<id={self.id}, filename={self.filename}, result={self.result}>"
        return text