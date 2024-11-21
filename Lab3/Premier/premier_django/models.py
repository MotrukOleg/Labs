from django.db import models

class club(models.Model):
    club_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stadium = models.ForeignKey('stadium', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    founded = models.DateField()
    coach = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class stadium(models.Model):
    stadium_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class match_info(models.Model):
    match_id = models.AutoField(primary_key=True)
    home_team = models.ForeignKey('club', on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey('club', on_delete=models.CASCADE, related_name='away_team')
    date = models.DateField()
    home_team_goals = models.IntegerField()
    away_team_goals = models.IntegerField()
    stadium = models.ForeignKey('stadium', on_delete=models.CASCADE)

    def __str__(self):
        return self.home_team.name + ' vs ' + self.away_team.name + ' ' + str(self.date) + ' ' + str(self.home_team_goals) + ':' + str(self.away_team_goals)

class player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    height = models.IntegerField()
    age = models.IntegerField(default=0)
    nationality = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    current_club = models.ForeignKey('club', on_delete=models.CASCADE)
    sign_contract_date = models.DateField()
    contract_expired = models.DateField()
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.player_name

class player_stats(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.ForeignKey('player', on_delete=models.CASCADE)
    player_goals = models.IntegerField()
    player_assists = models.IntegerField()
    player_yellow_cards = models.IntegerField()
    player_red_cards = models.IntegerField()

    def __str__(self):
        return self.player_name.player_name + ' ' + str(self.player_goals) + ' '

class standings(models.Model):
    id = models.AutoField(primary_key=True)
    club = models.ForeignKey('club', on_delete=models.CASCADE)
    games_played = models.IntegerField(default=0)
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    goals_scored = models.IntegerField()
    goals_conceded = models.IntegerField()
    goal_difference = models.IntegerField(default = 0)
    points = models.IntegerField()

    def __str__(self):
        return self.club.name + ' ' + str(self.points) + ' ' + str(self.wins) + ' ' + str(self.draws) + ' ' + str(self.losses) + ' ' + str(self.goals_for) + ' ' + str(self.goals_against) + ' ' + str(self.goal_difference)

class match_statictic(models.Model):
    match = models.ForeignKey('match_info', on_delete=models.CASCADE)
    possession_home = models.IntegerField()
    possession_away = models.IntegerField()

class goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    player = models.ForeignKey('player', on_delete=models.CASCADE)
    assist = models.ForeignKey('assist', on_delete=models.CASCADE, related_name='assist')
    match = models.ForeignKey('match_info', on_delete=models.CASCADE)
    goal_time = models.IntegerField()
    goal_type = models.CharField(max_length=100)
    def __str__(self):
        return self.player.player_name + ' ' + str(self.minute) + ' '

class assist(models.Model):
    assist_id = models.AutoField(primary_key=True)
    match = models.ForeignKey('match_info', on_delete=models.CASCADE)
    player = models.ForeignKey('player', on_delete=models.CASCADE)

    def __str__(self):
        return self.player.player_name + ' ' + str(self.minute) + ' '

class club_logo(models.Model):
    club_logo_id = models.AutoField(primary_key=True)
    club = models.ForeignKey('club', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='club_logos/')