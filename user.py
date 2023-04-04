class User:

    def __init__(self,first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name 
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
    def spend_points(self,amount):
        self.gold_card_points = self.gold_card_points - amount

User1 = User("Maliq","Harris","cool@gmail", "22")
User2 = User("Steven", "Universe", "mruniversejr@gmail.com","15")
User3 = User("Greg", "Universe", "Starchild@gmail.com", "56")
User1.enroll()
User1.display_info()
User1.spend_points(50)
User1.display_info()
User2.enroll()
User2.spend_points(80)
User1.display_info()
User2.display_info()
User3.display_info()
