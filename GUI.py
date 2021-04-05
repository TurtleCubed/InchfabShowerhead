import tkinter as tk
import tkinter.ttk as ttk
import GasNetworkSim
import numpy as np
import matplotlib.pyplot as plt
import json
import os
import shutil


class GUI:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame1 = ttk.Frame(self.toplevel1)
        self.label_hole_shape = ttk.Label(self.frame1)
        self.label_hole_shape.configure(text='Aperture Shape')
        self.label_hole_shape.grid(column='0', pady='5', row='0')
        self.combobox_hole_shape = ttk.Combobox(self.frame1)
        self.combobox_hole_shape.configure(state='readonly', values='Circle Rectangle')
        self.combobox_hole_shape.grid(column='1', columnspan='3', pady='5', row='0')
        self.label_hole_dim = ttk.Label(self.frame1)
        self.label_hole_dim.configure(text='Aperture Dimensions (inches)')
        self.label_hole_dim.grid(column='0', pady='5', row='1')
        self.entry_hole1 = ttk.Entry(self.frame1)
        self.entry_hole1.configure(validate='key', width='5')
        _text_ = '''0.039'''
        self.entry_hole1.delete('0', 'end')
        self.entry_hole1.insert('0', _text_)
        self.entry_hole1.grid(column='1', pady='5', row='1')
        self.entry_hole2 = ttk.Entry(self.frame1)
        self.entry_hole2.configure(validate='key', width='5')
        _text_ = '''0.052'''
        self.entry_hole2.delete('0', 'end')
        self.entry_hole2.insert('0', _text_)
        self.entry_hole2.grid(column='2', pady='5', row='1')
        self.entry_hole3 = ttk.Entry(self.frame1)
        self.entry_hole3.configure(validate='key', width='5')
        _text_ = '''0.075'''
        self.entry_hole3.delete('0', 'end')
        self.entry_hole3.insert('0', _text_)
        self.entry_hole3.grid(column='3', pady='5', row='1')
        self.label_hole_length = ttk.Label(self.frame1)
        self.label_hole_length.configure(text='Aperture Length (inches)')
        self.label_hole_length.grid(column='0', pady='5', row='4')
        self.entry_hole_length = ttk.Entry(self.frame1)
        self.entry_hole_length.configure(validate='key', width='5')
        _text_ = '''0.0625'''
        self.entry_hole_length.delete('0', 'end')
        self.entry_hole_length.insert('0', _text_)
        self.entry_hole_length.grid(column='2', pady='5', row='4')
        self.label_hole_width = ttk.Label(self.frame1)
        self.label_hole_width.configure(text='Aperture Width (inches)')
        self.label_hole_width.grid(column='0', row='3')
        self.entry_hole_width = ttk.Entry(self.frame1)
        self.entry_hole_width.configure(validate='key', width='5')
        _text_ = '''0'''
        self.entry_hole_width.delete('0', 'end')
        self.entry_hole_width.insert('0', _text_)
        self.entry_hole_width.grid(column='2', row='3')
        self.separator0 = ttk.Separator(self.frame1)
        self.separator0.configure(orient='horizontal')
        self.separator0.grid(column='0', columnspan='4', ipadx='100', pady='5', row='5')
        self.label_connecting_shape = ttk.Label(self.frame1)
        self.label_connecting_shape.configure(text='Connecting Tube Shape')
        self.label_connecting_shape.grid(column='0', pady='5', row='6')
        self.combobox_connecting_shape = ttk.Combobox(self.frame1)
        self.combobox_connecting_shape.configure(state='readonly', values='Circle Rectangle')
        self.combobox_connecting_shape.grid(column='1', columnspan='3', pady='5', row='6')
        self.label_connecting_dim = ttk.Label(self.frame1)
        self.label_connecting_dim.configure(text='Connecting Tube Diameter (inches)')
        self.label_connecting_dim.grid(column='0', pady='5', row='7')
        self.entry_connecting_dim = ttk.Entry(self.frame1)
        self.entry_connecting_dim.configure(validate='key', width='5')
        _text_ = '''0.125'''
        self.entry_connecting_dim.delete('0', 'end')
        self.entry_connecting_dim.insert('0', _text_)
        self.entry_connecting_dim.grid(column='2', pady='5', row='7')
        self.label_connecting_width = ttk.Label(self.frame1)
        self.label_connecting_width.configure(text='Connecting Tube Width (inches)')
        self.label_connecting_width.grid(column='0', row='8')
        self.entry_connecting_width = ttk.Entry(self.frame1)
        self.entry_connecting_width.configure(validate='key', width='4')
        _text_ = '''0'''
        self.entry_connecting_width.delete('0', 'end')
        self.entry_connecting_width.insert('0', _text_)
        self.entry_connecting_width.grid(column='2', row='8')
        self.label_connecting_length = ttk.Label(self.frame1)
        self.label_connecting_length.configure(text='Connecting Tube Length (inches)')
        self.label_connecting_length.grid(column='0', pady='5', row='9')
        self.entry_connecting_length = ttk.Entry(self.frame1)
        self.entry_connecting_length.configure(validate='key', width='5')
        _text_ = '''1.31'''
        self.entry_connecting_length.delete('0', 'end')
        self.entry_connecting_length.insert('0', _text_)
        self.entry_connecting_length.grid(column='2', pady='5', row='9')
        self.separator1 = ttk.Separator(self.frame1)
        self.separator1.configure(orient='horizontal')
        self.separator1.grid(column='0', columnspan='4', ipadx='100', pady='5', row='10')
        self.label_throughput = ttk.Label(self.frame1)
        self.label_throughput.configure(text='Throughput (SCCM)')
        self.label_throughput.grid(column='0', pady='5', row='11')
        self.entry_throughput = ttk.Entry(self.frame1)
        self.entry_throughput.configure(validate='key', width='5')
        _text_ = '''10'''
        self.entry_throughput.delete('0', 'end')
        self.entry_throughput.insert('0', _text_)
        self.entry_throughput.grid(column='2', pady='5', row='11')
        self.label_chamber_pressure = ttk.Label(self.frame1)
        self.label_chamber_pressure.configure(text='Chamber Pressure (millitorr)')
        self.label_chamber_pressure.grid(column='0', pady='5', row='12')
        self.entry_chamber_pressure = ttk.Entry(self.frame1)
        self.entry_chamber_pressure.configure(validate='key', width='5')
        _text_ = '''50'''
        self.entry_chamber_pressure.delete('0', 'end')
        self.entry_chamber_pressure.insert('0', _text_)
        self.entry_chamber_pressure.grid(column='2', pady='5', row='12')
        self.separator2 = ttk.Separator(self.frame1)
        self.separator2.configure(orient='horizontal')
        self.separator2.grid(column='0', columnspan='4', ipadx='100', padx='5', row='13')
        self.label_gas = ttk.Label(self.frame1)
        self.label_gas.configure(text='Gas')
        self.label_gas.grid(column='0', pady='5', row='14')
        self.combobox_gas = ttk.Combobox(self.frame1)
        self.combobox_gas.configure(state='readonly', values='He N2 O2 Ar')
        self.combobox_gas.grid(column='1', columnspan='3', pady='5', row='14')
        self.label_gamma = ttk.Label(self.frame1)
        self.label_gamma.configure(text='Gamma')
        self.label_gamma.grid(column='0', pady='5', row='15')
        self.entry_gamma = ttk.Entry(self.frame1)
        _text_ = '''1.608'''
        self.entry_gamma.delete('0', 'end')
        self.entry_gamma.insert('0', _text_)
        self.entry_gamma.grid(column='1', columnspan='3', pady='5', row='15')
        self.label_molar_mass = ttk.Label(self.frame1)
        self.label_molar_mass.configure(text='Molar Mass (Kg/mol)')
        self.label_molar_mass.grid(column='0', pady='5', row='16')
        self.entry_molar_mass = ttk.Entry(self.frame1)
        _text_ = '''0.03756'''
        self.entry_molar_mass.delete('0', 'end')
        self.entry_molar_mass.insert('0', _text_)
        self.entry_molar_mass.grid(column='1', columnspan='3', padx='5', row='16')
        self.label_particle_diameter = ttk.Label(self.frame1)
        self.label_particle_diameter.configure(text='Particle Diameter (m)')
        self.label_particle_diameter.grid(column='0', pady='5', row='17')
        self.entry_particle_diameter = ttk.Entry(self.frame1)
        _text_ = '''0.0000000003448'''
        self.entry_particle_diameter.delete('0', 'end')
        self.entry_particle_diameter.insert('0', _text_)
        self.entry_particle_diameter.grid(column='1', columnspan='3', pady='5', row='17')
        self.label_viscosity = ttk.Label(self.frame1)
        self.label_viscosity.configure(text='Viscosity (Pa*s)')
        self.label_viscosity.grid(column='0', pady='5', row='18')
        self.entry_viscosity = ttk.Entry(self.frame1)
        _text_ = '''0.00002136'''
        self.entry_viscosity.delete('0', 'end')
        self.entry_viscosity.insert('0', _text_)
        self.entry_viscosity.grid(column='1', columnspan='3', pady='5', row='18')
        self.separator3 = ttk.Separator(self.frame1)
        self.separator3.configure(orient='horizontal')
        self.separator3.grid(column='0', columnspan='4', ipadx='100', pady='5', row='19')
        self.label_temperature = ttk.Label(self.frame1)
        self.label_temperature.configure(text='Temperature (K)')
        self.label_temperature.grid(column='0', pady='5', row='20')
        self.entry_temperature = ttk.Entry(self.frame1)
        self.entry_temperature.configure(validate='key')
        _text_ = '''298'''
        self.entry_temperature.delete('0', 'end')
        self.entry_temperature.insert('0', _text_)
        self.entry_temperature.grid(column='2', pady='5', row='20')
        self.label_r = ttk.Label(self.frame1)
        self.label_r.configure(text='Gas Constant (J/mol*K)')
        self.label_r.grid(column='0', pady='5', row='21')
        self.entry_gas_constant = ttk.Entry(self.frame1)
        self.entry_gas_constant.configure(validate='key')
        _text_ = '''8.314'''
        self.entry_gas_constant.delete('0', 'end')
        self.entry_gas_constant.insert('0', _text_)
        self.entry_gas_constant.grid(column='2', pady='5', row='21')
        self.button_simulate = ttk.Button(self.frame1)
        self.button_simulate.configure(text='Run Simulation')
        self.button_simulate.grid(column='0', columnspan='4', pady='5', row='22')
        self.button_simulate.configure(command=self.run_simulate)
        self.frame1.configure(width='200')
        self.frame1.pack(side='top')
        self.toplevel1.configure(height='200', width='200')

        self.toplevel2 = tk.Toplevel(master)
        self.frame2 = ttk.Frame(self.toplevel2)
        self.scrollbar_y = ttk.Scrollbar(self.frame2)
        self.scrollbar_y.configure(orient='vertical')
        self.scrollbar_y.grid(column='1', ipady='100', row='0', sticky='w')
        self.scrollbar_x = ttk.Scrollbar(self.frame2)
        self.scrollbar_x.configure(orient='horizontal')
        self.scrollbar_x.grid(column='0', ipadx='180', row='1', sticky='n')
        self.text1 = tk.Text(self.frame2)
        self.text1.configure(height='20', state='disabled', width='75', wrap='none')
        self.text1.grid(column='0', row='0')
        self.text1.rowconfigure('0', pad='0')
        self.label_image = ttk.Label(self.frame2)
        self.blank_png = tk.PhotoImage(file='blank.png')
        self.label_image.configure(image=self.blank_png)
        self.label_image.grid(column='2', columnspan='2', row='0')
        self.label_optimized = ttk.Label(self.frame2)
        self.label_optimized.configure(text='Optimized Dimensions')
        self.label_optimized.grid(column='0', row='4')
        self.entry_dim1 = ttk.Entry(self.frame2)
        self.entry_dim1.configure(state='readonly')
        self.entry_dim1.grid(column='2', row='4')
        self.entry_dim2 = ttk.Entry(self.frame2)
        self.entry_dim2.configure(state='readonly')
        self.entry_dim2.grid(column='3', row='4')
        self.entry_dim3 = ttk.Entry(self.frame2)
        self.entry_dim3.configure(state='readonly')
        self.entry_dim3.grid(column='4', row='4')
        self.separator4 = ttk.Separator(self.frame2)
        self.separator4.configure(orient='horizontal')
        self.separator4.grid(column='0', columnspan='5', ipadx='300', pady='5', row='5')
        self.notebook_tolerances = ttk.Notebook(self.frame2)
        self.frame_default = ttk.Frame(self.notebook_tolerances)
        self.label_defaultcv = ttk.Label(self.frame_default)
        self.label_defaultcv.configure(text='Coefficient of Variation:')
        self.label_defaultcv.grid(column='0', row='0')
        self.entry_defaultcv = ttk.Entry(self.frame_default)
        self.entry_defaultcv.configure(state='readonly')
        self.entry_defaultcv.grid(column='1', row='0')
        self.label_imagedefault = ttk.Label(self.frame_default)
        self.blank_png = tk.PhotoImage(file='blank.png')
        self.label_imagedefault.configure(image=self.blank_png)
        self.label_imagedefault.grid(column='0', columnspan='2', row='1')
        self.frame_default.pack(side='top')
        self.notebook_tolerances.add(self.frame_default, text='Default')
        self.frame_highq = ttk.Frame(self.notebook_tolerances)
        self.label_highqcv = ttk.Label(self.frame_highq)
        self.label_highqcv.configure(text='Coefficient of Variation:')
        self.label_highqcv.grid(column='0', row='0')
        self.entry_highqcv = ttk.Entry(self.frame_highq)
        self.entry_highqcv.configure(state='readonly')
        self.entry_highqcv.grid(column='1', row='0')
        self.label_imagehighq = ttk.Label(self.frame_highq)
        self.blank_png = tk.PhotoImage(file='blank.png')
        self.label_imagehighq.configure(image=self.blank_png)
        self.label_imagehighq.grid(column='0', columnspan='2', row='1')
        self.frame_highq.configure(height='200', width='200')
        self.frame_highq.pack(side='top')
        self.notebook_tolerances.add(self.frame_highq, text='200% Throughput')
        self.frame_lowq = ttk.Frame(self.notebook_tolerances)
        self.label_lowqcv = ttk.Label(self.frame_lowq)
        self.label_lowqcv.configure(text='Coefficient of Variation:')
        self.label_lowqcv.grid(column='0', row='0')
        self.entry_lowqcv = ttk.Entry(self.frame_lowq)
        self.entry_lowqcv.configure(state='readonly')
        self.entry_lowqcv.grid(column='1', row='0')
        self.label_imagelowq = ttk.Label(self.frame_lowq)
        self.blank_png = tk.PhotoImage(file='blank.png')
        self.label_imagelowq.configure(image=self.blank_png)
        self.label_imagelowq.grid(column='0', columnspan='2', row='1')
        self.frame_lowq.configure(height='200', width='200')
        self.frame_lowq.pack(side='top')
        self.notebook_tolerances.add(self.frame_lowq, text='50% Throughput')
        self.frame_small1 = ttk.Frame(self.notebook_tolerances)
        self.label_smallcv = ttk.Label(self.frame_small1)
        self.label_smallcv.configure(text='Coefficient of Variation:')
        self.label_smallcv.grid(column='0', row='0')
        self.entry_smallcv = ttk.Entry(self.frame_small1)
        self.entry_smallcv.configure(state='readonly')
        self.entry_smallcv.grid(column='1', row='0')
        self.label_imagesmall = ttk.Label(self.frame_small1)
        self.blank_png = tk.PhotoImage(file='blank.png')
        self.label_imagesmall.configure(image=self.blank_png)
        self.label_imagesmall.grid(column='0', columnspan='2', row='1')
        self.frame_small1.configure(height='200', width='200')
        self.frame_small1.pack(side='top')
        self.notebook_tolerances.add(self.frame_small1, text='1st Opening 1 mil Small')
        self.frame_large1 = ttk.Frame(self.notebook_tolerances)
        self.label_largecv = ttk.Label(self.frame_large1)
        self.label_largecv.configure(text='Coefficient of Variation:')
        self.label_largecv.grid(column='0', row='0')
        self.entry_largecv = ttk.Entry(self.frame_large1)
        self.entry_largecv.configure(state='readonly')
        self.entry_largecv.grid(column='1', row='0')
        self.label_imagelarge = ttk.Label(self.frame_large1)
        self.blank_png = tk.PhotoImage(file='blank.png')
        self.label_imagelarge.configure(image=self.blank_png)
        self.label_imagelarge.grid(column='0', columnspan='2', row='1')
        self.frame_large1.configure(height='200', width='200')
        self.frame_large1.pack(side='top')
        self.notebook_tolerances.add(self.frame_large1, text='1st Opening 1 mil Large')
        self.notebook_tolerances.configure(height='350', width='450')
        self.notebook_tolerances.grid(column='0', columnspan='5', row='11')
        self.frame2.configure(height='200', width='200')
        self.frame2.pack(side='top')
        self.toplevel2.configure(height='200', width='200')

        vcmd = (self.frame1.register(self.onValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.entry_hole1.config(validatecommand=vcmd)
        self.entry_hole2.config(validatecommand=vcmd)
        self.entry_hole_width.config(validatecommand=vcmd)
        self.entry_hole_length.config(validatecommand=vcmd)
        self.entry_connecting_dim.config(validatecommand=vcmd)
        self.entry_connecting_width.config(validatecommand=vcmd)
        self.entry_connecting_length.config(validatecommand=vcmd)
        self.entry_temperature.config(validatecommand=vcmd)
        self.entry_gas_constant.config(validatecommand=vcmd)

        _, _, filenames = next(os.walk(os.path.join('Gas_Data')))
        gas_list = []
        for file in filenames:
            gas_list.append(file[0:file.index('.json')])
        self.combobox_gas.configure(state='readonly', values=gas_list)
        self.combobox_gas.bind('<<ComboboxSelected>>', self.on_gas_select)
        self.scrollbar_x.configure(command=self.text1.xview)
        self.scrollbar_y.configure(command=self.text1.yview)
        self.text1.configure(xscrollcommand=self.scrollbar_x.set)
        self.text1.configure(yscrollcommand=self.scrollbar_y.set)
        self.combobox_hole_shape.bind('<<ComboboxSelected>>', self.on_hole_shape_select)
        self.combobox_connecting_shape.bind('<<ComboboxSelected>>', self.on_connecting_shape_select)
        self.label_hole_width.grid_forget()
        self.entry_hole_width.grid_forget()
        self.label_connecting_width.grid_forget()
        self.entry_connecting_width.grid_forget()
        self.toplevel2.withdraw()
        self.toplevel2.protocol("WM_DELETE_WINDOW", self.on_sub_close)
        self.toplevel1.protocol("WM_DELETE_WINDOW", self.on_main_close)
        self.my_image = tk.PhotoImage()
        self.currently_running = False
        self.successful_run = False

        self.notebook_tolerances.bind('<<NotebookTabChanged>>', self.on_tab_select)
        self.tol_dict = {}

        # Main widget
        self.mainwindow = self.toplevel1

    def run_simulate(self):
        if self.currently_running:
            pass
        else:
            self.toplevel2.deiconify()
            # Parse data from the main window
            # Check if each is a valid entry
            self.currently_running = True
            self.successful_run = False
            try:
                if self.combobox_hole_shape.get() == 'Circle':
                    shp_o = 'circle'
                elif self.combobox_hole_shape.get() == 'Rectangle':
                    shp_o = 'rectangle'
                else:
                    raise ValueError("Aperture shape not selected")
                dim_o = [float(self.entry_hole1.get()), float(self.entry_hole2.get()), float(self.entry_hole3.get())]
                len_o = float(self.entry_hole_length.get())
                if self.combobox_connecting_shape.get() == 'Circle':
                    shp_c = 'circle'
                elif self.combobox_connecting_shape.get() == 'Rectangle':
                    shp_c = 'rectangle'
                else:
                    raise ValueError("Connecting pipe shape not selected")
                width_o = float(self.entry_hole_width.get())
                width_c = float(self.entry_connecting_width.get())
                dim_c = float(self.entry_connecting_dim.get())
                len_c = float(self.entry_connecting_length.get())
                thr = float(self.entry_throughput.get())
                ch_p = float(self.entry_chamber_pressure.get())
                gam = float(self.entry_gamma.get())
                mol_m = float(self.entry_molar_mass.get())
                par_d = float(self.entry_particle_diameter.get())
                vis = float(self.entry_viscosity.get())
                tem = float(self.entry_temperature.get())
                gas_r = float(self.entry_gas_constant.get())
                run = True
            except ValueError as error:
                self.append_txt(str(error) + '\n')
                run = False
                self.currently_running = False
            if run:
                self.append_txt('Optimizing...\n')
                try:
                    optimized_dim = self.optimize(shp_o, dim_o, width_o, len_o, shp_c, dim_c, width_c,
                                                  len_c, thr, ch_p, gam, mol_m, par_d, vis, tem, gas_r)
                    self.update_text(self.entry_dim1, str(optimized_dim[0]))
                    self.update_text(self.entry_dim2, str(optimized_dim[1]))
                    self.update_text(self.entry_dim3, str(optimized_dim[2]))
                    self.append_txt('...Finished!\n')
                    self.successful_run = True
                except RuntimeError:
                    self.append_txt('Run failed\n')
                self.currently_running = False

    def optimize(self, shape_o, dim_o, width_o, length_o, shape_c, dim_c, width_c, length_c, throughput,
                 chamber_pressure, gamma, molar_mass, particle_diameter, viscosity, temp, r_0):
        try:
            shutil.rmtree(os.path.join('temp'))
        except FileNotFoundError:
            pass
        self.tol_dict.clear()
        current_dim = dim_o
        depth = 0
        max_depth = len(current_dim)

        self.append_txt('Running with dimensions:')
        self.append_txt(str(current_dim))
        self.append_txt('\n')
        q = GasNetworkSim.sim(shape_o, current_dim, width_o, length_o, shape_c, dim_c, width_c, length_c, throughput,
                              chamber_pressure, gamma, molar_mass, particle_diameter, viscosity, temp, r_0)
        self.update_image(self.label_image, self.generate_graph(q, 'plot'))

        mean = np.mean(q)
        std = np.std(q)
        cv = std / mean
        devs = [(a - mean) / mean for a in q]
        index = [0] * len(devs)
        temp_devs = [abs(a) for a in devs]
        for i in range(len(devs)):
            index[temp_devs.index(max(temp_devs))] = i
            temp_devs[temp_devs.index(max(temp_devs))] = min(temp_devs) - 1
        self.append_txt('  Found throughputs: ' + str([round(a / 101325 * (60 * 10 ** 6), 3) for a in q]) + '\n')
        self.append_txt('  With coefficient of variation: ' + str(round(cv, 5)) + '\n')

        while depth < max_depth:
            temp_dim = current_dim.copy()
            if devs[index.index(depth)] < 0:
                temp_dim[index.index(depth)] += 0.001
            else:
                temp_dim[index.index(depth)] -= 0.001

            self.append_txt('Running with dimensions:')
            self.append_txt(str(temp_dim))
            self.append_txt('\n')
            temp_q = GasNetworkSim.sim(shape_o, temp_dim, width_o, length_o, shape_c, dim_c, width_c, length_c,
                                       throughput, chamber_pressure, gamma, molar_mass, particle_diameter, viscosity,
                                       temp, r_0)
            self.update_image(self.label_image, self.generate_graph(temp_q, 'plot'))
            temp_mean = np.mean(temp_q)
            temp_std = np.std(temp_q)
            temp_cv = temp_std / temp_mean
            self.append_txt('  Found throughputs: '
                            + str([round(a / 101325 * (60 * 10 ** 6), 3) for a in temp_q]) + '\n')
            self.append_txt('  With coefficient of variation: ' + str(round(temp_cv, 5)) + '\n')

            if temp_cv < cv:
                current_dim = temp_dim
                cv = temp_cv
                depth = 0
                q = temp_q
                mean = np.mean(q)
                std = np.std(q)
                devs = [(a - mean) / mean for a in q]
                index = [0] * len(devs)
                temp_devs = [abs(a) for a in devs]
                for i in range(len(devs)):
                    index[temp_devs.index(max(temp_devs))] = i
                    temp_devs[temp_devs.index(max(temp_devs))] = min(temp_devs) - 1
            else:
                depth += 1
        q_tol = [None]*5
        q_tol[0] = GasNetworkSim.sim(shape_o, current_dim, width_o, length_o, shape_c, dim_c, width_c, length_c,
                                     throughput, chamber_pressure, gamma, molar_mass, particle_diameter, viscosity,
                                     temp, r_0)
        q_tol[1] = GasNetworkSim.sim(shape_o, current_dim, width_o, length_o, shape_c, dim_c, width_c, length_c,
                                     throughput * 2, chamber_pressure, gamma, molar_mass, particle_diameter, viscosity,
                                     temp, r_0)
        q_tol[2] = GasNetworkSim.sim(shape_o, current_dim, width_o, length_o, shape_c, dim_c, width_c, length_c,
                                     throughput * 0.5, chamber_pressure, gamma, molar_mass, particle_diameter,
                                     viscosity,
                                     temp, r_0)
        small_dim = (current_dim[0] - 0.001, current_dim[1], current_dim[2])
        large_dim = (current_dim[0] + 0.001, current_dim[1], current_dim[2])
        q_tol[3] = GasNetworkSim.sim(shape_o, small_dim, width_o, length_o, shape_c, dim_c, width_c, length_c,
                                     throughput, chamber_pressure, gamma, molar_mass, particle_diameter, viscosity,
                                     temp, r_0)
        q_tol[4] = GasNetworkSim.sim(shape_o, large_dim, width_o, length_o, shape_c, dim_c, width_c, length_c,
                                     throughput, chamber_pressure, gamma, molar_mass, particle_diameter, viscosity,
                                     temp, r_0)
        for i in range(len(q_tol)):
            qs = q_tol[i]
            cv = np.std(q_tol[i]) / np.mean(q_tol[i])
            image = self.generate_graph(q_tol[i], str(i))
            self.tol_dict[i] = {'Q': qs, 'CV': cv, 'IMAGE': image}
        self.update_image(self.label_image, self.tol_dict[0]['IMAGE'])
        return current_dim

    def onValidate(self, d, i, P, s, S, v, V, W):
        try:
            float(P)
            return True
        except ValueError:
            self.frame1.bell()
            return False

    def on_tab_select(self, event):
        if self.successful_run:
            selected = self.notebook_tolerances.index(self.notebook_tolerances.select())
            tab_dict = self.tol_dict[selected]
            if selected == 0:
                self.update_text(self.entry_defaultcv, str(round(tab_dict['CV'], 5)))
                self.update_image(self.label_imagedefault, tab_dict['IMAGE'])
            elif selected == 1:
                self.update_text(self.entry_highqcv, str(round(tab_dict['CV'], 5)))
                self.update_image(self.label_imagehighq, tab_dict['IMAGE'])
            elif selected == 2:
                self.update_text(self.entry_lowqcv, str(round(tab_dict['CV'], 5)))
                self.update_image(self.label_imagelowq, tab_dict['IMAGE'])
            elif selected == 3:
                self.update_text(self.entry_smallcv, str(round(tab_dict['CV'], 5)))
                self.update_image(self.label_imagesmall, tab_dict['IMAGE'])
            elif selected == 4:
                self.update_text(self.entry_largecv, str(round(tab_dict['CV'], 5)))
                self.update_image(self.label_imagelarge, tab_dict['IMAGE'])
            else:
                pass

    def generate_graph(self, q, name):
        x = [1, 2, 3]
        y = [a / 101325 * (60 * 10 ** 6) for a in q]
        mean = np.mean(y)
        px = 1/plt.rcParams['figure.dpi']
        plt.subplots(figsize=(500*px, 300*px))
        plt.xlabel('Opening')
        plt.ylabel('Throughput (SCCM)')
        plt.ylim(mean * 0.75, mean * 1.25)
        plt.plot(x, y)
        plt.plot(x, [mean] * 3)
        for i in range(len(y)):
            plt.text(i + 1, y[i] + mean * 0.02, str(round(y[i], 2)), horizontalalignment='center')
        plt.tight_layout()
        try:
            os.mkdir('temp')
        except FileExistsError:
            pass
        plt.savefig(os.path.join('temp', name + '.png'))
        return os.path.join('temp', name + '.png')

    def on_hole_shape_select(self, eventObject):
        if self.combobox_hole_shape.get() == 'Circle':
            self.label_hole_dim.config(text='Aperture Diameters')
            self.entry_hole_width.grid_forget()
            self.label_hole_width.grid_forget()
            self.entry_hole_width.delete('0', 'end')
            self.entry_hole_width.insert('0', '0')
        else:
            self.label_hole_dim.config(text='Aperture Height')
            self.label_hole_width.grid(column=0, row=3)
            self.entry_hole_width.grid(column=2, row=3)

    def on_connecting_shape_select(self, eventObject):
        if self.combobox_connecting_shape.get() == 'Circle':
            self.label_connecting_dim.config(text='Connecting Tube Diameter')
            self.entry_connecting_width.grid_forget()
            self.label_connecting_width.grid_forget()
            self.entry_connecting_width.delete('0', 'end')
            self.entry_connecting_width.insert('0', '0')
        else:
            self.label_connecting_dim.config(text='Connecting Tube Height')
            self.label_connecting_width.grid(column=0, row=8)
            self.entry_connecting_width.grid(column=2, row=8)

    def on_main_close(self):
        quit()

    def on_sub_close(self):
        self.toplevel2.withdraw()

    def on_gas_select(self, eventObject):
        gas = 'Gas_Data\\' + self.combobox_gas.get() + '.json'
        with open(gas) as f:
            gas_data = json.load(f)
        self.entry_gamma.delete('0', 'end')
        self.entry_gamma.insert('0', gas_data['Gamma'])
        self.entry_gamma.update()
        self.entry_molar_mass.delete('0', 'end')
        self.entry_molar_mass.insert('0', gas_data['Molar Mass'])
        self.entry_molar_mass.update()
        self.entry_particle_diameter.delete('0', 'end')
        self.entry_particle_diameter.insert('0', gas_data['Particle Diameter'])
        self.entry_particle_diameter.update()
        self.entry_viscosity.delete('0', 'end')
        self.entry_viscosity.insert('0', gas_data['Viscosity'])
        self.entry_viscosity.update()

    def update_text(self, entry, text):
        entry.configure(state='normal')
        entry.delete('0', 'end')
        entry.insert('end', text)
        entry.configure(state='readonly')
        entry.update()

    def update_image(self, label, file_name):
        label.image = tk.PhotoImage(file=file_name)
        label.config(image=label.image)

    def append_txt(self, text):
        self.text1.config(state='normal')
        self.text1.insert('end', text)
        self.text1.update()
        self.text1.config(state='disabled')
        self.text1.yview(tk.END)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = GUI()
    app.run()

