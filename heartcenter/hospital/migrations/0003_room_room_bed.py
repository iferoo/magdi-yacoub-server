# Generated by Django 3.2.13 on 2022-05-15 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20220515_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room_Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=70)),
                ('Status', models.CharField(max_length=70)),
                ('RoomID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProposalItems', to='hospital.room')),
            ],
        ),
    ]
