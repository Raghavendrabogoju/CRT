
def calculate_average(grades):
    return sum(grades) / len(grades)


def get_status(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


def student_grade_system(name, grades):
    average = calculate_average(grades)
    status = get_status(average)
    return f"Average grade: {average:.2f}, Status: {status}"


if __name__ == "__main__":
    name = input().strip()
    grades = list(map(int, input().split()))
    print(student_grade_system(name, grades))