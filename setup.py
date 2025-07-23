import os


def repconf():
    files = [
        ".config/hypr/",
        ".config/rofi/",
        ".config/waybar/",
        ".config/qt5ct/",
        ".config/qt6ct/",
        ".config/waybar/.config/nvim/",
    ]
    for file in files:
        file = f"$HOME/{file}"
        os.remove(file)
    print("Deleting old config files completed !\n")
    print("Now copying new config files\n")
    os.system("cp .config .local $HOME/")
    os.system("cp Wallpaper $HOME/Pictures/")
    print("Finished !\nexiting .....")
    exit()


print(
    "This script is going to delete and replace your old config files for the following things :\n>hyprland\n>kitty\n>qt6ct\n>qt6ct\n>rofi\n>waybar\n>neovim"
)
yn = input("Are you sure you want to continue (y/n) : ")
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
