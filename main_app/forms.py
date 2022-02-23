from django.forms import ModelForm
from .models import Reout, Resp


class ReoutForm(ModelForm):
    class Meta:
        model = Reout
        fields = ('date', 'reout_name', 'source', 'notes')
        

class RespForm(ModelForm):
    class Meta:
        model = Resp
        fields = ('date', 'resp_name', 'source', 'notes')