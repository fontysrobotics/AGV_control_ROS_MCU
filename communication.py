import supervisor

class serial:
    def __init__(self, o_data, status):
        self.DATA = ""
        self.userInput = ""
        self.oDATA = o_data
        self.Status = status

    def write_data(self):
        print(self.oDATA)

        
    def read_data(self):
        if (supervisor.runtime.serial_bytes_available):
            value = input().strip()
            value = float(value)
            if value == "":
                pass
            else:
                self.DATA = value

    def user_input(self):
        if (supervisor.runtime.serial_bytes_available):
            iUser = input().strip()
            iUser = str(iUser)
            if iUser == "":
                pass
            elif iUser == "start":
                self.userInput = "start"
            
            elif iUser == "stop":
                self.userInput = "stop"

            else:
                self.userInput = "error"

    def status_message(self):
        print(self.Status)


   
