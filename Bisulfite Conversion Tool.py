from tkinter import *

my_window=Tk()
my_window.title("Bisulfite Conversion Tool")

def convert():
    seq=entry1.get()
    seq2 = seq.upper()
    c = "C"
    g = "G"
    conv_seq= ""
    cpg_count=0
    for i in range(0,len(seq2)):
        cur_base = seq2[i:i+1]
        next_base = seq2[i+1:i+2]
        if cur_base == c:
            if next_base == g:
                conv_seq = conv_seq + cur_base
                cpg_count += 1
            else:
                conv_seq = conv_seq + 'T'
                cpg_count += 0
        else:
            conv_seq = conv_seq + cur_base
    string_to_display=conv_seq
    second_string_to_display=str(cpg_count)
    label_2= Label (my_window,text="The bisulfite converted DNA is: ",bg="white",wraplength=550)
    label_2.grid(row=3,column=0)
    w=Text(my_window,height=5)
    w.insert(1.0,string_to_display)
    w.grid(row=3,column=1)
    label_3= Label (my_window,text="Number of CpG's in the sequence: ",bg="white",wraplength=550)
    label_3.grid(row=4,column=0)
    y=Text(my_window,height=1)
    y.insert(1.0,second_string_to_display)
    y.grid(row=4,column=1)
label_1=Label(my_window,text="Unconverted Sequence:", bg="white")
entry1=Entry(my_window,width=50,text="hello")
button_1=Button(my_window, text="Bisulfite Convert Please!",bg="lightblue",command=convert)
label_1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
button_1.grid(row=2, column=1)
my_window.mainloop()
