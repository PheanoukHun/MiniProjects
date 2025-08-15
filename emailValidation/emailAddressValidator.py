# Importing the Tkinter Module
import tkinter as tk

# Checks the Validity of a Custom Email
def validateEmail(emailStr):
    forbiddenDomainCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", "{", "}", "[", "]", "\"", "`", "\'", "\\", "/"]

    # Checks if the Email is too long or too short
    if len(emailStr) > 254:
        return False, "Email is Too Long"
    
    if len(emailStr) <= 4:
        if len(emailStr) == 0:
            return False, "Email Input Field is Empty"
        return False, "Email is Too Short"
    
    # Get the Username of the Email and Checks if there is an email server or not
    try:
        atIndex = emailStr.index("@")
        username = emailStr[:atIndex]
        validUsername, message = validateUsername(username)
        if not validUsername:
            return validUsername, message
    except:
        return False, "Cannot Find the Mail Server"
    
    # Checks if there is a Domain and Top-Level Domain
    try:
        domains = emailStr[atIndex+1:]    
        domainList = domains.split(".")
        
        for domain in domainList:
            if len(domain) == 0:
                return False, "You Cannot have an Empty Domain or Top-Level Domain"
            for char in domain:
                if char in forbiddenDomainCharacters:
                    return False, f"You cannot use {char} in a domain or top-level domain."
    except:
        return False, "Either Cannot Find Domain or Top-Level Domain. Please at least have one domain and subdomain (Ex: username@domain.topleveldomain | example@email.com)"
    
    # Returns True if there is no Problem
    return True, emailStr

# Checks the Validity of a Username
def validateUsername(username):
    forbiddenUsernameCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", "{", "}", "[", "]", "\"", "`", "\'", "\\", "/"]

    # Makes Sure that the Username is not Empty
    if len(username) == 0:
        return False, "Username cannot be Empty"

    # Check to See if the Username has any forbidden characters
    for char in username:
        if char.isspace():
            return False, "No Whitespaces in Username"
        
        if char in forbiddenUsernameCharacters:
            return False, f"You cannot use {char} in the username of an email address."
    
    # Returns True if the Username is Valid
    return True, "Valid Username"

def createNormalEmail(username, mailServer):
    
    # Checks to See if the Username is Valid
    valid, message = validateUsername(username)
    
    if valid:
        # Checks to See if a Email Server has been Chosen
        if mailServer == "---- Please Select an Option ----":
            return False, "Please Select an Email Server."
        
        # Returns True if both options are Valid
        return True, f"{username}{mailServer}"
    else:
        # Else Returns False with a the Invalid Username Message
        return False, message

class EmailValidatorMenu:
    
    # Initializes the Root and Draws the MainPage Page on Draw
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x400")
        MainPage(self)
    
    # Wipes the Screen
    def clearScreen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # Wipes the Screen and Draws the NormalEmailValidator Class
    def switchToNormalValidator(self):
        self.clearScreen()
        NormalEmailValidator(self)
    
    # Wipes the Screen and Draws the CustomEmailValidator Class
    def switchToCustomValidator(self):
        self.clearScreen()
        CustomEmailValidator(self)
    
    # Wipes the Screen and Draws the MainPage Class
    def switchToMainPage(self):
        self.clearScreen()
        MainPage(self)
    
    # Runs the program
    def run(self):
        self.root.mainloop()

class MainPage:
    def __init__(self, controller):
        self.root = controller.root
        self.root.title("Email Validator")
        
        # Configure the Grid Cells
        for i in range(4):
            self.root.rowconfigure(i, weight=1)
            
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.columnconfigure(2, weight=1)
        
        # Create a Title Label
        tk.Label(self.root, text="Email Validator",
                font=("Arial", 20)).grid(column=1, row=0, sticky=tk.NSEW, padx=5, pady=5)
        
        # Create a Button that Directs the User to a Normal Email Address Validator
        tk.Button(self.root, text="Normal Email Validator", font=("Arial", 16),
                command=lambda: controller.switchToNormalValidator()).grid(column=1, row=1, sticky=tk.NSEW, padx=5, pady=5)
        
        # Create a Button that Directs the User to a Custom Email Address Validator
        tk.Button(self.root, text="Custom Email Validator", font=("Arial", 16),
                command=lambda: controller.switchToCustomValidator()).grid(column=1, row=2, sticky=tk.NSEW, padx=5, pady=5)

        # Create a Button that Destroys the Root (Exiting Out of the Program)
        tk.Button(self.root, text="Exit", font=("Arial", 16),
                command=lambda: self.root.destroy()).grid(column=1, row=3, sticky=tk.NSEW, padx=5, pady=10)
    
# A Normal Email Address Screen (ex: example@gmail.com)
class NormalEmailValidator:
    def __init__(self, controller):
        self.root = controller.root
        self.root.title("Normal Email Validator")
        
        # Configure the Grid Cells
        for i in range(5):
            self.root.rowconfigure(i, weight=1)
            
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(2, weight=3)
        
        # Creates a Back Button that Returns the Program back to the Main Menu
        tk.Button(self.root, text="Back", font=("Arial", 16),
                command=lambda: controller.switchToMainPage()).grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)
        
        # Creates the Title Text Label
        tk.Label(self.root, text="Normal Email Validator",
                font=("Arial", 20)).grid(column=1, row=0, columnspan=2, sticky=tk.NSEW, padx=5, pady=10)
        
        # Create a Text Labels for the Normal Email Servers
        tk.Label(self.root, text="Normal Email Server: ",
                font=("Arial", 14)).grid(column=1, row=1, sticky=tk.NSEW, padx=5, pady=5)
        
        # Creating a Dropdown Menu
        
        ## Creating a Variable to Store the Selected Value
        self.dropdown = tk.StringVar()
        self.dropdown.set("---- Please Select an Option ----")
        
        ## Creating the Dropdown Menu
        options = ["@google.com", "@yahoo.com", "@icloud.com"]
        dropdown = tk.OptionMenu(self.root, self.dropdown, *options)
        dropdown.grid(column=2, row=1, sticky=tk.NSEW, padx=5, pady=5)
        
        # Creates the Username Text Label
        tk.Label(self.root, text="Username: ",
                font=("Arial", 14)).grid(column=1, row=2, sticky=tk.NSEW, padx=5, pady=5)
        
        # Creating a Input Field
        
        ## Create a StringVar to hold the Input
        self.usernameVar = tk.StringVar()
        
        ## Create the Input Field
        usernameEntry = tk.Entry(self.root, textvariable=self.usernameVar, width=20)
        usernameEntry.grid(column=2, row=2, sticky=tk.NSEW, padx=5, pady=5)
        
        # Creates the Validate Button
        tk.Button(self.root, text="Validate", font=("Arial", 14),
                command=lambda: self.validatePressed()).grid(column=2, row=3, sticky=tk.NSEW, padx=5, pady=5)
    
    def validatePressed(self):
        
        # Get the Current Values of The Dropdown and Username Field
        currServer = self.dropdown.get()
        currUsername = self.usernameVar.get()

        # Checks if the Email is Valid or Not and Displays the Results
        valid, message = createNormalEmail(currUsername, currServer)
        if valid:
            tk.Label(self.root,
                    text=f"{message} is a Valid Email Address.",
                    font=("Arial", 14)).grid(column=1, row=3, sticky=tk.NSEW, padx=5, pady=5)
        else:
            tk.Label(self.root, text=message,
                    font=("Arial", 14)).grid(column=1, row=3, sticky=tk.NSEW, padx=5, pady=5)

# A Custom Email Address Screen (ex: example@my.exampleInstitution.org)
class CustomEmailValidator:
    def __init__(self, controller):
        self.root = controller.root
        self.root.title("Custom Email Validator")
        
        # Configure the Grid Cells
        for i in range(5):
            self.root.rowconfigure(i, weight=1)
        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.columnconfigure(2, weight=3)
        self.root.columnconfigure(3, weight=1)
        
        # Creates a Back Button that Returns the Program back to the Main Menu
        tk.Button(self.root, text="Back", font=("Arial", 16),
                command=lambda: controller.switchToMainPage()).grid(column=0, row=0, sticky=tk.NSEW, padx=10, pady=10)
        
        # Creates the Title Text Label
        tk.Label(self.root, text="Custom Email Validator",
                font=("Arial", 20)).grid(row=0, column=1, columnspan=2, sticky=tk.NSEW, padx=5, pady=10)
        
        # Creates a Text Labels for Email Address
        tk.Label(self.root, text="Email Address: ",
                font=("Arial", 16)).grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=5)
        
        # Create a Text Input Field for the Email Address
        
        ## Creates a StringVar to Hold the Input
        self.emailVar = tk.StringVar()
        
        ## Create the Input Field
        tk.Entry(self.root, width=35,
                textvariable=self.emailVar).grid(row=2, column=2, sticky=tk.NSEW, padx=5, pady=5)
        
        # Creates the Validate Button
        tk.Button(self.root, text="Validate", font=("Arial", 14),
                command=lambda: self.validatePressed()).grid(row=3, column=1, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)
        
    def validatePressed(self):
        # Get the Current Value fo the Email Field
        currEmail = self.emailVar.get()
        
        # Checks if the Email is Valid or Not and Displays the Results
        valid, message = validateEmail(currEmail)
        if valid:
            tk.Label(self.root,
                    text=f"{message} is a Valid Email Address",
                    font=("Arial", 14)).grid(row=4, column=1, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)
        else:
            tk.Label(self.root,
                    text=f"{message}",
                    font=("Arial", 14)).grid(row=4, column=1, columnspan=2, sticky=tk.NSEW, padx=5, pady=5)

# Main Loop
if __name__ == "__main__":
    mainMenu = EmailValidatorMenu()
    mainMenu.run()