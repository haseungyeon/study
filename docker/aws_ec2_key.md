### aws ec2 pem-key 접속 시

1. 보안그룹 tcp 22 port open 설정 해주어야 함.

```pre
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0555 for 'example-1.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "example-1.pem": bad permissions
ec2-user@ec2-52-79-239-191.ap-northeast-2.compute.amazonaws.com: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).
```

2. wsl2에서 sudo를 통해 실행해줘야 함.

**tips**

- ec2에서는 docker와 같은 유틸리티를 보다 편리하게 설치할 수 있는 명령어가 내장되어 있음.

```bash
$ sudo yum update -y
$ sudo amazon-linux-extras install docker
$ sudo service docker start
```