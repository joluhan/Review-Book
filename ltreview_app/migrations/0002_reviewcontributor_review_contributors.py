# Generated by Django 5.0.1 on 2024-01-20 00:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ltreview_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.CharField(blank=True, max_length=255)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ltreview_app.review')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='contributors',
            field=models.ManyToManyField(related_name='contributions', through='ltreview_app.ReviewContributor', to=settings.AUTH_USER_MODEL),
        ),
    ]