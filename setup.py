import os


def repconf():
    print("Copying new config files\n")
    os.system("cp -r .config .local $HOME/")
    os.system("cp -r Wallpapers $HOME/Pictures/")
    print("Finished !\nexiting .....")
    exit()


print(
    "This script is going to replace your old config files for the following things :\n>hyprland\n>kitty\n>qt6ct\n>qt6ct\n>rofi\n>waybar\n>neovim"
)
yes = ["y", "Y", "yes", ""]
no = ["n", "N", "no"]

while True:
    yn = input("Are you sure you want to continue (y/n) : ")
    if yn in yes:
        print("Starting ....")
        repconf()
    elif yn in no:
        print("Exiting ...")
        break
    else:
        print("Error : invalid option")
    exit()
