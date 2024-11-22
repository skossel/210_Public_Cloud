## /quotes um url aufzurufen
curl https://quotes-233755-dthoma1.apps.exoscale-ch-gva-2-0.appuio.cloud/quotes


## Datei kompilieren (muss nach jedem change gemacht werden)
k apply -f .


## die URL bekommen
kubectl get routes


## Pod Anzahl verändern
kubectl scale deployments/quotes --replicas=3


kubectl get pvc

## set env variable
kubectl set env deployment/quotes DB_SERVICE_NAME=mysql

## HPa
k get hpa


Unterschied HPA und Load Balancer
- HPA: Skaliert die Anzahl der Pods automatisch basierend auf Ressourcenauslastung (z.B. CPU, RAM)
- Load Balancer: Verteilt den eingehenden Traffic gleichmässig auf mehrere Pods oder Server.

## Was macht ein HPA?
- Skaliert Pods basierend auf Ressourcenanforderungen (z. B. CPU, Speicher).
- Automatische Anpassung der Pod-Anzahl nach oben oder unten.

## Warum ist ein HPA nützlich?
- **Effizienz:** Ressourcenverbrauch wird an den Bedarf angepasst.
- **Kosteneinsparung:** Überflüssige Pods werden bei geringer Last entfernt.

## Was könnten die Risiken der Verwendung eines HPA sein?
- **Fehlkonfiguration:** Kann zu falscher Skalierung führen.
- **Instabilität:** Häufiges Skalieren bei Lastschwankungen oder Verzögerungen bei der Anpassung.


// aktuell hpa fragen beantworten (nr. 11) und hpa vollspamen für verbrauch gpu über 50%
