# Generated by Django 4.1.1 on 2022-10-16 12:43

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumName', models.CharField(max_length=30)),
                ('releasedDate', models.DateField()),
                ('genre', multiselectfield.db.fields.MultiSelectField(choices=[('KP', 'KPop'), ('P', 'Pop'), ('HHR', 'Hip-Hop Rap'), ('C', 'Country'), ('RB', 'Rhythm and Blues'), ('F', 'Folk'), ('J', 'Jazz'), ('HM', 'Heavy Metal'), ('EDM', 'Electronic Dance Music'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('D', 'Disco'), ('PR', 'Punk Rock'), ('CL', 'Classical'), ('H', 'House'), ('T', 'Techno'), ('IR', 'Indie Rock'), ('G', 'Grunge'), ('A', 'Ambient'), ('R', 'Reggae'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('G', 'Gospel'), ('LM', 'Latin Music'), ('GM', 'Grime'), ('T', 'Trap'), ('PK', 'Psychedelic Rock')], max_length=30)),
                ('dateRecorded', models.DateField()),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.singer')),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singleName', models.CharField(max_length=30)),
                ('recordedDate', models.DateField()),
                ('releasedDate', models.DateField()),
                ('genre', multiselectfield.db.fields.MultiSelectField(choices=[('KP', 'KPop'), ('P', 'Pop'), ('HHR', 'Hip-Hop Rap'), ('C', 'Country'), ('RB', 'Rhythm and Blues'), ('F', 'Folk'), ('J', 'Jazz'), ('HM', 'Heavy Metal'), ('EDM', 'Electronic Dance Music'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('D', 'Disco'), ('PR', 'Punk Rock'), ('CL', 'Classical'), ('H', 'House'), ('T', 'Techno'), ('IR', 'Indie Rock'), ('G', 'Grunge'), ('A', 'Ambient'), ('R', 'Reggae'), ('S', 'Soul'), ('F', 'Funk'), ('R', 'Reggae'), ('G', 'Gospel'), ('LM', 'Latin Music'), ('GM', 'Grime'), ('T', 'Trap'), ('PK', 'Psychedelic Rock')], max_length=30)),
                ('composer', models.CharField(max_length=30)),
                ('producer', models.CharField(max_length=30)),
                ('albums', models.ManyToManyField(to='release.album')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.singer')),
            ],
        ),
    ]
