def student_grade_system(name, g1, g2, g3) :
    average = (g1 + g2 + g3) / 3

    average = int(average*100) / 100
    if average >= 40:
        status = "Pass"
    else:
        status = "fail"
    return f"Average grade: {average}, Status: {status}"
if __name__ == "__main__":
    name = input().strip()
    grades = list(map(int, input().split()))
    print(student_grade_system(name, grades))