## **1. Wie muss der Command angepasst werden, damit es dennoch funktioniert?**

Das `nginxinc/nginx-unprivileged` Image lauscht standardmässig auf Port **8080** statt auf Port **80**. Daher muss der `docker run` Command wie folgt angepasst werden:

```bash
docker run -p 8081:8080 IMAGENAME
```

## Was sind die Unterschiede der beiden Images?

| **Eigenschaft**                    | **nginx**                              | **nginx-unprivileged**                |
|-------------------------------------|----------------------------------------|----------------------------------------|
| **Benutzer**                        | Läuft als `root`.                      | Läuft als nicht privilegierter Benutzer `nginx`. |
| **Standard-Port**                   | **80** (Root-Port).                    | **8080** (kein Root erforderlich).    |
| **Sicherheitsvorteil**              | Geringer, da Root-Berechtigungen.      | Höher, da keine Root-Berechtigungen notwendig sind. |
| **Einsatzgebiet**                   | Standard-Umgebungen.                   | Sicherheitskritische Umgebungen, z. B. Kubernetes. |
| **Flexibilität bei Ports**          | Kann auf Ports <1024 lauschen.         | Erfordert Ports ≥1024 (z. B. 8080).   |
