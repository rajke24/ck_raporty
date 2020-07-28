import tkinter as tk
import sms

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title('CK Raporty')
        self.prices = {'full_set': 200,
                       'fum': 50,
                       'leak': 70
        }
        self.day_info = {'date':'',
                        'worker_name': '',
                        'no_full_set': 0,
                        'no_fum': 0,
                        'no_leak': 0,
                        'money_earned': 0,
                        'random_sets': {}}

        # Label and entry for inserting date of raport
        self.date_label = tk.Label(parent, text='Wprowadź datę')
        self.date_entry = tk.Entry(parent)
        
        # Label and entry for inserting name of the worker
        self.name_label = tk.Label(parent, text='Wprowadź imię i nazwisko')
        self.name_entry = tk.Entry(parent)

        # Labels and buttons for normal full_set
        self.full_set_label = tk.Label(parent, text='Komplet (200 zł)')
        self.full_set_fr = tk.Frame(parent)
        self.full_set_minus = tk.Button(self.full_set_fr, text='-', command=lambda: self.decrease_sum(kind='full_set'))
        self.full_set_amount = tk.Label(self.full_set_fr, text='0')
        self.full_set_plus = tk.Button(self.full_set_fr, text='+', command=lambda: self.increase_sum(kind='full_set'))

        # Labels and buttons for normal full_set
        self.leakiness_label = tk.Label(parent, text='Nieszczelność')
        self.leakiness_fr = tk.Frame(parent)
        self.leakiness_minus = tk.Button(self.leakiness_fr, text='-', command= lambda: self.decrease_sum('leak'))
        self.leakiness_amount = tk.Label(self.leakiness_fr, text='0')
        self.leakiness_plus = tk.Button(self.leakiness_fr, text='+', command= lambda: self.increase_sum(kind='leak'))

        # Labels and buttons for normal full_set
        self.ac_fumigation_label = tk.Label(parent, text='Odgrzybianie')
        self.ac_fumigation_fr = tk.Frame(parent)
        self.ac_fumigation_minus = tk.Button(self.ac_fumigation_fr, text='-', command= lambda: self.decrease_sum(kind='fum'))
        self.ac_fumigation_amount = tk.Label(self.ac_fumigation_fr, text='0')
        self.ac_fumigation_plus = tk.Button(self.ac_fumigation_fr, text='+', command= lambda: self.increase_sum(kind='fum'))

        self.rand_price_label = tk.Label(parent, text='Komplet (Ponad 200 zł)')
        self.rand_price_fr = tk.Frame(parent)
        self.rand_price_entry = tk.Entry(self.rand_price_fr, width=12)
        self.rand_price_increase_sum = tk.Button(self.rand_price_fr, text='Dodaj', command=self.increase_sum_random_money)

        # Labels that show how much money were earned during that day 
        self.sum_frame = tk.LabelFrame(parent, text='Suma')

        # self.sum_label = tk.Label(self.sum_frame, text='Suma=').grid(row=3,column=0, sticky=tk.E)
        self.sum_value_label = tk.Label(self.sum_frame, text=str(self.day_info['money_earned']), borderwidth=2, relief='solid', width=12, anchor='e', padx=5)
        
        # Button that triggers confirmation and sending of a raport
        self.confirm_btn = tk.Button(parent, text='Zatwierdź i wyślij raport', command= lambda: self.send_message(self.day_info))

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
        self.rand_price_increase_sum.grid(row=0, column=2, padx=(5, 13))

        self.sum_frame.grid(row=6, column=1, sticky=tk.E, padx=10)
        self.sum_value_label.grid(row=0, column=1, sticky=tk.E, padx=(20, 10), pady=5)

        self.confirm_btn.grid(row=7, column=0, columnspan=2, pady=5)


    def increase_sum_random_money(self):
        set_cost = self.rand_price_entry.get()
        self.day_info['money_earned'] += int(set_cost)
        self.sum_value_label['text'] = str(self.day_info['money_earned'])

        if not set_cost in self.day_info['random_sets']:
            self.day_info['random_sets'].setdefault(str(set_cost), 1)
        else:
            self.day_info['random_sets'][str(set_cost)] += 1
            
    
    def increase_sum(self, kind=''):
        self.day_info['no_'+ kind] += 1
        self.day_info['money_earned'] += self.prices[kind]
        self.set_amount_labels(kind)

    def decrease_sum(self, kind=''):
        if self.day_info['no_'+ kind] > 0:
            self.day_info['no_'+ kind] -= 1
            self.day_info['money_earned'] -= self.prices[kind]
        self.set_amount_labels(kind)
        
    def set_amount_labels(self, kind):
        self.sum_value_label['text'] = str(self.day_info['money_earned'])
        if kind == 'full_set':
            self.full_set_amount['text'] = str(self.day_info['no_full_set'])
        elif kind == 'fum':
            self.ac_fumigation_amount['text'] = str(self.day_info['no_fum'])
        elif kind == 'leak':
            self.leakiness_amount['text'] = str(self.day_info['no_leak'])

    def send_message(self, day_info):
        self.day_info['worker_name']= self.name_entry.get()
        self.day_info['date'] = self.date_entry.get()
        sms.send_msg(day_info)
        
        
if __name__== '__main__':
    root = tk.Tk()
    main_win = MainApp(root)
    root.mainloop()
    