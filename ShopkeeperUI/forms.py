from django import forms
from ShopkeeperUI import models

class AddItems(forms.ModelForm):
    # shopProfile = forms.ModelChoiceField(queryset=[])
    name = forms.CharField(required=True, max_length=100,widget=forms.TextInput(attrs={ 'class' :'form-control'}))
    desc = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={ 'class' :'form-control'}))
    avail = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={ 'class' :'form-check-input'}))
    # avail = forms
    class Meta:
        model = models.Item
        fields = [
            'name',
            'desc',
            'avail',
            'shopProfile'
        ]
    def __init__(self, yourshop, *args, **kwargs):
        super(AddItems, self).__init__(*args, **kwargs)
        self.fields['shopProfile'].queryset = yourshop
        # self.shopProfile = forms.ModelChoiceField(queryset=self.shop)
    # def __init__(self, shopPro, *args, **kwargs):
    #     super(AddItems, self).__init__(*args, **kwargs)
    #     self.shopProfile.queryset= models.Shop.objects.filter(shopProfile=shopPro)

class AddShop(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class' :'form-control'}))
    desc = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class' :'form-control'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class' :'form-control'}))


