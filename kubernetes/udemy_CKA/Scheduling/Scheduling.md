## k8s kube-system namespace 조사해보기

- k8s의 동작과 관련된 pod들이 존재하는 namespace
- KodeKloud 강의에서는 스케줄러가 실행되는지를 kube-system namespace에서 확인했지만 이는 pod 이름으로 확인한 것이며 이전 Core Concepts 파트에서 제공된 lab 환경에는 `scheduler` 라는 단어로 명명된 pod가 없었음에도 pod가 정상적으로 잘 기동되었다.
- stackoverflow에 따르면 아래 명령어로 스케줄러의 상태를 확인 가능하다고 한다.

    ```bash
    kubectl get pods -n kube-system -l component=kube-scheduler
    ```

![Alt text](image.png)

결론 : 

위 명령을 KodeKloud의 Core Concepts 파트의 labs 환경에서 실행해 보았지만 no resource라는 결과만 얻을 뿐이었다. 

스케줄러가 제대로 기동되고 있는지는 강의내용에선 kube-system 네임스페이스 안에 pod 이름이 `scheduler` 인 것이 있는지를 통해 확인했지만 Core Concepts lab 환경에서는 `scheduler` 라는 단어가 포함된 pod

## labels & selector

명령어 팁

    ```bash
    kubectl get po --selector env=prod --no-headers | wc -l
    ```
=> header 제거하여 목록의 수를 반환(wc -l)

## Node selectors
## Node Affinity
## Resource Requirements and Limits

pod 기동 시 resource에 요구량을 작성하여 그만큼의 자원을 할당해줄 수 있는 node를 찾아 배포해주는 기능

    ```yaml
    apiVersion: v1
    kind: pod
    metadata:
      name: simple-webapp-color
      labels:
        name: simple-webapp-color
    spec:
        containers: 
        - name: simple-webapp-color
          image: simple-webapp-color
          ports:
          - containerPort: 8080
          resources:
            requests:
              memory: "1Gi"
              cpu: 1
            limits:
              memory: "2Gi"
              cpu: 2
    ```
    - memory 설정 시 사용가능한 단위 [G, M, K, Gi, Mi, Ki] ~i(~ibibyte)단위는 byte*2^10, 단순 G, M, K의 경우는 byte*10^3
    - requests는 사용량 최소값, limits는 사용량 최대값
    - requests 없이 limits만 설정할 경우 requests는 limits와 동일한 값으로 설정된다
    - limits를 설정하지 않을 경우 하나의 pod가 node 전체의 cpu를 독점해버릴 수 있기 때문에 문제가 발생할 수 있다
    
### LimitRange

default 자원 제한량 정책을  단위로 pod, container 단위로 설정해주는 `LimitRange`라는 오브젝트를 사용할 수 있다.

  ```yaml
  apiVersion: v1
  kind: LimitRange
  metadata:
    name: cpu-resource-constraint
  spec:
    limits:
    - default:
        cpu: 500m
      defaultRequest:
        cpu: 500m
      max:
        cpu: "1"
      min:
        cpu: 100m
      type: Container
  ```
단, 주의할 점은 기존에 생성되어 있는 pod에 적용이 되는것이 아니라 `LimitRange`가 적용된 이후에 기동된 pod의 컨테이너들에 적용된다

### resourceQuota
`LimitRange`가 pod, container 단위로 리소스를 제한한다면 `resourceQouta`는 cluster의 namespace 단위로 리소스 제한량을 설정한다

  ```yaml
  apiVersion: v1
  kind: ResourceQuota
  metadata:
    name: rq-1
    namespace: nm-3
  spec:
    hard:
      requests.memory: 1Gi
      limits.memory: 1Gi
  ```

**만약 ResourceQuota, LimitRange가 동시에 적용되어 있다면 무엇이 우선적용되는지??**
=> resourceQuota는 파드가 아닌 namespace 전체 리소스에 대한 제한, limitRange는 각각의 pod 또는 컨테이너의 리소스에 대한 제한이므로 두 개의 정책은 별도인 것 같다

## DaemonSets
## Static Pods
## Multiple Schedulers
## Configuring Scheduler Profiles