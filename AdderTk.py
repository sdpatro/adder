import Tkinter
import random
import sys


class AdderTk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.mainFrame = Tkinter.Frame(self, width=500, height=500, bd=3, relief=Tkinter.SUNKEN)
        self.SIZE = 4
        self.init_i = 0
        self.init_j = 0
        self.final_i = self.SIZE - 1
        self.final_j = self.SIZE - 1
        self.parent = parent
        self.initialize_grid()
        self.populate()
        self.calculate()
        self.execute()
        self.cur_i = 0
        self.cur_j = 0

    def initialize_grid(self):
        self.grid()
        self.mainFrame.pack_propagate(False)
        self.slot = [[0 for x in range(self.SIZE)] for x in range(self.SIZE)]

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
        self.my_sum_label = Tkinter.Label(self.mainFrame, textvariable=self.my_sum, anchor="w", fg="red")
        self.my_sum_label.place(relx=0.45, rely=0.97, anchor=Tkinter.CENTER)

        self.target_sum = Tkinter.IntVar()
        self.target_sum_label = Tkinter.Label(self.mainFrame, textvariable=self.target_sum, anchor="w", fg="blue")
        self.target_sum_label.place(relx=0.55, rely=0.97, anchor=Tkinter.CENTER)

        self.help_text = Tkinter.StringVar()
        self.help_text.set("Press DOWN or RIGHT to add. Reach the bottom right corner.")
        self.help_label = Tkinter.Label(self.mainFrame, textvariable=self.help_text, anchor="w", fg="red")
        self.help_label.place(relx=0.5, rely=0.05, anchor=Tkinter.CENTER)

        self.selected = [[0 for x in range(self.SIZE)] for x in range(self.SIZE)]

        self.select(self.init_i, self.init_j)
        self.mainFrame.pack()
        self.mainFrame.focus_set()

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
                print("i = " + str(i) + " j= " + str(j))
                j += 1
            else:
                temp_sum += self.slot_value[i][j].get()
                print("i = " + str(i) + " j= " + str(j))
                i += 1

        if i == self.SIZE - 1:
            while j != self.SIZE - 1:
                temp_sum += self.slot_value[i][j].get()
                print("i = " + str(i) + " j= " + str(j))
                j += 1

        else:
            while i != self.SIZE - 1:
                temp_sum += self.slot_value[i][j].get()
                print("i = " + str(i) + " j= " + str(j))
                i += 1

        temp_sum += self.slot_value[i][j].get()
        self.target_sum.set(str(temp_sum))

    def execute(self):
        self.my_sum.set(self.slot_value[0][0].get())

        def OnUpKey(event):
            print("up")
            if self.cur_i != 0 and self.selected[self.cur_i - 1][self.cur_j] == 1:
                self.unselect(self.cur_i, self.cur_j)
                self.cur_i -= 1
            self.check()

        def OnDownKey(event):
            print("down")
            if self.cur_i != self.SIZE - 1:
                self.cur_i += 1
                self.select(self.cur_i, self.cur_j)
            self.check()

        def OnLeftKey(event):
            print("left")
            if self.cur_j != 0 and self.selected[self.cur_i][self.cur_j - 1] == 1:
                self.unselect(self.cur_i, self.cur_j)
                self.cur_j -= 1
            self.check()

        def OnRightKey(event):
            print("right")
            if self.cur_j != self.SIZE - 1:
                self.cur_j += 1
                self.select(self.cur_i, self.cur_j)
            self.check()

        self.mainFrame.bind("<Up>", OnUpKey)
        self.mainFrame.bind("<Down>", OnDownKey)
        self.mainFrame.bind("<Left>", OnLeftKey)
        self.mainFrame.bind("<Right>", OnRightKey)

    def select(self, a, b):
        print("a= " + str(a) + " b= " + str(b))
        self.slot[a][b].config(fg="red")
        self.selected[a][b] = 1
        temp_sum = self.my_sum.get()
        temp_sum += self.slot_value[a][b].get()
        self.my_sum.set(temp_sum)

    def unselect(self, a, b):
        print("a= " + str(a) + " b= " + str(b))
        self.slot[a][b].config(fg="black")
        self.selected[a][b] = 0
        temp_sum = self.my_sum.get()
        temp_sum -= self.slot_value[a][b].get()
        self.my_sum.set(temp_sum)

    def check(self):
        def exitgame(event):
            sys.exit()

        if (self.cur_i == self.SIZE - 1) and (
                    self.cur_j == self.SIZE - 1) and self.my_sum.get() == self.target_sum.get():
            print("You win")
            for i in range(0, self.SIZE, 1):
                for j in range(0, self.SIZE, 1):
                    if self.selected[i][j] == 1:
                        self.slot[i][j].config(fg="blue")
                        self.help_text.set("Congrats. You win.")
                        self.help_label.config(fg="blue")
            self.mainFrame.bind("<Key>", exitgame)

if __name__ == "__main__":
    app = AdderTk(None)
    app.title("Adder")
    app.mainloop()
