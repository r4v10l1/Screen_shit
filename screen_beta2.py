import os, time

###############################
operative_system = "win"      #
trigger = True                #
###############################

if operative_system == "win":
    clear_command = "cls"
elif operative_system == "lin":
    clear_command = "cls"
else:
    print()
    print("Operative system error.")
    print()

#-----------------------------------------------------------------------------
# Default face
def default_sleep():
    os.system(clear_command)
    print()
    print(" /oo+      /oo+                              +oo/      +oo+ ")
    print(" -NMM+    -MMM+                              +MMM-    +MMN: ")
    print("  /MMN.  `mMMs                                sMMm`  .NMM+  ")
    print("   oMMh  sMMh`                                 hMMs  hMMs   ")
    print("    yMM+:MMm`                                  `dMM:+MMh`   ")
    print("    `dMNmMN-                                    .NMmNMm`    ")
    print("     .mNNN:                                      :NNNN.     ")
    print("      ````      ###########################       ````      ")
    print("                ###########################                  ")
    print()

# Calling icon
def calling():
    os.system(clear_command)
    print()
    print("             -/oyhhddddhhyo/-            ")
    print("         -+ydhs+:-.````.-:+shdy+-        ")
    print("      `/ydy/.                ./ydy/`     ")
    print("     /hdo.         .++/:-``     .odh/    ")
    print("   `sds.           .++oshhyo-`    .sds`  ")
    print("  .hd+   `-+:`     `::-.`.:sdy:     +dh. ")
    print(" `yd+   :ydddh+`   -ssyhho- -sds`    +dy`")
    print(" /dy   odddddddh.  `..`.:sds. +dy`    yd/")
    print(" yd/  .dddddddhs.  :yhho. +dy` yd+    /dy")
    print(" dd-   +ddddd/`      `+dy  hd: /dy    -dd")
    print(" hd:    +dddd:        `/:  -/` `/-    :dh")
    print(" odo     :hddd/`        ``            odo")
    print(" .dd-     .sdddy/.    .shyo-         -dd.")
    print("  /dh.      :ydddhs+/+hddddds.      .hd/ ")
    print("   /dh:      `-ohdddddddddddd+     :hd/  ")
    print("    -yds.       `-+yddddddds-    .sdy-   ")
    print("     `/hds:`       `.:+os/.    :sdy/`    ")
    print("       `:shhs/-`            /shhs:`      ")
    print("         -+ydhs+:-.````.-:+shdy+-        ")
    print("            `-/oyhhddddhhyo/-`           ")
    print()

# Alarm
# ...

#-----------------------------------------------------------------------------
# Main program
def main():
    user_command = "sleeping"
    action = default_sleep()
    while True:
        if trigger:
            # Mostrar la cara (dependiendo del comando)
            action
            while True:
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    user_command = input(" > ")
                    # Help
                    if user_command == "help":
                        print()
                        print("   Commands:")
                        print("       Help           -  Show this help")
                        print("       Sleep          -  Default face")
                        print("       Call           -  Calling icon")
                        print("       Exit           -  Exit the script")
                        print("       Other command  -  Execute that command in the terminal")
                        print()
                        input("   Press enter to continue...")
                        action = default_sleep()
                        break

                    # Comandos custom
                    elif user_command == "sleep" or user_command == "sleeping":
                        action = default_sleep()
                        break
                    elif user_command == "call" or user_command == "calling":
                        action = calling()
                        break
                    elif user_command == "exit":
                        os.system(clear_command)
                        exit(1)

                    # Comando no custom
                    else:
                        print(" Custom command detected. Executing...")
                        time.sleep(0.5)
                        os.system(clear_command)
                        os.system(user_command)
                        exit(1)
        else:
            print()
            print("Main trigger is off.")
            print()
            exit(1)

if __name__ == "__main__":
    main()
