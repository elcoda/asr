# Demo ASR con Speechmatics

Questo progetto dimostra come realizzare una piccola interfaccia web per la trascrizione automatica in tempo reale utilizzando la libreria [speechmatics-python](https://github.com/speechmatics/speechmatics-python).

Sono previste due pagine:

* **/admin** – pagina di amministrazione da cui avviare la registrazione e vedere la trascrizione.
* **/view** – pagina pubblica in sola lettura dove i visitatori possono seguire la trascrizione in tempo reale.
* **/** – una semplice copertina con animazione dell'onda e una breve descrizione del servizio.

Il codice è un esempio semplificato: la funzione di avvio della registrazione (`start_recognition`) va collegata alla reale API di Speechmatics e alla cattura dell'audio dal microfono.

## Avvio dell'applicazione

1. Installare le dipendenze Python:

```bash
pip install -r requirements.txt
```

2. Impostare le credenziali Speechmatics (ad esempio tramite variabili d'ambiente) e avviare il server:

```bash
python app.py
```

L'applicazione sarà disponibile su `http://localhost:5000`. Aprire `/admin` per controllare la registrazione e `/view` per i visitatori.
