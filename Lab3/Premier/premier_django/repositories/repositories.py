from premier_django.models import assist
from premier_django.models import club
from premier_django.models import goal
from premier_django.models import club_logo
from premier_django.models import player
from premier_django.models import standings
from premier_django.models import match_info
from premier_django.models import match_statictic
from premier_django.models import player_stats
from premier_django.models import stadium
from django.db.models import Sum, Avg, F, ExpressionWrapper, FloatField

class ClubRepository:

    @staticmethod
    def get_all():
        return club.objects.all()

    @staticmethod
    def get_by_id(club_id):
        return club.objects.get(pk=club_id)

    @staticmethod
    def create(name, city, stadium, address, tel, fax, website, founded, coach):
        new_club = club.objects.create(
            name=name,
            city=city,
            stadium=stadium,
        address=address,
            tel=tel,
            fax=fax,
            website=website,
            founded=founded,
            coach=coach
        )
        return new_club

    @staticmethod
    def update(club_id, **kwargs):
        club_instance = ClubRepository.get_by_id(club_id)

        if not club_instance:
            raise ValueError("Club with the specified ID does not exist.")

        for key, value in kwargs.items():
            setattr(club_instance, key, value)
        club_instance.save()
        return club_instance

    @staticmethod
    def delete(club_id):
        club_instance = ClubRepository.get_by_id(club_id)
        club_instance.delete()

class GoalRepository:
    def get_goals_for_player(self, player_id):
        return goal.objects.filter(player_name__id=player_id)

    @staticmethod
    def update(player_id, **kwargs):
        goal_instance = GoalRepository.get_goals_for_player(player_id).first()
        for key, value in kwargs.items():
            setattr(goal_instance, key, value)
        goal_instance.save()
        return goal_instance

    @staticmethod
    def delete_goals(self, player_id):
        goal_instance = self.get_goals_for_player(player_id).first()
        goal_instance.delete()

    @staticmethod
    def create_goal(self, **kwargs):
        return goal.objects.create(**kwargs)

    @staticmethod
    def get_all_goals(self):
        return goal.objects.all()

    @staticmethod
    def get_goal_by_id(self, goal_id):
        return goal.objects.get(pk=goal_id)

class AssistRepository:


    def get_assists_for_player(self, player_id):
        return assist.objects.filter(player_name__id=player_id)

    @staticmethod
    def update(self, player_id, **kwargs):
        assist_instance = self.get_assists_for_player(player_id).first()
        for key, value in kwargs.items():
            setattr(assist_instance, key, value)
        assist_instance.save()
        return assist_instance

    @staticmethod
    def delete(self, player_id):
        assist_instance = self.get_assists_for_player(player_id).first()
        assist_instance.delete()

    @staticmethod
    def create(self, **kwargs):
        return assist.objects.create(**kwargs)

    @staticmethod
    def get_all(self):
        return assist.objects.all()

    @staticmethod
    def get_by_id(self, assist_id):
        return assist.objects.get(pk=assist_id)

class ClubLogoRepository:

    def get_all_club_logos(self):
        return club_logo.objects.all()

    def get_club_logo_by_id(self, club_logo_id):
        return club_logo.objects.get(pk=club_logo_id)

    def create_club_logo(self, **kwargs):
        return club_logo.objects.create(**kwargs)

    def update_club_logo(self, club_logo_id, **kwargs):
        club_logo_instance = self.get_club_logo_by_id(club_logo_id)
        for key, value in kwargs.items():
            setattr(club_logo_instance, key, value)
        club_logo_instance.save()
        return club_logo_instance

    def delete_club_logo(self, club_logo_id):
        club_logo_instance = self.get_club_logo_by_id(club_logo_id)
        club_logo_instance.delete

class MatchRepository:
    @staticmethod
    def get_all():
        return match_info.objects.all()

    @staticmethod
    def get_by_id(match_id):
        return match_info.objects.get(pk=match_id)

    @staticmethod
    def get_high_scoring_matches():
        return match_info.objects.annotate(
            total_goals=F('home_team_goals') + F('away_team_goals')
        ).order_by('-total_goals')[:10]

    @staticmethod
    def create(home_team, away_team, date, home_team_goals, away_team_goals, stadium):
        match = match_info.objects.create(
            home_team=home_team,
            away_team=away_team,
            date=date,
            home_team_goals=home_team_goals,
            away_team_goals=away_team_goals,
            stadium=stadium
        )
        return match

    @staticmethod
    def update(match_id, **kwargs):
        match_instance = MatchRepository.get_by_id(match_id)
        for key, value in kwargs.items():
            setattr(match_instance, key, value)
        match_instance.save()
        return match_instance

    @staticmethod
    def delete(match_id):
        match_instance = MatchRepository.get_by_id(match_id)
        match_instance.delete()

class MatchStatsRepository:
    @staticmethod
    def get_all():
        return match_statictic.objects.all()

    def get_match_stat_by_id(self, match_stat_id):
        return match_statictic.objects.get(pk=match_stat_id)

    def create_match_stat(self, **kwargs):
        return match_statictic.objects.create(**kwargs)

    @staticmethod
    def get_high_scoring_matches():
        return match_info.objects.annotate(total_goals = F('home_team_goals') + F('away_team_goals'))\
    .order_by('-total_goals')


    def update_match_stat(self, match_stat_id, **kwargs):
        match_stat_instance = self.get_match_stat_by_id(match_stat_id)
        for key, value in kwargs.items():
            setattr(match_stat_instance, key, value)
        match_stat_instance.save()
        return match_stat_instance

    def delete_match_stat(self, match_stat_id):
        match_stat_instance = self.get_match_stat_by_id(match_stat_id)
        match_stat_instance.delete()

class PlayerRepository:

    @staticmethod
    def get_all():
        return player.objects.all().values(
            'player_id',
            'player_name',
            'date_of_birth',
            'place_of_birth',
            'height',
            'age',
            'nationality',
            'position',
            'current_club',
            'sign_contract_date',
            'contract_expired',
            'price',
            'player_stats__player_goals',
            'player_stats__player_assists',
            'player_stats__player_yellow_cards',
            'player_stats__player_red_cards'
        )


    @staticmethod
    def get_by_id(player_id):
        return player.objects.get(pk=player_id)

    @staticmethod
    def create(**kwargs):
        return player.objects.create(**kwargs)

    @staticmethod
    def update(player_id, **kwargs):
        player_instance = PlayerRepository.get_by_id(player_id)
        for key, value in kwargs.items():
            setattr(player_instance, key, value)
        player_instance.save()
        return player_instance

    @staticmethod
    def delete(player_id):
        player_instance = PlayerRepository.get_by_id(player_id)
        player_instance.delete()

class PlayerStatsRepository:
    def get_stats_for_player(self, player_id):
        return player_stats.objects.filter(player_name_id=player_id)


    @staticmethod
    def get_top_scorers():
        return player_stats.objects.values('player_name_id') \
                   .annotate(total_goals=Sum('player_goals')) \
                   .order_by('-total_goals')

    @staticmethod
    def get_cards_stat():
        return player_stats.objects.values('player_name_id')\
    .annotate(total_yellow = Sum('player_yellow_cards') , total_red = Sum('player_red_cards'))\
    .order_by('-total_yellow', '-total_red')

    @staticmethod
    def get_all():
        return player_stats.objects.all()

    def update_stats(self, player_id, **kwargs):
        stats_instance = self.get_stats_for_player(player_id).first()
        for key, value in kwargs.items():
            setattr(stats_instance, key, value)
        stats_instance.save()
        return stats_instance

class StadiumRepository:

    @staticmethod
    def get_all():
        return stadium.objects.all()

    def get_stadium_by_id(self, stadium_id):
        return stadium.objects.get(pk=stadium_id)

    def create_stadium(self, name, city, address, tel, fax, website, capacity, opened):
        return stadium.objects.create(
            name=name, city=city, address=address, tel=tel,
            fax=fax, website=website, capacity=capacity, opened=opened
        )
    @staticmethod
    def get_stadium_capacity():
        return stadium.objects.values('name')\
    .annotate(capacity = F('capacity'))\
    .order_by('-capacity')

    def update_stadium(self, stadium_id, **kwargs):
        stadium_instance = self.get_stadium_by_id(stadium_id)
        for key, value in kwargs.items():
            setattr(stadium_instance, key, value)
        stadium_instance.save()
        return stadium_instance

    def delete_stadium(self, stadium_id):
        stadium_instance = self.get_stadium_by_id(stadium_id)
        stadium_instance.delete()

class StandingRepository:
    @staticmethod
    def get_all():
        return standings.objects.all()

    @staticmethod
    def get_all_for_stats():
        return standings.objects.values('club', 'goals_scored', 'goals_conceded', 'goal_difference', 'wins', 'draws', 'losses', 'points')

    def get_standing_by_id(self, standing_id):
        return standings.objects.get(pk=standing_id)

    @staticmethod
    def get_avg_goals_by_club():
        return standings.objects.values('club') \
    .annotate(avg_goals = Avg('goals_scored'))\
    .order_by('-avg_goals')

    @staticmethod
    def get_percentage_wins():
        return standings.objects.values('club') \
    .annotate(percentage_wins = ExpressionWrapper((F('wins')  * 100 / (F('wins') + F('draws') + F('losses'))), output_field=FloatField()))\
    .order_by('-percentage_wins')

    @staticmethod
    def get_avg_goals_per_game():
        return standings.objects.values('club') \
            .annotate(avg_goals=Avg('goals_scored')) \
            .order_by('-avg_goals')


    def create_standing(self, **kwargs):
        return standings.objects.create(**kwargs)

    def update_standing(self, standing_id, **kwargs):
        standing_instance = self.get_standing_by_id(standing_id)
        for key, value in kwargs.items():
            setattr(standing_instance, key, value)
        standing_instance.save()
        return standing_instance

    def delete_standing(self, standing_id):
        standing_instance = self.get_standing_by_id(standing_id)
        standing_instance.delete()