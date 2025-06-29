def score_leads(df):
    def simple_score(row):
        score = 0
        if 'AI' in row['Industry']: score += 50
        if row['Location'] == 'India': score += 30
        if row['Email']: score += 20
        return score

    df['Lead Score'] = df.apply(simple_score, axis=1)
    return df.sort_values("Lead Score", ascending=False)
