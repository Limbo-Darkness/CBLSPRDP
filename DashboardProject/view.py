# Imports
import tkinter as tk
import tkinter.ttk
from tkinter import StringVar
from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class View:
    def __init__(self, model):
        #                #
        # Tkinter Setup  #
        #                #
        # root
        self.root = tk.Tk()
        self.root.title('J. Lopez Project 1')
        self.root.resizable(False, False)
        self.root.geometry('850x850')

        # MVC Definition
        self.model = model
        self.controller = None

        # Setting up the main frame that all buttons/labels reside in
        self.mainframe = tkinter.ttk.Frame(self.root, padding='5 5 5 5')
        self.mainframe.grid(row=0, column=0, sticky='')
        self.mainframe.grid_columnconfigure((0, 1, 2), weight=1)

        # Closer function and process prevents pyplot.subplots() from preventing the function from exiting properly.
        def _closer():
            if self.controller:
                self.controller._closer()
        self.root.protocol("WM_DELETE_WINDOW", _closer)

        #         #
        # Buttons #
        #         #
        # Connect command definition
        def connects():
            if self.controller:
                self.controller.connect_server()
                print(2)

        # Set thresholds command definition
        def thresholds():
            print(0)


        # Connect server button
        _connectserver_btn = tkinter.ttk.Button(self.mainframe, text='Connect To Server', command=connects)
        _connectserver_btn.grid(row=0, column=0, sticky='W')

        # Threshold setter button
        _thresholds_btn = tkinter.ttk.Button(self.mainframe, text='Set Thresholds', command=thresholds)
        _thresholds_btn.grid(row=0, column=1, sticky='W')



        #          #
        #  GRAPHS  #
        #          #
        # Empty Graph
        self.fig, ax = pyplot.subplots()
        data = 0
        time = 0
        ax.plot(time, data)
        pyplot.title("Default Graph")
        pyplot.xlabel("X-axis")
        pyplot.ylabel("Y-axis")
        canvas = FigureCanvasTkAgg(self.fig, master=self.mainframe)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=1)

        # Graphing buttons
        # CPU Graph button
        _cpu_btn = tkinter.ttk.Button(self.mainframe, text='CPU Graph', command=print(0))
        _cpu_btn.grid(row=3, column=0, sticky='W')

        # Mem Graph button
        _mem_btn = tkinter.ttk.Button(self.mainframe, text='Memory Graph', command=print(1))
        _mem_btn.grid(row=4, column=0, sticky='W')

        # IO Graph button
        _io_btn = tkinter.ttk.Button(self.mainframe, text='IO Graph', command=print(2))
        _io_btn.grid(row=5, column=0, sticky='W')

        # Filesystem Graph button
        _io_btn = tkinter.ttk.Button(self.mainframe, text='Filesystem Graph', command=print(3))
        _io_btn.grid(row=6, column=0, sticky='W')

        # Network Graph button
        _io_btn = tkinter.ttk.Button(self.mainframe, text='Network Graph', command=print(4))
        _io_btn.grid(row=7, column=0, sticky='W')


        #          #
        #  Labels  #
        #          #




    # Intensity Graph Implementation - This is the bonus graph
    # Waveform Graph Implementation (Default)
    def cpu_plot(self, cpu_usage, time):
        # Clear previous graph
        pyplot.clf()

        # Defining plot
        pyplot.plot(time, cpu_usage)

        # Updating plot labels
        pyplot.title("CPU Usage Graph")
        pyplot.xlabel("Time (s)")
        pyplot.ylabel("CPU Usage (%)")

        # Updating GUI
        canvas = FigureCanvasTkAgg(self.fig, master=self.mainframe)
        canvas.draw()
        canvas.get_tk_widget().grid(row=2, column=1)

    def mem_plot(self, mem_usage, time):
        print(3)

    def io_plot(self, io_usage, time):
        print(4)

    def filesystem_plot(self, filesystem_usage, time):
        print(5)

    def network_plot(self, network_usage, time):
        print(6)


    # Controller link
    def set_controller(self, controller):
        self.controller = controller
