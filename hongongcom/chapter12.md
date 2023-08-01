# 프로세스 동기화

## 1. 동기화란

- 공동의 목적을 위해 함께 실행되는 프로세스와 스레드들이 있고 이렇게 여러 실행의 흐름이 존재할 때 정상적인 동작을 위해 필요한 것이 동기화이다.

    1. 올바른 실행 순서 제어

        ![image](https://github.com/haseungyeon/fastapi/assets/59682268/bdd42506-5e1a-426b-8458-50cbd8bec1ed)

        => 만약 writing이 이루어지지 않은 상태에서 reading을 실행한다면 오류가 발생

    2. 임계 영역에 하나의 프로세스만 접근

        - 계좌 잔액 문제에서의 잔액, 그리고 생산자와 소비자 문제에서 물건의 개수를 **공유 자원**
        - 이러한 자원들에 접근하는 코드 영역을 **임계 구역**
        - 계좌 잔액 문제, 생산자와 소비자 문제 : 동시에 같은 데이터에 접근하여 수정이 일어난다면? 더 나중에 저장된 값을 기준으로 먼저 수정된 작업내역은 덮어씌어져 무시된다.
        
        => database에서의 cud 행위 시, 또 git 사용 시 같은 branch에서 같은 파일을 수정하는 경우를 생각해 봅시다.

    3. 레이스 컨디션

        - 고급 언어에서 한 줄로 표현되는 명령어가 여러 줄의 저급 언어로 변환됨에 따라 문맥 교환 과정에서 동기화가 깨지며 발생할 수 있다.

            ```python
            import threading

            counter = 0

            def increment():
                global counter
                for _ in range(1000000):
                    counter += 1

            def decrement():
                global counter
                for _ in range(1000000):
                    counter -= 1

            if __name__ == "__main__":
                t1 = threading.Thread(target=increment)
                t2 = threading.Thread(target=decrement)

                t1.start()
                t2.start()

                t1.join()
                t2.join()

                print("Counter:", counter)
            ```

            ![image](https://github.com/haseungyeon/fastapi/assets/59682268/f565c556-d9bd-423b-b91a-ed85a5a24dd4)
        - 위의 파이썬 코드에서 counter += 1, counter -= 1은 한 줄로 표현되었지만 저급 언어로 변환되는 과정에서 여러 줄로 나누어 계산된다. 이 과정에서 counter 값에 대한 동기화가 파괴되며 각각 r1과 r2라는 다른 값이 계산된다.

            ![image](https://github.com/haseungyeon/fastapi/assets/59682268/7c0c6a1f-eede-4081-b678-5e0dac8d55a5)

        - 따라서 동기화가 파괴되지 않게 하기 위해 아래 3가지 원칙을 따른다.

            - 한 프로세스만이 임계 구역에 진입(상호 배제)
            - 임계 구역이 비었다면 진입하고자 하는 프로세스가 진입할 수 있어야 함(진행)
            - 임계 구역에 진입하여야 하는 프로세스는 언젠가는 진입할 수 있어야 함(유한 대기)

            ![image](https://github.com/haseungyeon/fastapi/assets/59682268/b9817c67-895f-474e-b40f-e1c552ed51a3)

## 2. 동기화 기법

- 뮤텍스 락

    ![image](https://github.com/haseungyeon/fastapi/assets/59682268/9cc5ade5-1766-4f22-bcfe-3f6e773ea2ac)

    - 자물쇠 역할 : 프로세스들이 공유하는 전역 변수 lock
    - 임계 구역을 잠그는 역할 : acquire 함수
    - 임계 구역의 잠금을 해제하는 역할 : release 함수

    ```python
    import threading

    lock = threading.Lock()

    counter = 0

    def increment():
        global counter
        for _ in range(1000000):
            lock.acquire()
            counter += 1
            lock.release()
    def decrement():
        global counter
        for _ in range(1000000):
            lock.acquire()
            counter -= 1
            lock.release()

    if __name__ == "__main__":
        t1 = threading.Thread(target=increment)
        t2 = threading.Thread(target=decrement)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("Counter:", counter)
    ```
    ![image](https://github.com/haseungyeon/fastapi/assets/59682268/9ec5e1a7-20d6-470f-84a1-8c94c9b7f547)

    ![image](https://github.com/haseungyeon/fastapi/assets/59682268/529e0cff-8349-411b-94c9-2c852e489791)

    ![image](https://github.com/haseungyeon/fastapi/assets/59682268/dbd77ce0-5930-479a-9692-99781d462441)

    => lock 변수를 계속해서 체크하며 대기하는 방식을 **바쁜 대기**라고 하며 python에서는 위와 같이 뮤텍스 락 기능을 제공하고 있다.

- 세마포

    ![image](https://github.com/haseungyeon/fastapi/assets/59682268/e4f2aabe-4e03-4479-8a52-5566890a66ce)

    - 공유자원의 수가 2개 이상일 경우에도 사용 가능하다. (단, 각각의 공유자원에는 하나의 프로세스만 접근 가능함)
    - 단순히 2개 이상의 뮤텍스가 동시에 실행되는 것이라고 보면 된다.
    - 다만, 1개의 공유자원에는 1개의 프로세스만 접근할 수 있다는 원칙에 의거해 공유자원의 수가 곧 동시에 처리가능한 프로세스의 수가 된다.

        ![image](https://github.com/haseungyeon/fastapi/assets/59682268/4e1adec0-afcf-4714-84d7-8294d564afa0)

        ![image](https://github.com/haseungyeon/fastapi/assets/59682268/87e2d4bf-f6b5-42a2-a361-cd5c3ddca193)

    - 위와 같이 바쁜 대기를 통해 계속해서 wait() 함수 내에서 lock이 걸려 있는 상태인지를 확인한다면 그만큼 CPU를 사용하게 되므로 성능이 저하된다.

    - 대기, 준비 상태 큐를 사용하여 반복적인 확인 작업을 생략할 수 있다.

        ![image](https://github.com/haseungyeon/fastapi/assets/59682268/1f3b09d0-745f-4321-82ac-2ee4083983b2)

            => 대기 상태로 전환

        ![image](https://github.com/haseungyeon/fastapi/assets/59682268/bd6bffe5-992b-41f1-9b3b-92946a1edcc0)

            => 준비 상태로 전환

- 모니터

    - 세마포어에서 사용되는 공유 자원이 많아져 복잡해질 경우 wait(), signal()을 혼동하거나 중복사용하는 등의 실수를 해결하기 위해 사용된다.

        ![image](https://github.com/haseungyeon/fastapi/assets/59682268/8a356535-df8f-4a41-bd7d-76dd7e885a69)

    - 쉽게 말해, 세마포어를 사용할 때 발생할 수 있는 실수를 미연에 방지하기 위해 aquire(), wait() 함수와 release(), signal() 함수를 항상 같은 순서로 빠짐없이 실행되도록 만들었다고 이해하면 좋을 것 같다.

        ```python
        import threading

        lock = threading.Lock()

        counter = 0

        def increment():
            global counter
            for _ in range(1000000):
                with lock: # with 구문을 사용함으로써 lock == True일 경우에만 증감에 대한 스레드가 실행되며 연산 종료시 lock이 반환되므로 반드시 release()가 실행되는 효과를 낼 수 있다.
                    counter += 1

        def decrement():
            global counter
            for _ in range(1000000):
                with lock:
                    counter -= 1

        if __name__ == "__main__":
            t1 = threading.Thread(target=increment)
            t2 = threading.Thread(target=decrement)

            t1.start()
            t2.start()

            t1.join()
            t2.join()

            print("Counter:", counter)
        ```
    
    - 모니터는 임계 구역에 진입하기 위한 각각의 프로세스들과 잠시 중단된 프로세스들을 조건 변수로 매기고 이들을 각각 큐로 만들어 준다.

        ```pre
        1. 스레드가 특정 조건을 확인하고 조건이 충족되지 않으면 대기합니다.
        2. 다른 스레드가 특정 조건을 만족시키면 대기 중인 스레드를 깨웁니다.
        3. 깨어난 스레드는 조건이 충족되었으므로 작업을 수행합니다.
        ```