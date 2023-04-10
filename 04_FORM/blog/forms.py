from django import forms
from .models import Student

# 1. 사용자 입력의 유효성 검증 (Validation)
# 2. Views에서 입력 <=> 필드 직접 매칭 귀찮
# 3. HTML에서 input태그 생성 귀찮

class StudentForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=20)
    age = forms.IntegerField(min_value=19, max_value=100)
    balance = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Student
        fields = '__all__'
        # fields에 적힌 필드만 html input 태그 생성 및 검증해준다!!!!!!!!
        # fields = ('name', 'age', 'balance')
        # 위 처럼 적으면 name, age, balace의 값만 유효성을 검증함.
        # exclude = ('mbti', )
        # exclude로 쓰면 'mbti'는 유효성 검증에서 제외한다! 라는 말이 된다.
        # 하나만 쓰게 된다면 반드시 , 를 쓴다! 아니면 튜플이 아니게 된다..
