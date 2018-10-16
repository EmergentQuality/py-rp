class Phone:

    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print("Calling from", self.number, "to", other_number)

    def text(self, other_number, msg):
        print("Sending text from", self.number, "to", other_number)
        print(msg)


test_phone = Phone(333 - 1234)
test_phone.call(617)
test_phone.text(666, "Hi!")


class IPhone(Phone):

    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None
        self.os = "iOS"

    def set_fingerprint(self, fingerprint):
        self.fingerprint = fingerprint

    def unlock(self, fingerprint=None):
        if (self.fingerprint is None):
            print("Phone unlocked. No fingerprint needed.")
        elif (fingerprint == self.fingerprint):
            print("Phone unlocked. Fingerprint matches.")
        else:
            print("Phone locked. Fingerprint doesn't match.")

    def check_os(self, os):
        return self.os


my_iphone = IPhone(151)
my_iphone.unlock()
my_iphone.set_fingerprint("Jory's Fingerprint")
my_iphone.unlock()
my_iphone.unlock("Jory's Fingerprint")

# And we can call the Phone methods:
my_iphone.call(515)
my_iphone.text(51121, "Hi!")
