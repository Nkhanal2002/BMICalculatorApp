#imports json library
import json
#imports different kivy methods from its library
from kivy.app import App
from kivy.core.window import Window

class BmiCalculatorApp(App):
    """Represents the whole app widgets and calculates the BMI of a person"""

    def build(self):
        """Represents the title and background of an app"""
        #using clearcolor as rbga format for main window's background
        Window.clearcolor = 126/255, 143/255, 214/255, 1
        self.title = "BMI Calculator"
        self.peopleInfoDict = {}

    def clickMe(self):
        """Calculates BMI of a person when a button is clicked"""

        #executes try block when the inputs are error free
        try:
            self.root.ids.mainContent.text = f"{(float(self.root.ids.weight.text)/(float(self.root.ids.humanHeight.text)*float(self.root.ids.humanHeight.text)))*703:.1f}"
            
        except ZeroDivisionError: #executes only if user has ZeroDivision error
            self.root.ids.mainContent.text = f"Zero Division Error!"

        except: #executes only if user has other error
            self.root.ids.mainContent.text = f"Don't leave Input Boxes Empty!"
        
        self.root.ids.loadInformation.text = ""

    def accumulateBMI(self):
        """Collects BMI reports"""
        if self.root.ids.name.text.lower():

            self.peopleInfoDict[self.root.ids.name.text.lower()] = self.root.ids.mainContent.text

            #creates a peopleBMIInfo json file
            with open("peopleBMIInfo.json", "w") as f:
                json.dump(self.peopleInfoDict,f, indent=2)  #dumps added data into a peopleBMIInfo file

            # clears used input boxes and labels
            self.root.ids.name.text = "" 
            self.root.ids.weight.text = "" 
            self.root.ids.humanHeight.text = ""
            self.root.ids.mainContent.text = ""
            self.root.ids.loadInformation.text = ""
            
    def searchBMIWithName(self):
        """Searches the calculated BMI relevant to a person and tells if it falls within under, healthy, over, or obese range"""

        #executes when user provides error-free input data
        try:
            #loads the data from json file
            with open("peopleBMIInfo.json") as f:
                self.peopleInfoDict2 = json.load(f)

            #provides information relevant to user-entered data
            self.root.ids.loadInformation.text = f"Hi {self.root.ids.nameHistory.text}! Your BMI is {self.peopleInfoDict2[self.root.ids.nameHistory.text.lower()]}."

            #gives under weight range info
            if float(self.peopleInfoDict2[self.root.ids.nameHistory.text.lower()]) < 18.5:
                self.root.ids.loadInformation.text += f"\n(falls within Under Weight range)"

            #gives over weight range info
            elif 24.9 < float(self.peopleInfoDict2[self.root.ids.nameHistory.text.lower()])<=29.9:
                self.root.ids.loadInformation.text += f"\n(falls within Over Weight Range)"

            #gives obese range info
            elif float(self.peopleInfoDict2[self.root.ids.nameHistory.text.lower()])>29.9:
                self.root.ids.loadInformation.text += f"\n(falls within Obese Range)"

            #gives healthy weight range info
            else:
                self.root.ids.loadInformation.text += f"\n(falls within Healthy Weight Range)"
        
        #executes if any exception occurs
        except TypeError:
            self.root.ids.loadInformation.text = "Please enter Numeric Value!"
        except ZeroDivisionError:
            self.root.ids.loadInformation.text = "Zero Division Error!"
        except:
            self.root.ids.loadInformation.text = f"Please enter a name in search-bar first!"

        #clears used input boxes and labels
        self.root.ids.mainContent.text = ""
        self.root.ids.nameHistory.text = ""
            
#executes only if the name of file is main file
if __name__ == "__main__":
    BmiCalculatorApp().run() #calls the parent class, which is BmiCalculatorApp

