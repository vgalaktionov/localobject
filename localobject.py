import subprocess

import rumps


class LocalObject(rumps.App):
    def __init__(self):
        super(LocalObject, self).__init__("LocalObject", title="〓")
        self.menu = ["Start Minio", "Stop Minio", "Install Minio", "Version"]
        self.minio_process = None

    @rumps.clicked("Start Minio")
    def start_minio(self, _):
        if self.minio_process:
            rumps.alert(message="Minio is already running!")
            return

        try:
            self.minio_process = subprocess.Popen(
                [
                    "/opt/homebrew/bin/minio",
                    "server",
                    "~/.localobject_minio_data",
                    "--address",
                    ":59090",
                ]
            )
            rumps.notification(
                title="Minio",
                subtitle="Server Started",
                message="Minio server is running on port 59090",
            )
        except Exception as e:
            rumps.alert(message=str(e))

    @rumps.clicked("Stop Minio")
    def stop_minio(self, _):
        if self.minio_process:
            self.minio_process.terminate()
            self.minio_process = None
            rumps.notification(
                title="Minio",
                subtitle="Server Stopped",
                message="Minio server has been stopped.",
            )
        else:
            rumps.alert(message="Minio is not currently running!")

    @rumps.clicked("Install Minio")
    def install_minio(self, _):
        try:
            subprocess.run(["/opt/homebrew/bin/brew", "install", "minio/stable/minio"])
            rumps.notification(
                title="Minio",
                subtitle="Installation Successful",
                message="Minio has been installed successfully!",
            )
        except Exception as e:
            rumps.alert(message=str(e))

    @rumps.clicked("Version")
    def minio_version(self, _):
        try:
            output = (
                subprocess.check_output(
                    ["/opt/homebrew/bin/minio", "--version"], timeout=5
                )
                .decode("utf-8")
                .strip()
            )
            rumps.alert(message=output)
        except Exception:
            rumps.alert("Minio is not installed!")


if __name__ == "__main__":
    LocalObject().run()
