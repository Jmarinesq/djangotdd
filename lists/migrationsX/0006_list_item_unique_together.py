# Generated by Django 2.0 on 2020-10-27 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20201025_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]