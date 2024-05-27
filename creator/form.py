from django import forms

class UserInputForm(forms.Form):
    # here the user input variable means job description
    user_input = forms.CharField(label='Enter your data', widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
    # now taking the user old resume for reference
    old_resume_data = forms.CharField(label="Enter the resume data",
                                    widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}),
                                    required=False)
