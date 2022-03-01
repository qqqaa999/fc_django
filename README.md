# Django
<패스트캠퍼스 Django 강의>

## 웹 프레임워크에 대한 이해
    
 #####   프레임워크란
 + 자주 사용되는 코드를 체계화화여 쉽게 사용할 수 있도록 도와주는 코드 집합(클래스와 인터페이스의 집합)
 + 라이브러리와 혼동될 수 있지만 좀 더 규모가 크고 프로젝트의 기반이 됨
 + 건축에 비유하면 구조를 만드는 골조가 프레임 워크라면 그 외 자재들이 라이브러리가 됨
 
 #### Web 프레임워크
 + 웹 개발에 필요한 기본적인 구조와 코드(클래스, 함수 등)가 만들어져 있음
    + <웹 프레임워크> URL 파싱, 요청 파싱, 응답 생성, 세션 관리, 데이터베이스 연동, 관리자 페이지
    + <개발 영역> 비즈니스 로직, 데이터 정의

#### Django란
* Python으로 기반으로 만들어진 Web Application Framework 임.
* 장고의 목표 : 데이터베이스 기반 웹 사이트를 작성하는데 있어 수고를 더는 것이 주된 목표임.
* 장점
    * App 단위의 독립적인 구성<분업의 유리>
    * 반복적으로 구현해야 하는 부분이 이미 만들어져 있음 ex) 로그인, 회원가입, 인증 등등
    * 프론트와 관련된 프레임워크(React, Vue, angular)와 같은것을 사용하지 않고도 만들 수 있음
    * 데이터베이스 테이블을 models.py에 클래스로 작성하여 작업량을 줄이며, 한번 작업하면 테이블까지 생성되어 매핑되기 때문에 편하게 작업 가능함
    * 보안 : 장고는 다양한 공격을 방지할 수 있는 기능들이 이미 구현되어 있음
    * Admin을 이용하여 빠르게 요건을 구현한 후 수정해 나갈 수 있음 <https://www.slideshare.net/hannal.cha/django-admin-81652288> 를 참고
* 단점
    * 파이썬의 단점을 그래도 가져옴 <속도가 느림>
    * ORM 기반이기 때문에 원하는 결과가 나오지 않을떄가 있음


#### 라이브러리
 - 라이브러리는 단순 활용가능한 도구들의 집합을 말합니다.    
    즉, 개발자가 만든 클래스에서 호출하여 사용, 클래스들의 나열로 필요한 클래스를 불러서 사용하는 방식
+ 프로그래머가 어떠한 기능을 수행하기 위해 도움을 주는 또는 필요한 것을 제공해주는 역할을 하는 것
+ 라이브러리는 재사용이 필요한 기능으로 반복적인 코드 작성을 없애기 위해 언제든지 필요한 곳에서 호출하여 사용할 수 있도록 Class나 Function으로 만들어짐
+ 프로그램을 만들때 기존에 만들어진 함수들을 재활용함으로써, 프로그램의 제작 시간과 노력을 줄일 수 있음, 필요한 함수만 호출하여 사용할 수 있음
+ 독립성을 가지고, 응용 프로그램이 능동적으로 라이브러리를 사용함

#### 프레임워크 vs  라이브러리
+ 차이점: 제어권의 주도성을 누가 가지고 있느냐에 따라 차이가 있음
+ 프레임워크는 제어권을 스스로 가지며 사용자가 프레임워크에 필요한 코드를 만듬(비즈니스 로직)
+ 라이브러리는 사용자가 제어권을 가지고 있으며 라이브러리를 호출하여 사용함
+ 제어권: 프레임워크<내포> 라이브러리<호출>

#### API(Application Programming Interface)
응용 프로그램을 만드는데 사용된 Interface임
+ Interface란 서로 다른 사물이나 시스템 간에 커뮤니케이션(소통)이 가능하도록 설계한 상호 작용 방식
+ API는 응용 프로그램 간에 서로 호환이 가능하도록 상호 작용하는 방법을 정해 놓은 것
    + 직관적으로 말하면 API는 응용 프로그램 간에 데이터를 주고받는 방법

#### Class와 Object<객체>
- Class는 똑같은 무엇가를 계속해서 만들수 있는 설계, 틀과 같음 ex) 자동차 공장, 붕어빵 틀 등등
Object는 Class에 의해서 만들어진 물건, 실체를 말함 ex) 자동차, 붕어빵 등등

특징
* Class로 만들어진 Object는 Object별 독립적인 성격을 가짐 ex) 한 Object가 망가져도 다른 Object는 영향을 받지 않음
* Instance : Class에 의해서 만들어진 Object를 인스턴스라고도 함
    * 인스턴스는 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용
    * 클래스와 구체적인 객체 사이의 관꼐에 초점을 맞추면 인스턴스라는 용어를 사용함

#### 함수(Funtion)
* 함수는 특정 작업을 수행하는 ***코드 조각***임, 전역, 지역이던 ***독립된 기능***을 수행하는 단위임

#### 메서드(method)
* 메서드는 클래스, 구조체, 열거형에 포함되어있는 함수를 메소드라고 함, 쉽게 클래스 안에 있는 즉 클래스 함수를 메소드라고 함

#### 오버라이딩(overriding)
* 오버라이딩(overriding)이란 상속 관계에 있는 부모 클래스에서 이미 정의된 메소드를 자식 클래스에서 같은 시그니쳐를 갖는 메소드로 다시 정의하는 것이라고 할 수 있음.

    * overriding은 무시하다, 우선하다라는 뜻을 가지고 있는데 그 말 그대로 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다는 뜻임.

```python
class Dog:
    def dog_breed(self):
        print('개')
 
class Jindo_dog(Dog):
    def dog_breed(self):
        print('진돗개')
 
dog_1 = Jindo_dog()
dog_1.dog_breed()

```

## 디자인 패턴

#### MVC패턴
* MVC는 Model-View-Controller의 약자이며 디자인 패턴중의 하나임
* Model, View, Controller 세 가지로 역할에 따라 구분한느 패턴임
<디자인 패턴이란 효율적으로 코드를 작성하기 위한 코딩 규칙 or 프로젝트 구조>
*   * Model : 데이터 보유 및 처리 로직 (DB 관련)
    * View : 유저와 어플리케이션 간의 인터페이스 (화면 요청에 대한 결과물을 보여줌)
    * Controller : 모델과 뷰를 이어주는 역할 (유저의 입력과 요청에 관찬 처리를 Model에 의뢰함)
    ![MVC_이미지](https://blog.kakaocdn.net/dn/dIShYR/btq6cTveSuR/a4SOarsnoUf7JqF4adMzW0/tfile.svg)
#### MVC패턴의 특징
* 장점 : MVC패턴은 각각의 구성 요소가 분리되어 본연의 역할에만 충실한 구조임 그래서 유연성이 높고 유지보수가 용이하며 개발자와 디자이너 작업 영역을 분리할 수 있음
* 단점 : 프로젝트 규모가 클수록 컨트롤러가 비대화 되고 모델과 뷰의 의존성을 완벽히 분리 할 수 없기에 유지보수가 점점 어려워짐 이를 보안한 디자인 패턴 (MVP, MVVM 등등)

#### MTV패턴
* Django는 MVC(Model-View_Controller)를 기반으로 한 프레임워크임, MVC패턴을 Django에서는 MTV(Model-Template-View)패턴이라고 부르기도함 <Spring에서는 MVC로 부름>
*   Django에서는 MTV에 URL을 추가함 
*   1. User가 URL로 요청을 보냄
*   2. URLConf를 통해 URL과 매핑된 View를 호출
*   3. View는 요청에 따라 적절한 로직을 수행하며 이 과정에서 Model에 CRUD를 지시함
*   4. Model은 ORM을 통해 DB와 소통하며 CRUD를 수행함
*   5. View는 지정된 Template를 랜더링 함
*   6. User에게 응답함

    ![MTV_이미지](https://1.bp.blogspot.com/-upCjCNPicRc/XjfZTiPxLNI/AAAAAAAACkQ/lXvlwoCQQPk43nEkNL1WSSq9gQgltMe2wCLcBGAsYHQ/s1600/2.png)

## ORM(Object Relational Mapping)
* 장고에서 ORM이란 무엇인가? ORM의 장정과 단점은 무엇인가? 예시는 무엇인가?
* ORM이란 : Object-Relational-Mapping의 약자로 객체와 관계형 데이터베이스의 데이터를 매핑해주는 것을 의미함.
    * 객체지향 프로그래밍(OOP)은 Class 사용 관계형 데이터베이스(RDBMS)에서는 테이블을 사용함.
    * 객체지향 프로그래밍은 필드와 메서드등을 묶어서 캡슐화하고 ***사용하는것이*** 목표, 관계형 데이터베이스에서는 데이터를 잘 정규화해서 ***보관하는것이*** 목표
* 기능 : 객체간의 관계를 바탕으로 SQL을 자동 생성하여 SQL 퀴리문 없이도 데이터베이스의 데이터를 사용가능하게 함.
    ![ORM_이미지](https://yunsikus.github.io/assets/img/post_img/django_orm1.jpg)

* 장점
    * SQL query가 아닌 직관적인 코드로 데이터를 조작할 수 있어 개발자가 객체 모델로 프로그래밍 하는데 집중 할 수 있음
    * 각 객체에 대한 코드를 별도로 작성하기 때문에 코드 가독성이 좋음(선언문, 할당, 종료 같은 부수적인 코드가 줄어듬)
    * SQL의 절차적이고 순차적인 접근이 아닌 객체지향적인 접근으로 생산성이 좋음
    * 재사용 및 유지보수가 용이하고 매핑정보가 명확하며 ERD 의존성이 낮음
    * DBMS(DataBase Management System) 종속성이 낮음

* 단점
    * 완벽한 ORM만으로는 서비스 구현이 어려움, 사용하기는 편하나 설계는 신중히 해야함.
    * 프로젝트 복잡성이 커질 경우 난이도가 높아짐.
    * 잘못 구현하게 되면 속도가 저하되고 일관성이 없어질 수 있음

* 예시 : 회원에 나이정보를 추가하려고 함
    * ORM : Member 클래스에 age를 추가
    *  Without ORM : Insert, Select, Update등 관련된 모든 퀴리에 age 정보를 추가

* 쿼리셋이란
    * ***전달받은 모델의 객체 목록(핵심)***
    * 데이터베이스로부터 데이터를 읽고 필터를 걸거나 정렬등을 할 수 있음
    * 리스트와 구조는 같지만 파이썬 기본 자료구조가 아니기에 읽고 쓰기 위해서는 자료형 변환을 해줘야함. 퀴리셋은 데이터베이스의 여러 레코드(row)를 나타냄

참고 : <https://yunsikus.github.io/development/django/2021/05/19/Django_ORM/>

## DB CRUD
* CRUD는 대부분의 ***컴퓨터 소프트웨어***가 가지는 기본적인 데이터 처리 기능인 Create(생성), Read(읽기), Update(갱신), Delete(삭제)룰 묶어서 일컽는 말임.
* ***사용자 인터페이스***가 갖추어야 할 기능(정보의 참조/검색/갱신)을 가리키는 용어로서도 사용됨.

*   이름 | SQL | 사용자 인터페이스 EX
    * C : Create (생성) | INSERT | 커뮤니티 또는 게시판의 글 쓰기
    * R : Read   (읽기) | SELECT | 커뮤니티 또는 게시판의 글 읽기
    * U : Update (갱신) | UPDATE | 커뮤니티 또는 게시판의 글 편집
    * D : Delete (삭제) | DELETE | 커뮤니티 또는 게시판의 글 삭제

## CDN(Content Delivery Network)

* CDN이란 지리적으로 분산된 여러 개의 서버 이며, 지리적 제약 없이 전 세계 사용자들에게 빠르게 콘텐츠를 전송하는 기술임.
    ![CDN_이미지](https://wp-assets.highcharts.com/www-highcharts-com/blog/wp-content/uploads/2012/11/05143244/how-cdn-works.png)
    * CDN을 마치 ATM처럼 생각하면 이해하기 쉬움
* 원리 : 프록시 서버에서 출발한 웹 캐시의 클라우드화임, 전세계 각지에 캐시 서버를 엄청 많이 설치하고 사용자가 접속하면 가장 가까이 있는 캐시 서버가 정보를 보냄 
    * 캐시(Cache)란 : 데이터나 값을 미리 복사해 놓는 임시 장소를 말하며, 캐시는 저장 공간이 작고 비용이 비싼 대신 빠른 성능을 제공함. 
    * 프록시(Proxy)란 : 서버와 클라이언트 사이에서 대리로 통신을 수행해주 것을 프록시라고 함.
    * 프록시 서버(Proxy Server)란 : 클라이언트가 자신을 거쳐 다른 네트워크에 접속할 수 있도록 ***중간에서 대리해주는 서버***를 말함.
    * 프록시 서버 사용 목적
        1. 캐시 데이터 사용하기 위함 [캐시 저장 -> 외부 트래픽 줄임 -> 네트워크 병목 현상 방지]
        2. 보안 목적 [IP 숨기기, 방화벽]
        3. 접속 우회
    * 클라우드란 : 인터넷을 통해 액세스할 수 있는 서버와 이러한 서버에서 작동하는 소프트웨어와 데이터베이스를 의미함. 즉, 웹(Web)상의 중앙컴퓨터에서 받은 동일한 파일을 받을 수 있는 곳.
* 장점
    1. 병목 현상 해결
        1. 자주 사용되는 파일의 병목현상을 해결할 수 있음
        2. 데이터를 항상 빠르고 안정적으로 전송할 수 있음
        3. ISP에 장애가 발생해도 다른 ISP에 있는 캐시 서버에서 데이터를 전송하므로 전송 중단이 발생하지 않지만, 이렇게 되려면 여러 국가에 분산된 다수의 캐시 서버가 필요함.
    2. 트래픽 절약
        1. CDN을 쓰면 트래픽이 줄어들기 때문에 서버 유지 비용도 저절로 감소됨 원리는 caching과 비슷하며 자주 쓰이는 파일들을 중간중간에 replica로 만들어 놓아서 클라이언트가 replica에 접근할 수 있게 함

## Database 분석과 설계
* Table이란 : 행과 열로 구성된 표 형태로 된 데이터를 의미함.
* Field란 : ***세로 방향으로 표시된 열, column을 말함.*** 필드는 DB Table에서 가로로 표시한 레코드(Record)에 대한 개별적인 속성값을 표시함.
* Record란 : ***가로 방향으로 표시된 행, row을 말함.***
* 키(Key)란 : 테이블의 각 레코드를 구분할 수 있는 값임.
* 기본키(Primary Key)이란 : 각 행을 구분하는 ***유일한 열을 정의할 때 사용되는 됨***
* 외래키(Foreing Key)이란 : 한 테이블의 필드(attribute)중 다른 테이블의 행(row)을 식별할 수 있는 키를 말함.

#### 일대일 관계(One-to-One)
* 일대일 관계는 첫번쨰 테이블의 단일 레코드가 두번쨰 테이블의 하나의 레코드와 관련이 되어있으며, 두번쨰 테이블의 단일 레코드가 첫번째 테이블의 레코드 하나와만 관련이 있을 경우 사용됨. 
    * EX) 1번 테이블에 고객의 신체정보 2번 테이블에 고객의 재무정보 3번 테이블에 고객의 취미정보를 저장하면 고객 번호에 대한 일대일 관계가 형성 됨.
    * 내가 만든 EX) 수능을 예시로 생각 했을 때 1번 테이블에 학생 정보(학생 ID, 이름, 나이, 성별, 주소, 학교, 학번) 2번 테이블에 학생 성적(학생 ID, 국어 성적, 수학 성적, 영어 성적 등등) 이라면 1번 테이블의 단일 레코드인 학생 ID가 두번째 테이블의 학생 ID와 연관 되어 있으니 일대일 관계라고 생각함.
    * 방대한 자료를 다루는 기업에서 필요에 따라 사용되는 기능

#### 일대다 관계(One-to-Many)
* 하나의 레코드가 서로 다른 여러 개의 레코드와 연결된 경우
    * 내가 만든 EX) 견주와 강아지 같은 경우를 생각 했을 때 1번 테이블에 견주 정보(ID, 이름, 전화번호, 주소) 2번 테이블에 (견주 ID, 강아지 이름, 품종, 나이 등등)
        * 이 구조에서는 한 명의 견주가 여러 강아지를 가질 수 있음, 여러명의 견주가 한 강아지를 가질 수 없음
    * 관계형 데이터베이스에서 가장 많이  사용함.

#### 다대다(M:N)관계(ManyToMany)
* 두 개의 테이블이 서로의 레코드(Record)에 대해서 여러개로 연관 되어 있는 상태를 다대다(M:N)관계라고 함.
* 단점
    * 데이터의 무결성을 위반하게 되며, 데이터의 삭제와 추가, 수정을 할 때 많은 문제가 발생함. 하지만 DB 설계를 제대로 한다면 편할것 같음

#### Entity(엔티티)
* Entity란
    1. 데이터의 집합임.
    2. 저장되고, 관리되어야하는 데이터임.
    3. 개념, 장소, 사건 등을 가리킨다.
    4. 유형 또는 무형의 대상을 가리킴.
* Entity특징
    * 식별자, 인스턴스 집합, 속성, 관계, 업무
    1. 유일한 식별자를 가져야함.
    2. 2개 이상의 인스턴스가 있어야 함
    3. 반드시 속성을 가지고 있어야 함
    4. 다른 엔티티와 최소 한 개 이상 관계가 있어야 함
    5. 업무에서 괸리되어야 하는 집합임
* Entity의 종류
    * Entity는 유형과 무형에 따른 종류, 발생 시점에 따른 종류로 나뉘어짐
        * 유형과 무형에 따른 종류
            * 유형 엔티티 : 지속적으로 사용되는 엔티티(직원,사장 등)
            * 개념 엔티티 : 물리적 형태가 없는 엔티티, 개념적으로 사용되는 엔티티(보험상품, 조직 등)
            * 사건 엔티티 : 비즈니스 프로세를 실행하면서 생성되는 엔티티(주문, 결제 등)
        * 발생 시점에 따른 종류
            * 기본 엔티티 : 키 엔티티라고도 함, 다른 엔티티에 영향을 받지 않는 독립적으로 생성되는 엔티티(상품, 고객)
            * 중심 엔티티 : 기본 엔티티와 행위 엔티티 중간에 있는 것, 기본 엔티티로부터 발생되고 행위 엔티티를 생섬함(주문, 취소, 결제 등)
            * 행위 엔티티 : 2개 이상의 엔티티로부터 발생 됨(주문 내용, 취소 내용 등)
* ERD란?
    * Entity Relationship Diagram (ERD)는 시스템의 엔티티들이 무엇이 있는지 어떤 관계가 있는지를 나타내는 다이어그램임.
    * 구체적으로
        1. 데이터 모델은 데이터베이스에 독립적임
        2. 데이터 모델링은 건축물의 설계도를 그리는 작업과 같음
        3. 관계형 데이터 모델은 여러 가지 데이터 모델 중 가정 널리 사용되는 모델이며, 실체(Entity), 속성(Attribute), 관계(Relationship)로 구성된 ER diageram으로 표현 됨
        4. Entity는 하나 이상의 식별자(UIDL Unique ldentifier)를 가져야 하며, UID가 없다면 Entity가 아님
        5. ER diagram 작성 시, 관계를 표현할 때에는 어떤 entity가 "주"인가를 잘 따져서 표현해야함

## Decorator
* 함수를 Wrapping 즉, 어떤 함수를 받아 명령을 추가한 뒤 이를 다시 함수의 형태로 반환하는 함수(말 그대로 다른 함수를 꾸며주는 함수임)

``` python
@login_required
def test_func1():
    print('Do something1')

@login_required
def test_func2():
    print('Do something2')

def login_required(func): '''데코레이터'''
    def wrap():
        if user in None:
            return redirect('/login')
        return func()
    return wrap
''' 이런식으로 작성 함
    login_required을 보면 함수를 인자로 받고 wrap안에 있는 기능을 실행함
    함수를 데코레이터에게 전달해주므로써 사실은 login_required 함수를 호출하는것
 '''
 ```

 ## REST 및 REST API
 #### REST
 * REST 정의
    * Representational State Transfer의 약자이며, 자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든것을 의미함
        * 즉, 자원(resource)의 표현(representation)에 의한 상태 전달
            1. 자원 : 해당 소프트웨어가 관리하는 모든것(문서,이미지,데이터,해당 소프트웨어 자체 등), 
            2. 표현 : 자원을 표현하기 위한 이름(DB의 사용자 정보가 자원일 때, user를 자원의 표현으로 정함)
        * 상태(정보)전달
            1. 데이터 요청이 되는 시점에서 자원의 상태(정보)를 전달함
            2. JSON 혹은 XML를 통해 데이터를 주고 받는 것이 일반적
    * HTTP URI(Uniform Resource Identifier)를 통해 자원(Resource)을 명시하고 HTTP Method(POST, GET, PUT, DELETE)를 통해 해당 자원(URI)에 대한 CRUD Operation을 적용하는 것을 의미함
        * CRUD 동작 예시
            + Create : 데이터 생성(POST)
            + Read : 데이터 조회(GET)
            + Update : 데이터 수정(PUT)
            + Delete : 데이터 삭제(DELETE)
            + HEAD : 네트워크상 데이터의 header 정보 조회(HEAD)

* REST 구성 요소
    1. 자원(Resource) : HTTP URI
    2. 자원에 대한 행위(Verb) : HTTP Method
    3. 자원에 대한 행위의 내용(Representations) : HTTP Message Pay Load

* REST 특징
    1. Server-Client(서버-클라이언트 구조) : 서버는 API 제공, 클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보) 등을 직접 관리하는 구조이므로, 역할이 확실히 구분되고 서버와 클라이언트에서의 개발 내용이 명확해지며, 서로 간 의존성이 줄어들게 됨
    2. Stateless(무상태) : 작업을 위한 상태정보(세션,쿠키)를 따로 저장하고 관리하지 않음
    3. Cacheable(캐시 처리 가능) :  웹에서 사용하는 기존 인프라를 그대로 활용 가능, HTTP가 가진 캐싱 기능을 적용할 수 있음
    4. Layered System(계층화) : REST 서버는 다중 계층으로 구성 가능하므로 보안, 로드 밸런싱, 암호화 계층을 추가하여 구조상의 유연성을 둘 수 있으며 PROXY, 게이트웨이 같은 네트워크 기반의 중간매체를 사용할 수 있음
    5. Uniform Interface(인터페이스 일관성) : 특정 플랫폼(안드로이드, IOS 등), 특정 언어나 기술에 종속되지 않고 모든 플랫폼에서 사용가능, URI로 지정한 리소스에 대한 조작이 가능한 아키텍쳐 스타일을 의미함
    6. self-descriptiveness(자체 표현 구조) : REST API 메세지만 보고도 쉽게 이해할 수 있는 자체 표현 구조로 되어있음

* REST 장단점
    * 장점
        1. HTTP 프로토콜의 인프라를 그래도 사용하므로 REST API 사용을 위한 별도의 인프라를 구축할 필요가 없음
        2. HTTP 프로토콜의 표준을 최대한 활용하여 여러 추가적인 장점을 함께 가져갈 수 있게 해줌
        3. HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용가능
        4. Hypermedia API의 기본을 충실히 지키면서 범용성을 보장함
        5. REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있음
        6. 여러 가지 서비스 디자인에서 생길 수 있는 문제를 최소화함
        7. 서버와 클라이언트의 역할을 명확하게 분리함
    * 단점
        1. 표준이 자체가 존재하지 않아 정의가 필요함
        2. 사용할 수 있는 메소드가 4가지밖에 없음(CRUD)
        3. HTTP Method 형태가 제한적임
        4. 브라우저를 통해 테스트할 일이 많은 서비스라면 쉽게 고칠 수 있는 URL보다 Header 정보의 값을 처리해야 하므로 전문성이 요구됨
        5. 구형 브라우저에서 호환이 되지 않아 지원해주지 못하는 동작이 많음 ex)익스폴로어

#### REST API

References <https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html>

## DRF

* form은 form 자체를 관리할 코드만 작성 form이 정상적으로 채워졌을 때  view 안에서 form_valid 함수를 이용해서 데이터 저장
* 정리할것 : 오버라이딩, clean함수, form_valid, form_invalid, django field종류, djnago orm 작성법, djnago view import 종류

* (form단)clean함수

* (view단)form_valid함수, form_invalid함수, djnago view import 종류, get_form_kwargs, get_queryset

* (model단)django field종류, djnago orm 작성법, Meta함수
## Djnago Routing
* 접속한 주소에 따라서 적절한 처리 로직을 연결해주는 작업을 라우팅이라고 함.
* 라우팅을 해주는 도구를 라우터라고 부름. (Django의 라우터는 urls.py임)
* 장고는 크게 Project 단위와 Application 단위가 존재하며, 하나의 장고 Project는 여러 Application을 가질 수 있는데 이것은 곧 Project 단위의 Routing 관리와 Application 관리가 존재한다는 것을 의미함 그리고 장고는 들어오는 URL 경로를 View로 라우팅하여 요청을 처리함.

## Django Form 정리
* Django Form의 기능 : 폼을 통해서 값을 수정 / 검사를 하며, HTML 코드로 랜더링 할 수 있음.

* class Meta : python의 메타 클래스와는 다른 개념이며, django form의 class Meta는 단순히 이름이 Meta인 내부 클래스(inner class)임. Meta class는 ModelForm class에 메타데이터를 제공하기 위해 사용됨. 
    * Meta 데이터란 : 메타 데이터는 다른 데이터에 대한 정보를 제공하는 특정 데이터 집합을 나타냄. ex) file이라는데이터가 있다면, 그 file의 '작성자가 누구고, 언제, 어디서 작성이 되었는가' == Meta data

```python
from django.db import models

class MyModel(models.Model):
    pass
    class Meta:
        pass
```

* 메타 옵션
    * db_table : 이 옵션은 데이터베이스 내에서 테이블을 식별하는데 사용해야하는 이름을 설정하는데 사용됨.
    * ordering : 이 옵션은 모델 필드 인 문자열 값 목록을 사용함. 모델 객체의 순서를 정의하는데 사용됨.
    * verbose_name : 이 옵션은 사람이 읽을 수 있는 모델의 단일 이름을 정의하는데 사용되며, Django의 기본 명명 규칙을 덮어씀, admin에도 반영이 됨.
    * verbose_name_plural : 이 옵션은 모델에 대해 사람이 읽을 수 있는 복수형 이름을 정의하는데 사용되며, Django의 기본 명명 규칙을 덮어씀, admin에도 반영이 됨.
    * Djnago document <https://docs.djangoproject.com/en/3.2/ref/models/options/> 여기서 더 다양한 option을 확인해보자