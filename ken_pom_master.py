import json, matplotlib.pyplot as plt

y = input("Team 1? ")
z = input("Team 2? ")
x = 0
teams = []
team1 = []
team2 = []
team3 = []
team4 = []
# number of teams in graph
index = [0,2,4,6,8,10,12,14,16]
index1 = [1,3,5,7,9,11,13,15, 17]
# open JSON file
with open("scrapy/tutorial/kenpom/json_testing0113.json", "r") as read_file:
    data = json.load(read_file)

 # -1 to avoid out of index error
while x <= len(data[0]['team'])-1:
    # looks for teams in z or y
    if data[0]['team'][x] == y:
        team1 = data[0]['adjem'][x], data[0]['adjo'][x], data[0]['adjd'][x], data[0]['adjt'][x], data[0]['luck'][x], data[0]['sos-adjem'][x], data[0]['sos-oppo'][x], data[0]['sos-oppd'][x], data[0]['ncsos-adjem'][x]
        for i in team1: team3.append(float(i))
        team3[4] = team3[4]*1000
        teams.append(data[0]['team'][x])
    #else:
        #pass

    if data[0]['team'][x] == z:
        team2 = data[0]['adjem'][x], data[0]['adjo'][x], data[0]['adjd'][x], data[0]['adjt'][x], data[0]['luck'][x], data[0]['sos-adjem'][x], data[0]['sos-oppo'][x], data[0]['sos-oppd'][x], data[0]['ncsos-adjem'][x]
        for i in team2: team4.append(float(i))
        team4[4] = team4[4]*1000
        teams.append(data[0]['team'][x])
    #else:
        #pass
        # append team to teams dict

    # increment to next index
    x += 1

teams.reverse()
# plot graph
team5 = plt.bar(index, team3, width = .5, bottom=None, align = 'edge')
team6 = plt.bar(index1, team4, width = -.5, bottom=None, align = 'edge')
plt.legend((team5, team6), teams)
#newIndex = [e / 2 for e in index1]
plt.xticks((.5, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5), ('adjem', 'adjo', 'adjd', 'adjt', 'luck*1000', 'sos-adjem', 'sos-oppo', 'sos-oppd', 'ncsos-adjem'))
plt.show()


#N = 5
#men_means = (20, 35, 30, 35, 27)
#women_means = (25, 32, 34, 20, 25)

##ind = np.arange(N)
#width = 0.35
#plt.bar(ind, men_means, width, label='Men')
#plt.bar(ind + width, women_means, width,
#    label='Women')

#plt.ylabel('Scores')
#plt.title('Scores by group and gender')

#plt.xticks(ind + width / 2, ('G1', 'G2', 'G3', 'G4', 'G5'))
#plt.legend(loc='best')
#plt.show()
