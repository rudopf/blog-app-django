from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]