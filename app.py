import tkinter as tk
app=tk.Tk()
app.geometry('1000x500')
app.title('RESTAURANT BILLING SYSTEM')
app.resizable(False,False)
app.configure(background='#4285F4')


"""fuctions"""
def Reset():
    cake_entry.delete(0,tk.END)
    cookies_entry.delete(0,tk.END)
    drumstick_entry.delete(0,tk.END)
    chocolate_entry.delete(0,tk.END)
    juice_entry.delete(0,tk.END)
    icecream_entry.delete(0,tk.END)
    bugger_entry.delete(0,tk.END)
    pizza_entry.delete(0,tk.END)

def Total():
    try:a1=int(cake.get())
    except :a1=0
    try:a2=int(cookies.get())
    except :a2=0
    try:a3=int(drumstick.get())
    except :a3=0
    try:a4=int(chocolate.get())
    except :a4=0
    try:a5=int(juice.get())
    except :a5=0
    try:a6=int(icecream.get())
    except :a6=0
    try:a7=int(bugger.get())
    except :a7=0
    try:a8=int(pizza.get())
    except :a8=0
    #defining costs
    cost1=800*a1
    cost2=300*a2
    cost3=999*a3
    cost4=400*a4
    cost5=500*a5
    cost6=700*a6
    cost7=350*a7
    cost8=999*a8
    total_label=tk.Label(
        frame3,text="Total",
        font=('aria',20,'bold'),
        width=16,
        foreground='black',
        background='#0F9D58'
        )
    total_label.place(x=10,y=50)
    total_entry=tk.Entry(
        frame3,
        font=('aria',20,'bold'),
        textvariable=total_bill,
        width=16,background='#0F9D58',
        foreground='black'
        )
    total_entry.place(x=30,y=100)
    total_cost=cost1+cost2+cost3+cost4+cost5+cost6+cost7+cost8
    output=f'Ksh. {total_cost}.00'
    total_bill.set(output)
    
    
    """navigation section"""
label=tk.Label(
    text='BILL MANAGEMENT',
    background='#DB4437',
    foreground='white',
    width='300',
    height='2',
    font=('calibri',33)
    )
label.pack(expand=0,fill=tk.X)


"""Menu Card"""
frame1=tk.Frame(app,
                background='#0F9D58',
                highlightbackground='#F4B400',
                highlightthickness=1,
                width='300',
                height=370,
                )

frame1.pack(side=tk.LEFT,padx=10)
label_menu=tk.Label(
    frame1,text='Menu',
    font=('Gabriola',40,'bold'),
    foreground='black',
    background='#0F9D58',
    )

label_menu.place(x=80,y=0)
label=tk.Label(
    frame1,
    font=('Lucida Calligraphy',15,'bold'),
    text='Cake:--Ksh.800',
    foreground='black',
    background='#0F9D58',
    ).place(x=10,y=80)

label=tk.Label(
    frame1,
    font=('Lucida Calligraphy',15,'bold'),
    text='Cookies:--Ksh.300',
    foreground='black',
    background='#0F9D58',
    ).place(x=10,y=110)

label=tk.Label(
    frame1,
    font=('Lucida Calligraphy',15,'bold'),
    text='Drum stick:--Ksh.999',
    foreground='black',
    background='#0F9D58',
    ).place(x=10,y=140)

label=tk.Label(
    frame1,
    font=('Lucida Calligraphy',15,'bold'),
    text='Chocolate:--Ksh.400',
    foreground='black',
    background='#0F9D58',
    ).place(x=10,y=170)

label=tk.Label(
    frame1,
    font=('Lucida Calligraphy',15,'bold'),
    text='Juice--:Ksh.500',
    foreground='black',
    background='#0F9D58',
    ).place(x=10,y=200)

label=tk.Label(
    frame1,
    font=('Lucida Calligraphy',15,'bold'),
    text='Ice Cream:--Ksh.700',
    foreground='black',
    background='#0F9D58',
    ).place(x=10,y=230)

label=tk.Label(
    frame1,
    font=('Lucida Calligraphy',15,'bold'),
    text='Bugger:--Ksh.350',
    foreground='black',
    background='#0F9D58',
    ).place(x=10,y=260)

label=tk.Label(
    frame1,
    font=('Lucida Calligraphy',15,'bold'),
    text='Pizza:--Ksh.999',
    foreground='black',
    background='#0F9D58',
    ).place(x=10,y=290)


"""Entries"""
frame2=tk.Frame(
    app,
    width=300,
    height=370,
    relief=tk.RAISED,
    background='#F4B400',
    highlightbackground='white',
    highlightthickness=1,
    )
frame2.pack(side=tk.LEFT)


"""bill"""
frame3=tk.Frame(
    app,
    width=300,
    height=370,
    relief=tk.RAISED,
    background='white',
    highlightbackground='white',
    highlightthickness=1,
    )

frame3.pack(side=tk.RIGHT,padx=20)
bill_label=tk.Label(
    frame3,text='BILL',
    font=('calibri',20),
    background='white',
    foreground='black'
    )
bill_label.place(x=120,y=10)

"""declaring variables to store entries"""
cake=tk.StringVar()
cookies=tk.StringVar()
drumstick=tk.StringVar()
chocolate=tk.StringVar()
juice=tk.StringVar()
icecream=tk.StringVar()
bugger=tk.StringVar()
pizza=tk.StringVar()
total_bill=tk.StringVar()


"""labels on frame2"""
cake_label=tk.Label(
    frame2,font=('aria',20,'bold'),
    text='CAKE',
    width=12,
    foreground='white',
    background='#DB4437'
    )

cookies_label=tk.Label(
    frame2,font=('aria',20,'bold'),
    text='COOKIES',
    width=12,
    foreground='white',
    background='#DB4437'
    )

drumstick_label=tk.Label(
    frame2,font=('aria',20,'bold'),
    text='DRUM-STICK',
    width=12,
    foreground='white',
    background='#DB4437'
    )

chocolate_label=tk.Label(
    frame2,font=('aria',20,'bold'),
    text='CHOCOLATE',
    width=12,
    foreground='white',
    background='#DB4437'
    )

juice_label=tk.Label(
    frame2,font=('aria',20,'bold'),
    text='JUICE',
    width=12,
    foreground='white',
    background='#DB4437'
    )

icecream_label=tk.Label(
    frame2,font=('aria',20,'bold'),
    text='ICE-CREAM',
    width=12,
    foreground='white',
    background='#DB4437'
    )

bugger_label=tk.Label(
    frame2,font=('aria',20,'bold'),
    text='BUGGER',
    width=12,
    foreground='white',
    background='#DB4437'
    )

pizza_label=tk.Label(
    frame2,font=('aria',20,'bold'),
    text='PIZZA',
    width=12,
    foreground='white',
    background='#DB4437'
    )

cake_label.grid(row=1,column=0)
cookies_label.grid(row=2,column=0)
drumstick_label.grid(row=3,column=0)
chocolate_label.grid(row=4,column=0)
juice_label.grid(row=5,column=0)
icecream_label.grid(row=6,column=0)
bugger_label.grid(row=7,column=0)
pizza_label.grid(row=8,column=0)


"""Entries"""
cake_entry=tk.Entry(
    frame2,font=('aria',20,'bold'),
    textvariable=cake,
    border=1,
    width=8,
    background='white'
    )

cookies_entry=tk.Entry(
    frame2,font=('aria',20,'bold'),
    textvariable=cookies,
    border=1,
    width=8,
    background='white'
    )

drumstick_entry=tk.Entry(
    frame2,font=('aria',20,'bold'),
    textvariable=drumstick,
    border=1,
    width=8,
    background='white'
    )

chocolate_entry=tk.Entry(
    frame2,font=('aria',20,'bold'),
    textvariable=chocolate,
    border=1,
    width=8,
    background='white'
    )

juice_entry=tk.Entry(
    frame2,font=('aria',20,'bold'),
    textvariable=juice,
    border=1,
    width=8,
    background='white'
    )

icecream_entry=tk.Entry(
    frame2,font=('aria',20,'bold'),
    textvariable=icecream,
    border=1,
    width=8,
    background='white'
    )

bugger_entry=tk.Entry(
    frame2,font=('aria',20,'bold'),
    textvariable=bugger,
    border=1,
    width=8,
    background='white'
    )

pizza_entry=tk.Entry(
    frame2,font=('aria',20,'bold'),
    textvariable=pizza,
    border=1,
    width=8,
    background='white'
    )

cake_entry.grid(row=1,column=1)
cookies_entry.grid(row=2,column=1)
drumstick_entry.grid(row=3,column=1)
chocolate_entry.grid(row=4,column=1)
juice_entry.grid(row=5,column=1)
icecream_entry.grid(row=6,column=1)
bugger_entry.grid(row=7,column=1)
pizza_entry.grid(row=8,column=1)


"""buttons"""
reset_button=tk.Button(
    frame2,
    border=2,
    foreground='black',
    background='white',
    font=('ariel',16,'bold'),
    width=8,
    text='RESET',
    command=Reset
    )

total_button=tk.Button(
    frame2,
    border=2,
    foreground='black',
    background='#DB4437',
    font=('ariel',16,'bold'),
    width=8,
    text='TOTAL',
    command=Total
    )

reset_button.grid(row=9,column=0,pady=10)
total_button.grid(row=9,column=1,pady=10,)


app.mainloop()