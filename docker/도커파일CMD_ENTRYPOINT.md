### CMD와 ENTRYPOINT 커맨드 작성 시 주의사항

- CMD 명령어만 사용할 경우

    ```dockerfile
    FROM ubuntu:20.04

    CMD ["echo", "CMD test"]
    ```

    ![image](https://user-images.githubusercontent.com/59682268/212460397-d38f47e7-c568-4786-b6b8-600aba339627.png)

- ENTRYPOINT만 사용할 경우

    ```dockerfile
    FROM ubunut:20.04

    ENTRYPOINT [ "echo", "ENTRYPOINT test" ]
    ```
    ![image](https://user-images.githubusercontent.com/59682268/212460459-c929fc9e-0766-4e95-99a4-97d9272c658a.png)

=> docker run을 통해 컨테이너를 생성 시 추가 명령어를 입력하지 않으면 CMD와 ENTRYPOINT는 같은 동작을 하지만,
추가 명령을 주게 될 경우 CMD는 작성된 명령어 대신 docker run 뒤에 붙게 되는 명령어로 대체된다. 반면 ENTRYPOINT는 반드시 ENTRYPOINT에 작성된 명령어를 실행하게 된다.

- CMD만 작성된 파일에서 docker run [추가 명령] 실행

    ![image](https://user-images.githubusercontent.com/59682268/212460627-4106a7f8-c07f-4b67-80e6-6aafcfa5803f.png)

- ENTRYPOINT만 작성된 파일에서 docker run [추가 명령] 실행

    ![image](https://user-images.githubusercontent.com/59682268/212460709-8b4a1c61-15ce-4383-9f2d-9f43ceba60ac.png)

=> 위의 결과를 통해 알 수 있듯이 CMD 파일을 통해 생성된 이미지에선 run 옵션 뒤의 명령어로 대체된 반면, ENTRYPOINT의 경우 작성된 명령어가 사라지지 않고 첫 번째로 실행된 뒤 run 옵션 뒤에 작성된 명령어는 단순히 문자열 출력으로 이어졌음을 알 수 있다.(echo hello라면 hello만 출력되어야 하지만 echo hello 전체가 출력됨.)

- ENTRYPOINT와 CMD가 같이 사용된 경우
    ```dockerfile
    FROM ubuntu:20.04

    CMD ["echo", "cmd test"]

    ENTRYPOINT [ "echo", "entry test" ]
    ```
    - docker run 기본 실행
    
        ![image](https://user-images.githubusercontent.com/59682268/212460984-4e753364-f387-4829-b5ee-24122d58dcc4.png)
    - docker run 추가 명령어 실행
    
        ![image](https://user-images.githubusercontent.com/59682268/212460937-02739cd5-f914-4ca2-88d9-0d1a9d9e28c5.png)
    
=> 위의 실행 결과에서 알 수 있듯이 ENTRYPOINT와 CMD가 같이 사용되면 ENTRYPOINT를 쉘 명령어로 인식하고 CMD에 작성된 명령은 일반 문자열로 인식해버린다. (Dockerfile의 CMD와 ENTRYPOINT 위치를 바꿔서 생성된 이미지로도 동일한 결과)