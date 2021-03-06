# Generated by Django 4.0.4 on 2022-07-26 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('private', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', related_query_name='review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
