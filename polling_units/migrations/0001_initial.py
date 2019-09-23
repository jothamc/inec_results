# Generated by Django 2.2.3 on 2019-09-23 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lgas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('uniqueid', models.AutoField(primary_key=True, serialize=False)),
                ('polling_unit_id', models.IntegerField()),
                ('ward_id', models.IntegerField()),
                ('uniquewardid', models.IntegerField()),
                ('polling_unit_number', models.IntegerField()),
                ('polling_unit_name', models.CharField(max_length=200)),
                ('polling_unit_description', models.TextField()),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('entered_by_user', models.CharField(max_length=200)),
                ('date_entered', models.DateField(auto_now_add=True)),
                ('user_ip_address', models.GenericIPAddressField(null=True)),
                ('lga', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lgas.LGA')),
            ],
            options={
                'db_table': 'polling_unit',
            },
        ),
    ]