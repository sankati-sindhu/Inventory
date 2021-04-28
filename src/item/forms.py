from django import forms

STATUS_CHOICES  = (
   ('a', 'Available'),
	('d', 'defecitve'),
	('r', 'returned'),
	('e', 'defective/expired'),
	('s', 'sold')
)
class ItemSearchForm(forms.Form):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    status = forms.ChoiceField( choices=STATUS_CHOICES, required=False)

class ItemAddForm(forms.Form):
   pass
