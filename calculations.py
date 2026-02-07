"""
Core calculations for exam readiness and scoring.
"""


def calculate_projected_band(listening, reading, writing, speaking):
    """
    Calculate projected band based on section scores.
    
    Args:
        listening, reading, writing, speaking: Individual section scores (0-9)
    
    Returns:
        tuple: (projected_band, average, weakest)
    """
    sections = [listening, reading, writing, speaking]
    average = sum(sections) / 4
    weakest = min(sections)
    
    # Band ceiling is constrained by weakest section
    projected_band = min(average, weakest + 0.5)
    projected_band = round(projected_band, 1)
    
    return projected_band, average, weakest, sections


def calculate_readiness(accuracy, consistency, mocks, average):
    """
    Calculate overall readiness score.
    
    Args:
        accuracy: Practice accuracy percentage (0-100)
        consistency: Study days per week (0-7)
        mocks: Number of mock tests taken (0-10)
        average: Average section score (0-9)
    
    Returns:
        int: Readiness percentage (0-100)
    """
    readiness = (
        accuracy * 0.35 +
        (consistency / 7) * 100 * 0.25 +
        (mocks / 10) * 100 * 0.2 +
        (average / 9) * 100 * 0.2
    )
    return int(min(100, readiness))


def determine_zone(readiness):
    """
    Determine readiness zone based on readiness score.
    
    Args:
        readiness: Readiness percentage (0-100)
    
    Returns:
        str: Zone indicator with emoji
    """
    if readiness < 50:
        return "🔴 Risk Zone"
    elif readiness < 75:
        return "🟡 Momentum Zone"
    else:
        return "🟢 Safe Zone"


def get_next_action(readiness):
    """
    Get recommended next action based on readiness level.
    
    Args:
        readiness: Readiness percentage (0-100)
    
    Returns:
        tuple: (action_type, message)
    """
    if readiness < 50:
        return "error", "Increase study consistency to at least 4 days/week and take a mock test immediately."
    elif readiness < 75:
        return "info", "Focus on your weakest section and increase accuracy by ~10% to enter the safe zone."
    else:
        return "success", "Maintain momentum and focus on advanced practice."


def get_risk_assessment(band_gap, exam_days):
    """
    Assess exam risk based on band gap and time remaining.
    
    Args:
        band_gap: Difference between target and projected band
        exam_days: Days until exam
    
    Returns:
        tuple: (assessment_level, message)
    """
    if band_gap > 0 and exam_days < 30:
        return "error", f"At current pace, you may miss your target by ~{band_gap} band."
    else:
        return "success", "You are currently on track based on preparation velocity."


def get_confidence_level(mocks, consistency):
    """
    Determine prediction confidence based on data points.
    
    Args:
        mocks: Number of mock tests taken
        consistency: Study days per week
    
    Returns:
        str: Confidence level
    """
    if mocks >= 5 and consistency >= 4:
        return "High"
    elif mocks >= 2:
        return "Medium"
    else:
        return "Low"
