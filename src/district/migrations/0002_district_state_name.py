# Generated by Django 2.2.10 on 2020-04-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='state_name',
            field=models.CharField(default='', max_length=20, verbose_name='지역구 행정구역 명'),
            preserve_default=False,
        ),
    ]
