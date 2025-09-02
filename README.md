# Scripting mit Bash Shell

Inhaltsübersicht

****
- [Scripting mit Bash Shell](#scripting-mit-bash-shell)
  - [Einführung in Scripting mit Bash](#einführung-in-scripting-mit-bash)
  - [Alias: Abkürzungen für Befehle](#alias-abkürzungen-für-befehle)
  - [Erster Script: welcome.sh](#erster-script-welcomesh)
  - [Ablaufsteuerung von Scripts](#ablaufsteuerung-von-scripts)
  - [Vergleiche](#vergleiche)
    - [Verzweigung mit IF THEN ELSE](#verzweigung-mit-if-then-else)
    - [Logische Operatoren](#logische-operatoren)
    - [Script compare_number.sh](#script-compare_numbersh)
  - [Schlaufen](#schlaufen)
  - [Script md5_Loop](#script-md5_loop)
- [Linux Kommandos](#linux-kommandos)
  - [Dateien und Verzeichnisse](#dateien-und-verzeichnisse)
  - [Verwendung von Dateinhalten](#verwendung-von-dateinhalten)
  - [Verwaltung von Prozessen](#verwaltung-von-prozessen)
  - [Kommandos die Ausgaben machen](#kommandos-die-ausgaben-machen)
  - [Ausgaben von Kommandos steuern (streams)](#ausgaben-von-kommandos-steuern-streams)
[TOC]

## Einführung in Scripting mit Bash

Ein Script beinhaltet mehrere Kommandos, welche in einer genauen Seqeuenz abgearbeitet werden. Das bietet den Vorteil, dass wir die eingesetzten Kommandos nicht mehr einzeln absetzen, sondern nur den einen Script aufrufen können.

Es ist zudem garantiert, dass der Ablauf immer exakt gleich ausgeführt wird.

Bevor wir einen ersten Script schreiben, noch eine Variante zur Vereinfachung einzelner Befehle:

## Alias: Abkürzungen für Befehle

Ein Alias ist ein Synonym für einen einfachen Befehl, gebildet aus einem existierenden Shell Befehlswort. Mit folgendem Befehl werden alle bereits definierten Alias aufgelistet:

```bash
~$ alias
alias ls='ls --color=auto'
```

Einen neuen Alias erstellen sie mit folgendem Befehl:

```bash
~$ alias ll='ls -ltrah'
```

Ab jetzt können sie den Alias verwenden und sparen sich die Tipparbeit für die Parameter.

Ein bestehender Alias kann bei Bedarf auch wieder entfernt werden mit:

```bash
~$ unalias ll
```

## Find: Dateien und Ordner suchen

Der einfachste Weg, Dateien unter Linux zu suchen, ist find. Find benötigt den Start-Ordner und den zu suchenden Datei- oder Ordnernamen:

```bash
~$ find /home -name dateidieichsuche.sh
/home/benutzer/dateidieichsuche.sh
```

Suchen Sie die nach der Datei Welcome.sh in /home-Verzeichnis. Recherchieren Sie mir im manual (man find), wie Gross- und Kleinschreibung bei einer Suche mit find ignoriert werden können.

## rm und mv: Löschen, verschieben und umbennenen

Wenn Sie eine Datei umbennenen, "verschieben" Sie sie vom alten zum neuen Dateinamen

```bash
~$ mv dateidieichsuche.sh DateiDieSichSuche.sh
```

Eine Datei löschen Sie mir rm:
```bash
~$ rm DateiDieSichSuche.sh
```

Ein Ordner ist unter Linux eine Datei, die weitere Dateien beinhaltet. Einen Ordner löschen Sie darum mit -r was für "rekursiv" steht. rm -r löscht zuerst die Inhalte eines Ordners, danach den Ordner selbst.
```bash
~$ rm -r MeinOrdner
```

## Erster Script: welcome.sh

Führen sie folgende Befehle zur Erstellung des Scripts in der Linux Shell bash aus:

```bash
~$ nano welcome.sh
```

Im Editorfenster füllen sie untenstehenden Text ein:

```
#!/bin/bash
# Variable current_user mit dem eingelogten Benutzer befüllen
current_user=$(whoami)
# Variable timestamp mit aktueller Systemzeit befüllen
timestamp=$(date +%H:%M)
echo "Guten Tag $current_user!"
echo "Es ist jetzt genau: $timestamp"
```

Mit der Tastenkombination Ctrl-x und im Anschluss Y speichern sie den Script.

Jetzt braucht der Script noch die Berechtigung ausgeführt werden zu können, dazu folgender Befehl:

```bash
~$ chmod +x welcome.sh
```

Nun rufen sie Ihren ersten Script auf:

```bash
~$ ./welcome.sh
```

Auf dem Bildschirm sieht das dann so aus:

```bash
benutzer@bzu-deb-vm:~$ ./welcome.sh
Guten Tag benutzer!
Es ist jetzt genau: 09:27
benutzer@bzu-deb-vm:~$ 
```

## Ablaufsteuerung von Scripts

## Vergleiche verwenden den Operator und sind erfüllt, wenn die Bedingung richtig ist.

|              Operator | Description                                                           |
| --------------------: | :-------------------------------------------------------------------- |
|          ! EXPRESSION | The EXPRESSION is false.                                              |
|             -n STRING | The length of STRING is greater than zero.                            |
|             -z STRING | The lengh of STRING is zero (ie it is empty).                         |
|     STRING1 == STRING2 | STRING1 is equal to STRING2                                           |
|    STRING1 != STRING2 | STRING1 is not equal to STRING2                                       |
| INTEGER1 -eq INTEGER2 | INTEGER1 is numerically equal to INTEGER2                             |
| INTEGER1 -gt INTEGER2 | INTEGER1 is numerically greater than INTEGER2                         |
| INTEGER1 -lt INTEGER2 | INTEGER1 is numerically less than INTEGER2                            |
|       FILE1 -nt FILE2 | FILE1 is newer then FILE2
|               -d FILE | FILE exists and is a directory.                                       |
|               -f FILE | FILE exists.                                                          |
|               -r FILE | FILE exists and the read permission is granted.                       |
|               -s FILE | FILE exists and it's size is greater than zero (ie. it is not empty). |
|               -w FILE | FILE exists and the write permission is granted.                      |
|               -x FILE | FILE exists and the execute permission is granted.                    |

Folgendes Beispiel für je einen Vergleiche

```bash
~$ [ 100 -eq 99 ]; echo $?
1
```

```bash
~$ [ "hund" != "katz" ]; echo $?
0
```

Ist das Resultat so, wie erwartet? 

Im Bash script entspricht 0 logisch True und 1 logisch False. Also genau umgekehrt, als man erwarten könnte!!

Ein weiteres Beispiel als Script compare_cars.sh

```bash
#!/bin/bash

string_a="Tesla"
string_b="VW"

echo "Sind $string_a und  $string_b gleich lange Wörter?"
[ $string_a == $string_b ]
echo $?

num_a=200
num_b=200

echo "Ist $num_a gleich wie $num_b ?"
[ $num_a -eq $num_b ]
echo $?
```

Für die Verwendung von Verzweigungen im Scipt-Ablauf können wir "Wenn....dann... oder sonst" verwenden.

### Verzweigung mit IF THEN ELSE

**if [ <Bedingung aus Vergleichen> ]**
**then**
**<Befehl(e)>**
**else**
**<andere Befehle(e)>**
**fi**



### Logische Operatoren

- **and** - &&
- **or** - ||



### Script compare_number.sh

```bash
#!/bin/bash
# Prüfung ob dem Script Parameter mitgegeben wurden. Wenn nicht, nehmen wir fixe Zahlen
# Bedingung setzt sich aus mehrern Vergleichen zusammen, diese sind logisch UND verknüpft
if [ ! -z $1 ] && [ ! -z $2 ]; then
   nummer_a=$1
   nummer_b=$2
else
   nummer_a=200
   nummer_b=400
fi

# Vergleiche sind die Bedingung für die Verzweigung
if [ $nummer_a -lt $nummer_b ]; then
    echo "$nummer_a is less than $nummer_b!"

else
    echo "$nummer_a is greater than $nummer_b!"
fi
```

### Script Prüfen, ob eine Datei existert

```bash
#!/bin/bash
file="datei.txt"

if [ -f "$file" ]; then
    echo "Die Datei $file ist eine gültige Datei."
else
    echo "Die Datei $file existiert nicht."
fi
```


## Schlaufen

Solange die Bedingung erfüllt ist, oder der Bereich nicht abearbeitet wird (Siehe Range), wird eine Schlaufe ausgeführt.

## Script md5_Loop

```bash
#!/bin/bash
for directory in $*; do
    if [ ! -d $directory ]; then
       file=$directory
       md5sum $file
    else
       echo "Verzeichnis $directory, wird ausgelassen!"
    fi

done;
```

Auch in Bash sind die Schlaufen nach dem Pattern While machbar:

```bash
#!/bin/bash
counter=1
 while [ $counter -le 10 ]
 do
 echo $counter
 ((counter++))
done

echo Fertig
```



# Linux Kommandos

Untenstehend eine nicht abschliessende Auflistung von häufig verwendeten Kommandos für Linux, gruppiert nach Anwendungsfall.

Die meisten Kommandos sind mit Optionen und Parametern aufrufbar. Optionen können auf weggelassen werden

command *[options]*  <parameter>

--> In Terminal haben sie die Möglichkeit, sich mit man <command> eine Beschreibung anzeigen zu lassen.

## Dateien und Verzeichnisse

| Kommando                 | Beschreibung                                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **cd** <folder>          | In Verzeichnis <folder> wechseln                                                                               |
| **pwd**                  | Gibt aktuelles Verzeichnis aus                                                                                 |
| **ls**                   | Listet den Inhalt des aktuellen Verzeichnis auf                                                                |
| **mkdir** <folder>       | Erstellt ein Verzeichnis mit dem Namen <folder>                                                                |
| **rmdir** <folder>       | Löscht ein Verzeichnis <folder>                                                                                |
| **cp** <source> <target> | Kopiert eine Datei von <source> nach <target>                                                                  |
| **mv** <source> <target> | Verschiebt eine Datei von <source> nach <target>                                                               |
| **touch** <file>         | Erstellt eine leere Datei <file> oder aktualisiert den Veränderungszeitpunkt, wenn die Datei bereits existiert |
| **chmod** <flags> <file> | Ändert die Berechtigung auf der Datei <file> gemäss den Angaben <flags>                                        |
| **chown** <user> <file>  | Ändert den Eigentümer <user> für eine Datei <file>                                                             |
| **chgrp** <group> <file> | Ändert die Gruppe <group> für eine Datei <file>                                                                |

## Verwendung von Dateinhalten

| Kommando        | Beschreibung                                                           |
| --------------- | ---------------------------------------------------------------------- |
| **cat** <file>  | Zeigt den Inhalt der Datei <file> auf standard output                  |
| **wc** <file>   | Zählt die Anzahl Wörter der Datei <file>                               |
| **file** <file> | Gibt den vom OS erkannten Dateityp für die angegebene Datei <file> aus |
| **head** <file> | Gibt die ersten 10 Zeilen für die Datei <file> aus                     |
| **tail** <file> | Gibt die letzten 10 Zeilen für die Datei <file> aus                    |
| **less** <file> | Scrollt durch den Inhalt der Datei <file>, (Anzeige mit q verlassen)   |
| **sort** <file> | Sortiert die Textzeilen einer Datei alphabetisch                       |

## Verwaltung von Prozessen

| Kommando       | Beschreibung                                                                                          |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| **ps**         | Listet alle Prozesse im Terminal für den aktuellen Benutzer auf.<br />Jeder Prozess hat eine Id <PID> |
| **ps** ax      | Listet alle Prozesse für jeden Benutzer, die gerade ausgeführt werden                                 |
| **ps** e       | Zeigt neben dem Prozess die entsprechende Umgebung an                                                 |
| **kill** <PID> | Befehlt beendet einen Prozess, indem er das Signal SIGTERM an den Prozess <PID> sendet                |
| **fg**         | Bringt einen gestoppten oder in den Hintergrund gebrachten Job wieder in den Vodergrund               |
| **bg**         | Bringt einen gestoppten Job in den Hintergrund                                                        |
| **jobs**       | Listet alle Jobs auf                                                                                  |
| **top**        | Zeigt die Prozesse, welche im Moment die meiste CPU Zeit brauchen (Verlassen mit q)                   |



## Kommandos die Ausgaben machen

| Kommando          | Beschreibung                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------- |
| **echo** <string> | Gibt Meldung <string> auf Standard output aus                                               |
| **date**          | Gibt das aktuelle Systemdatum aus                                                           |
| **who**           | Gibt eine Liste der eingeloggten Benutzer aus                                               |
| **man** <command> | Zeigt die Hilfe und Beschreibung zu einem Befehl aus (Anzeige mit q verlassen, Suche mit /) |
| **uptime**        | Zeigt, wie lange das System schon läuft                                                     |
| **free** -h       | Zeigt die Grösse des ungenutzen Speichers für das System                                    |
|                   |                                                                                             |

## Ausgaben von Kommandos steuern (streams)

| Steuerzeichen             | Beschreibung                                                                                 |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| command **>** file        | Standard output in Datei umleiten (überschreibt bestehende Datei <file>)                     |
| command **>>** file       | Standard Output in Datei umleiten, an bestehende Datei <file> anhängen                       |
| command 2> file           | Standard Error Anzeige umleiten in Datei <file><br /> Mit "dev/null" wird Ausgabe verhindert |
| command1 **\|** command 2 | Verbindet Ausgabe von Command1 mit Eingabe von Command2                                      |
|                           |                                                                                              |
|                           |                                                                                              |

