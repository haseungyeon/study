## Configure Environment Variables in Applications

- Pod에 적용 방식

  ```yaml
  # plain value 사용
  apiVersion: v1
  kind: Pod
  metadata: 
    name: simple-webapp-color
  spec:
    containers:
    - name: simple-webapp-color
      image: simple-webapp-color
      ports:
        - containerPort: 8080
      env:
        - name: APP_COLOR
          value: pink
  ```
  ```yaml
  # configmap의 특정 env만 사용
  apiVersion: v1
  kind: Pod
  metadata: 
    name: simple-webapp-color
  spec:
    containers:
    - name: simple-webapp-color
      image: simple-webapp-color
      ports:
        - containerPort: 8080
      env:
        - name: APP_COLOR
          valueFrom: 
            configMapKeyRef:
              name: webapp-config-map
              key: APP_COLOR
  ```
  ```yaml
  # secretKey 사용
  apiVersion: v1
  kind: Pod
  metadata: 
    name: simple-webapp-color
  spec:
    containers:
    - name: simple-webapp-color
      image: simple-webapp-color
      ports:
        - containerPort: 8080
      env:
        - name: APP_COLOR
          valueFrom: 
            secretKeyRef:
              name: app-secret
              key: DB_Password
  ```

### configmap

- imperative 방식
  ```bash
  # 직접 선언
  kubectl create configmap <config-name> --from-literal=<key>=<value>
  ```
  ```bash
  # 파일 이용하여 key, value 생성
  kubectl create configmap <config-name> --from-file=<path-to-file>
  ```
  **참고**
  configmap의 alias는 `cm`

- declarative 방식

  ```yaml
  apiVersion: v1
  kind: ConfigMap
  metadata:
      name: app-config
  data:
    APP_COLOR: blue
    APP_MODE: prod
  ```

- pod에서 configMap 사용

  ```yaml
  # configMap 사용
  apiVersion: v1
  kind: Pod
  metadata: 
    name: simple-webapp-color
  spec:
    containers:
    - name: simple-webapp-color
      image: simple-webapp-color
      ports:
        - containerPort: 8080
      envFrom:
        - configMapRef:
            name: app-config
  ```
### secret

  - imperative 방식
  ```bash
  # 직접 선언
  kubectl create secret generic <secret-name> --from-literal=<key>=<value>
  ```
  ```bash
  # 파일 이용하여 key, value 생성
  kubectl create secret generic <secret-name> --from-file=<path-to-file>
  ```
  **참고**
  configmap의 alias는 `cm`

  - declarative 방식

  ```yaml
  apiVersion: v1
  kind: Secret
  metadata:
      name: app-secret
  data:
    DB_Host: bXlzcWw=
    DB_User: cm9vdA==
    DB_Password: cGFzd3Jk
  ```
  **encode & decode**

  ```bash
  echo -n <string> | base64
  echo -n <string> | base64 --decode
  ```
  => encoded 된 값을 사용한다. (하지만 같은 문자열은 동일한 문자열로 encode 된다는 점을 숙지할 것)

  - pod에서 secret 사용

  ```yaml
  # secret 사용
  apiVersion: v1
  kind: Pod
  metadata: 
    name: simple-webapp-color
  spec:
    containers:
    - name: simple-webapp-color
      image: simple-webapp-color
      ports:
        - containerPort: 8080
      envFrom:
        - secretRef:
            name: app-config
  ```
=> [secret은 base64로 쉽게 decode 될 수 있기 때문에 반드시 encrypt를 해서 사용하여야 한다.](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)

=> [secret을 사용하는 방법](https://kubernetes.io/docs/concepts/configuration/secret/#risks)

=> [Vault 사용](https://www.vaultproject.io/)

참고
```pre
Also the way kubernetes handles secrets. Such as:

A secret is only sent to a node if a pod on that node requires it.

Kubelet stores the secret into a tmpfs so that the secret is not written to disk storage.

Once the Pod that depends on the secret is deleted, kubelet will delete its local copy of the secret data as well.
```