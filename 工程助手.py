import tkinter as tk  # 导入GUI模块tk
import sys  # 导入sys模块
import webbrowser  # 导入浏览器模块
import time  # 导入时间模块

Home = tk.Tk()  # 创建一个主窗口
Home.geometry('800x600+500+200')  # 设置窗口大小和位置
Home.title('工程创建助手')  # 设置窗口标题


def show_time():  # 定义一个函数，用于显示当前时间
    time_now = time.strftime('  当前日期与时间：' + '%Y年%m月%d日 %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
    label_time.config(text=time_now)  # 在标签上显示当前时间
    label_time.after(1000, show_time)  # 设置时间刷新间隔,当前单位为毫秒


def about():  # 定义一个函数，用于显示关于信息
    about_window = tk.Tk()  # 创建一个窗口
    about_window.geometry('300x150+750+400')  # 设置窗口大小和位置
    about_window.resizable(False, False)  # 设置窗口不可改变大小
    about_window.title('关于软件')  # 设置窗口标题
    tk.Label(about_window, text='\n工程创建助手 V1.0', font=('', '16'), foreground='#C38B5A').pack()  # 创建一个标签，并设置文本和字体
    # 创建一个主框架
    frm = tk.Frame(about_window)
    frm.pack()
    # 基于frm框架创建一个左边的子框架
    frm_t = tk.Frame(frm)
    # 基于frm框架创建一个右边的子框架
    frm_b = tk.Frame(frm)
    frm_t.pack(side='top')  # pack中的side方法是将frm_l,frm_r两个子框架按照左或右的方向添加到frm上
    frm_b.pack(side='bottom')

    tk.Label(frm_t, text='\n本软件旨在帮助后期人员\n快速并标准化创建管理工程\n使用教程请点击菜单栏帮助按钮\n', font=('', '11')).pack()  # 创建一个标签，并设置文本和字体
    tk.Label(frm_b, text='by Cui Qiangqiang', foreground='#DFE0DF').pack()  # 创建一个标签，并设置文本和字体

    about_window.mainloop()


def end_window():  # 定义一个函数，用于关闭主窗口
    sys.exit()  # 关闭程序


def browser():  # 定义一个函数，用于打开浏览器
    webbrowser.open("https://space.bilibili.com/120602530?spm_id_from=333.337.0.0")  # 打开网址


def setting():  # 定义一个函数，用于设置
    setting_window = tk.Tk()  # 创建一个窗口
    setting_window.geometry('500x300+650+350')  # 设置窗口大小和位置
    setting_window.resizable(False, False)  # 设置窗口不可改变大小
    setting_window.title('设置')  # 设置窗口标题

    parent_frame = tk.Frame(setting_window)    # 创建一个主框架
    parent_frame.grid()
    frame_top = tk.Frame(parent_frame, height=30, width=500, bg='Black')    # 基于主框架创建一个上边的子框架
    frame_top.grid(row=0)   # 将上边的子框架添加到主框架上
    frame_middle = tk.Frame(parent_frame, height=220, width=500)    # 基于主框架创建一个中间的子框架
    frame_middle.grid(row=1)   # 将中间的子框架添加到主框架上
    frame_beneath = tk.Frame(parent_frame, height=50, width=500, bg='Red')    # 基于主框架创建一个下面的子框架
    frame_beneath.grid(row=2)  # 将下面的子框架添加到主框架上

    contents = tk.Label(frame_middle, text='工程目录位置:', font=('', '13'))  # 创建一个标签，并设置文本和字体
    contents.grid(row=0, column=0, padx=10, pady=30)  # 将标签添加到中间的子框架上
    project_files = tk.Label(frame_middle, text='工程存放位置:', font=('', '13'))  # 创建一个标签，并设置文本和字体
    project_files.grid(row=1, column=0, padx=10)  # 将标签添加到中间的子框架上

    contents_entry = tk.Entry(frame_middle, width=26)  # 创建一个输入框，并设置宽度
    contents_entry.grid(row=0, column=1, padx=15)  # 将输入框添加到中间的子框架上
    contents_entry.insert(0, "contents_path")  # 将输入框中的文本插入到输入框中
    contents_entry.config(state='readonly')  # 设置输入框为只读
    contents_entry.bind('<Button-1>', lambda event: contents_entry.selection_clear())  # 绑定单击事件，清除输入框的选中

    project_entry = tk.Entry(frame_middle, width=26)  # 创建一个输入框，并设置宽度
    project_entry.grid(row=1, column=1, padx=15)  # 将输入框添加到中间的子框架上
    project_entry.insert(0, "project_files_path")  # 将输入框中的文本插入到输入框中
    project_entry.config(state='readonly')  # 设置输入框为只读
    project_entry.bind('<Button-1>', lambda event: project_entry.selection_clear())  # 绑定单击事件，清除输入框的选中

    contents_button = tk.Button(frame_middle, text='浏览')  # 创建一个按钮，并设置文本和点击事件
    contents_button.grid(row=0, column=2)  # 将按钮添加到中间的子框架上

    project_button = tk.Button(frame_middle, text='浏览')  # 创建一个按钮，并设置文本和点击事件
    project_button.grid(row=1, column=2)  # 将按钮添加到中间的子框架上

    setting_window.mainloop()


def menubar():  # 定义一个函数，用于创建菜单栏
    menu_bar = tk.Menu(Home)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='工程创建助手', menu=file_menu), \
        file_menu.add_command(label='关于工程创建助手', command=about), \
        file_menu.add_separator(), \
        file_menu.add_command(label='设置', command=setting), \
        file_menu.add_separator(), \
        file_menu.add_command(label='帮助', command=browser), \
        file_menu.add_separator(), \
        file_menu.add_command(label='退出', command=end_window)
    Home.config(menu=menu_bar)  # 将菜单栏添加到主窗口


menubar()  # 调用函数，创建菜单栏

# 创建一个标签，并设置其文本内容为当前时间，动态显示时间
label_time = tk.Label(Home, font=('', 12), bd=1, relief=tk.SUNKEN, anchor=tk.W)
label_time.pack(side=tk.BOTTOM, fill=tk.X)  # 将标签放置在主窗口的底部，并填充X轴
show_time()  # 调用函数显示当前时间

Home.mainloop()  # 进入主循环
