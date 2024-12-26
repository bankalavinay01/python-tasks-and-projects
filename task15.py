#        *** OOP'S CODING EXERCISE ***

class mobiles(): 
    brand   = "samsung" 
    colour  = "green"
    size    = "6 inches"
    storage = "1TB"
    def course(self): 
        print("writing a program in",self.brand)
    def game(self):
        print("playing the games")
        self.course()
    def files(self):
        print("creating a files")
        self.game()
#objectname = classname()
brand = mobiles()
brand.course()
brand.game()
brand.files()

                
 


