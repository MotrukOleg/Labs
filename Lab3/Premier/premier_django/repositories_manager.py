
from .repositories.repositories import ClubRepository, StadiumRepository, MatchRepository, ClubLogoRepository, \
    AssistRepository, GoalRepository, PlayerRepository, StandingRepository, PlayerStatsRepository, MatchStatsRepository


class RepositoryManager:
    club = ClubRepository
    stadium = StadiumRepository
    match = MatchRepository
    match_stat = MatchStatsRepository
    club_logo = ClubLogoRepository
    assist = AssistRepository
    goal = GoalRepository
    player = PlayerRepository
    player_stat = PlayerStatsRepository
    standing = StandingRepository

