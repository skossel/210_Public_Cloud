Was ist Container-Technologie oder Container-Virtualisierung?
- Container-Technologie: Kernel wird mit dem Betriebssystem geteilt
- Container-Virtualisierung (VM): Eigenes Betriebssystem

Was sind die Vor- und Nachteile der Container-Technologie zu virtuellen Servern (VM)?
Container-Technologie:
- Vorteile
  - schnelle Startzeit
  - plattformunabhängig
- Nachteile
  - instabil bei Host-System Überlastung
  - weniger sicher als VMs (einfacher aus Container auszubrechen)
virtuelle Server (VM):
  - Vorteile
    - geeignet für umfangreiche Anwendungen
  - Nachteile
    - hoher Reccourcenverbrauch (RAM, CPU)
    - langsamer, da Betriebssystem die VM starten muss

Welche Produkte kennen Sie im Zusammenhang mit virtuellen Servern und Container?
- Virtuelle Server: VMware, VirtualBox
- Container: Docker

Wie unterscheiden sich die Technologien VM und Container in Bezug auf Bereitstellung, Speicherplatz, Portabilität, Effizienz und Betriebssystem (Kernel)?

| **Kriterium**           | **Virtuelle Maschinen (VMs)**       | **Container**                   |
|--------------------------|-------------------------------------|----------------------------------|
| **Bereitstellung**       | Langsam, OS-Boot nötig             | Schnell, wenige Sekunden        |
| **Speicherplatz**        | Groß, mehrere GB                   | Klein, oft nur MB               |
| **Portabilität**         | Hypervisor-abhängig                | Plattformunabhängig             |
| **Effizienz**            | Ressourcenintensiv                | Leichtgewichtig                 |
| **Betriebssystem (Kernel)** | Eigenes OS                      | Teilt Kernel mit Host           |

Können virtuelle Server immer durch Container ersetzt werden?
#### **Nein, VMs können nicht immer durch Container ersetzt werden.**
### **Warum nicht?**
- **Betriebssystem-Anforderungen**:
  - VMs: Verschiedene OS (z. B. Linux + Windows).
  - Container: Gleicher Kernel wie Host nötig.
- bei Low Level Uscases kann dies Container nicht machen

### **Wann Container sinnvoll sind:**
- Microservices-Architekturen.
- Agile Entwicklung und CI/CD.
- Hohe Skalierbarkeit.

### **Wann VMs unverzichtbar sind:**
- Gemischte Betriebssysteme (Windows + Linux).
- Legacy- und sicherheitskritische Anwendungen.
- Ressourcenintensive und stabile Workloads.
- Persistenter Speicherbedarf

Was ist unterschied zwischen Self-Managed und Fully Managed? Notieren Sie sich die wichtigsten Merkmale und diskutieren Sie die Ergebnisse in der Gruppe.

| **Merkmal**           | **Self-Managed**                     | **Fully Managed**                |
|------------------------|--------------------------------------|----------------------------------|
| **Verantwortung**      | Nutzer übernimmt alles              | Anbieter übernimmt Betrieb      |
| **Flexibilität**       | Maximale Kontrolle                  | Eingeschränkte Anpassung        |
| **Wartung**           | Manuell (Updates, Backups)           | Automatisch                     |
| **Kosten**             | Günstiger, aber zeitaufwändig        | Höher, weniger interner Aufwand |
| **Expertise nötig**    | Hohe technische Kenntnisse           | Kaum Fachwissen nötig           |
| **Einsatzzeit**        | Langsam (Einrichtung/Wartung)        | Schnell (Out-of-the-box)        |
| **Abhängigkeit**       | Keine Abhängigkeit                  | Abhängig vom Anbieter           |
| **Beispiele**          | Kubernetes, selbst verwaltete DBs    | AWS RDS, Google GKE             |


Container: 
- schnell Repo clonen und lokal starten
- man kann Dependencies vom Container angeben
