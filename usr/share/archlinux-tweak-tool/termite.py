#============================================================
# Authors: Brad Heffernan - Erik Dubois - Cameron Percival
#============================================================

import Functions as fn
import numpy as np
import Settings

# ====================================================================
#                       TERMITE
# ====================================================================

def get_themes(combo):  # noqa
    if fn.path.isdir(fn.home + "/.config/termite/themes/"):
        themes = fn.listdir(fn.home + "/.config/termite/themes/")
        combo.get_model().clear()
        with open(fn.termite_config, "r", encoding="utf-8") as f:
            lines = f.readlines()
            f.close()

        try:
            theme_line = lines[fn.get_position(lines, "[colors]") + 1]

            active = ""
            coms = []
            for theme in themes:
                if ".config" in theme:
                    if theme.replace("base16-",
                                     "").replace(".config",
                                                 "").capitalize() in theme_line:
                        active = theme.replace(".config", "")
                    coms.append(theme.replace(".config", ""))

            coms.sort()

            if fn.fn.path.isfile(fn.config):
                themes = Settings.read_settings("TERMITE", "theme")
                if len(themes) > 1:
                    active = themes

            for i in range(len(coms)):
                combo.append_text(coms[i])
                if active == coms[i]:
                    combo.set_active(i)
        except:  # noqa

            pass

    # print(lines[fn.get_position(lines, "[colors]") + 1])


def get_config():
    if fn.path.isfile(fn.termite_config):
        with open(fn.termite_config, "r", encoding="utf-8") as f:
            lists = f.readlines()
            f.close()
        target_element = "[colors]\n"
        try:
            target_index = lists.index(target_element)
        except:  # noqa
            return lists

        return lists[:target_index]
    return []


def set_config(self, theme):
    if not fn.path.isfile(fn.termite_config + ".bak"):
        fn.shutil.copy(fn.termite_config,
                              fn.termite_config + ".bak")

    try:
        config = get_config()

        with open(fn.home +
                  "/.config/termite/themes/" +
                  theme +
                  ".config", "r", encoding="utf-8") as f:
            theme_list = f.readlines()
            f.close()

        configs = list(np.append(config, theme_list))

        if configs is not None:
            with open(fn.termite_config, "w") as f:
                f.writelines(list(configs))
                f.close()

            fn.show_in_app_notification(self,
                                               "Settings Saved Successfully")
        if fn.path.isfile(fn.config):
            Settings.write_settings("TERMITE", "theme", theme)

    except Exception as e:
        print(e)
        fn.MessageBox(self,
                             "Error!!",
                             "Something went wrong setting this theme.")
