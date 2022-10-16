time_for_photos = int(input())
scenes = int(input())
time_for_scene = int(input())
total_time_for_scenes = scenes * time_for_scene
prepare_for_photos = round(time_for_photos * 0.15)
total_time = total_time_for_scenes + prepare_for_photos
difference = abs(total_time - time_for_photos)
if total_time <= time_for_photos:
    print(f'You managed to finish the movie on time! You have {difference} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {difference} minutes.')
