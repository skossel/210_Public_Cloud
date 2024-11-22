
## Step 1
What is the application doing?
displays quotes

Which programming language is used for the backend?
Python

Which programming language is used for the frontend?
JS (React)

## Step 2
To which resource type does the Route forward it’s request to?
Zu diesem Port -> targetPort: 10000-tcp

How does a Service know, to which Pod’s it need to forward requests to?
Zu diesen targetPorts:
  targetPort: 10000
  targetPort: 8443
  targetPort: 8778

## Step 3
Who creates the requests to the Backend? The Frontend or the Browser?
I send a command to Openshift und Openshift creates the request.

## Step 4

Persistent Volume Claim (PVC)
Ein Persistent Volume Claim (PVC) ist eine Anfrage in Kubernetes, mit der ein Pod Speicherplatz anfordert. PVCs sind die Schnittstelle zwischen einem Pod und einem Persistent Volume (PV), sodass der Speicher dynamisch oder statisch bereitgestellt wird.

## Step 7
export PODNAME=$(kubectl get pods -l app=mysql -o jsonpath='{.items[0].metadata.name}')

git checkout .
kubectl cp ./create_database_quotesdb.sql $PODNAME:/tmp/create_database_quotesdb.sql
kubectl cp ./create_database.sh $PODNAME:/tmp/create_database.sh
kubectl exec deploy/mysql -- /bin/bash ./tmp/create_database.sh

kubectl cp ./create_table_quotes.sql $PODNAME:/tmp/create_table_quotes.sql
kubectl cp ./create_tables.sh $PODNAME:/tmp/create_tables.sh
kubectl exec deploy/mysql -- /bin/bash ./tmp/create_tables.sh

kubectl cp ./populate_table_quotes_BASH.sql $PODNAME:/tmp/populate_table_quotes_BASH.sql
kubectl cp ./quotes.csv $PODNAME:/tmp/quotes.csv
kubectl cp ./populate_tables_BASH.sh $PODNAME:/tmp/populate_tables_BASH.sh
kubectl exec deploy/mysql -- /bin/bash ./tmp/populate_tables_BASH.sh

kubectl cp ./query_table_quotes.sql $PODNAME:/tmp/query_table_quotes.sql
kubectl cp ./query_table_quotes.sh $PODNAME:/tmp/query_table_quotes.sh
kubectl exec deploy/mysql -- /bin/bash ./tmp/query_table_quotes.sh

## Step 9 (evt. Fragen)
How does the backend know to which database it needs to connect?
wegen de Service Name

## Step 11
Horizontal Pod Autoscaler (HPA)
