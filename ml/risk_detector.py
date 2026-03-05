def detect_risk(text):

    risk_keywords = [
        "penalty",
        "termination",
        "liability",
        "breach",
        "indemnify"
    ]

    score = 0

    for word in risk_keywords:

        if word in text.lower():

            score += 1

    return score