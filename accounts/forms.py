# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = u'Используйте английские буквы'