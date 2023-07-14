from app.models import *

from django import forms


class TopicModelForm(forms.ModelForm): 
    class Meta:
        model=Topic
        fields='__all__'


class WebpageModelForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        help_texts={'topic_name':'select the required Topic name'}
        widgets={'topic_name':forms.RadioSelect}

    
class AccessRecordModelForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
        help_texts={'name':'select the required Webpage name'}
        widgets={'name':forms.RadioSelect}
