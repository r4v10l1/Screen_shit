import os, time

operative_system = "win"
trigger = True

if operative_system == "win":
    clear_command = "cls"
elif operative_system == "lin":
    clear_command = "cls"
else:
    print("\nOperative system error.\n")

#-----------------------------------------------------------------------------
# Default face
def default_sleep():
    os.system(clear_command)
    print()
    print("█    █        █    █")
    print(" █  █          █  █ ")
    print("  ██            ██  ")
    print("      ████████      ")
    print()

# Calling icon
def calling():
    os.system(clear_command)
    print("           `-/oyhhddddhhyo/-`           ")
    print("        -+ydhs+:-.````.-:+shdy+-        ")
    print("     `/ydy/.                ./ydy/`     ")
    print("    /hdo.         .++/:-``     .odh/    ")
    print("  `sds.           .++oshhyo-`    .sds`  ")
    print(" .hd+   `-+:`     `::-.`.:sdy:     +dh. ")
    print("`yd+   :ydddh+`   -ssyhho- -sds`    +dy`")
    print("/dy  `odddddddh.  `..`.:sds. +dy`    yd/")
    print("yd/  .dddddddhs.  :yhho. +dy` yd+    /dy")
    print("dd-   +ddddd/`      `+dy  hd: /dy    -dd")
    print("hd:    +dddd:        `/:  -/` `/-    :dh")
    print("odo     :hddd/`        ``            odo")
    print(".dd-     .sdddy/.    .shyo-         -dd.")
    print(" /dh.      :ydddhs+/+hddddds.      .hd/ ")
    print("  /dh:      `-ohdddddddddddd+     :hd/  ")
    print("    `/hds:`       `.:+os/.   `:sdy/`    ")
    print("   -yds.       `-+yddddddds-    .sdy-   ")
    print("      `:shhs/-`          `-/shhs:`      ")
    print("         `-+shdhyssoossyhdhs+-`         ")
    print()

# Alarm
# ...

#-----------------------------------------------------------------------------
# Main program
action = default_sleep()
try:
    while True:
        if trigger:
            action
            while True:
                # Cosas que checkear
                if user_command == ("call" or "calling"):
                    action = calling()
                    break
                else:
                    exit(1)
                # Si no cambia nada
                time.sleep(1)
        else:
            print("\nMain trigger is off.\n")
            exit(1)

except KeyboardInterrupt:
    user_command = input(" > ")
    if user_command == ("fortune" or "surprise"):
        os.system(clear_command)
        os.system("fortune")
        exit(1)
    else:
        print(" That is not a command!")
