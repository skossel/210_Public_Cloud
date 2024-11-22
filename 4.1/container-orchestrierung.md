Warum braucht man Container-Orchestrierung?
- um einfach viele Container zu verwalten
- Docker Compose: Orchestrator von Docker Containern

Wie funktioniert Container-Orchestrierung?
- Verwaltung von Containern

Welche Container-Orchestrierung Technologien gibt es?
- Kubernetes
- Docker Swarm
- Docker Compose

Was versteht man unter "Scaling Container"?
- mehrere Container auf einmal starten oder beenden
- vertikal: mehr Leistung für Applikation
    - stateless: speichert keine Daten
    - stateful: speichert Daten
    - Ziel: Applikation stateless machen und Datenbank für Daten Speicherung verwenden
- horziontal: Applikation auf mehrere Container verteilen

Was gibt es für Depolyment Strategien?

Rolling Updates
- neue Version wird schrittweise über bestehende Instanzen verteilt
- Vorteil: keine Downtime
- Nachteil: benötigt doppelte Anzahl Ressourcen

1. Recreate Deployment
  - bestehende Instanzen werden beendet und durch neue ersetzt
2. Rolling Deployment
  - neue Version wird schrittweise über bestehende Instanzen verteilt
3. Blue-Green Deployment
  - es werden zwei seperate, aber identische Umgebungen erstellt
4. Canary Deployment
  - neue Version wird an eine kleine Benutzergruppe veröffentlicht
5. Shadow Deployment
  - neue Version wird live getestet, ohne Benutzer zu beeinflussen
6. A/B Testing
- Verschiedene Versionen werden parallel getestet, um Feedback zu vergleichen.  
7. **Feature Toggles (Dark Launching)**
- Funktionen werden aktiviert/deaktiviert, ohne neuen Code bereitzustellen.
8. **Serverless Deployment**
- Code wird in serverlose Umgebungen bereitgestellt.


Load Balancer
- verteilt Anfragen gleichmässig auf die Instanzen



Node, Cluster
