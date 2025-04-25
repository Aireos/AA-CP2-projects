def info_pull():
    with open('overall.csv', 'r') as file:
        reader = reader(file)
        next(reader)
        level_scores = []
        for row in reader:
            score = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
            level_scores.append(score)

    with open('personal.csv', 'r') as file:
        reader = reader(file)
        next(reader)
        users = []
        for row in reader:
            user = {
                "name": row[0],
                "password": row[1],
                "unlocked": row[2],
                "scores": row[3],
                "preferences": row[4]
            }
            users.append(user)

    return users, level_scores

def personal_leaderboard(old_user_score, new_score):
    if old_user_score >= new_score:
        best_score = old_user_score
    else:
        best_score = new_score
    user_score = best_score
    return user_score

def overall_leaderboard(old_level_scores, new_score):
    combined_scores = old_level_scores + new_score
    combined_scores.sort(key=lambda x: x['score'], reverse=True)
    top_9 = combined_scores[:9]
    level_scores = []
    for score in top_9:
        level_scores.append(score)
    return level_scores

def save_info(level_scores, users):
    with open('overall.csv', 'w') as file:
        writer = writer(file)
        writer.writerow(['Level Number', 'Score 1', 'Score 2', 'Score 3', 'Score 4', 'Score 5', 'Score 6', 'Score 7', 'Score 8', 'Score 9'])
        for level in level_scores:
            writer.writerow(level)

    with open('personal.csv', 'w') as file:
        writer = writer(file)
        writer.writerow(['Username', 'Password', 'Unlocked Levels', 'Top Score for Each Level', 'Preferences'])
        for user in users:
            writer.writerow([user['name'], user['password'], user['unlocked'], user['scores'], user['preferences']])