### Dockerfile builden
```bash
docker build -t public_cloud_uek_3.2 .
```
### Image ausführen -> Container wird dafür erstellt
```bash
docker run -p 8081:80 public_cloud_uek_3.2
```
### Container umbenennen
```bash
docker rename eloquent_torvalds public_cloud_uek
```
