import pexpect 
import exsh
import sys 
dName = raw_input('Wie soll das Geraet benannt werden?\n') 
answer = raw_input('Soll das Geraet wirklich '+dName+' genannt werden? (j/N) ') 
if answer == 'j': 
    exsh.clicmd('configure snmp sysName '+dName, True) 
else: 
    print 'Vorgang abgebrochen' 
answer = raw_input("Los geht's! (press any Knopf) ") 
exsh.clicmd('disable ports all', True) 
answer = raw_input('Alle Ports wurden deaktiviert! (press any Knopf) ') 
exsh.clicmd('conf vlan Default dele por all', True) 
answer = raw_input('Default VLAN wurde von allen Ports entfernt! (press any Knopf) ') 
exsh.clicmd('disable telnet', True) 
answer = raw_input('Telnet wurde deaktiviert! (press any Knopf) ') 
exsh.clicmd('disable stp', True) 
answer = raw_input('STP wurde deaktiviert! (press any Knopf) ') 
exsh.clicmd('enable ssh', True) 
answer = raw_input('SSH wurde aktiviert! (press any Knopf) ')
while True:     
    prefix = raw_input('Mit welchem Namen sollen die VLANs beginnen:')     
    if len(prefix):         
        break 

while True:     
    reply = raw_input('Welches Tag soll dem ersten VLAN zugewiesen werden:')     
    if reply.isdigit():         
        minTag = int(reply)         
        break 

while True:     
   reply = raw_input('Welches Tag soll dem letzten VLAN zugewiesen werden:')     
   if reply.isdigit():         
       maxTag = int(reply)         
       break 

if minTag > maxTag:     
    print 'Die erste VLAN ID kann nicht kleiner als die letzte VLAN ID sein!'     
    sys.exit(-1) 

while True:     
    portlist = raw_input('Auf welche Ports sollen diese VLANs getagged laufen?:')     
    if len(portlist):         
        break 

print 'Erzeuge VLANs von ',prefix+str(minTag),'bis',prefix+str(maxTag) 

for vlanId in range(minTag,maxTag + 1):     
    vlanName = prefix + '{0:>04d}'.format(vlanId)     
    cmd = 'create vlan '+vlanName + ' tag ' + str(vlanId)     
    print exsh.clicmd(cmd, True)     
    cmd = 'config vlan ' + vlanName + ' add port ' + portlist + ' tag'     
    print exsh.clicmd(cmd, True) 
answer = raw_input('Fertig!! Zu Ihren Diensten, h0nigd4chs! (press any Knopf) ') 
