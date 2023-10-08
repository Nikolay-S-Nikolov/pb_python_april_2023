import math

series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_duration_without_commercials = float(input())

episode_duration = episode_duration_without_commercials * (1 + 0.20)
special_episode_time_extension = seasons_count * 10
total_time = math.floor(seasons_count * episodes_count * episode_duration + special_episode_time_extension)

print(f"Total time needed to watch the {series_name} series is {total_time} minutes.")
