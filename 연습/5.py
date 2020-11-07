import requests
MYKEY = '2e55b602956681cb520a7d64930d1274'
tmd_id = 278
CREDITS_URL = f"https://api.themoviedb.org/3/movie/{tmd_id}/credits?api_key={MYKEY}"
creditsData = requests.get(CREDITS_URL)
crewDatas = creditsData.json().get('crew')
chk1 = False
for i in range(10):
    if crewDatas[i].get('job') == 'Director':
        director_name = crewDatas[i].get('name')
        director_id = crewDatas[i].get('id')
        print(director_name)
        break