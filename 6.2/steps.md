
## Dockerfile builden
docker build -t nginxinc/nginx-unprivileged:latest

## Container aus dem Image starten
docker run -p 8080:8080 nginxinc/nginx-unprivileged:latest

## Container in Container Registry pushen
docker build -t ghcr.io/skossel/html-openshift-app:v1 .
docker push ghcr.io/skossel/html-openshift-app:v1

## Deployment applizieren
kubectl apply -f deployment.yaml
kubectl get deployments

## Route abrufen
kubectl get services
kubectl get routes

## Openshift Container builden (zum Webseite anzeigen)
docker run -p 8080:8080 ghcr.io/skossel/html-openshift-app:v1
