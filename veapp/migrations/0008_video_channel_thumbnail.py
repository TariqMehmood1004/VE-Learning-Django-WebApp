# Generated by Django 4.2.5 on 2024-01-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veapp', '0007_userinteraction_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='channel_thumbnail',
            field=models.CharField(default='https://images.unsplash.com/photo-1532074205216-d0e1f4b87368?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTAyfHx1c2VyfGVufDB8fDB8fHww', max_length=255),
        ),
    ]