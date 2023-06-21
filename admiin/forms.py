from django import forms
from index.models import Category, Model, Product, Responsible, RoomsModel, Group
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RoomsForm(forms.ModelForm):
    class Meta:
        model = RoomsModel
        fields = '__all__'


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_en', 'name_ru', 'name_uz', 'image']
        labels = {
            'name': 'Kategoriya nomi ',
            'image': 'Kategoriya rasmi ',
        }


class ResponsibleCreateForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = ['fullname_en', 'fullname_ru', 'fullname_uz', 'description_en', 'description_ru', 'description_uz' ]
        labels = {
            'fullname': 'Javobgar shaxs ism-familiyasi ',
            'description': 'Shaxs haqida izoh ',
        }


class ModelCreateForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = ['name', 'description', 'image']
        labels = {
            'name': 'Jihoz modeli nomi ',
            'image': 'Jihoz modeli rasmi ',
            'description': 'Izoh ',
        }
        print(labels)


status_choices = (
    (1, _('Ishlatilmoqda')),
    (3, _('Olib ketilgan')),
    (0, _('Yaroqsiz')),
    (2, _('Zahirada')),
)


class EquipmentCreateForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nomi', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}))
    schet = forms.CharField(max_length=100, label='Schet', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}))
    room_number = forms.CharField(max_length=30, label='Xona raqami',
                                    widget=forms.TextInput(attrs={'class': "form-control", 'maxlength': '30'}))
    inventar_number = forms.CharField(required=True, label='Inventar raqami',
                                         widget=forms.TextInput(attrs={'class': "form-control"}))
    model_id = forms.ModelChoiceField(queryset=Model.objects.none(), label='Modeli',
                                      widget=forms.Select(attrs={'class': "form-control"}))
    responsible_id = forms.ModelChoiceField(queryset=Responsible.objects.none(), label='Javobgar shaxs',
                                            widget=forms.Select(attrs={'class': "form-control"}))
    image = forms.FileField(label='Rasm yuklang', required=False, widget=forms.ClearableFileInput(attrs={'class': "form-control"}))
    seria_number = forms.CharField(max_length=70, label='Seria raqami', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '25', 'id': "alloptions"}))
    year_of_manufacture = forms.CharField(max_length=50, label='Ishlab chiqarilgan yili', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}))
    unit_of_measurement = forms.CharField(max_length=50, label='O\'lchov birligi', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}))
    description = forms.CharField(required=False, label='Xulosa', widget=forms.Textarea(attrs={'class': "form-control"}))

    def clean_inventar_number(self):
        inventar_number = self.cleaned_data['inventar_number']
        qs = Product.objects.filter(inventar_number=inventar_number)
        if qs:
            raise ValidationError('Bu inventar raqam boshqa jihozga berilgan')
        return inventar_number

    def __init__(self, user, *args, **kwargs):
        super(EquipmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['responsible_id'].queryset = Responsible.objects.filter(group=user.groups.first())
        self.fields['model_id'].queryset = Model.objects.filter(group=user.groups.first())

    


class ProductUpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Nomi', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}))
    schet = forms.CharField(max_length=100, label='Schet', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}))
    category_id = forms.ModelChoiceField(queryset=Category.objects.none(), label='Kategoriyasi', widget=forms.Select(attrs={'class': "form-control"}))
    room_number = forms.CharField(max_length=30, label='Xona raqami',
                                    widget=forms.TextInput(attrs={'class': "form-control", 'maxlength': '30'}))
    inventar_number = forms.CharField(label='Inventar raqami',
                                         widget=forms.TextInput(attrs={'class': "form-control"}))
    model_id = forms.ModelChoiceField(queryset=Model.objects.all(), label='Modeli',
                                      widget=forms.Select(attrs={'class': "form-control"}))
    responsible_id = forms.ModelChoiceField(queryset=Responsible.objects.none(), label='Javobgar shaxs',
                                            widget=forms.Select(attrs={'class': "form-control"}))
    images = forms.FileField(label='Rasm yuklang', required=False, widget=forms.ClearableFileInput(attrs={'class': "form-control"}))
    seria_number = forms.CharField(max_length=70, label='Seria raqami', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': "25"}))
    year_of_manufacture = forms.CharField(max_length=50, label='Ishlab chiqarilgan yili', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}))
    unit_of_measurement = forms.CharField(max_length=50, label='O\'lchov birligi', required=False,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}))
    description = forms.CharField(label='Xulosa', required=False, widget=forms.Textarea(attrs={'class': "form-control", 'rows':3}))
    responsible_person = forms.CharField(max_length=256, required=False, label='Masul shaxs', widget=forms.TextInput(attrs={'class': "form-control"}))
    status = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))

    class Meta:
        model = Product
        exclude = ('qr_code', 'group')

    def __init__(self, user, *args, **kwargs):
        super(ProductUpdateForm, self).__init__(*args, **kwargs)
        self.fields['responsible_id'].queryset = Responsible.objects.filter(group=user.groups.first())
        self.fields['category_id'].queryset = Category.objects.filter(group=user.groups.first())
        self.fields['model_id'].queryset = Model.objects.filter(group=user.groups.first())

    # def clean_inventar_number(self):
    #     inventar_number = self.cleaned_data['inventar_number']
    #     qs = Product.objects.filter(inventar_number=inventar_number)
    #     if qs:
    #         raise ValidationError('Bu inventar raqam boshqa jihozga berilgan')
    #     return inventar_number


class ProductDetailUpdateForm(forms.ModelForm):

    # status = forms.TypedChoiceField(choices=status_choices, label='', widget=forms.Select(attrs={'class': "form-control"}))
    status = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': "form-control"}))
    responsible_person = forms.CharField(max_length=256, required=False, label='Masul shaxs',
                                         widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = Product
        fields = ['status', 'responsible_person']

# CATEGORIES Forms
        
class CategoryEditForm(forms.ModelForm):

    name = forms.CharField(max_length=70, label='Nomi', required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    image = forms.ImageField(label='Rasm yuklang', widget=forms.ClearableFileInput(attrs={'class': "form-control"}))

    class Meta:
        model = Category
        fields = ['name', 'image']

class UploadExcelFileForm(forms.Form):
    excel_file_cat = forms.FileField(required=False)
    excel_file_pro = forms.FileField(required=False)
    excel_file_mod = forms.FileField(required=False)
    excel_file_per = forms.FileField(required=False)


class ModelEditForm(forms.ModelForm):
    name = forms.CharField(max_length=70, label='Nomi', required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    image = forms.ImageField(label='Rasm yuklang', widget=forms.ClearableFileInput(attrs={'class': "form-control"}))
    description = forms.CharField(label='Xulosa', widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = Model
        fields = ['name', 'image', 'description']


class ResponsibleEditForm(forms.ModelForm):
    fullname = forms.CharField(max_length=70, label='Ism-familiya', required=True,
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(label='Izoh', widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = Responsible
        fields = ['fullname', 'description']
