# Generated by Django 4.1.1 on 2022-12-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0010_alter_karyawanmodels_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karyawanmodels',
            name='alamat',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
