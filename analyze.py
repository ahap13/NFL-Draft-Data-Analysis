
import sqlite3
import itertools

conn = sqlite3.connect("draft_picks.sqlite")
cur = conn.cursor()

# What year produced the most HOF, AP, PB, Games, Seasons Started?
def year_top5():
    scores = dict()
    # Get the top 5 by year for each category. Assign points for scoring top 5, add to respective table
    cur.execute('SELECT year, sum(hof) FROM Player GROUP BY year ORDER BY sum(hof) DESC LIMIT 5')
    count = 1
    print("Top 5 years producing HOFers:")
    for row in cur:
        year = row[0]
        yhof = row[1]
        # Add score
        if count == 1: scores[year] = 5
        elif count == 2: scores[year] = 4
        elif count == 3: scores[year] = 3
        elif count == 4: scores[year] = 2
        elif count == 5: scores[year] = 1
        # Print data
        print(str(year) + ": " + str(yhof))
        count += 1
    
    cur.execute('SELECT year, count(ap) FROM Player WHERE ap > 0 GROUP BY year ORDER BY count(ap) DESC LIMIT 5')
    count = 1
    print("\nTop 5 years producing all-pros:")
    for row in cur:
        year = row[0]
        yap = row[1]
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 5
            else: scores[row[0]] = 5
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 4
            else: scores[row[0]] = 4
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(year) + ": " + str(yap))
        count += 1
    
    cur.execute('SELECT year, sum(ap) FROM Player GROUP BY year ORDER BY sum(ap) DESC LIMIT 5')
    count = 1
    print("\nTop 5 years by total all-pro appearances:")
    for row in cur:
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 5
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 2.5
            else: scores[row[0]] = 4
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 3
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 1.5
            else: scores[row[0]] = 2
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(row[0]) + ": " + str(row[1]))
        count += 1

    cur.execute('SELECT year, count(pb) FROM Player WHERE pb > 0 GROUP BY year ORDER BY count(pb) DESC LIMIT 5')
    print("\nTop 5 years producing pro-bowlers:")
    count = 1
    for row in cur:
        year = row[0]
        ypb = row[1]
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 5
            else: scores[row[0]] = 5
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 4
            else: scores[row[0]] = 4
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(year) + ": " + str(ypb))
        count += 1

    cur.execute('SELECT year, sum(pb) FROM Player GROUP BY year ORDER BY sum(pb) DESC LIMIT 5')
    print("\nTop 5 years by total pro-bowl appearances:")
    count = 1
    for row in cur:
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 5
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 2.5
            else: scores[row[0]] = 4
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 3
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 1.5
            else: scores[row[0]] = 2
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(row[0]) + ": " + str(row[1]))
        count += 1

    cur.execute('SELECT year, sum(games) FROM Player GROUP BY year ORDER BY sum(games) DESC LIMIT 5')
    print("\nTop 5 years by total games played:")
    count = 1
    for row in cur:
        year = row[0]
        ygms = row[1]
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 5
            else: scores[row[0]] = 5
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 4
            else: scores[row[0]] = 4
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(year) + ": " + str(ygms))
        count += 1
    
    cur.execute('SELECT year, sum(seasons_started) FROM Player GROUP BY year ORDER BY sum(seasons_started) DESC LIMIT 5')
    print("\nTop 5 years by total seasons started:")
    count = 1
    for row in cur:
        year = row[0]
        yss = row[1]
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 5
            else: scores[row[0]] = 5
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 4
            else: scores[row[0]] = 4
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(year) + ": " + str(yss))
        count += 1

    # Return top 5 draft classes of all time
    scores_sorted = dict(sorted(scores.items(), key=lambda item:item[1], reverse=True))
    count = 1
    print("\n-------------------------")
    print("Top 5 draft classes of all time:")
    for k,v in  scores_sorted.items():
        if count == 6: break
        print(str(k) + ": " + str(v) + " points")
        count += 1
    print("-------------------------\n")


# What round produced the most HOF, AP, PB, Games, Seasons Started?
def by_round():
    scores = dict()

    # Sort by round for each category. Assign points based on position, add to respective table
    cur.execute('SELECT round, sum(hof) FROM Player WHERE round > 0 GROUP BY round ORDER BY sum(hof) DESC')
    count = 1
    print("HOFers produced by round:")
    for row in cur:
        if row[0] == "round": continue
        round = row[0]
        rhof = row[1]
        if count == 1: scores[row[0]] = 7
        elif count == 2: scores[row[0]] = 6
        elif count == 3: scores[row[0]] = 5
        elif count == 4: scores[row[0]] = 4
        elif count == 5: scores[row[0]] = 3
        elif count == 6: scores[row[0]] = 2
        elif count == 7: scores[row[0]] = 1
        else: scores[row[0]] = 0
        print(str(round) + ": " + str(rhof))
        count += 1
    
    cur.execute('SELECT round, count(ap) FROM Player WHERE ap > 0 GROUP BY round ORDER BY count(ap) DESC')
    count = 1
    print("\nAll-pros produced by round:")
    for row in cur:
        if row[0] == "round": continue
        round = row[0]
        rap = row[1]
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 7
            else: scores[row[0]] = 7
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 6
            else: scores[row[0]] = 6
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 5
            else: scores[row[0]] = 5
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 4
            else: scores[row[0]] = 4
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 6: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 7: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(round) + ": " + str(rap))
        count += 1

    cur.execute('SELECT round, sum(ap) FROM Player GROUP BY round ORDER BY sum(ap) DESC')
    count = 1
    print("\nTotal all-pro appearances by round:")
    for row in cur:
        if row[0] == "round": continue
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 3.5
            else: scores[row[0]] = 3.5
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 2.5
            else: scores[row[0]] = 2.5
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 1.5
            else: scores[row[0]] = 1.5
        if count == 6: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        if count == 7: 
            if row[0] in scores: scores[row[0]] += .5
            else: scores[row[0]] = .5
        print(str(row[0]) + ": " + str(row[1]))
        count += 1

    cur.execute('SELECT round, count(pb) FROM Player WHERE pb > 0 GROUP BY round ORDER BY count(pb) DESC')
    print("\nPro-bowlers produced by round:")
    count = 1
    for row in cur:
        if row[0] == "round": continue
        round = row[0]
        rpb = row[1]
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 7
            else: scores[row[0]] = 7
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 6
            else: scores[row[0]] = 6
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 5
            else: scores[row[0]] = 5
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 4
            else: scores[row[0]] = 4
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 6: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 7: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(round) + ": " + str(rpb))
        count += 1

    cur.execute('SELECT round, sum(pb) FROM Player GROUP BY round ORDER BY sum(pb) DESC')
    print("\nTotal pro-bowl appearances by round:")
    count = 1
    for row in cur:
        if row[0] == "round": continue
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 3.5
            else: scores[row[0]] = 3.5
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 2.5
            else: scores[row[0]] = 2.5
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 1.5
            else: scores[row[0]] = 1.5
        if count == 6: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        if count == 7: 
            if row[0] in scores: scores[row[0]] += .5
            else: scores[row[0]] = .5
        print(str(row[0]) + ": " + str(row[1]))
        count += 1
    
    conn.commit()

    cur.execute('SELECT round, sum(games) FROM Player GROUP BY round ORDER BY sum(games) DESC')
    print("\nTop draft rounds by games played:")
    count = 1
    for row in cur:
        if row[0] == "round": continue
        round = row[0]
        rgms = row[1]
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 7
            else: scores[row[0]] = 7
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 6
            else: scores[row[0]] = 6
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 5
            else: scores[row[0]] = 5
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 4
            else: scores[row[0]] = 4
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 6: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 7: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(round) + ": " + str(int(rgms)))
        count += 1

    cur.execute('SELECT round, sum(seasons_started) FROM Player GROUP BY round ORDER BY sum(seasons_started) DESC')
    print("\nTop 5 years by total seasons started:")
    count = 1
    for row in cur:
        if row[0] == "round": continue
        round = row[0]
        rss = row[1]
        if count == 1: 
            if row[0] in scores: scores[row[0]] += 7
            else: scores[row[0]] = 7
        if count == 2: 
            if row[0] in scores: scores[row[0]] += 6
            else: scores[row[0]] = 6
        if count == 3: 
            if row[0] in scores: scores[row[0]] += 5
            else: scores[row[0]] = 5
        if count == 4: 
            if row[0] in scores: scores[row[0]] += 4
            else: scores[row[0]] = 4
        if count == 5: 
            if row[0] in scores: scores[row[0]] += 3
            else: scores[row[0]] = 3
        if count == 6: 
            if row[0] in scores: scores[row[0]] += 2
            else: scores[row[0]] = 2
        if count == 7: 
            if row[0] in scores: scores[row[0]] += 1
            else: scores[row[0]] = 1
        print(str(round) + ": " + str(rss))
        count += 1

    # Return ranked draft rounds
    scores_sorted = dict(sorted(scores.items(), key=lambda item:item[1], reverse=True))
    print("\n-------------------------")
    print("All draft rounds ranked:")
    for k,v in  scores_sorted.items():
        print(str(k) + ": " + str(v) + " points")
    print("-------------------------\n")


# Get most common picked side and pos, avg age each year
def position_stats():

    # Count side, display how many times each side was preferred
    count = dict() # Y O F {1980, [145, 167], 1981, [150, 158]}
    cur.execute('SELECT year, side FROM Player')
    for row in cur:
        year = row[0]
        side = row[1]
        if year == "season": continue
        if year in count: 
            if side == "O": count[year][0] += 1
            else: count[year][1] +=1 
        else: 
            if side == "O": count[year] = [1, 0]
            else: count[year] = [0, 1]
    
    o_count = 0
    d_count = 0
    for k,v in count.items():
        if v[0] < v[1]: d_count +=1
        else: o_count += 1
    
    print("Years that picked more offense: " + str(o_count))
    print("Years that picked more defense: " + str(d_count))
    print("")


    # Top 5 Pos with most years as most picked
    pos_counts = dict()
    cur.execute('SELECT year, pos FROM Player')
    for row in cur:
        year = row[0]
        pos = row[1]
        if year == "season": continue
        # Populate pos_counts with how many times each position was picked.
        if year not in pos_counts.keys(): 
            pos_counts[year] = {pos: 1}
        else:
            if pos not in pos_counts[year]:
                pos_counts[year][pos] = 1
            else:
                pos_counts[year][pos] += 1
    
    # Calc top pos picked each year
    for key in pos_counts.keys():
        max = -1
        for second_key, val in pos_counts[key].items():
            pos = second_key
            freq = val
            if freq > max: 
                max = freq
                pos_counts[key] = {pos: freq}
    
    top_pos_count = dict()
    for key in pos_counts.keys():
        for second_key, val in pos_counts[key].items():
            if second_key not in top_pos_count:
                top_pos_count[second_key] = 1
            else:
                top_pos_count[second_key] += 1
    
    # Get top 5 top positions
    top_pos_sorted = dict(sorted(top_pos_count.items(), key=lambda item:item[1], reverse=True))
    top_pos_sorted = list(top_pos_sorted.items())[:5]
    print("Top 5 positions that have been picked the most in a given year:")
    for pos in top_pos_sorted:
        print(pos[0] + ": " + str(pos[1]))


year_top5()
by_round()
position_stats()
    
conn.close()
