# classroom/models.py

from django.db import models
# views.py안에 models.py에서 정의한 클래스를 import하려면
# from .models import Student

# 1 model class : 1 DB table
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    major = models.CharField(max_length=20)  
    phone = models.TextField()

    def __str__(self):
        return f'({self.pk}) => {self.name}'


if __name__ == '__main__':
    # CRUD operations
    # 생성 Create
    s1 = Student()
    s1.name = '김지우'
    s1.age = 20
    s1.major = '국어국문학'
    s1.phone = '01012341234'
    s1.save()

    s2 = Student(name='홍길동', age=30, major='컴퓨터공학', phone='01056785678')
    s2.save()

    Student.objects.create(name='김우진', age=21, major='경영학과', phone='01012345678')

    # 조회 Read/Retrieve
    # 레코드 전체조회
    Student.objects.all()
    # 레코드 단일조회
    Student.objects.get(id=1)
    # 레코드의 컬럼별 조회
    s1.name
    s1.age
    s1.major

    # 수정 Update => 모든 레코드의 모든 컬럼 수정 가능. id는 수정하면 안된다!
    # 1개의 '특정' 레코드를 선택하여, 원하는 값을 수정하고, 저장한다.
    s2 = Student.objects.get(pk=2)
    s2.major = '경영학'
    s2.save()

    # 삭제 Delete
    # '특정' 레코드를 선택하여, 삭제한다.
    s3 = Student.objects.get(pk=3)
    s3.delete()


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    year = models.CharField(max_length=10)
    quantity = models.IntegerField()

if __name__ == '__main__':

    # 생성 (3가지 중 2, 3번째 방법)
    p1 = Product(name='의자', price=70000, year='2020', quantity=25)
    p1.save() 

    p2 = Product(name='책상', price=100000, year='2021', quantity=12)
    p2.save()

    p3 = Product(name='모니터', price=145000, year='2022', quantity=25)
    p3.save()

    Product.objects.create(name='컴퓨터', price=670000, year='2019', quantity=25)

    Product.objects.create(name='칠판', price=500000, year='2018', quantity=1)

    Product.objects.create(name='프로젝터', price=1200000, year='2021', quantity=1)

    # 조회 (2가지 방법)

    Product.objects.all()

    Product.objects.get(pk=2)

    # 수정 (2가지 방법)

    Product.objects.get(pk=2).name = '신식 책상'

    p2 = Product.objects.get(pk=2)
    p2.name = '신식 책상'
    p2.save()

    # 삭제 (되돌릴 수 있는 방법은 없다! 다시 생성해줘야함. 대신 id값은 달라짐)

    p6 = Product.objects.get(pk=6)
    p6.delete()



    
