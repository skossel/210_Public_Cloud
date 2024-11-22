
## I. Thema: Codebase

Um was geht es bei diesem Faktor?
- Quellcode durch Versionsverwaltung zentral gespeichert und verwaltet

Welches Problem löst dieser Faktor?
- hilft bei Wartung und Zusammenarbeit
- ermöglicht die Nachverfolgung von Änderungen

Wie wird dieser Faktor in der realen Welt umgesetzt?
- Versionierung: Git-Repos (z.B. GitHub, GitLab)
- Organisation: klare Ordnerstruktur und Namenskonventionen
- Teamwork: Pull-Requests, Code-Reviews, CI/CD

## II. Dependencies
1. **Um was geht es?** Abhängigkeiten explizit deklarieren und isolieren.
2. **Welches Problem löst es?** Verhindert fehlende oder inkompatible Abhängigkeiten.
3. **Reale Umsetzung?** Nutzung von Package-Managern wie Maven, npm oder pip.

---

## III. Config
1. **Um was geht es?** Konfigurationen in der Umgebung speichern.
2. **Welches Problem löst es?** Trennung von Code und Umgebungsdaten.
3. **Reale Umsetzung?** Umgebungsvariablen oder `.env`-Dateien.

---

## IV. Backing Services
1. **Um was geht es?** Dienste wie Datenbanken als externe Ressourcen behandeln.
2. **Welches Problem löst es?** Austauschbarkeit von Diensten ohne Codeänderungen.
3. **Reale Umsetzung?** Nutzung von Diensten via API oder DNS (z. B. externe Datenbanken).

---

## V. Build, Release, Run
1. **Um was geht es?** Trennung von Build-, Release- und Laufzeitphasen.
2. **Welches Problem löst es?** Klare Phasen und weniger Fehler bei Deployments.
3. **Reale Umsetzung?** CI/CD-Pipelines für Build und Deployment.

---

## VI. Processes
1. **Um was geht es?** Die App läuft als zustandslose Prozesse.
2. **Welches Problem löst es?** Skalierbarkeit und einfache Wartung.
3. **Reale Umsetzung?** Zustandsverwaltung in Datenbanken statt im Arbeitsspeicher.

---

## VII. Port Binding
1. **Um was geht es?** Dienste werden über Ports bereitgestellt.
2. **Welches Problem löst es?** Erlaubt unabhängige und flexible Kommunikation.
3. **Reale Umsetzung?** HTTP-Server mit spezifiziertem Port (z. B. 8080).

---

## VIII. Concurrency
1. **Um was geht es?** Skalierung über Prozesse statt Threads.
2. **Welches Problem löst es?** Effiziente Nutzung von Ressourcen bei hoher Last.
3. **Reale Umsetzung?** Lastverteilung mit mehreren Instanzen.

---

## IX. Disposability
1. **Um was geht es?** Prozesse starten und stoppen schnell und robust.
2. **Welches Problem löst es?** Reduziert Ausfallzeiten und verbessert Skalierung.
3. **Reale Umsetzung?** Container-Technologien wie Docker.

---

## X. Dev/prod Parity
1. **Um was geht es?** Gleiche Bedingungen in Entwicklung, Test und Produktion.
2. **Welches Problem löst es?** Reduziert Fehler durch Umgebungsunterschiede.
3. **Reale Umsetzung?** Nutzung von Containern und Infrastructure-as-Code.

---

## XI. Logs
1. **Um was geht es?** Logs als kontinuierliche Ereignisströme behandeln.
2. **Welches Problem löst es?** Zentralisierte Überwachung und Fehleranalyse.
3. **Reale Umsetzung?** Verwendung von Log-Streams (z. B. ELK-Stack).

---

## XII. Admin Processes
1. **Um was geht es?** Admin-Tasks als separate Einmalprozesse ausführen.
2. **Welches Problem löst es?** Flexibles Management ohne laufende Prozesse zu stören.
3. **Reale Umsetzung?** Migrationen oder Datenjobs als Skripte.



# Hinweise:

Wieso heissen diese 12 Faktors?
- kommt von Cloud Plattform Heroku

Umgebungsvariablen einem Config File vorziehen, damit man nicht nach jeder Änderung einen neuen Release erstellen muss.

Versionen:
- Dev
- Staging
- Production

Standard-Out: Standardausgabe meistens Terminal
