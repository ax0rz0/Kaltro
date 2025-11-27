from tkinter import simpledialog


def PingTool(self):
    Target = simpledialog.askstring("Ping Tool", "Enter an IP address or domain:")

    if not Target:
        messagebox.showinfo("Ping Tool", "No target entered.")
        return

    Result = RunPing(Target)

    if Result["success"]:
        messagebox.showinfo("Ping Result", f"Ping successful:\n\n{Result['output']}")
    else:
        messagebox.showerror("Ping Failed", f"Ping failed:\n\n{Result['output']}")
