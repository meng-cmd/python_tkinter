from tkinter import *
from tkinter.filedialog import askopenfilename


def select_file():
    global filename
    filename = askopenfilename(title="选择文件", initialdir="D", filetypes=[("文本文档", ".txt")])
    filename = filename[18:len(filename)]
    show["text"] = filename


def select_algorithm():
    global flag
    s = v.get()
    if s == 'SNP-Miner':
        flag = 1
        print('当前选择算法为：' + s)
    elif s == 'SNP-df':
        flag = 2
        print('当前选择算法为：' + s)
    elif s == 'SNP-bf':
        flag = 3
        print('当前选择算法为：' + s)
    elif s == 'SNP-nogap':
        flag = 4
        print('当前选择算法为：' + s)
    elif s == 'SNP-sn':
        flag = 5
        print('当前选择算法为：' + s)


def get_Threshold(event):
    pass


def run_procedure(event):
    pass


if __name__ == '__main__':
    root = Tk()
    root.geometry("700x600")
    root.resizable(False, False)
    root.title("SNP-Miner")
    label00 = Label(root, text="SNP-Miner", height=2, width=20, fg="blue", bg="green",
                    font=("Times New Roman", 18, "bold", "italic"))
    label00.grid(row=0, column=1)

    label01 = Label(root, text="Choose an algorithm", font=("Times New Roman", 10))
    label01.grid(row=1, column=0, ipadx=0)
    label01["width"] = 22

    label02 = Label(root, text="Choose input file", font=("Times New Roman", 10))
    label02.grid(row=2, column=0, ipadx=0)
    label02["width"] = 22

    label03 = Label(root, text="Min.support", font=("Times New Roman", 10))
    label03.grid(row=3, column=0, ipadx=0)
    label03["width"] = 22

    v = StringVar(root)
    v.set("SNP-Miner")
    om = OptionMenu(root, v, "SNP-nogap", "SNP-Miner", "SNP-bf", "SNP-df")
    om["width"] = 25
    om.grid(row=1, column=1)

    btn01 = Button(root, text="?", command=select_algorithm, width=5)
    btn01.grid(row=1, column=2)

    btn02 = Button(root, text="...", command=select_file, width=5)
    btn02.grid(row=2, column=2)

    show = Label(root, width=40, height=1, relief="raised")
    show.grid(row=2, column=1)
    show["text"] = "文件名"

    v2 = IntVar()
    v2.set(4300)
    entry01 = Entry(textvariable=v2, width=40)
    entry01.grid(row=3, column=1)
    # entry01.bind("<Return>", get_Threshold)

    btn03 = Button(root, text="确定")
    btn03.grid(row=3, column=2)
    btn03["width"] = 5
    btn03.bind("<Button-1>", get_Threshold)

    btn04 = Button(root, text="Run Algorithm", relief="groove")
    btn04.grid(row=4, column=1)
    btn04["width"] = 20
    btn04.bind("<Button-1>", run_procedure)

    text01 = Text(root, width=50, height=20, relief="raised", font=("Times New Roman", 12, "bold", "italic"))
    text01.grid(row=5, column=1)

    root.mainloop()
