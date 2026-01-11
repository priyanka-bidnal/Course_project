from online import calculate_engagement_score, get_learning_status
def test_calculate_engagement_score():
    # 20 students studying 4 hours each
    assert calculate_engagement_score(20, 4) == 80
def test_highly_engaged_course():
    assert get_learning_status(150) == "Highly Engaged Course"
def test_moderately_engaged_course():
    assert get_learning_status(90) == "Moderately Engaged Course"
def test_low_engagement_course():
    assert get_learning_status(40) == "Low Engagement Course"
