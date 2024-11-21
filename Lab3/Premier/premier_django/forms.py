from django import forms
from .models import club, player, match_info

class ClubForm(forms.ModelForm):
    class Meta:
        model = club
        fields = [
            'name', 'city', 'stadium', 'address', 'tel', 'fax',
            'website', 'founded', 'coach'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Club Name'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'stadium': forms.Select(attrs={'placeholder': 'Stadium'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'tel': forms.TextInput(attrs={'placeholder': 'Telephone'}),
            'fax': forms.TextInput(attrs={'placeholder': 'Fax'}),
            'website': forms.URLInput(attrs={'placeholder': 'Website URL'}),
            'founded': forms.DateInput(attrs={'placeholder': 'Founded Year'}),
            'coach': forms.TextInput(attrs={'placeholder': 'Coach Name'}),
        }

        labels = {
            'name': 'Club Name',
            'city': 'City',
            'stadium': 'Stadium',
            'address': 'Address',
            'tel': 'Telephone',
            'fax': 'Fax',
            'website': 'Website',
            'founded': 'Founded Year',
            'coach': 'Coach Name',
        }
class PlayerForm(forms.ModelForm):
    class Meta:
        model = player
        fields = ['player_name', 'date_of_birth', 'place_of_birth', 'height', 'nationality', 'position', 'current_club', 'sign_contract_date', 'contract_expired']

        widgets = {
            'player_name': forms.TextInput(attrs={'placeholder': 'Player Name'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'Date of Birth'}),
            'place_of_birth': forms.TextInput(attrs={'placeholder': 'Place of Birth'}),
            'height': forms.NumberInput(attrs={'placeholder': 'Height'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'}),
            'position': forms.TextInput(attrs={'placeholder': 'Position'}),
            'current_club': forms.Select(attrs={'placeholder': 'Current Club'}),
            'sign_contract_date': forms.DateInput(attrs={'placeholder': 'Sign Contract Date'}),
            'contract_expired': forms.DateInput(attrs={'placeholder': 'Contract Expired'}),
        }

        labels = {
            'player_name': 'Player Name',
            'date_of_birth': 'Date of Birth',
            'place_of_birth': 'Place of Birth',
            'height': 'Height',
            'nationality': 'Nationality',
            'position': 'Position',
            'current_club': 'Current Club',
            'sign_contract_date': 'Sign Contract Date',
            'contract_expired': 'Contract Expired',
        }
class MatchForm(forms.ModelForm):
    class Meta:
        model = match_info
        fields = ['home_team', 'away_team', 'date', 'home_team_goals', 'away_team_goals', 'stadium']

    widgets = {
        'home_team': forms.Select(attrs={'placeholder': 'Home Team'}),
        'away_team': forms.Select(attrs={'placeholder': 'Away Team'}),
        'date': forms.DateInput(attrs={'placeholder': 'Date'}),
        'home_team_goals': forms.NumberInput(attrs={'placeholder': 'Home Team Goals'}),
        'away_team_goals': forms.NumberInput(attrs={'placeholder': 'Away Team Goals'}),
        'stadium': forms.Select(attrs={'placeholder': 'Stadium'}),
    }

    labels = {
        'home_team': 'Home Team',
        'away_team': 'Away Team',
        'date': 'Date',
        'home_team_goals': 'Home Team Goals',
        'away_team_goals': 'Away Team Goals',
        'stadium': 'Stadium',
    }
