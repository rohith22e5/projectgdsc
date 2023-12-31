# Generated by Django 4.2.1 on 2023-09-17 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('allfurnitures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='furnitures/default.jpg', upload_to='furnitures')),
                ('category', models.CharField(max_length=64)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='furnitures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
