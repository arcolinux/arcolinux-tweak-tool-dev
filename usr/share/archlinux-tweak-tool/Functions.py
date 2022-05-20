# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

import os
import distro
import sys
import shutil
import psutil
import datetime
# import time
import subprocess
import threading  # noqa
import gi
# import configparser
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk  # noqa

distr = distro.id()

sudo_username = os.getlogin()
home = "/home/" + str(sudo_username)

gpg_conf = "/etc/pacman.d/gnupg/gpg.conf"
gpg_conf_local = home + "/.gnupg/gpg.conf"

gpg_conf_original = "/usr/share/archlinux-tweak-tool/data/any/gpg.conf"
gpg_conf_local_original = "/usr/share/archlinux-tweak-tool/data/any/gpg.conf"

sddm_default = "/etc/sddm.conf"
sddm_default_original = "/usr/share/archlinux-tweak-tool/data/arco/sddm/sddm.conf"

sddm_default_d1 = "/etc/sddm.conf"
sddm_default_d2 = "/etc/sddm.conf.d/kde_settings.conf"
sddm_default_d2_dir = "/etc/sddm.conf.d/"
sddm_default_d_sddm_original_1 = "/usr/share/archlinux-tweak-tool/data/arco/sddm/sddm.conf"
sddm_default_d_sddm_original_2 = "/usr/share/archlinux-tweak-tool/data/arco/sddm.conf.d/kde_settings.conf"

if os.path.exists("/etc/sddm.conf.d/kde_settings.conf"):
    sddm_conf = "/etc/sddm.conf.d/kde_settings.conf"
else:
    sddm_conf = "/etc/sddm.conf"

arcolinux_mirrorlist = "/etc/pacman.d/arcolinux-mirrorlist"
arcolinux_mirrorlist_original = "/usr/share/archlinux-tweak-tool/data/arco/arcolinux-mirrorlist"
pacman = "/etc/pacman.conf"
pacman_arch = "/usr/share/archlinux-tweak-tool/data/arch/pacman/pacman.conf"
pacman_arco = "/usr/share/archlinux-tweak-tool/data/arco/pacman/pacman.conf"
pacman_eos = "/usr/share/archlinux-tweak-tool/data/eos/pacman/pacman.conf"
pacman_garuda = "/usr/share/archlinux-tweak-tool/data/garuda/pacman/pacman.conf"
blank_pacman_arch = "/usr/share/archlinux-tweak-tool/data/arch/pacman/blank/pacman.conf"
blank_pacman_arco = "/usr/share/archlinux-tweak-tool/data/arco/pacman/blank/pacman.conf"
blank_pacman_eos = "/usr/share/archlinux-tweak-tool/data/eos/pacman/blank/pacman.conf"
blank_pacman_garuda = "/usr/share/archlinux-tweak-tool/data/garuda/pacman/blank/pacman.conf"
neofetch_arco = "/usr/share/archlinux-tweak-tool/data/arco/neofetch/config.conf"
alacritty_arco = "/usr/share/archlinux-tweak-tool/data/arco/alacritty/alacritty.yml"
oblogout_conf = "/etc/oblogout.conf"
# oblogout_conf = home + "/oblogout.conf"
gtk3_settings = home + "/.config/gtk-3.0/settings.ini"
gtk2_settings = home + "/.gtkrc-2.0"
grub_theme_conf = "/boot/grub/themes/Vimix/theme.txt"
grub_default_grub = "/etc/default/grub"
xfce_config = home + "/.config/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml"
xfce4_terminal_config = home + "/.config/xfce4/terminal/terminalrc"
alacritty_config = home + "/.config/alacritty/alacritty.yml"
alacritty_config_dir = home + "/.config/alacritty"
slimlock_conf = "/etc/slim.conf"
termite_config = home + "/.config/termite/config"
neofetch_config = home + "/.config/neofetch/config.conf"
lightdm_conf = "/etc/lightdm/lightdm.conf"
bd = ".att_backups"
config = home + "/.config/archlinux-tweak-tool/settings.ini"
config_dir = home + "/.config/archlinux-tweak-tool/"
polybar = home + "/.config/polybar/"
desktop = ""
autostart = home + "/.config/autostart/"

bash_config = ""
zsh_config = ""
fish_config = ""

if os.path.isfile(home + "/.config/fish/config.fish"):
    fish_config = home + "/.config/fish/config.fish"
if os.path.isfile(home + "/.zshrc"):
    zsh_config = home + "/.zshrc"
if os.path.isfile(home + "/.bashrc"):
    bash_config = home + "/.bashrc"

zshrc_arco = "/usr/share/archlinux-tweak-tool/data/arco/.zshrc"
account_list = ["Standard","Administrator"]
i3wm_config = home + "/.config/i3/config"
awesome_config = home + "/.config/awesome/rc.lua"
qtile_config = home + "/.config/qtile/config.py"

seedhostmirror = "Server = https://ant.seedhost.eu/arcolinux/$repo/$arch"
aarnetmirror = "Server = https://mirror.aarnet.edu.au/pub/arcolinux/$repo/$arch"

atestrepo = "[arcolinux_repo_testing]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/arcolinux-mirrorlist"

arepo = "[arcolinux_repo]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/arcolinux-mirrorlist"

a3drepo = "[arcolinux_repo_3party]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/arcolinux-mirrorlist"

axlrepo = "[arcolinux_repo_xlarge]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/arcolinux-mirrorlist"

chaotics_repo = "[chaotic-aur]\n\
SigLevel = Required DatabaseOptional\n\
Include = /etc/pacman.d/chaotic-mirrorlist"

endeavouros_repo = "[endeavouros]\n\
SigLevel = PackageRequired\n\
Include = /etc/pacman.d/endeavouros-mirrorlist"

nemesis_repo = "[nemesis_repo]\n\
SigLevel = Optional TrustedOnly\n\
Server = https://erikdubois.github.io/$repo/$arch"

arch_testing_repo = "[testing]\n\
Include = /etc/pacman.d/mirrorlist"

arch_core_repo = "[core]\n\
Include = /etc/pacman.d/mirrorlist"

arch_extra_repo = "[extra]\n\
Include = /etc/pacman.d/mirrorlist"

arch_community_testing_repo = "[community-testing]\n\
Include = /etc/pacman.d/mirrorlist"

arch_community_repo = "[community]\n\
Include = /etc/pacman.d/mirrorlist"

arch_multilib_testing_repo = "[multilib-testing]\n\
Include = /etc/pacman.d/mirrorlist"

arch_multilib_repo = "[multilib]\n\
Include = /etc/pacman.d/mirrorlist"

# =====================================================
#               Create log file
# =====================================================

log_dir="/var/log/archlinux/"
att_log_dir="/var/log/archlinux/att/"

def create_log(self):
    print('Making log in /var/log/archlinux')
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d-%H-%M-%S" )
    destination = att_log_dir + 'att-log-' + time
    command = 'sudo pacman -Q > ' + destination
    subprocess.call(command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT)
    #GLib.idle_add(show_in_app_notification, self, "Log file created")

# =====================================================
#               NOTIFICATIONS
# =====================================================

def show_in_app_notification(self, message):
    if self.timeout_id is not None:
        GLib.source_remove(self.timeout_id)
        self.timeout_id = None

    self.notification_label.set_markup("<span foreground=\"white\">" +
                                       message + "</span>")
    self.notification_revealer.set_reveal_child(True)
    self.timeout_id = GLib.timeout_add(3000, timeOut, self)


def timeOut(self):
    close_in_app_notification(self)


def close_in_app_notification(self):
    self.notification_revealer.set_reveal_child(False)
    GLib.source_remove(self.timeout_id)
    self.timeout_id = None

# =====================================================
#               PERMISSIONS
# =====================================================


def test(dst):
    for root, dirs, filesr in os.walk(dst):
        # print(root)
        for folder in dirs:
            pass
            # print(dst + "/" + folder)
            for file in filesr:
                pass
                # print(dst + "/" + folder + "/" + file)
        for file in filesr:
            pass
            # print(dst + "/" + file)


def permissions(dst):
    try:
        # original_umask = os.umask(0)
        # calls = subprocess.run(["sh", "-c", "cat /etc/passwd | grep " +
        #                         sudo_username],
        #                        shell=False,
        #                        stdout=subprocess.PIPE,
        #                        stderr=subprocess.STDOUT)
        groups = subprocess.run(["sh", "-c", "id " +
                                 sudo_username],
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        for x in groups.stdout.decode().split(" "):
            if "gid" in x:
                g = x.split("(")[1]
                group = g.replace(")", "").strip()
        # print(group)
        # name = calls.stdout.decode().split(":")[0].strip()
        # group = calls.stdout.decode().split(":")[4].strip()

        subprocess.call(["chown", "-R",
                         sudo_username + ":" + group, dst], shell=False)

    except Exception as e:
        print(e)

# =====================================================
#               COPY FUNCTION
# =====================================================

def copy_func(src, dst, isdir=False):
    if isdir:
        subprocess.run(["cp", "-Rp", src, dst], shell=False)
    else:
        subprocess.run(["cp", "-p", src, dst], shell=False)
    # permissions(dst)

# =====================================================
#               SOURCE
# =====================================================


def source_shell(self):
    process = subprocess.run(["sh", "-c", "echo \"$SHELL\""],
                             stdout=subprocess.PIPE)

    output = process.stdout.decode().strip()
    print(output)
    if output == "/bin/bash":
        subprocess.run(["bash", "-c", "su - " + sudo_username +
                        " -c \"source " + home + "/.bashrc\""],
                       stdout=subprocess.PIPE)
    elif output == "/bin/zsh":
        subprocess.run(["zsh", "-c", "su - " + sudo_username +
                        " -c \"source " + home + "/.zshrc\""],
                       stdout=subprocess.PIPE)
    elif output == "/usr/bin/fish":
        subprocess.run(["fish", "-c", "su - " + sudo_username +
                        " -c \"source " + home + "/.config/fish/config.fish\""],
                       stdout=subprocess.PIPE)

def get_shell():
    process = subprocess.run(["su", "-", sudo_username,"-c","echo \"$SHELL\""],
                             #shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)

    output = process.stdout.decode().strip().strip('\n')
    if output == "/bin/bash" or output == "/usr/bin/bash":
        return "bash"
    elif output == "/bin/zsh" or output == "/usr/bin/zsh":
        return "zsh"
    elif output == "/bin/fish" or output == "/usr/bin/fish":
        return "fish"

def run_as_user(script):
    subprocess.call(["su - " + sudo_username + " -c " + script], shell=False)

# =====================================================
#               MESSAGEBOX
# =====================================================


def MessageBox(self, title, message):
    md2 = Gtk.MessageDialog(parent=self,
                            flags=0,
                            message_type=Gtk.MessageType.INFO,
                            buttons=Gtk.ButtonsType.OK,
                            text=title)
    md2.format_secondary_markup(message)
    md2.run()
    md2.destroy()

# =====================================================
#               CONVERT COLOR
# =====================================================


def rgb_to_hex(rgb):
    if "rgb" in rgb:
        rgb = rgb.replace("rgb(", "").replace(")", "")
        vals = rgb.split(",")
        return "#{0:02x}{1:02x}{2:02x}".format(clamp(int(vals[0])),
                                               clamp(int(vals[1])),
                                               clamp(int(vals[2])))
    return rgb


def clamp(x):
    return max(0, min(x, 255))


# =====================================================
#               GLOBAL FUNCTIONS
# =====================================================


def _get_position(lists, value):
    data = [string for string in lists if value in string]
    position = lists.index(data[0])
    return position

def _get_positions(lists, value):
    data = [string for string in lists if value in string]
    position = []
    for d in data:
        position.append(lists.index(d))
    return position

def _get_variable(lists, value):
    data = [string for string in lists if value in string]

    if len(data) >= 1:

        data1 = [string for string in data if "#" in string]

        for i in data1:
            if i[:4].find('#') != -1:
                data.remove(i)
    if data:
        data_clean = [data[0].strip('\n').replace(" ", "")][0].split("=")
    return data_clean

# Check  value exists


def check_value(list, value):
    data = [string for string in list if value in string]
    if len(data) >= 1:
        data1 = [string for string in data if "#" in string]
        for i in data1:
            if i[:4].find('#') != -1:
                data.remove(i)
    return data


def check_backups(now):
    if not os.path.exists(home + "/" + bd + "/Backup-" +
                          now.strftime("%Y-%m-%d %H")):
        os.makedirs(home + "/" + bd + "/Backup-" +
                    now.strftime("%Y-%m-%d %H"), 0o777)
        permissions(home + "/" + bd + "/Backup-" + now.strftime("%Y-%m-%d %H"))

# =====================================================
#               Check if File Exists
# =====================================================


def file_check(file):
    if os.path.isfile(file):
        return True

    return False


def path_check(path):
    if os.path.isdir(path):
        return True

    return False

# =====================================================
#               GTK3 CONF
# =====================================================


def gtk_check_value(my_list, value):
    data = [string for string in my_list if value in string]
    if len(data) >= 1:
        data1 = [string for string in data if "#" in string]
        for i in data1:
            if i[:4].find('#') != -1:
                data.remove(i)
    return data


def gtk_get_position(my_list, value):
    data = [string for string in my_list if value in string]
    position = my_list.index(data[0])
    return position


# =====================================================
#               OBLOGOUT CONF
# =====================================================
# Get shortcuts index


def get_shortcuts(conflist):
    sortcuts = _get_variable(conflist, "shortcuts")
    shortcuts_index = _get_position(conflist, sortcuts[0])
    return int(shortcuts_index)

# Get commands index


def get_commands(conflist):
    commands = _get_variable(conflist, "commands")
    commands_index = _get_position(conflist, commands[0])
    return int(commands_index)

# =====================================================
#               LIGHTDM CONF
# =====================================================


def check_lightdm_value(list, value):
    data = [string for string in list if value in string]
    # if len(data) >= 1:
    #     data1 = [string for string in data if "#" in string]

    return data

# =====================================================
#               SDDM CONF
# =====================================================

def check_sddm_value(list, value):
    data = [string for string in list if value in string]
    return data

# =====================================================
#               HBLOCK CONF
# =====================================================

def hblock_get_state(self):
    lines = int(subprocess.check_output('wc -l /etc/hosts',
                                        shell=True).strip().split()[0])
    if os.path.exists("/usr/local/bin/hblock") and lines > 100:
        return True

    self.firstrun = False
    return False

def do_pulse(data, prog):
    prog.pulse()
    return True

def set_hblock(self, toggle, state):
    GLib.idle_add(toggle.set_sensitive, False)
    GLib.idle_add(self.label7.set_text, "Run..")
    GLib.idle_add(self.progress.set_fraction, 0.2)

    timeout_id = None
    timeout_id = GLib.timeout_add(100, do_pulse, None, self.progress)

    if not os.path.isfile("/etc/hosts.bak"):
            shutil.copy("/etc/hosts", "/etc/hosts.bak")

    try:

        install = 'pacman -S arcolinux-hblock-git --needed --noconfirm'
        enable = "/usr/local/bin/hblock"

        if state:
            if os.path.exists("/usr/local/bin/hblock"):
                GLib.idle_add(self.label7.set_text, "Database update...")
                subprocess.call([enable],
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
            else:
                GLib.idle_add(self.label7.set_text, "Install Hblock......")
                subprocess.call(install.split(" "),
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
                GLib.idle_add(self.label7.set_text, "Database update...")
                subprocess.call([enable],
                                shell=False,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)

        else:
            GLib.idle_add(self.label7.set_text, "Remove update...")
            subprocess.run(["sh", "-c",
                            "HBLOCK_SOURCES=\'\' /usr/local/bin/hblock"],
                           shell=False,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)

        GLib.idle_add(self.label7.set_text, "Complete")
        GLib.source_remove(timeout_id)
        timeout_id = None
        GLib.idle_add(self.progress.set_fraction, 0)

        GLib.idle_add(toggle.set_sensitive, True)
        if state:
            GLib.idle_add(self.label7.set_text, "HBlock Active")
        else:
            GLib.idle_add(self.label7.set_text, "HBlock Inactive")

    except Exception as e:
        MessageBox(self, "ERROR!!", str(e))
        print(e)

# =====================================================
#               UBLOCK ORIGIN
# =====================================================

def ublock_get_state(self):
    if os.path.exists("/usr/lib/firefox/browser/extensions/uBlock0@raymondhill.net.xpi"):
        return True
    return False

def set_firefox_ublock(self, toggle, state):
    GLib.idle_add(toggle.set_sensitive, False)
    GLib.idle_add(self.label7.set_text, "Run..")
    GLib.idle_add(self.progress.set_fraction, 0.2)

    timeout_id = None
    timeout_id = GLib.timeout_add(100, do_pulse, None, self.progress)

    try:

        install_ublock = "pacman -S firefox-ublock-origin --needed --noconfirm"
        uninstall_ublock = 'pacman -Rs firefox-ublock-origin --noconfirm'

        if state:
            GLib.idle_add(self.label7.set_text, "Installing ublock Origin...")
            subprocess.call(install_ublock.split(" "),
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
        else:
            GLib.idle_add(self.label7.set_text, "Removing ublock Origin...")
            subprocess.call(uninstall_ublock.split(" "),
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

        GLib.idle_add(self.label7.set_text, "Complete")
        GLib.source_remove(timeout_id)
        timeout_id = None
        GLib.idle_add(self.progress.set_fraction, 0)

        GLib.idle_add(toggle.set_sensitive, True)
        if state:
            GLib.idle_add(self.label7.set_text, "uBlock Origin installed")
        else:
            GLib.idle_add(self.label7.set_text, "uBlock Origin removed")

    except Exception as e:
        MessageBox(self, "ERROR!!", str(e))
        print(e)

# =====================================================
#               REFLECTOR
# =====================================================

def install_reflector(self):
    install = 'pacman -S reflector --needed --noconfirm'

    if os.path.exists("/usr/bin/reflector"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

# =====================================================
#               RATE-MIRRORS
# =====================================================

def install_rate_mirrors(self):
    install = 'pacman -S rate-mirrors --needed --noconfirm'

    if os.path.exists("/usr/bin/rate-mirrors"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

# =====================================================
#               ZSH + PACKAGES (ARCOLINUXD)
# =====================================================

def install_zsh(self):
    install = 'pacman -S zsh zsh-completions zsh-syntax-highlighting --needed --noconfirm'

    try:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Installing zsh zsh-completions zsh-syntax-highlighting if needed")
    except Exception as e:
        print(e)

# =====================================================
#               FISH + PACKAGES (ARCOLINUXD)
# =====================================================

def install_fish(self):
    install = 'pacman -S fish arcolinux-fish-git --needed --noconfirm'

    if os.path.exists("/usr/bin/fish") and os.path.exists("/etc/skel/.config/fish/config.fish") :
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

def remove_fish(self):
    install = 'pacman -Rs fish --noconfirm'

    if not os.path.exists("/usr/bin/fish") :
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

# =====================================================
#               ARCOLINUX-DESKTOP-TRASHER
# =====================================================

def install_adt(self):
    install = 'pacman -S arcolinux-desktop-trasher-git --noconfirm'

    if os.path.exists("/usr/local/bin/arcolinux-desktop-trasher"):
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

# =====================================================
#               GRUB CONF
# =====================================================


def get_grub_wallpapers():
    if os.path.isdir("/boot/grub/themes/Vimix"):
        lists = os.listdir("/boot/grub/themes/Vimix")

        rems = ['select_e.png', 'terminal_box_se.png', 'select_c.png',
                'terminal_box_c.png', 'terminal_box_s.png',
                'select_w.png', 'terminal_box_nw.png',
                'terminal_box_w.png', 'terminal_box_ne.png',
                'terminal_box_sw.png', 'terminal_box_n.png',
                'terminal_box_e.png']

        ext = ['.png', '.jpeg', '.jpg']

        new_list = [x for x in lists if x not in rems for y in ext if y in x]

        new_list.sort()
        return new_list


def set_grub_wallpaper(self, image):
    if os.path.isfile(grub_theme_conf):
        if not os.path.isfile(grub_theme_conf + ".bak"):
            shutil.copy(grub_theme_conf, grub_theme_conf + ".bak")
        try:
            with open(grub_theme_conf, "r") as f:
                lists = f.readlines()
                f.close()

            val = _get_position(lists, "desktop-image: ")
            lists[val] = "desktop-image: \"" + os.path.basename(image) + "\"" + "\n"

            with open(grub_theme_conf, "w") as f:
                f.writelines(lists)
                f.close()
            print("Grub wallpaper saved")
            show_in_app_notification(self, "Grub wallpaper saved")
            # MessageBox(self, "Success!!", "Settings Saved Successfully")
        except:  # noqa
            pass

def set_default_theme(self):
    if os.path.isfile(grub_default_grub):
        if not os.path.isfile(grub_default_grub + ".bak"):
            shutil.copy(grub_default_grub, grub_default_grub + ".bak")
        try:
            with open(grub_default_grub, "r") as f:
                grubd = f.readlines()
                f.close()

            if distro.id() == "arch":
                try:
                    val = _get_position(grubd, '#GRUB_THEME="/path/to/gfxtheme"')
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                    pass

            if distro.id() == "arch":
                try:
                    # for Carli
                    val = _get_position(grubd, 'GRUB_THEME=/usr/share/grub/themes/poly-dark/theme.txt')
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                    pass

            if distro.id() == "arcolinux":
                try:
                    val = _get_position(grubd, "#GRUB_THEME")
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                    pass

            if distro.id() == "endeavouros":
                try:
                    val = _get_position(grubd, "GRUB_THEME=/boot/grub/themes/EndeavourOS/theme.txt")
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                    pass

            if distro.id() == "garuda":
                try:
                    val = _get_position(grubd, 'GRUB_THEME="/usr/share/grub/themes/garuda/theme.txt"')
                    grubd[val] = 'GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"\n'
                except IndexError:
                   pass

            with open(grub_default_grub, "w") as f:
                f.writelines(grubd)
                f.close()

            print("Settings saved successfully in /etc/default/grub")
            print("We made sure you have a backup - /etc/default/grub.bak")
            print("This line has changed in /etc/default/grub")
            print('GRUB_THEME="/boot/grub/themes/Vimix/theme.txt"')

            show_in_app_notification(self, "Settings Saved Successfully in /etc/default/grub")
        except Exception as e:
            print(e)

# =====================================================
#               NEOFETCH CONF
# =====================================================

def neofetch_set_value(lists, pos, text, state):
    if state:
        if text in lists[pos]:
            if "#" in lists[pos]:
                lists[pos] = lists[pos].replace("#", "")
    else:
        if text in lists[pos]:
            if "#" not in lists[pos]:
                lists[pos] = "#" + lists[pos]

    return lists


def neofetch_set_backend_value(lists, pos, text, value):
    if text in lists[pos] and "#" not in lists[pos]:
        lists[pos] = text + value + "\"\n"

# ====================================================================
#                      GET DESKTOP
# ====================================================================

def get_desktop(self):
    base_dir = os.path.dirname(os.path.realpath(__file__))

    desktop = subprocess.run(["sh", base_dir + "/get_desktop.sh", "-n"],
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
    dsk = desktop.stdout.decode().strip().split("\n")
    self.desktop = dsk[-1].strip()

# =====================================================
#               COPYTREE
# =====================================================

def copytree(self, src, dst, symlinks=False, ignore=None):  # noqa

    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.exists(d):
            try:
                shutil.rmtree(d)
            except Exception as e:
                print(e)
                os.unlink(d)
        if os.path.isdir(s):
            try:
                shutil.copytree(s, d, symlinks, ignore)
            except Exception as e:
                print(e)
                print("ERROR2")
                self.ecode = 1
        else:
            try:
                shutil.copy2(s, d)
            except:  # noqa
                print("ERROR3")
                self.ecode = 1

# =====================================================
#               CHECK RUNNING PROCESS
# =====================================================

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            if processName == pinfo['pid']:
                return True
        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass
    return False

# =====================================================
#               RESTART PROGRAM
# =====================================================

def restart_program():
    os.unlink("/tmp/att.lock")
    python = sys.executable
    os.execl(python, python, *sys.argv)

# =====================================================
#               CHECK VALUE true / false
# =====================================================

def check_content(value, file):         # noqa
    with open(file, "r") as myfile:
        lines = myfile.readlines()
        myfile.close()

    for line in lines:
        if value in line:
            if value in line:
                return True
            else:
                return False
    return False

# =====================================================
#               DISTRO LABEL
# =====================================================

def change_distro_label(name):      # noqa
    if name == "arcolinux":
        name = "ArcoLinux"
    if name == "garuda":
        name = "Garuda"
    if name == "endeavouros":
        name = "EndeavourOS"
    if name == "arch":
        name = "Arch Linux"
    return name

# =====================================================
#               ALACRITTY
# =====================================================

def install_alacritty(self):
    install = 'pacman -S alacritty --needed --noconfirm'

    if os.path.exists("/usr/bin/alacritty"):
        #print("Alacritty is already installed")
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Alacritty is now installed")

# =====================================================
#               ALACRITTY-THEMES
# =====================================================

def install_alacritty_themes(self):
    install = 'pacman -S alacritty-themes --noconfirm'

    if os.path.exists("/usr/bin/alacritty-themes"):
        #print("Alacritty-themes is already installed")
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Alacritty-themes is now installed")

# =====================================================
#               INSTALL PACE
# =====================================================

def install_pace(self):
    install = 'pacman -S pace --noconfirm --needed'

    if os.path.exists("/usr/bin/pace"):
        #print("Pace is already installed")
        pass
    else:
        subprocess.call(install.split(" "),
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)
        print("Pace is now installed")