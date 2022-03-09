from django.conf import settings as django_settings

SETTINGS = getattr(django_settings, 'django_gpg', {})
PUBLIC_KEY_REQUIRED = SETTINGS.get('PUBLIC_KEY_REQUIRED', True)

INSTALLED_APPS = [

    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}