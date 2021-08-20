Devops: DEVASC SKILLS
============

Task 1 -- GitHub Skills Test
------------

Task Preperation

- Inloggen op github.com
- Remote repository aanmaken
    
Task implementation

- De directory "Devasc_Skills" aanmaken
- Git initialiseren
    "git init"
- README.md aanmaken in de dir
- Staging van alle bestanden
    git add .
- Tracking changes
    git commit -m "Task 1: Manage github scripts and documents"
- De lokale directory linken aan de remote repository
    git remote add origin https://github.com/ElioTcholakov/  Devasc_Skills.git
- Gestagede bestanden naar remote repository uploaden
    git push origin master

Task troubleshooting

    Wanneer ik de eerste keer probeerde te 'pushen' en dus mijn
    gebruikersnaam en wachwoord invulde, kreeg ik een error-bericht
    dat zei dat Github geen wachtwoorden meer accepteerd
    en dat ze nu met personal access tokens werken.
    Dit heb ik dan aangemaakt op github.com en vervolgens werkte mijn push
    wel wanneer ik de token dan invulde ipv mijn wachtwoord.

Task verification

Succesvol pushen naar de remote repository:



Task 2 -- Ansible Skills Test
------------

Task Preperation

- Aanmaken van de bestand: "hosts"
- Aanmaken configuratie bestand: "ansible.cfg"
    
Task implementation

- Aanmaken playbook met naam "ntp_install.yml"  
- Connectie testen met ping-commando

Task troubleshooting

- Bij het uitvoeren van het commando: "ansible-playbook -v ntp_install.yml", kreeg ik de volgende error:

Task verification

Connectie testen met host:


Task 3 -- Docker
------------

Task Preperation

- Maak een lege DockerFile aan
- Bestudeer de code van het gegeven Ansible playbook
    
Task implementation

- Implementeren van code in Dockerfile
- Een Docker Image maken van het bestand
- Het laten runnen in een container   

Task troubleshooting

- Docker kon geen container aanmaken waardoor ik het niet kon 'runnen':




Task 4 -- Webex Teams API
------------

Task Preperation

- Inloggen op webex developer website met je webex account
- Inloggen en je access token aanvragen.
    
Task implementation

*Scripts gebaseerd op die van het labo 8.6.7*

- Authorizeren van mijn webex account:
https://github.com/ElioTcholakov/3TI_DevOps/blob/master/Webex/authorization.png
- Aanmaken van een room:
![Create Room](roomcreation.png "Create Room")
- Het toevoegen van een member:
![Add Member](Webex/addmember.png "Add Member")
- Het sturen van een bericht:
![Send Message](sendmessage.png "Send Message")

Task troubleshooting

    Het was niet meteen duidelijk wat de room id was: 
    (bv owner-id, id, ...)
    Uiteindelijk bleek het de eerste id te zijn 
    die niet leek te werken de eerste keer
    zoals op de schermopname kan gezien worden.

Task verification

Het resultaat:

