import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
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
        self.label_hole_shape.grid(column='0', pady='5', row='0', sticky='e')
        self.combobox_hole_shape = ttk.Combobox(self.frame1)
        self.combobox_hole_shape.configure(state='readonly', values='Circle Rectangle')
        self.combobox_hole_shape.grid(column='1', columnspan='3', pady='5', row='0')
        self.scrollbar_canvas = ttk.Scrollbar(self.frame1)
        self.scrollbar_canvas.configure(orient='vertical')
        self.scrollbar_canvas.grid(column='8', ipady='300', row='0', rowspan='30')
        self.canvas1 = tk.Canvas(self.frame1)
        self.canvas1.configure(confine='true', height='800', scrollregion=(0, 0, 600, 1000), width='1000')
        self.canvas1.grid(column='7', columnspan='1', row='0', rowspan='30')
        self.canvas1.configure(yscrollcommand=self.scrollbar_canvas.set)
        self.label_hole_count = ttk.Label(self.frame1)
        self.label_hole_count.configure(text='Number of Openings')
        self.label_hole_count.grid(column='0', row='1', sticky='e')
        self.combobox_hole_count = ttk.Combobox(self.frame1)
        self.combobox_hole_count.configure(state='readonly', values='6 8 10', width='5')
        self.combobox_hole_count.grid(column='1', columnspan='3', row='1')
        self.label_hole_dim = ttk.Label(self.frame1)
        self.label_hole_dim.configure(text='Aperture Dimensions')
        self.label_hole_dim.grid(column='0', pady='5', row='2', sticky='e')
        self.entry_hole1 = ttk.Entry(self.frame1)
        self.entry_hole1.configure(validate='key', width='5')
        _text_ = '''0.039'''
        self.entry_hole1.delete('0', 'end')
        self.entry_hole1.insert('0', _text_)
        self.entry_hole1.grid(column='2', padx='2', pady='5', row='2')
        self.entry_hole2 = ttk.Entry(self.frame1)
        self.entry_hole2.configure(validate='key', width='5')
        _text_ = '''0.052'''
        self.entry_hole2.delete('0', 'end')
        self.entry_hole2.insert('0', _text_)
        self.entry_hole2.grid(column='3', padx='2', pady='5', row='2')
        self.entry_hole3 = ttk.Entry(self.frame1)
        self.entry_hole3.configure(validate='key', width='5')
        _text_ = '''0.075'''
        self.entry_hole3.delete('0', 'end')
        self.entry_hole3.insert('0', _text_)
        self.entry_hole3.grid(column='4', padx='2', pady='5', row='2')
        self.entry_hole4 = ttk.Entry(self.frame1)
        self.entry_hole4.configure(validate='key', width='5')
        self.entry_hole4.grid(column='5', padx='2', pady='5', row='2')
        self.entry_hole5 = ttk.Entry(self.frame1)
        self.entry_hole5.configure(validate='key', width='5')
        self.entry_hole5.grid(column='6', padx='2', pady='5', row='2')
        self.combobox_units_holedim = ttk.Combobox(self.frame1)
        self.combobox_units_holedim.configure(state='readonly', values='(in.) (mil) (m) (mm)', width='8')
        self.combobox_units_holedim.grid(column='1', padx='5', row='2')
        self.label_hole_width = ttk.Label(self.frame1)
        self.label_hole_width.configure(text='Aperture Width')
        self.label_hole_width.grid(column='0', row='3', sticky='e')
        self.combobox_units_holewidth = ttk.Combobox(self.frame1)
        self.combobox_units_holewidth.configure(state='readonly', values='(in.) (mil) (m) (mm)', width='8')
        self.combobox_units_holewidth.grid(column='1', padx='5', row='3')
        self.entry_hole_width = ttk.Entry(self.frame1)
        self.entry_hole_width.configure(validate='key', width='10')
        _text_ = '''0'''
        self.entry_hole_width.delete('0', 'end')
        self.entry_hole_width.insert('0', _text_)
        self.entry_hole_width.grid(column='2', columnspan='3', pady='5', row='3')
        self.label_hole_length = ttk.Label(self.frame1)
        self.label_hole_length.configure(text='Aperture Length')
        self.label_hole_length.grid(column='0', pady='5', row='4', sticky='e')
        self.combobox_units_holelength = ttk.Combobox(self.frame1)
        self.combobox_units_holelength.configure(state='readonly', values='(in.) (mil) (m) (mm)', width='8')
        self.combobox_units_holelength.grid(column='1', padx='5', row='4')
        self.entry_hole_length = ttk.Entry(self.frame1)
        self.entry_hole_length.configure(validate='key', width='10')
        _text_ = '''0.0625'''
        self.entry_hole_length.delete('0', 'end')
        self.entry_hole_length.insert('0', _text_)
        self.entry_hole_length.grid(column='2', columnspan='3', pady='5', row='4')
        self.separator0 = ttk.Separator(self.frame1)
        self.separator0.configure(orient='horizontal')
        self.separator0.grid(column='0', columnspan='5', ipadx='150', pady='5', row='5')
        self.label_ring_tube_dim = ttk.Label(self.frame1)
        self.label_ring_tube_dim.configure(text='Ring Tube Diameter')
        self.label_ring_tube_dim.grid(column='0', pady='5', row='7', sticky='e')
        self.combobox_units_ring_tube_dim = ttk.Combobox(self.frame1)
        self.combobox_units_ring_tube_dim.configure(state='readonly', values='(in.) (mil) (m) (mm)', width='8')
        self.combobox_units_ring_tube_dim.grid(column='1', padx='5', row='7')
        self.entry_ring_tube_dim = ttk.Entry(self.frame1)
        self.entry_ring_tube_dim.configure(validate='key', width='10')
        _text_ = '''0.125'''
        self.entry_ring_tube_dim.delete('0', 'end')
        self.entry_ring_tube_dim.insert('0', _text_)
        self.entry_ring_tube_dim.grid(column='2', columnspan='3', pady='5', row='7')
        self.label_ring_diameter = ttk.Label(self.frame1)
        self.label_ring_diameter.configure(text='Ring Diameter')
        self.label_ring_diameter.grid(column='0', pady='5', row='9', sticky='e')
        self.combobox_units_ring_diameter = ttk.Combobox(self.frame1)
        self.combobox_units_ring_diameter.configure(state='readonly', values='(in.) (mil) (m) (mm)', width='8')
        self.combobox_units_ring_diameter.grid(column='1', padx='5', row='9')
        self.entry_ring_diameter = ttk.Entry(self.frame1)
        self.entry_ring_diameter.configure(validate='key', width='10')
        _text_ = '''2.5'''
        self.entry_ring_diameter.delete('0', 'end')
        self.entry_ring_diameter.insert('0', _text_)
        self.entry_ring_diameter.grid(column='2', columnspan='3', pady='5', row='9')
        self.separator1 = ttk.Separator(self.frame1)
        self.separator1.configure(orient='horizontal')
        self.separator1.grid(column='0', columnspan='5', ipadx='150', pady='5', row='10')
        self.label_throughput = ttk.Label(self.frame1)
        self.label_throughput.configure(text='Throughput')
        self.label_throughput.grid(column='0', pady='5', row='11', sticky='e')
        self.combobox_units_throughput = ttk.Combobox(self.frame1)
        self.combobox_units_throughput.configure(state='readonly', values='(sccm) (Pa*m^3/s)', width='8')
        self.combobox_units_throughput.grid(column='1', padx='5', row='11')
        self.entry_throughput = ttk.Entry(self.frame1)
        self.entry_throughput.configure(validate='key', width='10')
        _text_ = '''10'''
        self.entry_throughput.delete('0', 'end')
        self.entry_throughput.insert('0', _text_)
        self.entry_throughput.grid(column='2', columnspan='3', pady='5', row='11')
        self.label_chamber_pressure = ttk.Label(self.frame1)
        self.label_chamber_pressure.configure(text='Chamber Pressure')
        self.label_chamber_pressure.grid(column='0', pady='5', row='12', sticky='e')
        self.combobox_units_pressure = ttk.Combobox(self.frame1)
        self.combobox_units_pressure.configure(state='readonly', values='(millitorr) (torr) (atm) (bar) (Pa)',
                                               width='8')
        self.combobox_units_pressure.grid(column='1', padx='5', row='12')
        self.entry_chamber_pressure = ttk.Entry(self.frame1)
        self.entry_chamber_pressure.configure(validate='key', width='10')
        _text_ = '''50'''
        self.entry_chamber_pressure.delete('0', 'end')
        self.entry_chamber_pressure.insert('0', _text_)
        self.entry_chamber_pressure.grid(column='2', columnspan='3', pady='5', row='12')
        self.separator2 = ttk.Separator(self.frame1)
        self.separator2.configure(orient='horizontal')
        self.separator2.grid(column='0', columnspan='5', ipadx='150', padx='5', row='13')
        self.label_gas = ttk.Label(self.frame1)
        self.label_gas.configure(text='Gas')
        self.label_gas.grid(column='0', pady='5', row='14', sticky='e')
        self.combobox_gas = ttk.Combobox(self.frame1)
        self.combobox_gas.configure(state='readonly', values='He N2 O2 Ar')
        self.combobox_gas.grid(column='1', columnspan='3', pady='5', row='14')
        self.label_gamma = ttk.Label(self.frame1)
        self.label_gamma.configure(text='Gamma')
        self.label_gamma.grid(column='0', pady='5', row='15', sticky='e')
        self.entry_gamma = ttk.Entry(self.frame1)
        self.entry_gamma.configure(validate='key')
        _text_ = '''1.608'''
        self.entry_gamma.delete('0', 'end')
        self.entry_gamma.insert('0', _text_)
        self.entry_gamma.grid(column='1', columnspan='3', pady='5', row='15')
        self.label_molar_mass = ttk.Label(self.frame1)
        self.label_molar_mass.configure(text='Molar Mass (Kg/mol)')
        self.label_molar_mass.grid(column='0', pady='5', row='16', sticky='e')
        self.entry_molar_mass = ttk.Entry(self.frame1)
        self.entry_molar_mass.configure(validate='key')
        _text_ = '''0.03756'''
        self.entry_molar_mass.delete('0', 'end')
        self.entry_molar_mass.insert('0', _text_)
        self.entry_molar_mass.grid(column='1', columnspan='3', padx='5', row='16')
        self.label_particle_diameter = ttk.Label(self.frame1)
        self.label_particle_diameter.configure(text='Particle Diameter (m)')
        self.label_particle_diameter.grid(column='0', pady='5', row='17', sticky='e')
        self.entry_particle_diameter = ttk.Entry(self.frame1)
        self.entry_particle_diameter.configure(validate='key')
        _text_ = '''0.0000000003448'''
        self.entry_particle_diameter.delete('0', 'end')
        self.entry_particle_diameter.insert('0', _text_)
        self.entry_particle_diameter.grid(column='1', columnspan='3', pady='5', row='17')
        self.label_viscosity = ttk.Label(self.frame1)
        self.label_viscosity.configure(text='Viscosity (Pa*s)')
        self.label_viscosity.grid(column='0', pady='5', row='18', sticky='e')
        self.entry_viscosity = ttk.Entry(self.frame1)
        self.entry_viscosity.configure(validate='key')
        _text_ = '''0.00002136'''
        self.entry_viscosity.delete('0', 'end')
        self.entry_viscosity.insert('0', _text_)
        self.entry_viscosity.grid(column='1', columnspan='3', pady='5', row='18')
        self.separator3 = ttk.Separator(self.frame1)
        self.separator3.configure(orient='horizontal')
        self.separator3.grid(column='0', columnspan='5', ipadx='150', pady='5', row='19')
        self.label_temperature = ttk.Label(self.frame1)
        self.label_temperature.configure(text='Temperature')
        self.label_temperature.grid(column='0', pady='5', row='20', sticky='e')
        self.entry_temperature = ttk.Entry(self.frame1)
        self.entry_temperature.configure(validate='key', width='10')
        _text_ = '''298'''
        self.entry_temperature.delete('0', 'end')
        self.entry_temperature.insert('0', _text_)
        self.entry_temperature.grid(column='2', columnspan='3', pady='5', row='20')
        self.label_r = ttk.Label(self.frame1)
        self.label_r.configure(text='Gas Constant (J/mol*K)')
        self.label_r.grid(column='0', pady='5', row='21', sticky='e')
        self.entry_gas_constant = ttk.Entry(self.frame1)
        self.entry_gas_constant.configure(validate='key')
        _text_ = '''8.314'''
        self.entry_gas_constant.delete('0', 'end')
        self.entry_gas_constant.insert('0', _text_)
        self.entry_gas_constant.grid(column='1', columnspan='3', pady='5', row='21')
        self.button_import = ttk.Button(self.frame1)
        self.button_import.configure(text='Import From JSON')
        self.button_import.grid(column='0', columnspan='4', row='22')
        self.button_import.configure(command=self.import_from_json)
        self.button_simulate = ttk.Button(self.frame1)
        self.button_simulate.configure(text='Optimize Dimensions')
        self.button_simulate.grid(column='0', columnspan='4', pady='5', row='23')
        self.button_simulate.configure(command=self.run_simulate)
        self.button_run_once = ttk.Button(self.frame1)
        self.button_run_once.configure(text='Run Once')
        self.button_run_once.grid(column='2', columnspan='2', row='23')
        self.button_run_once.configure(command=self.run_once)
        self.combobox_units_temperature = ttk.Combobox(self.frame1)
        self.combobox_units_temperature.configure(state='readonly', values='(K) (C) (F)', width='8')
        self.combobox_units_temperature.grid(column='1', padx='5', row='20')
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
        self.text1.grid(column='0', columnspan='5', row='0')
        self.text1.rowconfigure('0', pad='0')
        self.label_image = ttk.Label(self.frame2)
        self.blank_png = tk.PhotoImage(file='blank.png')
        self.label_image.configure(image=self.blank_png)
        self.label_image.grid(column='5', columnspan='5', row='0')
        self.label_optimized = ttk.Label(self.frame2)
        self.label_optimized.configure(text='Optimized Dimensions (in.)')
        self.label_optimized.grid(column='0', row='4')
        self.entry_dim1 = ttk.Entry(self.frame2)
        self.entry_dim1.configure(state='readonly', width='8')
        self.entry_dim1.grid(column='5', padx='2', row='4')
        self.entry_dim2 = ttk.Entry(self.frame2)
        self.entry_dim2.configure(state='readonly', width='8')
        self.entry_dim2.grid(column='6', padx='2', row='4')
        self.entry_dim3 = ttk.Entry(self.frame2)
        self.entry_dim3.configure(state='readonly', width='8')
        self.entry_dim3.grid(column='7', padx='2', row='4')
        self.entry_dim4 = ttk.Entry(self.frame2)
        self.entry_dim4.configure(state='readonly', width='8')
        self.entry_dim4.grid(column='8', padx='2', row='4')
        self.entry_dim5 = ttk.Entry(self.frame2)
        self.entry_dim5.configure(state='readonly', width='8')
        self.entry_dim5.grid(column='9', padx='2', row='4')
        self.separator4 = ttk.Separator(self.frame2)
        self.separator4.configure(orient='horizontal')
        self.separator4.grid(column='0', columnspan='5', ipadx='300', pady='5', row='5')
        self.notebook_tolerances = ttk.Notebook(self.frame2)
        self.frame_default = ttk.Frame(self.notebook_tolerances)
        self.label_defaultcv = ttk.Label(self.frame_default)
        self.label_defaultcv.configure(text='Standard deviation as a percentage of the mean: ')
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
        self.button_export = ttk.Button(self.frame2)
        self.button_export.configure(text='Export to JSON')
        self.button_export.grid(column='0', pady='2', row='12', sticky='e')
        self.button_export.configure(command=self.export_to_json)
        self.frame2.configure(height='200', width='200')
        self.frame2.pack(side='top')
        self.toplevel2.configure(height='200', width='200')

        vcmd = (self.frame1.register(self.on_validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.entry_hole1.config(validatecommand=vcmd)
        self.entry_hole2.config(validatecommand=vcmd)
        self.entry_hole3.config(validatecommand=vcmd)
        self.entry_hole4.config(validatecommand=vcmd)
        self.entry_hole5.config(validatecommand=vcmd)
        self.entry_hole_width.config(validatecommand=vcmd)
        self.entry_hole_length.config(validatecommand=vcmd)
        self.entry_ring_tube_dim.config(validatecommand=vcmd)
        self.entry_ring_diameter.config(validatecommand=vcmd)
        self.entry_throughput.config(validatecommand=vcmd)
        self.entry_chamber_pressure.config(validatecommand=vcmd)
        self.entry_gamma.config(validatecommand=vcmd)
        self.entry_molar_mass.config(validatecommand=vcmd)
        self.entry_particle_diameter.config(validatecommand=vcmd)
        self.entry_viscosity.config(validatecommand=vcmd)
        self.entry_temperature.config(validatecommand=vcmd)
        self.entry_gas_constant.config(validatecommand=vcmd)

        _, _, filenames = next(os.walk(os.path.join('Gas_Data')))
        gas_list = []
        for file in filenames:
            gas_list.append(file[0:file.index('.json')])
        self.combobox_gas.configure(state='readonly', values=gas_list)
        self.combobox_gas.bind('<<ComboboxSelected>>', self.on_gas_select)
        self.scrollbar_canvas.config(command=self.canvas1.yview)
        self.scrollbar_x.configure(command=self.text1.xview)
        self.scrollbar_y.configure(command=self.text1.yview)
        self.text1.configure(xscrollcommand=self.scrollbar_x.set)
        self.text1.configure(yscrollcommand=self.scrollbar_y.set)
        self.combobox_hole_shape.bind('<<ComboboxSelected>>', self.on_hole_shape_select)
        self.combobox_hole_count.bind('<<ComboboxSelected>>', self.on_hole_count_select)
        self.entry_hole4.grid_forget()
        self.entry_hole5.grid_forget()
        self.label_hole_width.grid_forget()
        self.entry_hole_width.grid_forget()
        self.combobox_units_holewidth.grid_forget()
        self.toplevel2.withdraw()
        self.toplevel2.protocol("WM_DELETE_WINDOW", self.on_sub_close)
        self.toplevel1.protocol("WM_DELETE_WINDOW", self.on_main_close)
        self.my_image = tk.PhotoImage()
        self.combobox_hole_shape.current('0')
        self.combobox_hole_count.current('0')
        self.combobox_units_holedim.current('0')
        self.entry_hole1.unit = '(in.)'
        self.entry_hole2.unit = '(in.)'
        self.entry_hole3.unit = '(in.)'
        self.entry_hole4.unit = '(in.)'
        self.entry_hole5.unit = '(in.)'
        self.combobox_units_holedim.bind('<<ComboboxSelected>>', self.on_unit_select)
        self.combobox_units_holewidth.current('0')
        self.entry_hole_width.unit = '(in.)'
        self.combobox_units_holewidth.bind('<<ComboboxSelected>>', self.on_unit_select)
        self.combobox_units_holelength.current('0')
        self.entry_hole_length.unit = '(in.)'
        self.combobox_units_holelength.bind('<<ComboboxSelected>>', self.on_unit_select)
        self.combobox_units_ring_tube_dim.current('0')
        self.entry_ring_tube_dim.unit = '(in.)'
        self.combobox_units_ring_tube_dim.bind('<<ComboboxSelected>>', self.on_unit_select)
        self.combobox_units_ring_diameter.current('0')
        self.entry_ring_diameter.unit = '(in.)'
        self.combobox_units_ring_diameter.bind('<<ComboboxSelected>>', self.on_unit_select)
        self.combobox_units_throughput.current('0')
        self.entry_throughput.unit = '(sccm)'
        self.combobox_units_throughput.bind('<<ComboboxSelected>>', self.on_unit_select)
        self.combobox_units_pressure.current('0')
        self.entry_chamber_pressure.unit = '(millitorr)'
        self.combobox_units_pressure.bind('<<ComboboxSelected>>', self.on_unit_select)
        self.combobox_units_temperature.current('0')
        self.entry_temperature.unit = '(K)'
        self.combobox_units_temperature.bind('<<ComboboxSelected>>', self.on_unit_select)
        self.currently_running = False
        self.successful_run = False

        self.notebook_tolerances.bind('<<NotebookTabChanged>>', self.on_tab_select)
        self.tol_dict = {}
        self.export_dict = {}

        self.canvas1.config(bg='white')
        self.ring_image = tk.PhotoImage(file=os.path.join('Assets', '6HoleCircle3d.png'))
        self.canvas1.create_image(0, 120, image=self.ring_image, anchor='nw')
        self.overlay = tk.PhotoImage(file=os.path.join('Assets', '6HoleCircleOverlay.png'))
        self.canvas1.create_image(6, 4, image=self.overlay, anchor='nw')
        self.labels = []
        self.labels.append(self.canvas1.create_text(0, 0, font=('', 20), text=''))
        self.labels.append(self.canvas1.create_text(0, 0, font=('', 20), text=''))
        self.labels.append(self.canvas1.create_text(0, 0, font=('', 20), text=''))
        self.labels.append(self.canvas1.create_text(0, 0, font=('', 20), text=''))
        self.labels.append(self.canvas1.create_text(0, 0, font=('', 20), text=''))
        self.labels.append(self.canvas1.create_text(0, 0, font=('', 20), text=''))
        self.labels.append(self.canvas1.create_text(0, 0, font=('', 20), text=''))
        self.labels.append(self.canvas1.create_text(0, 0, font=('', 20), text=''))
        self.update_preview(None)

        self.toplevel1.bind('<KeyPress>', self.update_preview)

        # Main widget
        self.mainwindow = self.toplevel1

    def run_simulate(self):
        if self.currently_running:
            pass
        else:
            self.toplevel2.deiconify()
            self.currently_running = True
            self.successful_run = False
            self.tol_dict.clear()
            self.export_dict.clear()
            try:
                # Grab data from main window
                if self.combobox_hole_shape.get() == 'Circle':
                    shp_o = 'Circle'
                elif self.combobox_hole_shape.get() == 'Rectangle':
                    shp_o = 'Rectangle'
                else:
                    raise ValueError("Aperture shape not selected")
                dim_o = [float(self.entry_hole1.get()), float(self.entry_hole2.get()), float(self.entry_hole3.get())]
                if self.combobox_hole_count.get() == '8':
                    dim_o.append(float(self.entry_hole4.get()))
                elif self.combobox_hole_count.get() == '10':
                    dim_o.append(float(self.entry_hole4.get()))
                    dim_o.append(float(self.entry_hole5.get()))
                else:
                    pass
                len_o = float(self.entry_hole_length.get())
                shp_c = 'Circle'
                width_o = float(self.entry_hole_width.get())
                dim_c = float(self.entry_ring_tube_dim.get())
                ring_d = float(self.entry_ring_diameter.get())
                thr = float(self.entry_throughput.get())
                ch_p = float(self.entry_chamber_pressure.get())
                gam = float(self.entry_gamma.get())
                mol_m = float(self.entry_molar_mass.get())
                par_d = float(self.entry_particle_diameter.get())
                vis = float(self.entry_viscosity.get())
                tem = float(self.entry_temperature.get())
                gas_r = float(self.entry_gas_constant.get())

                # Convert to proper units
                for i in range(len(dim_o)):
                    dim_o[i] = self.convert(dim_o[i], self.combobox_units_holedim.get(), '(in.)')
                width_o = self.convert(len_o, self.combobox_units_holewidth.get(), '(in.)')
                len_o = self.convert(len_o, self.combobox_units_holelength.get(), '(in.)')
                dim_c = self.convert(dim_c, self.combobox_units_ring_tube_dim.get(), '(in.)')
                ring_d = self.convert(ring_d, self.combobox_units_ring_diameter.get(), '(in.)')
                thr = self.convert(thr, self.combobox_units_throughput.get(), '(sccm)')
                ch_p = self.convert(ch_p, self.combobox_units_pressure.get(), '(millitorr)')
                tem = self.convert(tem, self.combobox_units_temperature.get(), '(K)')

                # Prepare data for potential export
                self.export_dict['Aperture Shape'] = shp_o
                self.export_dict['Number of Openings'] = self.combobox_hole_count.get()
                self.export_dict['Aperture Dimensions'] = dim_o
                self.export_dict['Aperture Width'] = width_o
                self.export_dict['Aperture Length'] = len_o
                self.export_dict['Ring Tube Diameter'] = dim_c
                self.export_dict['Ring Diameter'] = ring_d
                self.export_dict['Throughput'] = thr
                self.export_dict['Chamber Pressure'] = ch_p
                self.export_dict['Gamma'] = gam
                self.export_dict['Molar Mass'] = mol_m
                self.export_dict['Particle Diameter'] = par_d
                self.export_dict['Viscosity'] = vis
                self.export_dict['Temperature'] = tem
                self.export_dict['Gas Constant'] = gas_r

                run = True
            except ValueError as error:
                self.append_txt(str(error) + '\n')
                run = False
                self.currently_running = False
            if run:
                self.append_txt('Optimizing...\n')
                try:
                    optimized_dim = self.optimize(shp_o, dim_o, width_o, len_o, shp_c, dim_c, 0,
                                                  ring_d*np.pi/float(self.combobox_hole_count.get()),
                                                  thr, ch_p, gam, mol_m, par_d, vis, tem, gas_r)
                    self.update_text(self.entry_dim1, str(optimized_dim[0]))
                    self.update_text(self.entry_dim2, str(optimized_dim[1]))
                    self.update_text(self.entry_dim3, str(optimized_dim[2]))
                    if len(dim_o) == 4:
                        self.update_text(self.entry_dim4, str(optimized_dim[3]))
                    if len(dim_o) == 5:
                        self.update_text(self.entry_dim4, str(optimized_dim[3]))
                        self.update_text(self.entry_dim5, str(optimized_dim[4]))
                    self.append_txt('...Finished!\n')

                    self.export_dict['Aperture Dimensions'] = optimized_dim
                    self.successful_run = True
                    self.on_tab_select(None)
                except (ValueError, RuntimeError):
                    self.append_txt('Run failed\n')
                    self.successful_run = False
                    self.export_dict.clear()
                    self.tol_dict.clear()
                self.currently_running = False

    def run_once(self):
        if self.currently_running:
            pass
        else:
            self.toplevel2.deiconify()
            self.currently_running = True
            self.successful_run = False
            self.tol_dict.clear()
            self.export_dict.clear()
            try:
                # Grab data from main window
                if self.combobox_hole_shape.get() == 'Circle':
                    shp_o = 'Circle'
                elif self.combobox_hole_shape.get() == 'Rectangle':
                    shp_o = 'Rectangle'
                else:
                    raise ValueError("Aperture shape not selected")
                dim_o = [float(self.entry_hole1.get()), float(self.entry_hole2.get()), float(self.entry_hole3.get())]
                if self.combobox_hole_count.get() == '8':
                    dim_o.append(float(self.entry_hole4.get()))
                elif self.combobox_hole_count.get() == '10':
                    dim_o.append(float(self.entry_hole4.get()))
                    dim_o.append(float(self.entry_hole5.get()))
                else:
                    pass
                len_o = float(self.entry_hole_length.get())
                shp_c = 'Circle'
                width_o = float(self.entry_hole_width.get())
                dim_c = float(self.entry_ring_tube_dim.get())
                ring_d = float(self.entry_ring_diameter.get())
                thr = float(self.entry_throughput.get())
                ch_p = float(self.entry_chamber_pressure.get())
                gam = float(self.entry_gamma.get())
                mol_m = float(self.entry_molar_mass.get())
                par_d = float(self.entry_particle_diameter.get())
                vis = float(self.entry_viscosity.get())
                tem = float(self.entry_temperature.get())
                gas_r = float(self.entry_gas_constant.get())

                # Convert to proper units
                for i in range(len(dim_o)):
                    dim_o[i] = self.convert(dim_o[i], self.combobox_units_holedim.get(), '(in.)')
                width_o = self.convert(len_o, self.combobox_units_holewidth.get(), '(in.)')
                len_o = self.convert(len_o, self.combobox_units_holelength.get(), '(in.)')
                dim_c = self.convert(dim_c, self.combobox_units_ring_tube_dim.get(), '(in.)')
                ring_d = self.convert(ring_d, self.combobox_units_ring_diameter.get(), '(in.)')
                thr = self.convert(thr, self.combobox_units_throughput.get(), '(sccm)')
                ch_p = self.convert(ch_p, self.combobox_units_pressure.get(), '(millitorr)')
                tem = self.convert(tem, self.combobox_units_temperature.get(), '(K)')

                # Prepare data for potential export
                self.export_dict['Aperture Shape'] = shp_o
                self.export_dict['Number of Openings'] = self.combobox_hole_count.get()
                self.export_dict['Aperture Dimensions'] = dim_o
                self.export_dict['Aperture Width'] = width_o
                self.export_dict['Aperture Length'] = len_o
                self.export_dict['Ring Tube Diameter'] = dim_c
                self.export_dict['Ring Diameter'] = ring_d
                self.export_dict['Throughput'] = thr
                self.export_dict['Chamber Pressure'] = ch_p
                self.export_dict['Gamma'] = gam
                self.export_dict['Molar Mass'] = mol_m
                self.export_dict['Particle Diameter'] = par_d
                self.export_dict['Viscosity'] = vis
                self.export_dict['Temperature'] = tem
                self.export_dict['Gas Constant'] = gas_r

                run = True
            except ValueError as error:
                self.append_txt(str(error) + '\n')
                run = False
                self.currently_running = False
            if run:
                self.append_txt('Running once...\n')
                q_tol = [None] * 5
                try:
                    q_tol[0] = GasNetworkSim.sim(shp_o, dim_o, width_o, len_o, shp_c, dim_c, 0,
                                                 ring_d*np.pi/float(self.combobox_hole_count.get()),
                                                 thr, ch_p, gam, mol_m, par_d, vis, tem, gas_r)
                    q_tol[1] = GasNetworkSim.sim(shp_o, dim_o, width_o, len_o, shp_c, dim_c, 0,
                                                 ring_d*np.pi/float(self.combobox_hole_count.get()),
                                                 thr * 2, ch_p, gam, mol_m, par_d, vis, tem, gas_r)
                    q_tol[2] = GasNetworkSim.sim(shp_o, dim_o, width_o, len_o, shp_c, dim_c, 0,
                                                 ring_d*np.pi/float(self.combobox_hole_count.get()),
                                                 thr * 0.5, ch_p, gam, mol_m, par_d, vis, tem, gas_r)
                    small_dim = dim_o.copy()
                    small_dim[0] -= 0.001
                    large_dim = dim_o.copy()
                    large_dim[0] += 0.001
                    q_tol[3] = GasNetworkSim.sim(shp_o, small_dim, width_o, len_o, shp_c, dim_c, 0,
                                                 ring_d*np.pi/float(self.combobox_hole_count.get()),
                                                 thr, ch_p, gam, mol_m, par_d, vis, tem, gas_r)
                    q_tol[4] = GasNetworkSim.sim(shp_o, large_dim, width_o, len_o, shp_c, dim_c, 0,
                                                 ring_d*np.pi/float(self.combobox_hole_count.get()),
                                                 thr, ch_p, gam, mol_m, par_d, vis, tem, gas_r)
                    self.successful_run = True
                except RuntimeError or ValueError:
                    self.append_txt('...Run Failed\n')
                    self.successful_run = False
                    self.export_dict.clear()
                    self.tol_dict.clear()
                self.currently_running = False

                if self.successful_run:
                    self.append_txt('...Run Finished\n')
                    for i in range(len(q_tol)):
                        qs = q_tol[i]
                        cv = np.std(q_tol[i]) / np.mean(q_tol[i])
                        image = self.generate_graph(q_tol[i], str(i))
                        self.tol_dict[i] = {'Q': qs, 'CV': cv, 'IMAGE': image}
                        self.export_dict['run_type' + str(i)] = {'Q': qs}
                    self.update_image(self.label_image, self.tol_dict[0]['IMAGE'])

    def optimize(self, shape_o, dim_o, width_o, length_o, shape_c, dim_c, width_c, length_c, throughput,
                 chamber_pressure, gamma, molar_mass, particle_diameter, viscosity, temp, r_0):
        try:
            shutil.rmtree(os.path.join('temp'))
        except FileNotFoundError:
            pass
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
                temp_dim[index.index(depth)] = round(temp_dim[index.index(depth)] + 0.001, 6)

            else:
                temp_dim[index.index(depth)] = round(temp_dim[index.index(depth)] - 0.001, 6)

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
        small_dim = current_dim.copy()
        small_dim[0] -= 0.001
        large_dim = current_dim.copy()
        large_dim[0] += 0.001
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
            self.export_dict['run_type' + str(i)] = {'Q': qs}
        self.update_image(self.label_image, self.tol_dict[0]['IMAGE'])
        return current_dim

    def on_validate(self, d, i, P, s, S, v, V, W):
        try:
            if P == '':
                return True
            float(P)
            return True
        except ValueError:
            self.frame1.bell()
            return False

    def on_unit_select(self, event):
        to_edit = []
        for widget in self.frame1.winfo_children():
            try:
                if widget.grid_info()['row'] == event.widget.grid_info()['row']:
                    if str(type(widget)) == str(type(self.entry_hole1)):
                        to_edit.append(widget)
            except KeyError:
                pass
        for entry in to_edit:
            previous = entry.unit
            next = event.widget.get()
            if entry.get() == '':
                pass
            else:
                new_value = self.convert(float(entry.get()), previous, next)
                entry.delete('0', 'end')
                entry.insert('0', str(new_value))
                entry.unit = next
        self.update_preview(None)

    def on_hole_count_select(self, event):
        if self.combobox_hole_count.get() == '6':
            self.entry_hole4.grid_forget()
            self.entry_hole5.grid_forget()
            self.entry_hole4.delete('0', 'end')
            self.entry_hole5.delete('0', 'end')
        elif self.combobox_hole_count.get() == '8':
            self.entry_hole5.grid_forget()
            self.entry_hole5.delete('0', 'end')
            self.entry_hole4.grid(column='5', row='2', padx='2')
        else:
            self.entry_hole4.grid(column='5', row='2', padx='2')
            self.entry_hole5.grid(column='6', row='2', padx='2')
        self.update_preview(None)

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
        x = range(1, len(q) + 1)
        y = [a / 101325 * (60 * 10 ** 6) for a in q]
        mean = np.mean(y)
        px = 1/plt.rcParams['figure.dpi']
        plt.subplots(figsize=(500*px, 300*px))
        plt.xlabel('Opening')
        plt.ylabel('Throughput (sccm)')
        plt.ylim(mean * 0.75, mean * 1.25)
        plt.plot(x, y)
        plt.plot(x, [mean] * len(q))
        for i in range(len(y)):
            plt.text(i + 1, y[i] + mean * 0.02, str(round(y[i], 2)), horizontalalignment='center')
        plt.tight_layout()
        try:
            os.mkdir('temp')
        except FileExistsError:
            pass
        plt.savefig(os.path.join('temp', name + '.png'))
        plt.close('all')
        return os.path.join('temp', name + '.png')

    def on_hole_shape_select(self, eventObject):
        if self.combobox_hole_shape.get() == 'Circle':
            self.label_hole_dim.config(text='Aperture Diameters')
            self.label_hole_width.grid_forget()
            self.combobox_units_holewidth.grid_forget()
            self.entry_hole_width.grid_forget()
            self.entry_hole_width.insert('0', '0')
            self.entry_hole_width.delete('1', 'end')
        else:
            self.label_hole_dim.config(text='Aperture Height')
            self.label_hole_width.grid(column=0, row=3, sticky='e')
            self.combobox_units_holewidth.grid(column=1, row=3)
            self.combobox_units_holewidth.current('0')
            self.entry_hole_width.grid(column=2, row=3, columnspan=3)
            self.entry_hole_width.unit = '(in.)'
        self.update_preview(None)

    def update_preview(self, event):
        layout = self.combobox_hole_count.get() + 'Hole' + self.combobox_hole_shape.get()
        dim_unit = self.combobox_units_holedim.get()
        tube_dim_unit = self.combobox_units_ring_tube_dim.get()
        ring_dim_unit = self.combobox_units_ring_diameter.get()
        through_unit = self.combobox_units_throughput.get()

        self.ring_image.config(file=os.path.join('Assets', layout + '3d.png'))
        self.overlay.config(file=os.path.join('Assets', layout + 'Overlay.png'))
        if layout == '6HoleCircle':
            self.canvas1.itemconfig(self.labels[0], text=self.entry_hole1.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[0], 260, 155)
            self.canvas1.itemconfig(self.labels[1], text=self.entry_hole2.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[1], 506, 87)
            self.canvas1.itemconfig(self.labels[2], text=self.entry_hole3.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[2], 748, 155)
            self.canvas1.itemconfig(self.labels[3], text='')
            self.canvas1.itemconfig(self.labels[4], text='')
            self.canvas1.itemconfig(self.labels[5], text=self.entry_ring_tube_dim.get() + ' ' + tube_dim_unit)
            self.canvas1.coords(self.labels[5], 110, 390)
            self.canvas1.itemconfig(self.labels[6], text=self.entry_ring_diameter.get() + ' ' + ring_dim_unit)
            self.canvas1.coords(self.labels[6], 500, 450)
            self.canvas1.itemconfig(self.labels[7], text=self.entry_throughput.get() + ' ' + through_unit)
            self.canvas1.coords(self.labels[7], 220, 570)
        elif layout == '8HoleCircle':
            self.canvas1.itemconfig(self.labels[0], text=self.entry_hole1.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[0], 243, 176)
            self.canvas1.itemconfig(self.labels[1], text=self.entry_hole2.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[1], 395, 98)
            self.canvas1.itemconfig(self.labels[2], text=self.entry_hole3.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[2], 613, 98)
            self.canvas1.itemconfig(self.labels[3], text=self.entry_hole4.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[3], 768, 173)
            self.canvas1.itemconfig(self.labels[4], text='')
            self.canvas1.itemconfig(self.labels[5], text=self.entry_ring_tube_dim.get() + ' ' + tube_dim_unit)
            self.canvas1.coords(self.labels[5], 110, 390)
            self.canvas1.itemconfig(self.labels[6], text=self.entry_ring_diameter.get() + ' ' + ring_dim_unit)
            self.canvas1.coords(self.labels[6], 500, 450)
            self.canvas1.itemconfig(self.labels[7], text=self.entry_throughput.get() + ' ' + through_unit)
            self.canvas1.coords(self.labels[7], 220, 570)
        elif layout == '10HoleCircle':
            self.canvas1.itemconfig(self.labels[0], text=self.entry_hole1.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[0], 234, 186)
            self.canvas1.itemconfig(self.labels[1], text=self.entry_hole2.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[1], 340, 116)
            self.canvas1.itemconfig(self.labels[2], text=self.entry_hole3.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[2], 506, 90)
            self.canvas1.itemconfig(self.labels[3], text=self.entry_hole4.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[3], 670, 116)
            self.canvas1.itemconfig(self.labels[4], text=self.entry_hole5.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[4], 776, 186)
            self.canvas1.itemconfig(self.labels[5], text=self.entry_ring_tube_dim.get() + ' ' + tube_dim_unit)
            self.canvas1.coords(self.labels[5], 110, 390)
            self.canvas1.itemconfig(self.labels[6], text=self.entry_ring_diameter.get() + ' ' + ring_dim_unit)
            self.canvas1.coords(self.labels[6], 500, 450)
            self.canvas1.itemconfig(self.labels[7], text=self.entry_throughput.get() + ' ' + through_unit)
            self.canvas1.coords(self.labels[7], 220, 570)
        elif layout == '6HoleRectangle':
            self.canvas1.itemconfig(self.labels[0], text=self.entry_hole1.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[0], 235, 168)
            self.canvas1.itemconfig(self.labels[1], text=self.entry_hole2.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[1], 514, 87)
            self.canvas1.itemconfig(self.labels[2], text=self.entry_hole3.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[2], 785, 174)
            self.canvas1.itemconfig(self.labels[3], text='')
            self.canvas1.itemconfig(self.labels[4], text='')
            self.canvas1.itemconfig(self.labels[5], text=self.entry_ring_tube_dim.get() + ' ' + tube_dim_unit)
            self.canvas1.coords(self.labels[5], 80, 370)
            self.canvas1.itemconfig(self.labels[6], text=self.entry_ring_diameter.get() + ' ' + ring_dim_unit)
            self.canvas1.coords(self.labels[6], 500, 450)
            self.canvas1.itemconfig(self.labels[7], text=self.entry_throughput.get() + ' ' + through_unit)
            self.canvas1.coords(self.labels[7], 65, 510)
        elif layout == '8HoleRectangle':
            self.canvas1.itemconfig(self.labels[0], text=self.entry_hole1.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[0], 221, 188)
            self.canvas1.itemconfig(self.labels[1], text=self.entry_hole2.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[1], 388, 99)
            self.canvas1.itemconfig(self.labels[2], text=self.entry_hole3.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[2], 640, 99)
            self.canvas1.itemconfig(self.labels[3], text=self.entry_hole4.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[3], 807, 190)
            self.canvas1.itemconfig(self.labels[4], text='')
            self.canvas1.itemconfig(self.labels[5], text=self.entry_ring_tube_dim.get() + ' ' + tube_dim_unit)
            self.canvas1.coords(self.labels[5], 80, 370)
            self.canvas1.itemconfig(self.labels[6], text=self.entry_ring_diameter.get() + ' ' + ring_dim_unit)
            self.canvas1.coords(self.labels[6], 500, 450)
            self.canvas1.itemconfig(self.labels[7], text=self.entry_throughput.get() + ' ' + through_unit)
            self.canvas1.coords(self.labels[7], 65, 510)
        elif layout == '10HoleRectangle':
            self.canvas1.itemconfig(self.labels[0], text=self.entry_hole1.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[0], 211, 204)
            self.canvas1.itemconfig(self.labels[1], text=self.entry_hole2.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[1], 329, 124)
            self.canvas1.itemconfig(self.labels[2], text=self.entry_hole3.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[2], 513, 87)
            self.canvas1.itemconfig(self.labels[3], text=self.entry_hole4.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[3], 701, 122)
            self.canvas1.itemconfig(self.labels[4], text=self.entry_hole5.get() + ' ' + dim_unit)
            self.canvas1.coords(self.labels[4], 814, 200)
            self.canvas1.itemconfig(self.labels[5], text=self.entry_ring_tube_dim.get() + ' ' + tube_dim_unit)
            self.canvas1.coords(self.labels[5], 80, 370)
            self.canvas1.itemconfig(self.labels[6], text=self.entry_ring_diameter.get() + ' ' + ring_dim_unit)
            self.canvas1.coords(self.labels[6], 500, 450)
            self.canvas1.itemconfig(self.labels[7], text=self.entry_throughput.get() + ' ' + through_unit)
            self.canvas1.coords(self.labels[7], 65, 510)

    def on_main_close(self):
        try:
            quit()
        except NameError:
            self.toplevel2.quit()
            self.toplevel1.quit()

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

    def import_from_json(self):
        files = [('JSON Files', '*.json'),
                 ('All Files', '*.*')]
        file = filedialog.askopenfile(filetypes=files, defaultextension=files)
        if file is None:
            return
        try:
            json_dict = json.loads(file.read())
        except ValueError:
            self.frame1.bell()
            return
        if 'Aperture Shape' in json_dict:
            if json_dict['Aperture Shape'] == 'Circle':
                self.combobox_hole_shape.set('Circle')
            else:
                self.combobox_hole_shape.set('Rectangle')
            self.on_hole_shape_select(None)
        if 'Number of Openings' in json_dict:
            self.combobox_hole_count.set(json_dict['Number of Openings'])
            self.on_hole_count_select(None)
        if 'Aperture Dimensions' in json_dict:
            self.combobox_units_holedim.set('(in.)')
            self.entry_hole1.delete('0', 'end')
            self.entry_hole2.delete('0', 'end')
            self.entry_hole3.delete('0', 'end')
            self.entry_hole1.insert('0', json_dict['Aperture Dimensions'][0])
            self.entry_hole2.insert('0', json_dict['Aperture Dimensions'][1])
            self.entry_hole3.insert('0', json_dict['Aperture Dimensions'][2])
            try:
                if self.combobox_hole_count.get() == '8':
                    self.entry_hole4.delete('0', 'end')
                    self.entry_hole4.insert('0', json_dict['Aperture Dimensions'][3])
                if self.combobox_hole_count.get() == '10':
                    self.entry_hole4.delete('0', 'end')
                    self.entry_hole4.insert('0', json_dict['Aperture Dimensions'][4])
                    self.entry_hole5.delete('0', 'end')
                    self.entry_hole5.insert('0', json_dict['Aperture Dimensions'][4])
            except IndexError:
                pass
        if 'Aperture Width' in json_dict:
            self.entry_hole_width.delete('0', 'end')
            self.entry_hole_width.insert('0', json_dict['Aperture Width'])
            self.combobox_units_holewidth.set('(in.)')
        if 'Aperture Length' in json_dict:
            self.entry_hole_length.delete('0', 'end')
            self.entry_hole_length.insert('0', json_dict['Aperture Length'])
            self.combobox_units_holelength.set('(in.)')
        if 'Ring Tube Diameter' in json_dict:
            self.entry_ring_tube_dim.delete('0', 'end')
            self.entry_ring_tube_dim.insert('0', json_dict['Ring Tube Diameter'])
            self.combobox_units_ring_tube_dim.set('(in.)')
        
        if 'Ring Diameter' in json_dict:
            self.entry_ring_diameter.delete('0', 'end')
            self.entry_ring_diameter.insert('0', json_dict['Ring Diameter'])
            self.combobox_units_ring_diameter.set('(in.)')
        if 'Throughput' in json_dict:
            self.entry_throughput.delete('0', 'end')
            self.entry_throughput.insert('0', json_dict['Throughput'])
            self.combobox_units_throughput.set('(sccm)')
        if 'Chamber Pressure' in json_dict:
            self.entry_chamber_pressure.delete('0', 'end')
            self.entry_chamber_pressure.insert('0', json_dict['Chamber Pressure'])
            self.combobox_units_pressure.set('(millitorr)')
        if 'Gamma' in json_dict:
            self.entry_gamma.delete('0', 'end')
            self.entry_gamma.insert('0', json_dict['Gamma'])
        if 'Molar Mass' in json_dict:
            self.entry_molar_mass.delete('0', 'end')
            self.entry_molar_mass.insert('0', json_dict['Molar Mass'])
        if 'Particle Diameter' in json_dict:
            self.entry_particle_diameter.delete('0', 'end')
            self.entry_particle_diameter.insert('0', json_dict['Particle Diameter'])
        if 'Viscosity' in json_dict:
            self.entry_viscosity.delete('0', 'end')
            self.entry_viscosity.insert('0', json_dict['Viscosity'])
        if 'Temperature' in json_dict:
            self.entry_temperature.delete('0', 'end')
            self.entry_temperature.insert('0', json_dict['Temperature'])
            self.combobox_units_temperature.set('(K)')
        if 'Gas Constant' in json_dict:
            self.entry_gas_constant.delete('0', 'end')
            self.entry_gas_constant.insert('0', json_dict['Gas Constant'])

    def export_to_json(self):
        files = [('JSON Files', '*.json'),
                 ('All Files', '*.*')]
        file = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
        json_obj = json.dumps(self.export_dict, indent=4)
        if file is None:
            return
        file.write(json_obj)
        file.close()

    def convert(self, value, old_unit, new_unit):
        if old_unit == '(in.)':
            value *= 0.0254
        elif old_unit == '(mil)':
            value *= 0.0000254
        elif old_unit == '(m)':
            pass
        elif old_unit == '(mm)':
            value *= 0.001
        elif old_unit == '(sccm)':
            value *= 101325 / (60 * 10 ** 6)
        elif old_unit == '(Pa*m^3/s)':
            pass
        elif old_unit == '(millitorr)':
            value *= 0.133322
        elif old_unit == '(torr)':
            value *= 133.322
        elif old_unit == '(atm)':
            value *= 101325
        elif old_unit == '(bar)':
            value *= 100000
        elif old_unit == '(Pa)':
            pass
        elif old_unit == '(K)':
            pass
        elif old_unit == '(C)':
            value += 273.15
        elif old_unit == '(F)':
            value = ((value - 32) * 5/9) + 273.15

        if new_unit == '(in.)':
            value /= 0.0254
        elif new_unit == '(mil)':
            value /= 0.0000254
        elif new_unit == '(m)':
            pass
        elif new_unit == '(mm)':
            value /= 0.001
        elif new_unit == '(sccm)':
            value /= (101325 / (60 * 10 ** 6))
        elif new_unit == '(Pa*m^3/s)':
            pass
        elif new_unit == '(millitorr)':
            value /= 0.133322
        elif new_unit == '(torr)':
            value /= 133.322
        elif new_unit == '(atm)':
            value /= 101325
        elif new_unit == '(bar)':
            value /= 100000
        elif new_unit == '(Pa)':
            pass
        elif new_unit == '(K)':
            pass
        elif new_unit == '(C)':
            value -= 273.15
        elif new_unit == '(F)':
            value = ((value - 273.15) * 9/5) + 32
        return round(value, 8)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = GUI()
    app.run()

