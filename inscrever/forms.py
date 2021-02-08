from django import forms


class Inscrever(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email
