# Generated by Django 4.0.3 on 2022-12-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0003_rename_player_sport_user_user_age_user_sex_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLGNIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='human_language',
            name='user',
        ),
        migrations.RemoveField(
            model_name='interest',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='user',
        ),
        migrations.RemoveField(
            model_name='programming_language',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='interest',
            field=models.ManyToManyField(to='connect.interest'),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.ManyToManyField(to='connect.human_language'),
        ),
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.ManyToManyField(to='connect.profession'),
        ),
        migrations.AddField(
            model_name='user',
            name='programming_language',
            field=models.ManyToManyField(to='connect.programming_language'),
        ),
        migrations.AddField(
            model_name='user',
            name='sport',
            field=models.ManyToManyField(to='connect.sport'),
        ),
        migrations.AddField(
            model_name='user',
            name='clgnit',
            field=models.ManyToManyField(to='connect.clgnit'),
        ),
    ]
