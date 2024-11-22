minikube start driver --docker

als Root starten: 
minikube start --force

minikube status

kubectl get node
kubectl get pod

create username and password:
echo -n mongouser | base64
echo -n mongopassword | base64

load the kubernetes components:
kubectl apply -f mongo-config.yaml
kubectl apply -f mongo-secret.yaml
kubectl apply -f mongo.yaml
kubectl apply -f webapp.yaml

give all the components created in the cluster:
kubectl get all

kubectl get configmap
kubectl get secret
kubectl get pod

kubectl --help
kubectl get --help

kubectl describe service webapp-service
kubectl get pod mongo-deployment-798f55b8-vj8gb

kubectl get svc

get ip adress to access:
minikube ip 
kubectl get node -o wide

get web url:
minikube service webapp-service
