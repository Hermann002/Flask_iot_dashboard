class User:
    is_admin = False
    
    def __init__(self, userName, userEmail, password, is_admin):
        self.userName = userName
        self.userEmail = userEmail
        self.password = password
        self.is_admin = is_admin

    def signUp(self, userName, userEmail, password):
        pass # mettre les informations dans une base de donnée mongoDB/postgres/detabase