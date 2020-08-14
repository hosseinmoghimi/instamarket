# Generated by Django 3.1 on 2020-08-14 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_contract_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='color',
            field=models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info')], default='primary', max_length=50, verbose_name='color'),
        ),
        migrations.AddField(
            model_name='contract',
            name='icon',
            field=models.CharField(choices=[('account_circle', 'account_circle'), ('add_shopping_cart', 'add_shopping_cart'), ('alarm', 'alarm'), ('attach_file', 'attach_file'), ('attach_money', 'attach_money'), ('backup', 'backup'), ('build', 'build'), ('chat', 'chat'), ('dashboard', 'dashboard'), ('delete', 'delete'), ('description', 'description'), ('face', 'face'), ('favorite', 'favorite'), ('get_app', 'get_app'), ('home', 'home'), ('important_devices', 'important_devices'), ('link', 'link'), ('local_shipping', 'local_shipping'), ('lock', 'lock'), ('mail', 'mail'), ('notification_important', 'notification_important'), ('psychology', 'psychology'), ('publish', 'publish'), ('reply', 'reply'), ('schedule', 'schedule'), ('send', 'send'), ('settings', 'settings'), ('share', 'share'), ('sync', 'sync'), ('vpn_key', 'vpn_key')], default='link', max_length=50, verbose_name='icon'),
        ),
    ]
