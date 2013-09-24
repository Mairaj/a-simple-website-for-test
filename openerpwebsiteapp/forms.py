from django import forms

class ContactusForm(forms.Form):
        name=forms.CharField(
                                max_length=30,
                                widget=forms.TextInput(
                                                        attrs={'placeholder':'Name'},
                                                        )
                                )
        email=forms.EmailField(
                                         widget=forms.TextInput(
                                                                attrs={'placeholder':'Email'},
                                                        )
                                )
        mobile=forms.IntegerField(
                                        widget=forms.TextInput(
                                                                attrs={'placeholder':'Mobile'},
                                                              )
                                )
        message=forms.CharField(
                                max_length=100,
                                widget=forms.Textarea(
                                                                attrs={'placeholder':'Message...'},
                                                                )
                                )

        class Media:
                css={'all':('contactus.css',)}
                js=('contactusform.js',)

class OpenERPModulesForm(forms.Form):
        module_name=forms.CharField(max_length=50)
        module_description=forms.CharField(max_length=2000,
                                                widget=forms.Textarea(
                                                                        attrs={
                                                                                'placeholder':'place your message here',
                                                                                }
                                                                )
                                                )
