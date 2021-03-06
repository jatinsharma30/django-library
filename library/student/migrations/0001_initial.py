# Generated by Django 3.2.8 on 2021-11-01 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('issue', 'issue'), ('extend', 'extend')], default='issue', max_length=6)),
                ('response', models.CharField(choices=[('accept', 'accept'), ('pending', 'pending'), ('decline', 'decline')], default='pending', max_length=7)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
