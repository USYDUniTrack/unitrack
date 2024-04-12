from django import forms
from .models import Degree

DEGREES = [
    ("Select Degree", (
        (1, "Bachelor of Advanced Computing"),
        (2, "Bachelor of Science"),
        (3, "Bachelor of Interaction Design"),)
     )
]
MAJORS = [
    ("1", "Computer Science"),
    ("2", "Data Science"),
    ("3", "Software Development"),
]
MINORS = [
    ("1", "Computer Science"),
    ("2", "Data Science"),
    ("3", "Software Development"),
    ("4", "Minors"),
]


class DegreeForm(forms.ModelForm):

    degree = forms.ChoiceField(
        choices=DEGREES,
        required=True,
    )
    major = forms.ChoiceField(
        label="Major",
        required=False,
        choices=MAJORS,
    )
    second_major = forms.ChoiceField(
        label="Second Major (if applicable)",
        required=False,
        choices=MINORS,
    )
    minor = forms.ChoiceField(
        label="Minor (if applicable)",
        required=False,
        choices=MINORS,
    )

    class Meta:
        model = Degree
        fields = {"degrees", "majors", "second_majors", "minors"}
