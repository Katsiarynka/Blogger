#coding: utf-8
from django.utils.translation import ugettext as _
from django import forms
from django.contrib.auth.models import User
import settings


class PasswordResetRequestForm(forms.Form):
    username_reset = forms.CharField(required=True, label=(u'Имя пользователя'),)

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data:
            try:
                self.user = User.objects.get(username=cleaned_data['username_reset'])
            except User.DoesNotExist:
                self.user = None
        return cleaned_data


class UserLoginForm2(forms.Form):
    username = forms.CharField(required=True, label=_(u'Username'))
    password = forms.CharField(widget=forms.PasswordInput, label=_(u'Password'), required=True)
    def __init__(self, *a, **kw):
        super(UserLoginForm2, self).__init__(*a, **kw)
        self.user = None

    def clean(self):
        if self._errors:
            return {}
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        
        self.user = User.objects.filter(username=username, password = password)[0]
        if not self.user:
            self.cleaned_data = {}
            raise forms.ValidationError(_(u'Please enter a correct username and password. Note that both fields are case-sensitive'))
        return self.cleaned_data


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label=u"Email", required=True)
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(), min_length=8, max_length=64, required=True)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput, min_length=8, max_length=64, required=True)
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = _(u'Логин')
        self.fields['email'].label = _(u"Email")
        

    
    class Meta:
        model = User
        fields = ['username', 'email']
        
    
   
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        import re  
        reg_ex = re.match(r"((.?)[A-Z]{1,}(.*?)[0-9]{1,}(.*?))|((.*?)[0-9]{1,}(.*?)[A-Z]{1,}(.?))",self.cleaned_data['password1'])
        if reg_ex == None:
            raise forms.ValidationError(u"��� ������ ������� �������. ����������� ��������� ����� � �����")
        return password2

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user

    def get_row_password(self):
        try:
            return self.cleaned_data['password1']
        except KeyError:
            raise Exception("You should call get_row_password only after form validation")

    def clean_username(self):
        data = self.cleaned_data['username']
        if data.lower() in settings.BLOCKED_USERNAME:
            raise forms.ValidationError(u'������������ � ����� ������ ��� ����������')
        
        try:
            User.objects.get(login=data)
            raise forms.ValidationError(u'������������ � ����� ������ ��� ����������.')
        except User.DoesNotExist:
            pass
        try:
            int(data)
        except Exception:
            return data
        else:
            raise forms.ValidationError(u'����� �� ����� �������� ������ �� ����')
