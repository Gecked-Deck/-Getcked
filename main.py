#In an attempt to keep things modular, I've tried to split things up into categories, you SHOULD be able to remove one of the categories below (Excluding the essential ones) and the program should still run fine
browsers=["Chrome", "Chromium", "ungoogled-chromium", "Brave", "Librewolf"]
launchers=["Heroic", "Bottles"]
emulators=["Yuzu", "Citra", "Xemu", "RPCS3", "PCSX2", "PPSSPP", "Duckstation", "Retroarch"]
tools=["Flatseal", "protonup-qt", ]
flathubNames = {"Chrome":"com.google.Chrome", "Chromium":"org.chromium.Chromium", "ungoogled-chromium":"com.github.Eloston.UngoogledChromium", "Brave":"com.brave.Browser", "Librewolf":"io.gitlab.librewolf-community", "Heroic":"com.heroicgameslauncher.hgl", "Bottles":"com.usebottles.bottles", "Yuzu":"org.yuzu_emu.yuzu", "Citra":"org.citra_emu.citra", "Xemu":"app.xemu.xemu", "RPCS3":"net.rpcs3.RPCS3", "PCSX2":"net.pcsx2.PCSX2", "PPSSPP":"org.ppsspp.PPSSPP", "Duckstation":"org.duckstation.DuckStation", "Retroarch":"org.libretro.RetroArch", "Flatseal":"com.github.tchx84.Flatseal", "protonup-qt":"net.davidotek.pupgui2"}
categories=[browsers, launchers, emulators, tools]
categoriesNames=["browsers", "launchers", "emulators", "tools"]
installList=[]
print("""Getcked - The Essential Steam Deck Package Script v0.1
Thanks to the folks who helped me out making this ♡
""")
userChoice = str()
#This cycles through each package in a category and questions a user on if they want it to be put in the install script or not.
def packageInstall(category, userChoice, installList):
  for x in range (0, len(category)):
    userChoice = input("---Do you want to install " + str(category[x]) + "? [y/N]: ")
    if userChoice == "y":
      installList.append(category[x])
  return installList
for x in range (0, len(categories)):
  print()
  categoryChoice = input("Do you want to install packages from the '" + str(categoriesNames[x]) + "' category? [y/N]: ")
  if categoryChoice == "y":
    packageInstall(categories[x], userChoice, installList)
scriptinstallList = []
for x in range (0, (len(installList))):
  scriptinstallList.append(flathubNames[installList[x]])
print (scriptinstallList)
packages = 'echo -e "Installing ' + str(installList[0]) + '..." && flatpak install flathub ' + str(scriptinstallList[0]) + ' > /dev/null -y'
for x in range (1, len(scriptinstallList)):
  packages = str(packages) + ' && echo -e "Installing ' + str(installList[x]) + '..." && flatpak install flathub ' + str(scriptinstallList[x]) + ' > /dev/null -y'
packages = str(packages) + ' && echo -e "Completed" && sleep 5'
print()
print(packages)
install = open("install.desktop", "w")
install.truncate(0)
install.close()
write = """#!/usr/bin/env xdg-open
    [Desktop Entry]
    Name=Install script
    Exec=""" + str(packages) + """
    Terminal=true
    Type=Application
    StartupNotify=false"""
install = open("install.desktop", "w")
install.write(write)
install.close()

packages = 'echo -e "Unnstalling ' + str(installList[0]) + '..." && flatpak uninstall ' + str(scriptinstallList[0]) + ' > /dev/null -y'
for x in range (1, len(scriptinstallList)):
  packages = str(packages) + ' && echo -e "Uninstalling ' + str(installList[x]) + '..." && flatpak uninstall ' + str(scriptinstallList[x]) + ' > /dev/null -y'
packages = str(packages) + ' && echo -e "Completed" && sleep 5'

install = open("uninstall.desktop", "w")
install.truncate(0)
install.close()
write = """#!/usr/bin/env xdg-open
    [Desktop Entry]
    Name=Uninstall script
    Exec=""" + str(packages) + """
    Terminal=true
    Type=Application
    StartupNotify=false"""
install = open("uninstall.desktop", "w")
install.write(write)
install.close()