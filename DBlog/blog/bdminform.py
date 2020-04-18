from django import forms


class PostAdminForm(forms.ModelForm):
    status = forms.BooleanField(label='是否删除', required=True)
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
