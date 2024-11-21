from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django_pandas.io import read_frame
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from premier_django.NetworkHelper import NetworkHelper
from premier_django.forms import ClubForm, PlayerForm, MatchForm
from premier_django.models import club, player, match_info, assist
from premier_django.repositories.repositories import MatchRepository, StadiumRepository, ClubRepository,PlayerRepository
from premier_django.repositories_manager import RepositoryManager
from premier_django.serializers import ClubSerializer, PlayerSerializer, MatchSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

API_BASE_URL = 'http://127.0.0.1:8080/users'

def home(request):
    return render(request, 'home/home.html')

def club_list(request):
    clubs = RepositoryManager.club.get_all()
    return render(request, 'clubs/club_list.html', {'clubs': clubs})

def club_create(request):

    if request.method == 'POST':
        form = ClubForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            stadium = form.cleaned_data['stadium']
            address = form.cleaned_data['address']
            tel = form.cleaned_data['tel']
            fax = form.cleaned_data['fax']
            website = form.cleaned_data['website']
            founded = form.cleaned_data['founded']
            coach = form.cleaned_data['coach']

            RepositoryManager.club.create(name, city, stadium, address, tel, fax, website, founded, coach)

            return redirect('club_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = ClubForm()

    return render(request, 'clubs/club_form.html', {'form': form})

def club_update(request, club_id):
    club_instance = get_object_or_404(club, pk=club_id)
    form = ClubForm(request.POST or None, instance=club_instance)
    if form.is_valid():
        form.save()
        return redirect('club_list')
    return render(request, 'clubs/club_form.html', {'form': form})

def club_delete(request, club_id):
    RepositoryManager.club.delete(club_id)
    return redirect('club_list')

def club_detail(request, club_id):
    try:
        club_instance = RepositoryManager.club.get_by_id(club_id)
    except club.DoesNotExist:
        raise Http404("Club not found")
    return render(request, 'clubs/club_detail.html', {'club': club_instance})

def player_list(request):
    players = RepositoryManager.player.get_all()
    return render(request, 'players/player_list.html', {'players': players})

def player_create(request):

    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date_of_birth = form.cleaned_data['date_of_birth']
            place_of_birth = form.cleaned_data['place_of_birth']
            height = form.cleaned_data['height']
            nationality = form.cleaned_data['nationality']
            position = form.cleaned_data['position']
            current_club = form.cleaned_data['current_club']
            sign_contract_date = form.cleaned_data['sign_contract_date']
            contract_expired = form.cleaned_data['contract_expired']

            RepositoryManager.player.create(name, date_of_birth, place_of_birth, height , nationality , position , current_club , sign_contract_date , contract_expired)

            return redirect('player_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = PlayerForm()

    return render(request, 'players/player_form.html', {'form': form})

def player_update(request, player_id):
    player_instance = RepositoryManager.player.get_by_id(player_id)
    form = PlayerForm(request.POST or None, instance=player_instance)
    if form.is_valid():
        form.save()
        return redirect('player_list')
    return render(request, 'players/player_form.html', {'form': form})

def player_delete(request, player_id):
    RepositoryManager.player.delete(player_id)
    return redirect('player_list')

def player_detail(request, player_id):
    try:
        player_instance = RepositoryManager.player.get_by_id(player_id)
    except player.DoesNotExist:
        raise Http404("Player not found")
    return render(request, 'players/player_detail.html', {'player': player_instance})

def match_list(request):
    matches = RepositoryManager.match.get_all()
    return render(request, 'matches/match_list.html', {'matches': matches})

def match_create(request):
    teams = MatchRepository.get_all()
    stadiums = StadiumRepository.get_all()
    if request.method == 'POST':
        form = MatchForm(request.POST)

        if form.is_valid():
            home_team = form.cleaned_data['home_team']
            away_team = form.cleaned_data['away_team']
            date = form.cleaned_data['date']
            home_team_goals = form.cleaned_data['home_team_goals']
            away_team_goals = form.cleaned_data['away_team_goals']
            stadium = form.cleaned_data['stadium']

            RepositoryManager.match.create(home_team, away_team, date, home_team_goals, away_team_goals, stadium)

            return redirect('match_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = MatchForm()

    return render(request, 'matches/match_form.html', {'form': form})

def match_update(request, match_id):
    match_instance = RepositoryManager.match.get_by_id(match_id)
    form = MatchForm(request.POST or None, instance=match_instance)
    if form.is_valid():
        form.save()
        return redirect('match_list')
    return render(request, 'matches/match_form.html', {'form': form})

def match_delete(request, match_id):
    RepositoryManager.match.delete(match_id)
    return redirect('match_list')

def match_detail(request, match_id):
    try:
        match_instance = RepositoryManager.match.get_by_id(match_id)
    except match_info.DoesNotExist:
        raise Http404("Match not found")
    return render(request, 'matches/match_detail.html', {'match': match_instance})

def player_stats_list(request):
    player_stats = RepositoryManager.player_stat.get_all()
    return render(request, 'player_stats_list.html', {'player_stats': player_stats})

def player_stats_update(request, player_id):
    player_stats_instance = RepositoryManager.player_stat.get_by_id(player_id).first()
    if request.method == 'POST':
        RepositoryManager.player_stat.update(player_id, **request.POST.dict())
        return redirect('player_stats_list')
    return render(request, 'player_stats_form.html', {'player_stats': player_stats_instance})

def standings_list(request):
    standings = RepositoryManager.standing.get_all()
    return render(request, 'standings_list.html', {'standings': standings})

def goal_list(request):
    goals = RepositoryManager.goal.get_all()
    return render(request, 'goal_list.html', {'goals': goals})

def goal_create(request):
    players = player.objects.all()
    matches = match_info.objects.all()
    assists = assist.objects.all()
    if request.method == 'POST':
        RepositoryManager.goal.create(
            player=get_object_or_404(player, pk=request.POST['player']),
            assist=get_object_or_404(assist, pk=request.POST['assist']),
            match=get_object_or_404(match_info, pk=request.POST['match']),
            goal_time=request.POST['goal_time'],
            goal_type=request.POST['goal_type']
        )
        return redirect('goal_list')
    return render(request, 'goal_form.html', {'players': players, 'matches': matches, 'assists': assists})

def goal_delete(request, goal_id):
    RepositoryManager.goal.delete(goal_id)
    return redirect('goal_list')

def goal_update(request, goal_id):
    goal_instance = RepositoryManager.goal.get_by_id(goal_id)
    players = player.objects.all()
    matches = match_info.objects.all()
    assists = assist.objects.all()
    if request.method == 'POST':
        RepositoryManager.goal.update(goal_id, **request.POST.dict())
        return redirect('goal_list')
    return render(request, 'goal_form.html', {'players': players, 'matches': matches, 'assists': assists, 'goal': goal_instance})

def assist_list(request):
    assists = RepositoryManager.assist.get_all()
    return render(request, 'assist_list.html', {'assists': assists})

def assist_create(request):
    players = player.objects.all()
    matches = match_info.objects.all()
    if request.method == 'POST':
        RepositoryManager.assist.create(
            player=get_object_or_404(player, pk=request.POST['player']),
            match=get_object_or_404(match_info, pk=request.POST['match']),
            assist_time=request.POST['assist_time']
        )
        return redirect('assist_list')
    return render(request, 'assist_form.html', {'players': players, 'matches': matches})

def assist_delete(request, assist_id):
    RepositoryManager.assist.delete(assist_id)
    return redirect('assist_list')

def assist_update(request, assist_id):
    assist_instance = RepositoryManager.assist.get_by_id(assist_id)
    players = player.objects.all()
    matches = match_info.objects.all()
    if request.method == 'POST':
        RepositoryManager.assist.update(assist_id, **request.POST.dict())
        return redirect('assist_list')
    return render(request, 'assist_form.html', {'players': players, 'matches': matches, 'assist': assist_instance})

def stadium_list(request):

    stadiums = RepositoryManager.stadium.get_all()
    return render(request, 'stadiums/stadium_list.html', {'stadiums': stadiums})
class ClubViewSet(viewsets.ModelViewSet):
    queryset = RepositoryManager.club.get_all()
    serializer_class = ClubSerializer
    repository = ClubRepository()

    def list(self, request):
        clubs = self.repository.get_all()
        serializer = self.serializer_class(clubs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        club = self.repository.get_by_id(pk)
        serializer = self.serializer_class(club)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.repository.create(**serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        club = self.repository.get_by_id(pk)
        serializer = self.serializer_class(club, data=request.data)
        if serializer.is_valid():
            self.repository.update(pk, **serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        club = self.repository.get_by_id(pk)
        serializer = self.serializer_class(club)
        self.repository.delete(pk)
        return Response(serializer.data)
class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RepositoryManager.player.get_all()
    serializer_class = PlayerSerializer
    repository = PlayerRepository()

    def list(self, request):
        players = self.repository.get_all()
        serializer = self.serializer_class(players, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        player = self.repository.get_by_id(pk)
        serializer = self.serializer_class(player)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.repository.create(**serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        player = self.repository.get_by_id(pk)
        serializer = self.serializer_class(player, data=request.data)
        if serializer.is_valid():
            self.repository.update(pk, **serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        player = self.repository.get_by_id(pk)
        self.repository.delete(pk)
        return Response(status=204)
class MatchViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RepositoryManager.match.get_all()
    serializer_class = MatchSerializer
    repository = MatchRepository()

    def list(self, request):
        matches = self.repository.get_all()
        serializer = self.serializer_class(matches, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        match = self.repository.get_by_id(pk)
        serializer = self.serializer_class(match)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.repository.create(**serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def update(self, request, pk=None):
        match = self.repository.get_by_id(pk)
        serializer = self.serializer_class(match, data=request.data)
        if serializer.is_valid():
            self.repository.update(pk, **serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        match = self.repository.get_by_id(pk)
        self.repository.delete(pk)
        return Response(status=204)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def item_list(request):
    items = NetworkHelper.get_list('users')

    return render(request, 'API/item_list.html', {'items': items})
def delete_item(request, item_id):
    success = NetworkHelper.delete_item('delete' , item_id)

    if success:
        return redirect('item_list')
    else:
        return JsonResponse({'SUCCESS': 'Successfully deleted'}, status=200)

class TopScorersAPIView(APIView):
    def get(self, request):
        queryset = RepositoryManager.player_stat.get_top_scorers()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class AvgGoalsAPIView(APIView):
    def get(self, request):
        queryset = RepositoryManager.standing.get_avg_goals_by_club()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class TopGoalsPerMatchAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.match_stat.get_high_scoring_matches()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class PercentWinsAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.standing.get_percentage_wins()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class CardsStatAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.player_stat.get_cards_stat()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class StadiumCapacityAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.stadium.get_stadium_capacity()
        df = read_frame(queryset)
        return Response(df.to_dict(orient='records'))

class PlayerStatsAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.player_stat.get_all()
        df = read_frame(queryset)
        stats = df.describe(include=[int , float])
        stats = stats.to_dict()

        return Response(stats)

class ClubStatsAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.standing.get_all()
        df = read_frame(queryset)
        stats = df.describe(include=[int, float])
        stats = stats.to_dict()

        return Response(stats)

class GroupedStatsAPIView(APIView):
    def get(self , request):
        queryset = RepositoryManager.standing.get_all().filter(points__gt=0).values('club').annotate(avg_points = Avg('points'))
        df = read_frame(queryset)
        stat = df.describe(include=[int , float])
        stat = stat.to_dict()
        return Response(stat)