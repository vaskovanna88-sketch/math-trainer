def check_answer(user_answer, correct_answer):
    try:
        return abs(float(user_answer) - float(correct_answer)) < 0.001
    except:
        return False