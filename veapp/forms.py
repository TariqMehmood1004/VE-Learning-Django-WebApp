from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Write a comment...',
            'class': 'w-full border border-gray-300 p-2 rounded-md',
            'rows': '1',  # Adjust the number of rows as needed
        }),
        required=True
    )
    

class EditCommentForm(forms.Form):
    edit_comment_id = forms.IntegerField(widget=forms.HiddenInput())
    edit_user_id = forms.IntegerField(widget=forms.HiddenInput())
    edited_comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write a comment...'}), required=True)
