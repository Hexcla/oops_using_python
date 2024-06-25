class pychram:
     def execute(self): # To call praticular function
        print("compling")
        print("runing")

class myownide:
    def execute(self):
        print("spelling correction")
        print("expore extensions")
        print("Running")
        print("Compling")
        
class laptop:
    def code(self,ide):
        ide.execute()
        
ide = myownide()
lap1 = laptop()
lap1.code(ide)