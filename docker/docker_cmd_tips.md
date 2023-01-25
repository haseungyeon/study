### 이미지 관련

- 특정 이미지 태그 삭제
    ```shell
        docker rmi $(docker images 'completeimagename' -a -q)
    ```