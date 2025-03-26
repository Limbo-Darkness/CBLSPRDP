# Imports
import os
from tkinter import filedialog as fd

class Controller:
    def __init__(self, model, view):
        # MVC setup
        self.model = model
        self.view = view
        view.set_controller(self)
        # Precursor definitions
        self.thresh_cpu = 0
        self.thresh_mem = 0
        self.thresh_io = 0
        self.thresh_file = 0
        self.thresh_net = 0

    # Closer function implementation
    def _closer(self):
        self.view.root.quit()
        self.view.root.destroy()

    # Connect to server function implementation
    def connect_server(self):
        print(1)

    # Analyze file function implementation
    def analyze_server(self):
        #self.model.
        # Graph calls
        self.cpu_plotter()
        self.mem_plotter()
        #sleep(5)
        # Updating labels

    def threshold_setter(self):
        self.thresh_cpu = 1

    def messagefailure(self, string):
        print(string)

    # CPU Graph Data Connection from Model
    def cpu_plotter(self):
        # Set data (cpu usage, time)
        time = self.model.time
        cpu_usage = self.model.cpu
        if(cpu_usage >= self.thresh_cpu):
            self.messagefailure('cpu')
        self.view.cpu_plot(cpu_usage, time)

    def mem_plotter(self):
        time = self.model.time
        mem_usage = self.model.mem
        if(mem_usage >= self.thresh_mem):
            self.messagefailure('mem')
        self.view.mem_plot(mem_usage, time)

    def io_plotter(self):
        time = self.model.time
        io_usage = self.model.io
        if(io_usage >= self.io_usage):
            self.messagefailure('mem')
        self.view.io_plot(io_usage, time)

    def filesystem_plotter(self):
        time = self.model.time
        filesystem_usage = self.model.filesystem
        self.view.filesystem_plot(filesystem_usage, time)

    def network_plotter(self):
        time = self.model.time
        network_usage = self.model.network
        self.view.network_plot(network_usage, time)