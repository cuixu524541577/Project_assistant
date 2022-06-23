import tkinter as tk

setting_window = tk.Tk()  # 创建一个窗口
setting_window.geometry('500x300+650+350')  # 设置窗口大小和位置
setting_window.resizable(False, False)  # 设置窗口不可改变大小
setting_window.title('设置')  # 设置窗口标题

parent_frame = tk.Frame(setting_window)  # 创建一个主框架
parent_frame.grid()
frame_top = tk.Frame(parent_frame, height=30, width=500)  # 基于主框架创建一个上边的子框架
frame_top.grid(row=0)  # 将上边的子框架添加到主框架上
frame_middle = tk.Frame(parent_frame, height=220, width=500)  # 基于主框架创建一个中间的子框架
frame_middle.grid(row=1)  # 将中间的子框架添加到主框架上
frame_beneath = tk.Frame(parent_frame, height=50, width=500)  # 基于主框架创建一个下面的子框架
frame_beneath.grid(row=2, rowspan=20)  # 将下面的子框架添加到主框架上

contents = tk.Label(frame_middle, text='工程目录位置:', font=('', '13'))  # 创建一个标签，并设置文本和字体
contents.grid(row=0, column=0, sticky='w', ipady=30)  # 将标签添加到中间的子框架上
project_files = tk.Label(frame_middle, text='工程存放位置:', font=('', '13'))  # 创建一个标签，并设置文本和字体
project_files.grid(row=1, column=0, sticky='w')  # 将标签添加到中间的子框架上

contents_entry = tk.Entry(frame_middle, width=26)  # 创建一个输入框，并设置宽度
contents_entry.grid(row=0, column=2, padx=10)  # 将输入框添加到中间的子框架上
contents_entry.insert(0, "contents_path")  # 将输入框中的文本插入到输入框中
contents_entry.config(state='readonly')  # 设置输入框为只读
contents_entry.bind('<Button-1>', lambda event: contents_entry.selection_clear())  # 绑定单击事件，清除输入框的选中

project_entry = tk.Entry(frame_middle, width=26)  # 创建一个输入框，并设置宽度
project_entry.grid(row=1, column=2, padx=10)  # 将输入框添加到中间的子框架上
project_entry.insert(0, "project_files_path")  # 将输入框中的文本插入到输入框中
project_entry.config(state='readonly')  # 设置输入框为只读
project_entry.bind('<Button-1>', lambda event: project_entry.selection_clear())  # 绑定单击事件，清除输入框的选中

contents_button = tk.Button(frame_middle, text='浏览')  # 创建一个按钮，并设置文本和点击事件
contents_button.grid(row=0, column=4)  # 将按钮添加到中间的子框架上

project_button = tk.Button(frame_middle, text='浏览')  # 创建一个按钮，并设置文本和点击事件
project_button.grid(row=1, column=4)  # 将按钮添加到中间的子框架上

b1 = tk.Button(frame_beneath, text='保存', height=2, width=7)
b1.grid(row=0, column=0)
b2 = tk.Button(frame_beneath, text='关闭', height=2, width=7, command=setting_window.destroy)
b2.grid(row=0, column=1, sticky='')


setting_window.mainloop()