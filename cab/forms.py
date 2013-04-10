# Not needed.

# from django import forms
# from cab.models import Snippet, Language
# 
# class AddSnippetForm(forms.Form):
#     def __init__(self, author, *args, **kwargs):
#         super(AddSnippetForm, self).__init__(*args, **kwargs)
#         self.author = author
# 
#     title = forms.CharField(max_length=255)
#     description = forms.CharField(widget=forms.Textarea())
#     code = forms.CharField(widget=forms.Textarea())
#     tags = forms.CharField(max_length=255)
#     language = forms.ModelChoiceField(queryset=Language.objects.all())
#     
#     def save(self):
#         return Snippet.objects.create(title=self.cleaned_data['title'],
#                           description=self.cleaned_data['description'],
#                           code=self.cleaned_data['code'],
#                           tags=self.cleaned_data['tags'],
#                           author=self.author,
#                           language=self.cleaned_data['language'])