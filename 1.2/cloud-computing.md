# Cloud-Fragen

# wichtig: deployment und service modelle vor und nachteile


## Wie ist der Begriff Cloud entstanden?
- Vernetztes System, in welchem der Nutzer nicht genau weiss, wo er sich befindet.

## Wieso heisst es Cloud?
- Die Cloud symbolisiert eine Wolke, bei der man auch nicht genau weiss, wo sie beginnt und endet.

## Wie wird der Begriff Cloud definiert, z. B. gemäss NIST?
- **Definition gemäss NIST**:  
  Cloud Computing ist ein Modell, das einen bequemen, netzwerkbasierten Zugang zu einem gemeinsam genutzten Pool von konfigurierbaren IT-Ressourcen (z. B. Netzwerke, Server, Speicher, Anwendungen und Dienste) ermöglicht, die schnell bereitgestellt und mit minimalem Verwaltungsaufwand oder Interaktion des Anbieters freigegeben werden können.
- Ondemand
  - direkter Zugriff auf Ressource ohne dirkter Kontakt mit Anbieter

## Welches sind die 5 Merkmale einer Cloud?
1. **On-Demand Self-Service**:
    - Nutzer können IT-Ressourcen (z. B. Speicher, Rechenleistung) eigenständig und sofort bereitstellen, ohne manuelle Interaktion mit dem Anbieter.
2. **Breiter Netzwerkzugriff**:
    - Die Ressourcen sind über standardisierte Netzwerke verfügbar und können auf verschiedenen Geräten (z. B. PCs, Smartphones, Tablets) genutzt werden.
3. **Ressourcen-Pooling**:
    - IT-Ressourcen werden zentralisiert und dynamisch mehreren Nutzern oder Anwendungen zugewiesen („Multi-Tenant-Modell“).
    - Nutzer haben keine Kontrolle darüber, wo genau die Ressourcen physisch gehostet werden (Standortabstraktion).
4. **Schnelle Elastizität**:
    - Kapazitäten können flexibel und schnell skaliert werden, um den Anforderungen gerecht zu werden – sowohl nach oben als auch nach unten.
5. **Messbarer Dienst**:
    - Nutzung wird kontinuierlich überwacht und abgerechnet, unterstützt Optimierung und Kosteneffizienz.

## Welche Cloud-Dienstleistungen kennen Sie?
### **IaaS (Infrastructure as a Service)**
- **Beschreibung**: Bereitstellung von virtuellen Servern, Speicher, Netzwerken und anderen grundlegenden IT-Infrastrukturen.  
  Nutzer verwaltet Betriebssysteme und Anwendungen selbst.
- **Beispiele**:
    - Amazon Web Services (AWS EC2)

### **PaaS (Platform as a Service)**
- **Beschreibung**: Plattformen für die Entwicklung, Bereitstellung und Verwaltung von Anwendungen.  
  Entwickler konzentrieren sich auf die Programmierung, während die Infrastruktur vom Anbieter verwaltet wird.
- **Beispiele**:
    - Heroku

### **SaaS (Software as a Service)**
- **Beschreibung**: Vollständige Anwendungen, die über das Internet bereitgestellt und genutzt werden.  
  Nutzer braucht keine Infrastruktur oder Wartung zu übernehmen.
- **Beispiele**:
    - Microsoft 365
    - Google Workspace (Docs, Drive, Gmail)

## Welche Cloud-Anbieter kennen Sie?
- AWS
- Microsoft Azure
- Google Workspace

## Welche Cloud-Deployment-Modelle kennen Sie?
- **Public Cloud**: Öffentliche Cloud-Ressourcen, die von Drittanbietern betrieben werden, kosteneffizient und skalierbar, aber mit weniger Kontrolle und Sicherheit.
- **Private Cloud**: Exklusiv für eine Organisation, bietet hohe Sicherheit und Anpassung, ist jedoch teurer und weniger skalierbar.
- **Hybrid Cloud**: Kombination aus Public und Private Cloud für Flexibilität und Effizienz, jedoch komplex in der Verwaltung.
- **Community Cloud**: Geteilte Infrastruktur für Organisationen mit ähnlichen Anforderungen, fördert Zusammenarbeit, aber mit eingeschränkter Flexibilität.

## Was sind Cloud-Service-Modelle?
- Anwendungen und Infrastruktur-Ressourcen, die im Internet bereitgestellt werden.

## Weshalb soll ich Dienste aus der Cloud beziehen? Was sind die Vorteile?
- **Kosteneffizienz und Skalierbarkeit**: Bezahlung nur für genutzte Ressourcen und einfache Anpassung an wachsende oder schwankende Anforderungen.
- **Zugänglichkeit und Wartung**: Zugriff auf Dienste von überall, während der Anbieter Updates, Wartung und Sicherheit übernimmt.
- **Sicherheit und Innovation**: Hohe Sicherheitsstandards, automatische Backups und Zugang zu neuesten Technologien wie KI oder Big Data.

## Was sind die Nachteile?
- **Abhängigkeit vom Anbieter**: Bindung an spezifische Anbieter (Vendor Lock-in) kann Wechsel oder Migration erschweren.
- **Datenschutz und Sicherheit**: Sensible Daten liegen extern, was potenzielle Sicherheits- und Datenschutzrisiken birgt.
- **Abhängigkeit von Internetzugang**: Ohne stabile Internetverbindung ist der Zugriff auf Cloud-Dienste eingeschränkt oder unmöglich.

## Welche Dienstleistungen werden in Ihrem Betrieb On-Premise (eigenes Rechenzentrum) betrieben?
- Docker
- Intranet
- Jira
- Stash

## Wie werden technologische Beiträge in der Cloud geteilt bzw. zur Verfügung gestellt?
- **APIs und Marktplätze**: Dienste und Funktionen werden über APIs oder Cloud-Marktplätze bereitgestellt, sodass Entwickler diese einfach integrieren können (z. B. AWS Marketplace, Google APIs).
- **Open Source und Container**: Technologien wie Kubernetes, Docker oder Open-Source-Projekte werden über Plattformen wie GitHub oder Docker Hub geteilt und genutzt.
- **Daten- und Ressourcensharing**: Gemeinsame Nutzung von Daten, KI-Modellen oder Ressourcen in Multi-Tenant-Umgebungen (z. B. Google Public Datasets, AWS Open Data Registry).
