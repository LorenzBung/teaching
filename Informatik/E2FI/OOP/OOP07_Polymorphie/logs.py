class LogEntry:
    def __init__(self, message):
        self.message = message
    def display(self):
        print(self.message)

class InfoLog(LogEntry):
    def display(self):
        print(f"[INFO] {self.message}")

class ErrorLog(LogEntry):
    def display(self):
        print(f"[ERROR] {self.message} (!!!)")

log1 = InfoLog("System started")
log2 = ErrorLog("Disk not found")
log3 = InfoLog("Connection established")
log4 = ErrorLog("Permission denied")

log1.display()
log2.display()
log3.display()
log4.display()
