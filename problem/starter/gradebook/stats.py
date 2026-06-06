"""gradebook.stats — aggregate statistics over grade records."""
from typing import List,Dict,Set,Tuple

def average_per_student(records: List[Dict]) -> Dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    student_scores = {}
    for record in records:
        name = record["name"]
        score = record["score"]
        if name not in student_scores:
            student_scores[name] = []
        student_scores[name].append(score)
    averages = {}
    for name, scores in student_scores.items():
        averages[name] = round(sum(scores) / len(scores), 2)
    return averages

def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    return {record["subject"] for record in records}
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    averages = average_per_student(records)
    if not averages:
        return ("", 0.0)
    top_student = max(averages, key=averages.get)
    return (top_student, averages[top_student])
    pass


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    averages = average_per_student(records)
    passing = [name for name, avg in averages.items() if avg >= threshold]
    return sorted(passing)
    pass
