# Generated by Django 5.0.4 on 2024-11-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_propertycontacts_propertydetails_propertylocation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertyphoto',
            options={},
        ),
        migrations.RemoveField(
            model_name='propertyphoto',
            name='additional_photos',
        ),
        migrations.AddField(
            model_name='propertyphoto',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='properties/additional/'),
        ),
        migrations.AddField(
            model_name='propertyphoto',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='properties/additional/'),
        ),
        migrations.AddField(
            model_name='propertyphoto',
            name='photo_3',
            field=models.ImageField(blank=True, null=True, upload_to='properties/additional/'),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='amenities',
            field=models.CharField(choices=[('wifi', 'WiFi'), ('parking', 'Parking'), ('pool', 'Swimming Pool'), ('gym', 'Gym'), ('security', 'Security'), ('ac', 'Air Conditioning'), ('heating', 'Heating'), ('laundry', 'Laundry'), ('elevator', 'Elevator'), ('garden', 'Garden')], default='wifi', max_length=255),
        ),
    ]
