import os
print(os.getcwd())
# 학생 클래스 
class Student:
    # 생성자: 이름, 국어, 수학, 영어 점수를 초기화
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = float(korean)
        self.math = float(math)
        self.english = float(english)
    
    # 평균 점수를 계산하여 반환하는 메서드
    def get_average(self):
        return (self.korean + self.math + self.english) / 3

# 파일에서 데이터를 읽어와서 Student 객체 리스트를 생성하는 함수
def loadData(filepath):
    with open(r"C:\Users\asb09\py_test\PY202309\challenge\week11\student.csv", "r", encoding="utf8") as file:
        lines = file.readlines()
        
    students = []
    for line in lines[1:]:  # 첫 번째 줄(헤더)은 건너뛴다.
        name, korean, math, english = line.strip().split(',')
        students.append(Student(name, korean, math, english))
    return students

# 학생들의 평균 점수를 계산하고 파일에 저장하는 함수
def save_averages(students, filepath):
    with open(r"C:\Users\asb09\py_test\PY202309\challenge\week11\average1.txt", "w", encoding="utf8") as file:
        file.write("-----학생들의 평균 점수-----\n")
        print("-----학생들의 평균 점수-----")
        for student in students:
            average = student.get_average()
            output_line = f"{student.name}의 평균 점수는 {average} 입니다.\n"
            print(output_line.strip())  # 콘솔에 출력
            file.write(output_line)  # 파일에 저장

# 메인 실행 부분
if __name__ == "__main__":
    # loadData 함수를 호출하여 학생 정보를 불러온다.
    students = loadData(r"C:\Users\asb09\py_test\PY202309\challenge\week11\student.csv")
    
    # save_averages 함수를 호출하여 평균 점수를 계산하고 파일에 저장한다.
    save_averages(students, r"C:\Users\asb09\py_test\PY202309\challenge\week11\average1.txt")
