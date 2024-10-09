class User:
    nicknames = []
    passwords = []
    ages = []
    def __init__(self,nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        User.nicknames.append(nickname)
        User.passwords.append(password)
        User.ages.append(age)

class Video:
    title = []
    durations = []
    time_now = []
    adult_mode = []
    def __init__(self, title,  duration,  time_now=0, adult_mode = False):
        self.title = title
        self. durations =  duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        Video.title.append(title)
        Video.durations.append(duration)
        Video.time_now.append(time_now)
        Video.adult_mode.append(adult_mode)


class UrTube:
    users = []
    videos = []
    current_user = (None)
    def __init__(self, users, videos, current_user):
        self.current_user = current_user
        self.users = users
        self.videos = videos
    def  log_in(self, nickname, password):
        login = nickname
        password = password
        if login in User.nicknames:
            name = User.nicknames.index(f"{login}")
            if password == User.passwords[name]:
                print(f"Добро пожаловать {login}")
                UrTube.current_user = login
            else:
                print("Парроль не верен")
                exit()
    def register(self, nickname, password, age):
        i = 0
        for f in User.nicknames:
            if f == nickname:
                i += 1
        if i == 0:
            nickname = User(nickname,password,age)
            UrTube.users.append(nickname)
            UrTube.current_user = nickname
    def log_out(self):
        UrTube.current_user = None
    def add_vidio(self, *video):
        for i in video:
            if i not in UrTube.videos:
                UrTube.videos.append(i)
            elif not isinstance(i, Video):
                print("Объект не подходящего класса.")
                break
            elif i in UrTube.videos:
                print("Один из роликов уже есть на платформе")
                break
    def get_videos(self, name):
        name2 = name.lower()
        name3 = []
        f = 0
        for i in UrTube.videos:
            name1 = i.lower()
            if name2 in name1:
                name3.append(name1)
                f += 1
        if f > 0:
            print(name3)
        else:
            print("Ничего не найдено")
    def watch_video(self, name):
        if UrTube.current_user != None:
            for i in UrTube.videos:
                if name == i:
                    chel = UrTube.current_user
                    chelid = User.nicknames[f"{chel}"]
                    chelage = User.age[chelid]
                    if Video.adult_mode[f"{name}"] == True:
                        if chelage >= 18:
                            j == Video.title[f"{name}"]
                            l = 0
                            while l < Video.duration[j]:
                                print(f'{j}:{Video.durations[j]}')
                                l += 1
                            print("Конец видео")
                            break
                    else:
                        j == Video.title[f"{name}"]
                        l = 0
                        while l < Video.duration[j]:
                            print(f'{j}:{Video.durations[j]}')
                            l += 1
                        print("Конец видео")
                        break
        else:
            print("Вы не вошли в акаунт")


#ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
UrTube.add_vidio(Video,v1, v2)

# Проверка поиска
print(UrTube.get_videos(UrTube,'лучший'))
print(UrTube.get_videos(UrTube,'ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
UrTube.watch_video(UrTube,'Для чего девушкам парень программист?')
UrTube.register(UrTube,'vasya_pupkin', 'lolkekcheburek', 13)
UrTube.watch_video(UrTube,'Для чего девушкам парень программист?')
UrTube.register(UrTube,'urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
UrTube.watch_video(UrTube,'Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
UrTube.register(UrTube,'vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(UrTube.current_user)

# Попытка воспроизведения несуществующего видео
UrTube.watch_video(UrTube,'Лучший язык программирования 2024 года!')






