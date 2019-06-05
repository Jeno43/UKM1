from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ukmapp(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.author


class Sportukmapp(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.author



class RegistrationData(models.Model):
    Nama_UKM = models.CharField(max_length=100)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    No_HP = models.CharField(max_length=20)
    Alamat = models.CharField(max_length=100)


    def __str__(self):
        return self.Username




class DataKaryawan(models.Model):
    Nama_Lengkap = models.CharField(max_length=100)
    Tgl_Lahir = models.DateTimeField(max_length=50)
    Jenis_kelamin = models.CharField(max_length=50)
    Alamat = models.CharField(max_length=50)
    No_Hp = models.CharField(max_length=50)




    def __str__(self):
        return self.Nama_Lengkap


class DataBarang(models.Model):

    Nama_Barang = models.CharField(max_length=100)
    Stok_Barang = models.CharField(max_length=50)
    Tanggal_masuk = models.DateField(max_length=50)


    @classmethod
    def make_DataBarang(cls, Namabarang_item, New_item):
        DataBarang, created = cls.objects.get_or_create(
            Namabarang_item=Namabarang_item
        )
        DataBarang.items.add(New_item)


    @classmethod
    def lose_DataBarang(cls, Namabarang_item, New_item):
        DataBarang, created = cls.objects.get_our_cteate(
            Namabarang_item=Namabarang_item
        )
        DataBarang.items.remove(New_item)
