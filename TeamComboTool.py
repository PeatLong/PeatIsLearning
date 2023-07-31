import pandas as pd

print("Welcome to the NHL hybrid team tool! Work out the ultimate team to be made from mashing together two teams from the 92-93 season onwards.")

team1 = input("What's the first team you want to try today? Please note team names should be entered as just nickname and capitalised i.e. Ducks, Blue Jackets, Predators etc.etc. or the program will not work ")
team2 = input("What's the second team you want to try today? ")

if team1 == "Ducks":
    df = pd.read_csv('DucksS9223.csv')
    df2 = pd.read_csv('DucksG9223.csv')
elif team1 == "Coyotes":
    df = pd.read_csv('CoyotesS9223.csv')
    df2 = pd.read_csv('CoyotesG9223.csv')
elif team1 == "Bruins":
    df = pd.read_csv('BruinsS9223.csv')
    df2 = pd.read_csv('BruinsG9223.csv')
elif team1 == "Sabres":
    df = pd.read_csv('SabresS9223.csv')
    df2 = pd.read_csv('SabresG9223.csv')
elif team1 == "Flames":
    df = pd.read_csv('FlamesS9223.csv')
    df2 = pd.read_csv('FlamesG9223.csv')
elif team1 == "Hurricanes":
    df = pd.read_csv('HurricanesS9223.csv')
    df2 = pd.read_csv('HurricanesG9223.csv')
elif team1 == "Blackhawks":
    df = pd.read_csv('BlackhawksS9223.csv')
    df2 = pd.read_csv('BlackhawksG9223.csv')
elif team1 == "Avalanche":
    df = pd.read_csv('AvalancheS9223.csv')
    df2 = pd.read_csv('AvalancheG9223.csv')
elif team1 == "Blue Jackets":
    df = pd.read_csv('BluejacketsS9223.csv')
    df2 = pd.read_csv('BluejacketsG9223.csv')
elif team1 == "Stars":
    df = pd.read_csv('StarsS9223.csv')
    df2 = pd.read_csv('StarsG9223.csv')    
elif team1 == "Red Wings":
    df = pd.read_csv('RedwingsS9223.csv')
    df2 = pd.read_csv('RedwingsG9223.csv')
elif team1 == "Oilers":
    df = pd.read_csv('OilersS9223.csv')
    df2 = pd.read_csv('OilersG9223.csv')
elif team1 == "Panthers":
    df = pd.read_csv('PanthersS9223.csv')
    df2 = pd.read_csv('PanthersG9223.csv')
elif team1 == "Kings":
    df = pd.read_csv('KingsS9223.csv')
    df2 = pd.read_csv('KingsG9223.csv')    
elif team1 == "Wild":
    df = pd.read_csv('WildS9223.csv')
    df2 = pd.read_csv('WildG9223.csv')
elif team1 == "Canadiens":
    df = pd.read_csv('CanadiensS9223.csv')
    df2 = pd.read_csv('CanadiensG9223.csv')
elif team1 == "Predators":
    df = pd.read_csv('PredatorsS9223.csv')
    df2 = pd.read_csv('PredatorsG9223.csv')
elif team1 == "Devils":
    df = pd.read_csv('DevilsS9223.csv')
    df2 = pd.read_csv('DevilsG9223.csv')
elif team1 == "Islanders":
    df = pd.read_csv('IslandersS9223.csv')
    df2 = pd.read_csv('IslandersG9223.csv')    
elif team1 == "Rangers":
    df = pd.read_csv('RangersS9223.csv')
    df2 = pd.read_csv('RangersG9223.csv')
elif team1 == "Senators":
    df = pd.read_csv('SenatorsS9223.csv')
    df2 = pd.read_csv('SenatorsG9223.csv')    
elif team1 == "Flyers":
    df = pd.read_csv('FlyersS9223.csv')
    df2 = pd.read_csv('FlyersG9223.csv')       
elif team1 == "Penguins":
    df = pd.read_csv('PenguinsS9223.csv')
    df2 = pd.read_csv('PenguinsG9223.csv')
elif team1 == "Sharks":
    df = pd.read_csv('SharksS9223.csv')
    df2 = pd.read_csv('SharksG9223.csv')
elif team1 == "Kraken":
    df = pd.read_csv('KrakenS9223.csv')
    df2 = pd.read_csv('KrakenG9223.csv')
elif team1 == "Blues":
    df = pd.read_csv('BluesS9223.csv')
    df2 = pd.read_csv('BluesG9223.csv')
elif team1 == "Lightning":
    df = pd.read_csv('LightningS9223.csv')
    df2 = pd.read_csv('LightningG9223.csv')
elif team1 == "Leafs":
    df = pd.read_csv('LeafsS9223.csv')
    df2 = pd.read_csv('LeafsG9223.csv')    
elif team1 == "Canucks":
    df = pd.read_csv('CanucksS9223.csv')
    df2 = pd.read_csv('CanucksG9223.csv')
elif team1 == "Knights":
    df = pd.read_csv('KnightsS9223.csv')
    df2 = pd.read_csv('KnightsG9223.csv')    
elif team1 == "Capitals":
    df = pd.read_csv('CapitalsS9223.csv')
    df2 = pd.read_csv('CapitalsG9223.csv')       
elif team1 == "Jets":
    df = pd.read_csv('JetsS9223.csv')
    df2 = pd.read_csv('JetsG9223.csv')    
else:
    print ("Error, please choose again")

if team2 == "Ducks":
    df3 = pd.read_csv('DucksS9223.csv')
    df4 = pd.read_csv('DucksG9223.csv')
elif team2 == "Coyotes":
    df3 = pd.read_csv('CoyotesS9223.csv')
    df4 = pd.read_csv('CoyotesG9223.csv')
elif team2 == "Bruins":
    df3 = pd.read_csv('BruinsS9223.csv')
    df4 = pd.read_csv('BruinsG9223.csv')
elif team2 == "Sabres":
    df3 = pd.read_csv('SabresS9223.csv')
    df4 = pd.read_csv('SabresG9223.csv')
elif team2 == "Flames":
    df3 = pd.read_csv('FlamesS9223.csv')
    df4 = pd.read_csv('FlamesG9223.csv')
elif team2 == "Hurricanes":
    df3 = pd.read_csv('HurricanesS9223.csv')
    df4 = pd.read_csv('HurricanesG9223.csv')
elif team2 == "Blackhawks":
    df3 = pd.read_csv('BlackhawksS9223.csv')
    df4 = pd.read_csv('BlackhawksG9223.csv')
elif team2 == "Avalanche":
    df3 = pd.read_csv('AvalancheS9223.csv')
    df4 = pd.read_csv('AvalancheG9223.csv')
elif team2 == "Blue jackets":
    df3 = pd.read_csv('BluejacketsS9223.csv')
    df4 = pd.read_csv('BluejacketsG9223.csv')
elif team2 == "Stars":
    df3 = pd.read_csv('StarsS9223.csv')
    df4 = pd.read_csv('StarsG9223.csv')    
elif team2 == "Red Wings":
    df3 = pd.read_csv('RedwingsS9223.csv')
    df4 = pd.read_csv('RedwingsG9223.csv')
elif team2 == "Oilers":
    df3 = pd.read_csv('OilersS9223.csv')
    df4 = pd.read_csv('OilersG9223.csv')
elif team2 == "Panthers":
    df3 = pd.read_csv('PanthersS9223.csv')
    df4 = pd.read_csv('PanthersG9223.csv')
elif team2 == "Kings":
    df3 = pd.read_csv('KingsS9223.csv')
    df4 = pd.read_csv('KingsG9223.csv')    
elif team2 == "Wild":
    df3 = pd.read_csv('WildS9223.csv')
    df4 = pd.read_csv('WildG9223.csv')
elif team2 == "Canadiens":
    df3 = pd.read_csv('CanadiensS9223.csv')
    df4 = pd.read_csv('CanadiensG9223.csv')
elif team2 == "Predators":
    df3 = pd.read_csv('PredatorsS9223.csv')
    df4 = pd.read_csv('PredatorsG9223.csv')
elif team2 == "Devils":
    df3 = pd.read_csv('DevilsS9223.csv')
    df4 = pd.read_csv('DevilsG9223.csv')
elif team2 == "Islanders":
    df3 = pd.read_csv('IslandersS9223.csv')
    df4 = pd.read_csv('IslandersG9223.csv')    
elif team2 == "Rangers":
    df3 = pd.read_csv('RangersS9223.csv')
    df4 = pd.read_csv('RangersG9223.csv')
elif team2 == "Senators":
    df3 = pd.read_csv('SenatorsS9223.csv')
    df4 = pd.read_csv('SenatorsG9223.csv')    
elif team2 == "Flyers":
    df3 = pd.read_csv('FlyersS9223.csv')
    df4 = pd.read_csv('FlyersG9223.csv')    
elif team2 == "Penguins":
    df3 = pd.read_csv('PenguinsS9223.csv')
    df4 = pd.read_csv('PenguinsG9223.csv')
elif team2 == "Sharks":
    df3 = pd.read_csv('SharksS9223.csv')
    df4 = pd.read_csv('SharksG9223.csv')
elif team2 == "Kraken":
    df3 = pd.read_csv('KrakenS9223.csv')
    df4 = pd.read_csv('KrakenG9223.csv')
elif team2 == "Blues":
    df3 = pd.read_csv('BluesS9223.csv')
    df4 = pd.read_csv('BluesG9223.csv')
elif team2 == "Lightning":
    df3 = pd.read_csv('LightningS9223.csv')
    df4 = pd.read_csv('LightningG9223.csv')
elif team2 == "Leafs":
    df3 = pd.read_csv('LeafsS9223.csv')
    df4 = pd.read_csv('LeafsG9223.csv')    
elif team2 == "Canucks":
    df3 = pd.read_csv('CanucksS9223.csv')
    df4 = pd.read_csv('CanucksG9223.csv')
elif team2 == "Knights":
    df3 = pd.read_csv('KnightsS9223.csv')
    df4 = pd.read_csv('KnightsG9223.csv')    
elif team2 == "Capitals":
    df3 = pd.read_csv('CapitalsS9223.csv')
    df4 = pd.read_csv('CapitalsG9223.csv')       
elif team2 == "Jets":
    df3 = pd.read_csv('JetsS9223.csv')
    df4 = pd.read_csv('JetsG9223.csv')     
else:
    print ("Error, please choose again")

con_df1 = pd.concat([df, df3])
con_df2 = pd.concat([df2, df4])

df5 = con_df1[(con_df1.duplicated('Player')) & (con_df1['Pos']!='D')]
df6 = con_df1[(con_df1.duplicated('Player')) & (con_df1['Pos']=='D')]
df7 = con_df2[con_df2.duplicated('Player')]

#df6 = con_df1[con_df1.duplicated('Player')]

print("Here's the forwards", df5)
print("Here's the defencemen", df6)
print("Here's the goalies", df7)

