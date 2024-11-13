|

# Vergleichende Analyse führender Cloud-Anbieter: AWS, Microsoft Azure, Google Cloud

## 1. Wichtige Dienstleistungen

| **Dienstleistung**  | **AWS**                              | **Microsoft Azure**                    | **Google Cloud**                       |
|----------------------|--------------------------------------|----------------------------------------|----------------------------------------|
| **Speicherlösungen** | S3 (ab $0.023/GB), EBS ($0.08/GB/Monat), Glacier ($0.004/GB) | Blob Storage ($0.0184/GB), Disk Storage ($0.05/GB), Archive ($0.0012/GB) | Cloud Storage ($0.020/GB), Persistent Disks ($0.04/GB) |
| **Datenbanken**      | RDS ($0.016/DB-Instance/Stunde), DynamoDB ($1.25/WCU/Monat), Redshift ($0.25/Compute/Stunde) | Azure SQL ($0.021/DTU/Stunde), Cosmos DB ($0.008/RU/Stunde), Synapse ($4/TB) | Cloud SQL ($0.015/vCPU/Stunde), BigQuery ($5/TB), Firestore ($0.18/GB/Monat) |
| **AI/ML**            | SageMaker ($0.10/Training/Stunde), Rekognition ($1/1000 Anfragen), Forecast ($0.60/1000 Einheiten) | Azure AI (ab $0.004/Transaktion), Machine Learning Studio ($0.016/Stunde) | Vertex AI ($0.002/Prediction), AutoML ($20/Training-Modell) |
| **Netzwerkdienste**  | VPC (kostenlos), Route 53 ($0.40/Zone/Monat), Direct Connect ($0.03/GB) | Virtual Network ($0.005/VNET/Stunde), Traffic Manager ($0.375/1000 Anfragen) | VPC (kostenlos), Cloud CDN ($0.02/GB), Interconnect ($0.025/GB) |
| **Serverless**       | AWS Lambda (ab $0.20/Millionen Anfragen) | Azure Functions (ab $0.15/Millionen Anfragen) | Cloud Functions (ab $0.40/Millionen Anfragen) |

## 2. Vergleich der Kriterien

### **a) Kostenstruktur**
- **AWS**: Nutzt nutzungsbasierte Abrechnung, z. B. EC2-Instances ab $0.012/Stunde. Reserved Instances bieten bis zu 75% Rabatt.
- **Azure**: Preise ähnlich AWS, z. B. VM ab $0.009/Stunde. Kosteneinsparungen durch Hybrid Benefit (bis zu 50% Rabatt für Windows-Lizenzen).
- **Google Cloud**: Günstige Einstiegspreise, z. B. VMs ab $0.0075/Stunde. Automatische Rabatte von 20–30% bei langfristiger Nutzung.

### **b) Skalierbarkeit**
- **AWS**: 30+ Regionen, 99+ Verfügbarkeitszonen.
- **Azure**: 60+ Regionen, eng integriert in Microsoft-Dienste.
- **Google Cloud**: 38 Regionen, optimiert für datenintensive Workloads.

### **c) Sicherheit**
- **AWS**: IAM, Shield, umfangreiche Compliance (z. B. HIPAA, GDPR).
- **Azure**: Azure Defender, Sentinel, Hybrid-Cloud-Sicherheitslösungen.
- **Google Cloud**: BeyondCorp, Zero-Trust-Modell, starke Datenverschlüsselung.

### **d) Verfügbarkeit und Zuverlässigkeit**
- **AWS**: SLA von 99.99% Verfügbarkeit, Marktführer bei Ausfallsicherheit.
- **Azure**: SLA von 99.95%, historisch jedoch mehr Vorfälle.
- **Google Cloud**: SLA von 99.95%, profitiert von Googles Netzwerk.

### **e) Kundensupport**
- **AWS**: Supportpläne ab $29/Monat, detaillierte Dokumentation.
- **Azure**: Supportpläne ab $29/Monat, Vorteile für Microsoft-Nutzer.
- **Google Cloud**: Supportpläne ab $25/Monat, aber weniger etabliert.

## 3. Vor- und Nachteile

| **Anbieter**  | **Vorteile**                                                                 | **Nachteile**                                      |
|---------------|------------------------------------------------------------------------------|---------------------------------------------------|
| **AWS**       | Marktführer, größte Serviceauswahl, hohe Zuverlässigkeit                    | Kosten und Komplexität bei der Abrechnung         |
| **Azure**     | Perfekte Integration mit Microsoft-Produkten, Hybrid-Cloud-freundlich       | Weniger robust in Regionen ohne Microsoft-Fokus   |
| **Google Cloud** | Exzellent für Datenanalyse und AI/ML, intuitive Preisgestaltung           | Geringeres Serviceangebot, kleiner Marktanteil    |

## Fazit
- **AWS**: Beste Wahl für Unternehmen mit globaler Reichweite und vielfältigen Anforderungen.
- **Azure**: Ideal für Unternehmen, die Microsoft-Tools nutzen.
- **Google Cloud**: Starke Option für datenintensive Workloads und moderne ML/AI-Anwendungen.
