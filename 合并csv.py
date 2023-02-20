import tkinter as tk
from tkinter import filedialog
import pandas as pd
import glob

class App:
    def __init__(self, master):
        self.master = master
        master.title("CSV合并器")

        self.button = tk.Button(master, text="选择文件夹", command=self.load_files)
        self.button.pack()

    def load_files(self):
        path = filedialog.askdirectory()
        if path:
            all_files = glob.glob(path + '/*.csv')
            if all_files:
                df = pd.concat((pd.read_csv(f) for f in all_files))
                df.to_csv('合并的文件.csv', index=False)
                tk.messagebox.showinfo("提示", "CSV文件已合并。")
            else:
                tk.messagebox.showwarning("警告", "找不到任何CSV文件。")

root = tk.Tk()
app = App(root)
root.mainloop()
