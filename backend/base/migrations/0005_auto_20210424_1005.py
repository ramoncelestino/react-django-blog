# Generated by Django 3.2 on 2021-04-24 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210424_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='person_id',
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pers', to='base.address'),
        ),
    ]
