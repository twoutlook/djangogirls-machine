from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 
        # 'brief',
        'text',
        'r03c3','r03c4','r03c5','r03c6','r03c7',
        )
        
        #   <tr>
        #     <td> 結構 </td>
        #     <td> 格林柱 </td>
        #     <td> {{ form.r03c3 }}</td>
        #     <td> {{ form.r03c4 }}</td>
        #     <td> {{ form.r03c5 }}</td>
        #     <td> {{ form.r03c6 }}</td>
        #     <td> {{ form.r03c7 }}</td>
            
        # </tr>