from colorama import Fore

class Club:
    def __new__(cls, name, city, foundation_year , stadium):
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, city, foundation_year , stadium):
        self.name = name
        self.city = city
        self.foundation_year = foundation_year
        self.stadium = stadium

    club_list = dict()
    id = 1

    def club_add(self):
        Club.club_list[Club.id] = [self.name, self.city, self.foundation_year , self.stadium]
        Club.id += 1

    @property
    def name(self):
        return self.__name

    @property
    def city(self):
        return self.__city

    @property
    def foundation_year(self):
        return self.__foundation_year

    @name.setter
    def name(self, value):
        self.__name = value

    @city.setter
    def city(self, value):
        self.__city = value

    @foundation_year.setter
    def foundation_year(self, value):
        self.__foundation_year = value

    def display_info(self):
        print(f"Club: {self.name}, City: {self.city}, Foundation year: {self.foundation_year} , Stadium: {self.stadium}")


class Stadium(Club):

    def __new__(cls, name, city, foundation_year, stadium_name, capacity):
        instance = super().__new__(cls, name, city, foundation_year , stadium_name)
        return instance

    def __init__(self, name, city, foundation_year, stadium_name, capacity):
        super().__init__(name, city, foundation_year , stadium_name)
        self.stadium_name = stadium_name
        self.capacity = capacity

    stadium_list = dict()

    id = 1
    def stadium_add(self):
        Stadium.stadium_list[Stadium.id] = [self.stadium_name, self.city , self.foundation_year , self.capacity]
        Stadium.id += 1

    def display_info(self):
        print(f"Club: {self.name}, City: {self.city}, Foundation year: {self.foundation_year}")
        print(f"Stadium: {self.stadium_name}, Capacity: {self.capacity}")


    @staticmethod
    def get_capacity_by_id(stadium_id):
        return Stadium.stadium_list[stadium_id][3]


class Match:

    def __new__(cls , match_date , match_time ,home_team , away_team ,  stadium_id , amount_of_glories):
        instance = super().__new__(cls)
        return  instance

    def __init__(self , match_date , match_time , home_team , away_team, stadium_id , amount_of_glories):
        self.match_date = match_date
        self.match_time = match_time
        self.stadium_id = stadium_id
        self.amount_of_glories = amount_of_glories
        self.home_team = home_team
        self.away_team = away_team

    match_list = dict()
    id = 1

    def set_match(self):
        if self.amount_of_glories < Stadium.get_capacity_by_id(self.stadium_id) and self.match_date not in Match.match_list.values():
            Match.match_list[Match.id] = [self.match_date , self.match_time , self.home_team , self.away_team ,  self.stadium_id]
            Match.id += 1
        else:
            print(f"Stadium on {self.match_date} is full or match date is busy")
            return

    def display_info(self):
        print(Fore.GREEN + "-------------------------------------------------------------")
        print(f"Match date: {self.match_date}, Match time: {self.match_time}")
        print(f"Stadium: {Stadium.stadium_list[self.stadium_id][0]}, City: {Stadium.stadium_list[self.stadium_id][1]}")
        print("-------------------------------------------------------------")
        print(Fore.RESET)

    @staticmethod
    def show_matches():
        print(Fore.GREEN + "-------------------------------------------------------------")
        print("\t id         Plays          Date          Time       Stadium")
        for key, value in Match.match_list.items():
            match = list(value)
            print(f"Match {key}: {match[2]} vs {match[3]} | {match[0]}  | {match[1]} | {Stadium.stadium_list[match[4]][0]}")
        print("-------------------------------------------------------------")
        print(Fore.RESET)


class Person:

    def __new__(cls, name, age, height):
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

class Coach(Club , Person):

    def __new__(cls, name, city, foundation_year, coach_name, experience):
        instance = super().__new__(cls, name, city, foundation_year)
        return instance

    def __init__(self, name, city, foundation_year, coach_name, experience):
        super().__init__(name, city, foundation_year)
        self.coach_name = coach_name
        self.experience = experience

    def display_info(self):
        print(f"Club: {self.name}, City: {self.city}, Foundation year: {self.foundation_year}")
        print(f"Coach: {self.coach_name}, Experience: {self.experience}")


class Player(Person):
    player_list = dict()

    id = 1

    def player_add(self, club_id):
        Player.player_list[Player.id] = [self.name, self.age, self.height , int(club_id)]
        Player.id += 1

    def goal(self):
        print(f"{self.name} scored a goal")

    @staticmethod
    def show_players():
        print("\t id   Name | Age | Height")
        for key, value in Player.player_list.items():
            player = list(value)
            print(f"Player {key}: {player[0]}   {player[1]}     {player[2]}")

    @staticmethod
    def show_club_players():
        for club_key, club_value in Club.club_list.items():
            club_players = [player for player in Player.player_list.values() if player[3] == club_key]
            if club_players:
                print(f"Players in club {club_key} ({club_value[0]}):")
                print("id  Name | Age | Height")
                for player_key , player_value in Player.player_list.items():
                    if player_value[3] == club_key:
                        player = list(player_value)
                        print("________________________")
                        print(f"{player_key}  {player[0]}   {player[1]}    {player[2]}")
                        print("________________________")
                print("\n")
            else:
                print(Fore.RED + f"No players in club {club_key} Name: {club_value[0]}")
                print(Fore.RESET)

    def update_player(self, club_id):
        for key , value in Player.player_list.items():
            if value[0] == self.name and value[1] == self.age and value[2] == self.height:
                Player.player_list[key] = [self.name , self.age , self.height , int(club_id)]


player_Dynamo = Player("Oleg ", "18", "186")
player_Dynamo2 = Player("Vlad", "19", "190")
player_Shahtar = Player("Vova", "20", "180")
player_Shahtar2 = Player("Dima", "21", "175")

player_Dynamo.player_add(1)
player_Dynamo2.player_add(1)
player_Shahtar.player_add(2)
player_Shahtar2.player_add(2)

club1 = Club("Dynamo", "Kyiv", "1927" , "NSC Olimpiyskiy")
club2 = Club("Shakhtar", "Donetsk", "1936" , "Donbass Arena")
club3 = Club("Zorya" , "Luhansk" , "1923" , "Slavutych Arena")

club1.club_add()
club2.club_add()
club3.club_add()

Player.show_players()

stadium1 = Stadium("Dynamo", "Kyiv", "1927" , "NSC Olimpiyskiy", 70050)
stadium1.stadium_add()

match1 = Match("2021-10-10" , "20:00" , club1.name , club2.name ,  1 , 70000)
match1.set_match()

match2 = Match("2021-11-10" , "21:00" , club1.name , club3.name , 1 , 65000)
match2.set_match()
Match.show_matches()

club1.display_info()

Player.show_club_players()

player_Dynamo2.update_player(3)

Player.show_club_players()

player_Dynamo.goal()