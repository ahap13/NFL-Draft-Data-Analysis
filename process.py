
import sqlite3

# Connect to draft_picks DB
conn = sqlite3.connect("draft_picks.sqlite")
cur = conn.cursor()

# Drop table if exists, create player table with year, round, pick,
# ovr_pick, name, age, side, pos, pos group, pb, ap, hof, games, seasons_started
cur.execute("DROP TABLE IF EXISTS Player")

cur.execute('''CREATE TABLE Player (
            year INTEGER, round INTEGER, pick INTEGER,
            name TEXT, age INTEGER, side TEXT, pos TEXT,
            pb INTEGER, ap INTEGER, hof INTEGER, games INTEGER,
            seasons_started INTEGER)''')

# Open data
data = open("/Users/alechapiak/Desktop/SWE/py4e/capstone/project/draft_picks.csv")

# season,round,pick,team,gsis_id,pfr_player_id,cfb_player_id,pfr_player_name,hof,position,category,side,college,age,to,allpro,probowls,seasons_started,w_av,car_av,dr_av,games,pass_completions,pass_attempts,pass_yards,pass_tds,pass_ints,rush_atts,rush_yards,rush_tds,receptions,rec_yards,rec_tds,def_solo_tackles,def_ints,def_sacks
# 1980,    1,    1,  DET,  "",      SimsBi00,  billy-sims-1,  Billy Sims,  FALSE,   RB,       RB,    O,Oklahoma,24,1984,  0,     3,       5,             58,  ,       58,  60,       0  ,            0,             0,        0,      0,      1131,      5106,      42,      186,      2072,      5,          ,            ,
#  0       1     2    3     4          5           6             7          8       9         10    11   12     13  14   15     16        17             18   19      20   21        22              23              24        25     26      27          28         29       30        31          32        33             34         35      

# Parse data
for line in data:
    pieces = line.split(",")
    year = pieces[0]
    round = pieces[1]
    pick = pieces[2]
    name = pieces[7]
    age = pieces[13]
    side = pieces[11]
    pos = pieces[9]
    pb = pieces[16]
    ap = pieces[15]

    if pieces[8] == "TRUE": hof = 1
    else: hof = 0

    games = pieces[21]
    seasons_started = pieces[17]

    # Populate Player table
    cur.execute('''INSERT OR IGNORE INTO Player
                (year, round, pick, name, age, side, pos, pb, ap, hof, games, seasons_started)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (year, round, pick, name, age, side, pos, pb, ap, hof, games, seasons_started))
    
    print("Retreived " + name + "...")
    
    conn.commit()

print("Finished")

conn.close()
    