### 이미지 관련

- [특정 이미지 태그 삭제](https://velog.io/@soonbee/docker-image%EB%A5%BC-%EC%82%AD%EC%A0%9C%ED%95%98%EB%8A%94-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%B0%A9%EB%B2%95%EB%93%A4)
    ```shell
        docker rmi -f $(docker images --filter 'reference=pattern*'-q)
    ```

- wsl 환경 볼륨 옵션 복붙용
    ```shell
        docker run --name feedback-app --rm -d -p 3000:80 -v feedback:/app/feedback -v /mnt/c/Users/user/Desktop/git/docker-udemy/data-volumes-01-starting-setup/:/app -v /app/node_modules feed:env
    ```