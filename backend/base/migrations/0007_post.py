# Generated by Django 3.2 on 2021-04-28 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0006_alter_person_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_data', models.DateTimeField()),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]