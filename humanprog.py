import pyttsx3
import os

pyttsx3.speak("Welcome to my tools")
print("I will open the following tools for you.\n")
pyttsx3.speak("I will open the following tools for you.")


print("\n1.Google Chrome\t\t 2.Notepad\t\t 3.Media Player\t\t 4.Node\t\t 5.Calculator\n")

print("6.Microsoft Powerpoint\t 7.Microsoft Excel\t 8.Clock\t 9.Calender\t 10.Images\n")

print("11.Regional Setting\t 12.Mouse Properties\t 13.Sound Properties\t 14.Network Connections\n\n15.Power Plan Configuration\n")

print("16.Realtek Audio Manager\t\t 17.System Properties and change the computer name\n\n18.Location Information and telephone configuration\n\n19.Time and Date,Additional Clocks,Internet Time Configurations\t\t 20.Action Center\n")

print("21.User Account Management\t\t 22.Windows Update\t\t 23.Task Scheduler\t\t 24.Printers\n\n25.Default Programs\n")

print("26.Credential Manager\t\t 27.Color Management\t\t 28.Autoplay\t\t 29.Bit Locker Drive Encryption\n\n30.Administrative Tools\n\n")

print("31.Add Remove Programs\t 32.Screen Resolution\t 33.Change Windows Firewall\t 34.Device Manager\n\n35.Internet Properties\n")

print("Tell me which tool you want:")
pyttsx3.speak("Tell me which tool you want:")

while True:
    print("chat with me with your requirements : ",end=' ' )
    p=input()
    if (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("chrome" in p) or ("web browser" in p) or ("browser" in p)):
          os.system("chrome")
          print("You requested for Google Chrome.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("notepad" in p) or ("editor" in p)):
          os.system("notepad")
          print("You requested for Notepad.")

    elif (("run" in p) or ("open" in p) or ("launch" in p)  or ("execute" in p) or ("play" in p))and (("media" in p) or ("player" in p)):
          os.system("wmplayer")
          print("You requested for Media Player.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("node" in p) or ("nodejs" in p)):
          os.system("node")
          print("You requested for NodeJs.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("calc" in p) or ("calculator" in p)):
          os.system("calc")
          print("You requested for Calculator.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("mspowerpoint" in p) or ("powerpoint" in p)  or ("powerpnt" in p)
    or ("ppt" in p)):
          os.system("start powerpnt")
          print("You requested for Microsoft Powerpoint.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("msexcel" in p) or ("excel" in p)):
          os.system("start excel")
          print("You requested for Microsoft Excel.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p) or ("set" in p)) and (("clock" in p) or ("timer" in p) or     ("stopwatch" in p) or ("alarm" in p)):
          os.system("ms-clock:")
          print("You requested for Clock.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("calender" in p) or ("calen" in p) or     ("month" in p) or ("year" in p) or ("day" in p)):
          os.system("start outlookcal:")
          print("You requested for Calender.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("images" in p) or ("image" in p) or ("pictures" in p) or    ("picture" in p) or ("pics" in p) or ("pic" in p) or ("img" in p) or  ("photo" in p)):
          os.system("start ois")
          print("You requested for Images.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("regional" in p) or ("region" in p) or ("language" in p)):
          os.system("Intl.CPL")
          print("You requested for Region and Language Setting.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("mouse" in p) or ("pointer" in p)):
          os.system("Main.cpl")
          print("You requested for Mouse Properties.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("sound" in p) or ("voice" in p)):
          os.system("mmsys.CPL")
          print("You requested for Sound Properties.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("network" in p) or ("signal" in p)):
          os.system("ncpa.CPL")
          print("You requested for Network Connections.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("power" in p) or ("power plan" in p)):
          os.system("powercfg.CPL")
          print("You requested for Power Plan Configuration.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("play" in p)) and (("audio" in p) or ("audio manager" in p) or ("realtek             audio manager"     in p)):
          os.system("RTSnMg64.CPL")
          print("You requested for Realtek Audio Manager.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("system computer" in p) or ("system" in p)):
          os.system("sysdm.CPL")
          print("You requested for System Computer.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("telephone configure" in p) or ("telephone configuration" in p)):
          os.system("Telephon.CPL")
          print("You requested for Telephone Configuration.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("date" in p) or ("time" in p)):
          os.system("TimeDate.cpl")
          print("You requested for Date and Time.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("action center" in p) or ("action" in p)):
          os.system("Wscui.cpl")
          print("You requested for Action Center.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("user password" in p) or ("user account" in p)):
          os.system("control userpasswords")
          print("You requested for User Account.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("windows update" in p) or ("update windows" in p)):
          os.system("control /name Microsoft.WindowsUpdate")  
          print("You requested for Windows Update.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("task schedule" in p) or ("task scheduler" in p)):
          os.system("control schedtasks")
          print("You requested for Task Schedular.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("printer" in p) or ("printers" in p)):
          os.system("control printers")
          print("You requested for Printer.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("default" in p) or ("default programs" in p)):
          os.system("control /name Microsoft.DefaultPrograms")
          print("You requested for Default Programs.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("credential" in p) or ("credential manager" in p)):
          os.system("control /name Microsoft.CredentialManager")
          print("You requested for Credential Manager.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("color manager" in p) or ("color management" in p) or     ("color" in p)):
          os.system("control /name Microsoft.ColorManagement")
          print("You requested for Color Management.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("autoplay" in p) or ("auto" in p)):
          os.system("control /name Microsoft.AutoPlay")
          print("You requested for Autoplay.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("bitlockerdriveencryption" in p) or ("bit locker drive encryption" in p)       or ("bit locker drive" in p) or ("bit locker" in p)):
          os.system("control /name Microsoft.BitLockerDriveEncryption")
          print("You requested for Bit Locker Drive Encryption.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("admin tools" in p) or ("administrative tools" in p) or ("admin" in p) or       ("administrative" in p)):
          os.system("control admintools")
          print("You requested for Administrative Tools.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("add" in p) or ("remove" in p) or ("uninstall" in p) or ("change" in p)):
          os.system("Appwiz.cpl")
          print("You requested for Uninstall or Change a Program.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("screen" in p) or ("resolution" in p)):
          os.system("DESK.cpl")
          print("You requested for Screen Resolution.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("firewall" in p) or ("firewall setting" in p)):
          os.system("Firewall.cpl")
          print("You requested for Firewall Setting.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p)) and (("device" in p) or ("device manager" in p)):
          os.system("HdwWiz.cpl")
          print("You requested for Device Manager.")

    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch" in p) or ("show" in p)) and (("net" in p) or ("internet" in p)):
          os.system("Inetcpl.CPL")
          print("You requested for Internet Properties.")
    
    elif ("exit" in p) or ("quit" in p) or ("cancel" in p) or ("terminate" in p):
          break
    else:
          print("Sorry, seems like your desired application is not available. Thank You :)")
          pyttsx3.speak("Sorry, seems like your desired application is not available. Thank You :( ")