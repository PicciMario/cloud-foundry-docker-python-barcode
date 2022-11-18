# Esperimento di applicazione web su SAP Cloud Foundry.

Crea un endpoint POST che riceve un PDF come payload, e restituisce un oggetto JSON con la lista dei valori dei barcode rilevati nella prima pagina del documento.

## Creazione immagine Docker

- Richiede Docker sulla macchina locale.

- Creare account su [Docker Hub](https://hub.docker.com/).

- Creare immagine docker (nota: come prefisso del tag usare il proprio nome account su Docker Hub).

	`docker build -t piccimario/barcode-cf .`

- Test in locale (viene esposta la porta 3333).

	`docker run -p 3333:3333 piccimario/barcode-cf`

- Push su Docker Hub.

	`docker push piccimario/barcode-cf`

## Caricamento immagine su Cloud Foundry:

- Creare [account trial](https://account.hanatrial.ondemand.com/trial/#/home/trial).
- Installare [tools cli](https://github.com/cloudfoundry/cli/releases) per Cloud Foundry.
- `cf api https://api.cf.eu20.hana.ondemand.com` (usare endpoint cf corretto per il proprio trial)
- `cf login`
- `cf push barcode-docker --docker-image piccimario/barcode-cf --docker-username piccimario -k 512M -m 512M`

---

## Risorse varie:

https://adamtheautomator.com/flask-web-server/

https://blogs.sap.com/2021/01/02/deploy-python-application-on-sap-cloud-platform-using-docker-container/

https://techtutorialsx.com/2020/01/01/python-pyzbar-detecting-and-decoding-barcode/

Servizio gratuito per generare immagini di barcode in diversi formati
https://barcode.tec-it.com
