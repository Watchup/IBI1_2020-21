def grade_calculator(name, portfolio_grade, poster_grade, exam_grade):
    '''
    input:
        name: Student name
        portfolio_grade: Student grade for the code portfolio
        poster_grade: Student grade for the poster presentation
        exam_grade: tudent grade in the final exam
    returns: student names and their final grades
    '''
    final_grade = poster_grade*0.3 + portfolio_grade*0.4 + exam_grade*0.3
    return name, final_grade

# Example
Example = grade_calculator("San Zhang", 90, 80, 70)

print(Example[0], Example[1])
