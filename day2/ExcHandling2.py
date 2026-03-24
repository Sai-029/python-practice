def score(marks):
    try:
        marks = float(marks)

        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        else:
            return "Fail"

    except (ValueError, TypeError):
        return "Invalid input! Please enter a number."
    
print(score(85))
print(score("92"))
print(score("abc"))