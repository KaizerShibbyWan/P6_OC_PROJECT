# coding: utf-8
# 
#  "secure_os.py" regroupe les différents modules du projet et permet l'appel de leurs fonctions.
#  le fichier de configuration "config.yaml" est nécessaire lors du lancement du programme.
#  Pour lancer le programme, utilisez la commande suivante "python secure_os.py config.yaml" 
#  Programme sous license Apache Software Foundation (ASF), vous pouvez obtenir une copie de la license à l'adresse suivante:
#  https://www.apache.org/licenses/LICENSE-2.0.txt
#  Le programme se compose de 8 modules prenant en charge l'installation et la configuration des logiciels suivants :
#  fail2ban_openssh_cron-apt_logwatch_rkhunter_user_create_ipconfig_
#  Le module readyamfile permet la lecture du fichier de configuration "config.yaml"
#
import readyamlfile, ipconfig, cron_apt, openssh, sshkey, fail2ban, logwatch, user_create, rkhunter
import sys
import os

conf = sys.argv[1] 
vars = readyamlfile.read_conf(conf)


ipconfig.set_ipconfig(vars["network"])
ipconfig.hostname(vars["network"])
user_create.admin_create(vars["account"])
openssh.openssh_install(vars["sshd"])
cron_apt.cron_apt_config(vars["cron_apt"])
fail2ban.fail2ban_jail(vars["fail2ban_jail"])
fail2ban.fail2ban_default(vars["fail2ban_default"])
logwatch.logwatch_install(vars["logwatch"])
rkhunter.rkhunter_install(vars["rkhunter"])
