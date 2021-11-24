# Generated by Django 3.2.8 on 2021-11-24 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities_board', '0007_auto_20211124_0842'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='activities_board.user', verbose_name='Автор комментария'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activities_board.event', verbose_name='Мероприятие'),
        ),
    ]
