import tkinter as tk
from tkinter import messagebox
from Modules import Ping, Nmap, LogWrite, Scan
from Modules.Ping import RunPing
# Extra Modules TBI

from tkinter import simpledialog


class KaltroApp:

    def __init__(self, RootWindow):
        self.RootWindow = RootWindow
        self.RootWindow.title("Kaltro – Networking Swiss Army Knife")
        self.RootWindow.geometry("500x350")

        self.BuildInterface()

    def BuildInterface(self):
        TitleLabel = tk.Label(
            self.RootWindow,
            text="Kaltro – Networking Swiss Army Knife",
            font=("Arial", 16, "bold")
        )
        TitleLabel.pack(pady=10)

        DescriptionLabel = tk.Label(
            self.RootWindow,
            text="Select an option to begin:",
            font=("Arial", 12)
        )
        DescriptionLabel.pack()

        PingButton = tk.Button(
            self.RootWindow,
            text="Ping Tool",
            width=20,
            command=self.PingTool
        )
        PingButton.pack(pady=10)

        PortScanButton = tk.Button(
            self.RootWindow,
            text="Port Scanner",
            width=20,
            command=self.PortScannerTool
        )
        PortScanButton.pack(pady=10)

        NetworkMapButton = tk.Button(
            self.RootWindow,
            text="Network Map",
            width=20,
            command=self.NetworkMapTool
        )
        NetworkMapButton.pack(pady=10)

        LogButton = tk.Button(
            self.RootWindow,
            text="View Logs",
            width=20,
            command=self.LogViewer
        )
        LogButton.pack(pady=10)

    def PingTool(self):
        Ping.PingTool(self)

    def PortScannerTool(self):
        messagebox.showinfo("Port Scanner", "Port scanner function coming soon.")

    def NetworkMapTool(self):
        messagebox.showinfo("Network Map", "Network mapping coming soon.")

    def LogViewer(self):
        messagebox.showinfo("Logs", "Log viewer coming soon.")


if __name__ == "__main__":
    RootWindow = tk.Tk()
    App = KaltroApp(RootWindow)
    RootWindow.mainloop()
