# VSCode에서 SSH을 이용해 AWS EC2 접속하는 법
* 인스턴스의 퍼블릭 IP주소가 필요함
 - xx.xxx.xxx.xx
* .pem 파일이 필요함(인스턴스 생성할 때 같이 만듬) 
- ssh 설정 파일에 아래처럼 입력
```
    Host xx.xxx.xxx.xx
    HostName xx.xxx.xxx.xx
    IdentityFile C:\Users\Administrator\.ssh\awspwd.pem (.pem의 경로)
    User ubuntu
```