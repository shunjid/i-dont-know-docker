class User:
    def __init__(self, first_name, last_name, email_address, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.mobile_number = mobile_number
        pass

    def __repr__(self):
        return f"""
        Name: {self.first_name} {self.last_name},
        Email: {self.email_address} 
        and Mobile Number: {self.mobile_number}
        """

    def to_dict(self):
        return {
            "name": f"{self.first_name} {self.last_name}",
            "email": self.email_address,
            "mobile": self.mobile_number,
        }
