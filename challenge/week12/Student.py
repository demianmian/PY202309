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