# Generated by Django 4.1.1 on 2022-12-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0004_alter_karyawanmodels_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='karyawanmodels',
            old_name='nama',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='karyawanmodels',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/'),
        ),
    ]
