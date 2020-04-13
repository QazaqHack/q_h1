import os

def menu():

    print(""" 
 _   _            _    _
| | | | __ _  ___| | _(_)_ __   __ _
| |_| |/ _` |/ __| |/ / | '_ \ / _` |
|  _  | (_| | (__|   <| | | | | (_| |
|_| |_|\__,_|\___|_|\_\_|_| |_|\__, |
                               |___/

========================================
Скриптті шығарған Benjamin Engel
Версия 2.0
----
Қазақстан хакерлері!
----
Бұл скриптте тек 2 команда бар: 00-барлығын қондыру; 99-шығу.
==========================================
00. Бәрін қондыру
------------------------------------------
 |   Infinite-Bomber
 |
 |   Impulse
 |
 |   cloud-killer
 |
 |   hakddos
 |
 |   LITEDDOS
 |
 |   Virus-droid-creator
 |
 |   Nmap
 |
 |   xerxes
 |
 |   ngrok
 |
 |   saydog-framework 
 |                                                        
 |   Termux-Banner        
 |                                           
 |   termux-style
 |
 |   termux-tasker
 |
 |   Termux-Lazyscript
 |
 |   DDos-Attack
------------------------------------------
99. Шығу
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("Қондырылатын болады: Infinite-Bomber,Impulse,cloud-killer,hakddos,LITEDDOS,Virus-droid-creator,Nmap,Xerxes,ngrok,saydog-framework,Termux-Banner,termux-style,termux-tasker,Termux-Lazyscript,DDos-Attack.")
        print("----------------")
        hm = input("[?] Жалғастырайын ба? (y/n): ")
        print("================================")
        if hm == "y":
            print("========================================================")
            print("[+] Күтуіңізге тура келеді...")
            print("[+] Өткені уақыт алады...")
            print("========================================================")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Argisht44/android.git")
            os.system("cd /data/data/com.termux/files/home && cd android && ls && cd Infinite-Bomber-a64-without-tor && ls && chmod 777 infinite-bomber")
            os.system("cd /data/data/com.termux/files/home")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/white-hackers/hakddos.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/4L13199/LITEDDOS.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/FDX100/cloud-killer.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/saydog/Virus-droid-creator.git")
            os.system("pkg install Nmap")
            os.system("git clone https://github.com/sepehrdaddev/Xerxes.git")
            os.system("git clone https://github.com/inconshreveable/ngrok.git")
            os.system("git clone https://github.com/saydog/saydog-framework.git")
            os.system("git clone https://github.com/Bhai4You/Termux-Banner.git")
            os.system("git clone https://github.com/adi1090x/termux-style.git")
            os.system("git clone https://github.com/termux/termux-tasker.git")
            os.system("git clone https://github.com/TechnicalMujeeb/Termux-Lazyscript.git")
            os.system("git clone https://github.com/Ha3MrX/DDos-Attack.git")
            os.system("clear")
            print("========================================")
            print("[+] Барлығы қондырылды :)")
            print("[+] Сәттілік :)")
