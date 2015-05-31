import Tkinter
import random


class AdderTk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.SIZE = 5
        self.parent = parent
        self.initialize_grid()
        self.populate()
        self.calculate()

    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here")

        button = Tkinter.Button(self, text="u Click me !", command=self.OnButtonClick)
        button.grid(column=1, row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="blue")
        label.grid(column=0, row=1, columnspan=2, sticky='EW')
        self.labelVariable.set(u"Hello!")

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())

        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def initialize_grid(self):
        self.grid()
        self.mainFrame = Tkinter.Frame(self, width=500, height=500, bd=3, relief=Tkinter.SUNKEN)
        self.mainFrame.pack_propagate(False)
        self.slot = [[0 for x in range(10)] for x in range(10)]

        self.slot_value = [[0 for x in range(self.SIZE)] for x in range(10)]
        for i in range(0, self.SIZE, 1):
            for j in range(0, self.SIZE, 1):
                self.slot_value[i][j] = Tkinter.IntVar()

        grad = 1 / float(self.SIZE + 1)

        for i in range(0, self.SIZE, 1):
            for j in range(0, self.SIZE, 1):
                self.slot[i][j] = Tkinter.Label(self.mainFrame, textvariable=self.slot_value[i][j], anchor="w",
                                                fg="black")
                self.slot[i][j].place(relx=grad * j + grad, rely=grad * i + grad, anchor=Tkinter.CENTER)

        self.my_sum = Tkinter.IntVar()
        self.result_sum = Tkinter.IntVar()
        self.my_sum_label = Tkinter.Label(self.mainFrame, textvariable=self.my_sum, anchor="w", fg="red")
        self.my_sum_label.place(relx=0.45, rely=0.97, anchor=Tkinter.CENTER)
        self.result_sum_label = Tkinter.Label(self.mainFrame, textvariable=self.result_sum, anchor="w", fg="blue")
        self.result_sum_label.place(relx=0.55, rely=0.97, anchor=Tkinter.CENTER)
        self.mainFrame.pack()

    def populate(self):
        for i in range(0, self.SIZE, 1):
            for j in range(0, self.SIZE, 1):
                self.slot_value[i][j].set(random.randrange(0, 9))

    def calculate(self):
        i = 0
        j = 0
        temp_sum = 0
        temp_sum += self.slot_value[i][j].get()
        while i != self.SIZE - 1 and j != self.SIZE - 1:
            next_slot = random.randrange(0, 2)
            if next_slot == 0:
                temp_sum += self.slot_value[i][j].get()
                j += 1
            else:
                temp_sum += self.slot_value[i][j].get()
                i += 1

        if i == self.SIZE - 1:
            while j != self.SIZE - 1:
                temp_sum += self.slot_value[0][j].get()
                j += 1

        else:
            while i != self.SIZE - 1:
                temp_sum += self.slot_value[i][0].get()
                i += 1

        print("temp= "+str(temp_sum))


    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get() + "(You clicked the button)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self, event):
        self.labelVariable.set(self.entryVariable.get() + "(You pressed Enter)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


if __name__ == "__main__":
    app = AdderTk(None)
    app.title("Adder")
    app.mainloop()
