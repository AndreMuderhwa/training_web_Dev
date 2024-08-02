from django.db import models
import pathlib

# Create your models here.
def upload_image_etudiant(instance, filename):
    fpath=pathlib.Path(filename)
    new_fileName=str(f"{instance.nom}_{instance.postnom}_{instance.prenom}")
    return f"imgEtudiants/{new_fileName}{fpath.suffix}"


class Etudiant(models.Model):
    nom=models.TextField(max_length=250)
    postnom=models.TextField(max_length=250)
    prenom=models.TextField(max_length=250)
    sexe=models.TextField(max_length=50)
    image=models.ImageField(upload_to=upload_image_etudiant)

    class Meta:
        db_table='tbl_etudiant'
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

    


class Promotion(models.Model):
    designation=models.TextField(max_length=250)
    sigle=models.TextField(max_length=50)
    class Meta:
        db_table='tbl_promotion'
    
    def __str__(self):
        return self.designation

class Faculte(models.Model):
    designation=models.TextField(max_length=250)
    sigle=models.TextField(max_length=50)
    class Meta:
        db_table='tbl_faculte'
    
    def __str__(self):
        return self.designation


class Inscription(models.Model):
    refEtudiant=models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    refPromotion=models.ForeignKey(Promotion, on_delete=models.CASCADE)
    refFaculte=models.ForeignKey(Faculte, on_delete=models.CASCADE)
    date_inscription=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='tbl_inscription'


