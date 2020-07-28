import tkinter as tk
from sms import send_msg

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title('CK Raporty')
        self.money_earned = 0
        self.no_full_set = 0
        self.no_leakiness = 0
        self.no_ac_fumigation = 0

        # Label and entry for inserting date of raport
        self.date_label = tk.Label(parent, text='Wprowadź datę')
        self.date_entry = tk.Entry(parent)
        
        # Label and entry for inserting name of the worker
        self.name_label = tk.Label(parent, text='Wprowadź imię i nazwisko')
        self.name_entry = tk.Entry(parent)

        # Labels and buttons for normal full_set
        self.full_set_label = tk.Label(parent, text='Komplet (200 zł)')
        self.full_set_fr = tk.Frame(parent)
        self.full_set_minus = tk.Button(self.full_set_fr, text='-', command=lambda: self.subtract(kind='full'))
        self.full_set_amount = tk.Label(self.full_set_fr, text='0')
        self.full_set_plus = tk.Button(self.full_set_fr, text='+', command=lambda: self.add(kind='full'))

        # Labels and buttons for normal full_set
        self.leakiness_label = tk.Label(parent, text='Nieszczelność')
        self.leakiness_fr = tk.Frame(parent)
        self.leakiness_minus = tk.Button(self.leakiness_fr, text='-', command= lambda: self.subtract('leak'))
        self.leakiness_amount = tk.Label(self.leakiness_fr, text='0')
        self.leakiness_plus = tk.Button(self.leakiness_fr, text='+', command= lambda: self.add(kind='leak'))

        # Labels and buttons for normal full_set
        self.ac_fumigation_label = tk.Label(parent, text='Odgrzybianie')
        self.ac_fumigation_fr = tk.Frame(parent)
        self.ac_fumigation_minus = tk.Button(self.ac_fumigation_fr, text='-', command= lambda: self.subtract(kind='fum'))
        self.ac_fumigation_amount = tk.Label(self.ac_fumigation_fr, text='0')
        self.ac_fumigation_plus = tk.Button(self.ac_fumigation_fr, text='+', command= lambda: self.add(kind='fum'))

        self.rand_price_label = tk.Label(parent, text='Komplet (Ponad 200 zł)')
        self.rand_price_fr = tk.Frame(parent)
        self.rand_price_entry = tk.Entry(self.rand_price_fr, width=12)
        self.rand_price_add = tk.Button(self.rand_price_fr, text='Dodaj', command=self.add_random_money)

        # Labels that show how much money were earned during that day 
        self.sum_frame = tk.LabelFrame(parent, text='Suma')

        # self.sum_label = tk.Label(self.sum_frame, text='Suma=').grid(row=3,column=0, sticky=tk.E)
        self.sum_value_label = tk.Label(self.sum_frame, text=str(self.money_earned), borderwidth=2, relief='solid', width=12, anchor='e', padx=5)
        
        # Button that triggers confirmation and sending of a raport
        self.confirm_btn = tk.Button(parent, text='Zatwierdź i wyślij raport', command=self.send_message)

        self.setup_grid()

    def setup_grid(self):
        self.date_label.grid(row=0, column=0, padx=(4,0), sticky=tk.W)
        self.date_entry.grid(row=0, column=1, padx=(20,10), pady=5)

        self.name_label.grid(row=1, column=0, padx=(4,0))
        self.name_entry.grid(row=1, column=1, padx=(20,10), pady=5)

        self.full_set_label.grid(row=2, column=0, sticky=tk.W, padx=(4,0))
        self.full_set_fr.grid(row=2, column=1, sticky=tk.E, pady=(0,5))
        self.full_set_minus.grid(row=0, column=0, padx=5)
        self.full_set_amount.grid(row=0, column=1, padx=5)
        self.full_set_plus.grid(row=0, column=2, padx=(5, 13))

        self.leakiness_label.grid(row=3, column=0, sticky=tk.W, padx=(4,0))
        self.leakiness_fr.grid(row=3, column=1, sticky=tk.E, pady=(0, 5))
        self.leakiness_minus.grid(row=0, column=0, padx=5)
        self.leakiness_amount.grid(row=0, column=1, padx=5)
        self.leakiness_plus.grid(row=0, column=2, padx=(5, 13))

        self.ac_fumigation_label.grid(row=4, column=0, sticky=tk.W, padx=(4,0))
        self.ac_fumigation_fr.grid(row=4, column=1, sticky=tk.E, pady=(0, 5))
        self.ac_fumigation_minus.grid(row=0, column=0, padx=5)
        self.ac_fumigation_amount.grid(row=0, column=1, padx=5)
        self.ac_fumigation_plus.grid(row=0, column=2, padx=(5, 13))

        self.rand_price_label.grid(row=5, column=0, sticky=tk.W, padx=(4,0))
        self.rand_price_fr.grid(row=5, column=1, sticky=tk.E, pady=(0, 5))
        self.rand_price_entry.grid(row=0, column=0, padx=(20,10), pady=5)
        self.rand_price_add.grid(row=0, column=2, padx=(5, 13))

        self.sum_frame.grid(row=6, column=1, sticky=tk.E, padx=10)
        self.sum_value_label.grid(row=0, column=1, sticky=tk.E, padx=(20, 10), pady=5)

        self.confirm_btn.grid(row=7, column=0, columnspan=2, pady=5)


    def add_random_money(self):
        self.money_earned += int(self.rand_price_entry.get())
        self.sum_value_label['text'] = str(self.money_earned)

    def add(self, kind=''):
        if not kind:
            return
        upd_mode = '+'
        if kind == 'full':
            self.no_full_set += 1
            self.full_set_amount['text'] = str(self.no_full_set)
            self.update_sum(200, upd_mode)
        elif kind == 'fum':
            self.no_ac_fumigation += 1
            self.ac_fumigation_amount['text'] = str(self.no_ac_fumigation)
            self.update_sum(50, upd_mode)
        elif kind == 'leak':
            self.no_leakiness += 1
            self.leakiness_amount['text'] = str(self.no_leakiness)
            self.update_sum(70, upd_mode)


    def subtract(self, kind=''):
        if not kind:
            return
        upd_mode = '-'
        if kind == 'full' and self.no_full_set > 0:
            self.no_full_set -= 1
            self.full_set_amount['text'] = str(self.no_full_set)
            self.update_sum(200, upd_mode)
        elif kind == 'fum' and self.no_ac_fumigation > 0:
            self.no_ac_fumigation -= 1
            self.ac_fumigation_amount['text'] = str(self.no_ac_fumigation)
            self.update_sum(50, upd_mode)
        elif kind == 'leak' and self.no_leakiness > 0:
            self.no_leakiness -= 1
            self.leakiness_amount['text'] = str(self.no_leakiness)
            self.update_sum(70, upd_mode)

    
    def update_sum(self, cost, mode):
        if mode == '+':
            self.money_earned += cost
        elif mode == '-':
            self.money_earned -= cost
        self.sum_value_label['text'] = str(self.money_earned)

    def send_message(self):
        date=str(self.date_entry.get())
        name=str(self.name_entry.get())
        no_full= str(self.full_set_amount['text'])
        no_fum= str(self.ac_fumigation_amount['text'])
        no_leak= str(self.leakiness_amount['text'])
        money= str(self.money_earned)
        send_msg(date, name, no_full, no_fum, no_leak, money)
        
        
if __name__== '__main__':
    root = tk.Tk()
    main_win = MainApp(root)
    root.mainloop()
    