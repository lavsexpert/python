# Generated by Django 3.0.4 on 2020-04-07 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_auto_20200407_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='goods_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='goods.Goods'),
        ),
    ]
