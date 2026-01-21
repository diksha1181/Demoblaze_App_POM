from Page_Functions.Monitor_Functions import MonitorFunctions


class MonitorProcess:

    def __init__(self, monitor:MonitorFunctions):
        self.monitor = monitor

    def run_process(self):
        self.monitor.open_home()
        self.monitor.open_monitors()
        self.monitor.open_monitor1()
        self.monitor.cart()
        self.monitor.verify()
