# Generated by Django 2.2.3 on 2019-07-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attempt', '0003_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='country',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=53)),
                ('continent', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=50)),
                ('surfaceare', models.DecimalField(decimal_places=4, max_digits=10)),
                ('independentyear', models.IntegerField()),
                ('population', models.IntegerField()),
                ('lifeexpectancy', models.DecimalField(decimal_places=3, max_digits=50)),
                ('gnp', models.DecimalField(decimal_places=2, max_digits=50)),
                ('gnpld', models.DecimalField(decimal_places=3, max_digits=10)),
                ('localname', models.CharField(max_length=50)),
                ('govname', models.CharField(max_length=45)),
                ('headofstat', models.CharField(max_length=60)),
                ('capital', models.IntegerField()),
                ('code2', models.CharField(max_length=3)),
            ],
        ),
    ]
