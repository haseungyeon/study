# CPU의 작동 원리

## 1. ALU와 제어장치

- ALU

    ![image](https://user-images.githubusercontent.com/59682268/232853881-5485ab3c-b640-4735-b7fb-c3734ba813c4.png)

    - 입력값 : 피연산자, 제어신호
    - 출력값 : 데이터 또는 메모리 주소, 플래그

    => 피연산자와 제어신호를 입력받아 계산을 수행한 후 결과값으로 데이터 또는 메모리 주소로 플래그와 함께 레지스터에 저장한다

    **플래그의 역할**

    ![image](https://user-images.githubusercontent.com/59682268/232856507-aac5617d-c826-4585-9daa-7e94a2eada82.png)

- 제어장치

    ![image](https://user-images.githubusercontent.com/59682268/232857494-718fa7f6-bdb1-4c75-b92b-19e1ee053fe0.png)

    - 제어신호를 ALU에 보내 연산(명령)을 지시하고 처리된 결과를 다시 제어신호를 통해 입출력 장치로 전송한다
    - 클럭 신호를 받아들임. 클럭 신호란, 쉽게 말해 컴퓨터 내부에서 기준으로 사용하는 가장 작은 단위 시간. 모든 작업의 수행 시간은 자연수 N으로 1클럭 X N 클럭으로 표현할 수 있다

    - 입력값 : 클럭 신호, 명령어, 플래그, 입출력 장치 또는 외부장치를 통한 제어신호
    - 출력값 : CPU 내부 제어신호(레지스터, ALU), CPU 외부 제어신호(메모리, 입출력 장치)

## 2. 레지스터

- 주요 레지스터

    - 프로그램 카운터 : 읽어들일 명령어의 주소를 저장
    - 명령어 레지스터 : 명령어를 저장
    - 메모리 주소 레지스터 : 메모리의 주소를 저장
    - 메모리 버퍼 레지스터 : 메모리와 주고받을 값(데이터, 명령어)을 저장

        ![image](https://user-images.githubusercontent.com/59682268/232865409-466c5cb5-a8e2-4436-80a8-bb2e6acd911e.png)

        ![image](https://user-images.githubusercontent.com/59682268/232865509-9005a4c8-4be8-426e-adc3-2661aae38f2f.png)

        ![image](https://user-images.githubusercontent.com/59682268/232865598-af832fd5-672d-4c17-8a79-1b9a97960cbf.png)
        
        ![image](https://user-images.githubusercontent.com/59682268/232865683-7c0493eb-fc5e-463a-b926-11468607d566.png)

        ![image](https://user-images.githubusercontent.com/59682268/232865767-c36ba97c-b4b7-49da-997b-e1f8d213ab02.png)

        ![image](https://user-images.githubusercontent.com/59682268/232865861-58967999-6057-4c73-84c9-f059136529b8.png)

        ![image](https://user-images.githubusercontent.com/59682268/232865930-667c9edb-b04f-4d2f-8ab9-79c6532b6f29.png)

    - 플래그 레지스터 : 플래그 값(연산 결과의 부가 정보)을 저장
    - 범용 레지스터 : 데이터와 주소를 모두 저장할 수 있는 레지스터
    - 스택 포인터 : '스택 주소 지정 방식'으로 메모리 주소를 결정할 경우, 스택 공간에 채워진 마지막 주소값을 저장

        ![image](https://user-images.githubusercontent.com/59682268/232866498-927fb492-0c27-4850-9565-0c76a2461ba9.png)

    - 베이스 레지스터 : '베이스 레지스터 주소 지정 방식'으로 메모리 주소를 결정할 경우, 기준 주소값을 저장

        ![image](https://user-images.githubusercontent.com/59682268/232867100-6156dd72-3678-43c9-a687-bb6c83222aec.png)

- 주소 지정 방식

    - 상대 주소 지정 방식 : 프로그램 카운트와 오퍼랜드 값을 더하여 주소를 결정

        ![image](https://user-images.githubusercontent.com/59682268/232867944-cc41f151-6fe9-4053-83e6-e03503b4bda2.png)

    - 베이스 레지스터 주소 지정 방식 : 베이스 레지스터의 값과 오퍼랜드 값을 더하여 주소를 결정

## 3. 명령어 사이클과 인터럽트

- 명령어 사이클 

    1. CPU에서 메모리로부터 데이터와 명령어 **인출** 해온다
    2. CPU에서 명령어를 **실행** 한다

        ![image](https://user-images.githubusercontent.com/59682268/232870319-f4ccc2e0-30e9-4802-93b5-4fa7c241df13.png)

    3. 간접 주소 방식을 사용할 경우 메모리에 접근하여 데이터를 인출 해온다
    
        ![image](https://user-images.githubusercontent.com/59682268/232870842-3e4cf481-de6c-4374-a8b5-28afaaaf4166.png)

    4. 인터럽트가 포함된 명령어 사이클

        ![image](https://user-images.githubusercontent.com/59682268/232879349-5410bd08-66a9-4775-9363-f26f7bd951dd.png)

- 인터럽트

    - CPU가 하던 작업을 멈추게 하고 다른 작업이 개입되는 상황

    - 인터럽트의 예

        ![image](https://user-images.githubusercontent.com/59682268/232871178-7fc1dcd6-78df-4815-a0b1-5a1ba69506a0.png)

    - 인터럽트의 종류

        - 동기 인터럽트 : CPU가 명령어를 수행하는 도중 예상치 못한 상황에서 발생함. 예외라고도 한다

            예외의 종류

             - 폴트 : 예외 처리 후 **예외가 발생된** 명령어부터 실행을 재개. 보조기억장치로부터 메모리에 데이터를 올리기 위해 발생
             - 트랩 : 예외 처리 후 **예외가 발생된 다음** 명령어부터 실행을 재개. ex) 디버깅 중단점
             - 중단 : 심각한 오류로 인한 CPU의 강제적 중단. ex) 메모리 초과
             - 소프트웨어 인터럽트 : 시스템 호출에 의한 예외

        - 비동기 인터럽트 : 주로 입출력 장치에 의해 발생하는 인터럽트. 키보드, 마우스 인터럽트
        비동기 인터럽트가 필요한 이유는 CPU와 CPU를 제외한 기타 장치(입출력 및 보조기억장치, 메모리)를 분리시킴으로써 CPU는 CPU 본연의 작업에 집중할 수 있도록 하기 위함

        - 비동기(하드웨어) 인터럽트의 처리 순서

        1. 입출력 장치가 CPU로 인터럽트 신호 전송
        2. CPU의 명령어 사이클을 끝낸 후(명령어 실행 후) 인터럽트 발생 확인
        3. 인터럽트가 발생한 경우 인터럽트 플래그를 통해 실행여부 결정
        4. 인터럽트 실행결정 시 실행 중이던 작업을 백업. 스택 메모리에 저장
        5. 인터럽트 벡터를 참조하여 인터럽트 서비스 루틴 실행
        6. 4번에서 백업된 작업 재개

        **인터럽트 벡터** : 실행될 인터럽트 서비스 루틴의 주소가 저장됨