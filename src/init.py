import os

# PATHS
APP = f"/Applications"

# SUPPORTED
SUPPORTED = ["iterm", "obsidian", "alacritty", "vscode"]


class CLI:
    def start(self):
        print("Available:")
        for app in os.listdir(APP):
            if app.split(".")[0].lower() in SUPPORTED:
                print(f" • {app}")
        choose = input("\nApply theme to all? [Y/n] ").lower().strip()
        if choose in ("y", "yes"):
            for app in SUPPORTED:
                if app == "iterm":
                    self.iterm()

    def iterm(self):
        # API
        pass


def main():
    # INIT INSTANCE
    cli = CLI()
    cli.start()


main()
