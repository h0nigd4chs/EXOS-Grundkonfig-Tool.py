# EXOS Grundkonfigurationstool
Ein Python-Skript, das grundlegende Konfigurationen auf einem ExtremeXOS (EXOS) Switch übernimmt. Dieses Skript ermöglicht es, wichtige Grundeinstellungen wie das Deaktivieren von Telnet und STP, das Aktivieren von SSH, das Erstellen von VLANs und das Setzen eines Gerätenamens einfach über die CLI des Switches vorzunehmen.

## Funktionen

- **Gerätenamen setzen:** Der Benutzer wird nach einem Gerätenamen gefragt, der über SNMP gesetzt wird.
- **Ports deaktivieren:** Alle Ports werden deaktiviert, um eine saubere Ausgangsbasis zu schaffen.
- **VLAN-Konfiguration:** VLANs mit einem bestimmten Namenspräfix und ID-Bereich können erstellt und auf bestimmte Ports getagged werden.
- **Telnet deaktivieren & SSH aktivieren:** Telnet wird deaktiviert und SSH wird aktiviert, um die Sicherheit zu erhöhen.
- **STP deaktivieren:** STP wird deaktiviert.

## Voraussetzungen

- **ExtremeXOS-Switch**: Das Skript verwendet EXOS-spezifische Befehle und ist daher nur auf Geräten mit dem ExtremeXOS-Betriebssystem nutzbar.
- **CLI-Zugriff auf den Switch**: Du musst Zugriff auf die CLI des EXOS-Switches haben.

## Installation und Verwendung

1. **Skript erstellen:**

   Melde dich auf deinem EXOS-Switch an und öffne einen Texteditor, zum Beispiel `vi`, um das Skript zu erstellen.

   ```bash
   vi <EuerWunschname>.py
   ```

2. **Skriptinhalt einfügen:**

   Kopiere den Inhalt des Skripts (aus der Datei `EXOSGrundKonfigGERScript.py`) in den geöffneten Texteditor. Nachdem du den Code eingefügt hast, speichere und schließe den Editor:

   - **Speichern und Beenden in `vi`:** Drücke `ESC`, tippe `:x` und drücke `ENTER`.

3. **Skript ausführen:**

   Um das Skript auszuführen, benutze den Befehl `run script`. Achte darauf, dass du die Endung `.py` weglässt:

   ```bash
   run script <EuerWunschname>
   ```

   **Beispiel:**

   ```bash
   run script EXOSGrundKonfig
   ```

   Das Skript wird jetzt ausgeführt und führt dich Schritt für Schritt durch die Konfiguration.

## Ablauf der Konfiguration

Das Skript führt dich durch folgende Schritte:

1. **Gerätenamen setzen:**
   - Du wirst nach einem Namen für das Gerät gefragt. Der Name wird über SNMP gesetzt.

2. **Ports deaktivieren:**
   - Alle Ports auf dem Switch werden deaktiviert.

3. **Default VLAN-Konfiguration:**
   - Das Default-VLAN wird von allen Ports entfernt.

4. **Telnet deaktivieren, SSH aktivieren und STP deaktivieren:**
   - Telnet wird deaktiviert, SSH wird aktiviert und STP wird deaktiviert, um die Sicherheit zu erhöhen.

5. **VLANs erstellen:**
   - Das Skript fragt dich nach einem Präfix für die VLAN-Namen, sowie nach einem ID-Bereich (Start- und End-VLAN-Tag).
   - Danach kannst du die Ports angeben, auf denen diese VLANs getagged laufen sollen.
   - Die VLANs werden erstellt und den angegebenen Ports zugewiesen.

6. **Abschlussmeldung:**
   - Das Skript gibt eine Meldung aus, dass die Konfiguration abgeschlossen ist.

## Beispielausgabe

Beispielhafter Ablauf der Ausführung:

```
Wie soll das Gerät benannt werden?
MeinSwitch
Soll das Gerät wirklich MeinSwitch genannt werden? (j/N) j
Los geht's! (press any Knopf)
Alle Ports wurden deaktiviert! (press any Knopf)
Default VLAN wurde von allen Ports entfernt! (press any Knopf)
Telnet wurde deaktiviert! (press any Knopf)
STP wurde deaktiviert! (press any Knopf)
SSH wurde aktiviert! (press any Knopf)
Mit welchem Namen sollen die VLANs beginnen? VLAN
Welches Tag soll dem ersten VLAN zugewiesen werden? 100
Welches Tag soll dem letzten VLAN zugewiesen werden? 105
Auf welche Ports sollen diese VLANs getagged laufen? 1-48
Erzeuge VLANs von  VLAN0100 bis VLAN0105
Fertig!! Zu Ihren Diensten, h0nigd4chs! (press any Knopf)
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe die [LICENSE](LICENSE)-Datei für Details.

---

**Hinweis:** Dieses Skript wurde für die Verwendung auf ExtremeXOS-Switches entwickelt. Stelle sicher, dass dein Gerät mit EXOS kompatibel ist, bevor du das Skript ausführst.
