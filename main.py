import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

import os
import sys
import re

from music import download


def DownloadMusic():
    print('DownloadMusic')
    url = WebLink.get()
    download_dir = path.get()
    if not os.path.isdir(download_dir):
        tk.messagebox.showinfo(title='Error', message='Download path not exist')
        return
    # url = "https://music.163.com/#/song?id=1407551413"
    # download_dir = "D:\\Downloads\\"
    verify = re.search(r'music.163.com.+\?id\=\d+', url)
    if verify:
        but_text.set("Processing...")
        Download.configure(state='disabled')
        top.update()
        music_id = re.findall(r'\?id\=(\d+)', url)[0]
        stat = download(music_id, download_dir)
        if stat == 0:
            tk.messagebox.showinfo(title='Message', message='Download Success')
        elif stat == 1:
            tk.messagebox.showinfo(title='Error', message='Download error. Check music ID or download is restricted.')
    but_text.set("Download")
    Download.configure(state='normal')
    sys.stdout.flush()


def OpenDir():
    if path.get():
        set_dir = path.get()
    else:
        set_dir = os.getcwd()
    if not os.path.isdir(set_dir):
        tk.messagebox.showinfo(title='Error', message='Download path not exist')
        return
    print('OpenDir')
    print(set_dir)
    os.startfile(set_dir)
    sys.stdout.flush()


def SetDir():
    dir = tk.filedialog.askdirectory(title='Open...', initialdir=path.get())
    if not dir:
        dir = sys.path[0]
    print(dir)
    path.set(dir)
    sys.stdout.flush()


def cut(editor, event=None):
    editor.event_generate("<<Cut>>")


def copy(editor, event=None):
    editor.event_generate("<<Copy>>")


def paste(editor, event=None):
    editor.event_generate('<<Paste>>')


def rightKey(event, editor):
    menuBar.delete(0, 2)
    menuBar.add_command(label='剪切', command=lambda: cut(editor))
    menuBar.add_command(label='复制', command=lambda: copy(editor))
    menuBar.add_command(label='粘贴', command=lambda: paste(editor))
    menuBar.post(event.x_root, event.y_root)


top = tk.Tk()

top.geometry("700x335+609+300")  ## 主窗口设定
top.title("NeteaseMusicDownloader")
top.configure(background="#d9d9d9")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")

menuBar = tk.Menu(top, tearoff=0)

Title = tk.Message(top)  ## 标题
Title.place(relx=0.0, rely=0.03, relheight=0.194, relwidth=0.996)
Title.configure(background="#d9d9d9")
Title.configure(foreground="#000000")
Title.configure(font=('times', 24, 'italic'))
Title.configure(highlightbackground="#6e41d8")
Title.configure(highlightcolor="#000000")
Title.configure(justify='center')
Title.configure(text='''NeteaseMusicWebDownloader''')
Title.configure(width=697)

WebLinkTitle = tk.Message(top)  ## 音乐链接字样
WebLinkTitle.place(relx=0.1, rely=0.289, relheight=0.134
                   , relwidth=0.124)
WebLinkTitle.configure(background="#d9d9d9")
WebLinkTitle.configure(foreground="#000000")
WebLinkTitle.configure(highlightbackground="#d9d9d9")
WebLinkTitle.configure(highlightcolor="black")
WebLinkTitle.configure(text='''WebMusicLink''')
WebLinkTitle.configure(width=87)

default_link = tk.StringVar()
default_link.set("https://music.163.com/#/song?id=1407551413")
WebLink = tk.Entry(top, textvariable=default_link)  ## 音乐链接输入框
WebLink.place(relx=0.329, rely=0.328, height=17, relwidth=0.606)
WebLink.configure(background="white")
WebLink.configure(disabledforeground="#a3a3a3")
WebLink.configure(font="TkFixedFont")
WebLink.configure(foreground="#000000")
WebLink.configure(insertbackground="black")
WebLink.configure(width=424)
WebLink.bind("<Button-3>", lambda x: rightKey(x, WebLink))


DownloadNameTitle = tk.Message(top)  ## 下载目录字样
DownloadNameTitle.place(relx=0.057, rely=0.438, relheight=0.125
                        , relwidth=0.206)
DownloadNameTitle.configure(background="#d9d9d9")
DownloadNameTitle.configure(highlightbackground="#d9d9d9")
DownloadNameTitle.configure(highlightcolor="black")
DownloadNameTitle.configure(text='''DownloadMusicDir''')
DownloadNameTitle.configure(width=144)

path = tk.StringVar()
path.set(sys.path[0])
MusicDir = tk.Entry(top, textvariable=path)  ## 下载目录输入框
MusicDir.place(relx=0.329, rely=0.478, height=17, relwidth=0.606)
MusicDir.configure(background="white")
MusicDir.configure(disabledforeground="#a3a3a3")
MusicDir.configure(font="TkFixedFont")
MusicDir.configure(foreground="#000000")
MusicDir.configure(insertbackground="black")
MusicDir.configure(width=424)
MusicDir.bind("<Button-3>", lambda x: rightKey(x, MusicDir))

but_text = tk.StringVar()
but_text.set("Download")
Download = tk.Button(top, textvariable=but_text)  ## 下载按钮
Download.place(relx=0.229, rely=0.627, height=28, width=83)
Download.configure(activebackground="#ececec")
Download.configure(activeforeground="#000000")
Download.configure(background="#d9d9d9")
Download.configure(command=DownloadMusic)
Download.configure(disabledforeground="#a3a3a3")
Download.configure(foreground="#000000")
Download.configure(highlightbackground="#d9d9d9")
Download.configure(highlightcolor="black")
Download.configure(pady="0")

SetDownloadDir = tk.Button(top)  ## 设置下载目录按钮
SetDownloadDir.place(relx=0.429, rely=0.627, height=28, width=123)
SetDownloadDir.configure(activebackground="#ececec")
SetDownloadDir.configure(activeforeground="#000000")
SetDownloadDir.configure(background="#d9d9d9")
SetDownloadDir.configure(command=SetDir)
SetDownloadDir.configure(disabledforeground="#a3a3a3")
SetDownloadDir.configure(foreground="#000000")
SetDownloadDir.configure(highlightbackground="#d9d9d9")
SetDownloadDir.configure(highlightcolor="black")
SetDownloadDir.configure(pady="0")
SetDownloadDir.configure(text='''SelectDownloadDir''')

OpenDownloadDir = tk.Button(top)  ## 打开下载目录按钮
OpenDownloadDir.place(relx=0.686, rely=0.627, height=28, width=119)
OpenDownloadDir.configure(activebackground="#ececec")
OpenDownloadDir.configure(activeforeground="#000000")
OpenDownloadDir.configure(background="#d9d9d9")
OpenDownloadDir.configure(command=OpenDir)
OpenDownloadDir.configure(disabledforeground="#a3a3a3")
OpenDownloadDir.configure(foreground="#000000")
OpenDownloadDir.configure(highlightbackground="#d9d9d9")
OpenDownloadDir.configure(highlightcolor="black")
OpenDownloadDir.configure(pady="0")
OpenDownloadDir.configure(text='''OpenDownloadDir''')


Message1 = tk.Message(top)  ## 防伪标签
Message1.place(relx=0.0, rely=0.896, relheight=0.075, relwidth=0.996)
Message1.configure(background="#d9d9d9")
Message1.configure(foreground="#000000")
Message1.configure(highlightbackground="#d9d9d9")
Message1.configure(highlightcolor="black")
Message1.configure(text='''Designed by KevinMinG and KiraRin''')
Message1.configure(width=697)

top.mainloop()
