import tkinter as tk
#  实例化一个窗体对象
width = 355
height = 410

root = tk.Tk()
# 获取屏幕的宽度
screen_width = root.winfo_screenwidth()
# 获取屏幕的高度
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - width / 2)
center_y = int(screen_height / 2 - height / 2)
root.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))
# root = tk.Tk()
#  图片
# root.geometry("355x420+200+200")
img1 = tk.PhotoImage(file="img_1.png")
root.title('登录界面')
#  放入图片
label_image1 = tk.Label(root, image=img1)
label_image1.grid(row=0,columnspan=2)
tk.Label(root, text='用户名: ').grid(row=1,sticky=tk.E)#
tk.Label(root, text='密  码: ').grid(row=2,sticky=tk.E)

e1 = tk.Entry(root)
e2 = tk.Entry(root, show="*")
e1.grid(row=1, column=1, padx=10, pady=5)
e2.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text='登录',width=25).grid(row=3, column=1, sticky=tk.W, padx=10, pady=5,)
#  进入消息循环，显示窗口
# tk.Label(root, text='用户名: ').grid(row=0)
# tk.Label(root, text='密  码: ').grid(row=1)

# e1 = tk.Entry(root)
# e2 = tk.Entry(root, show="*")
# e1.grid(row=0, column=1, padx=10, pady=5)
# e2.grid(row=1, column=1, padx=10, pady=5)

# tk.Button(root, text='登录', width=10).grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
# tk.Button(root, text='退出', width=10).grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)
root.mainloop()

# import tkinter as tk
#
# root = tk.Tk()
# root.geometry("500x300+100+100")
#
# # column默认值是0
# tk.Entry(root).grid(row=1, column=1)
# tk.Entry(root).grid(row=1, column=2)
# # row span 跨行
# tk.Entry(root).grid(row=1, column=3, rowspan=2)
#
# tk.Entry(root, width=40, bg='red').grid(row=2, column=1, columnspan=2)
# # tk.Entry(root).grid(row=2, column=2)
# # tk.Entry(root).grid(row=2, column=3)
#
# tk.mainloop()