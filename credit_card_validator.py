'''Credit Card Validator 
- Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discover) 
and validates it to make sure that it is a valid number 


'''

class ValidCard:
    def __init__(self, number):
        self.number = number 
        self.vendors = ['4', '5', '6', '34', '37']

    def __len__(self):
        return len(self.number)

    def __str__(self):
        return f'The card number is {self.number}'

    def validate(self):

        number = self.number
    
        if len(number) < 15:
            return 'Invalid card number'
        
        if not number.startswith(tuple(self.vendors)):
            return 'Invalid vendor'

        #validation for Visa, Master and Discover
        if len(number)==16:
            #Verifying a 16-digit card number starts by taking the first 15 digits
            n = [int(i) for i in number[:-1]]

            #Starting with the first digit, multiply every second digit by 2
            n[::2] = [int(i)*2 for i in number[::2]]

            #Every time there is a two-digit number, add those digits together 
            digit_sum = [num%10 + num//10 for num in n]

            #When this number is added to the check digit, then the result must be an even multiple of 10
            #The number is therefore valid. If the algorithm doesn't produce a multiple of 10, then the card number cannot be valid.
            if (sum(digit_sum) + int(number[-1])) % 10 == 0:
                return 'The card is valid'
            return 'Invalid card'

        #Validation for Amex
        #same procedure, just without taking out and adding back in the last digit 
        if len(number) == 15:
            n = [int(i) for i in number]
            n[::2] = [int(i)*2 for i in number[::2]]
            digit_sum = [num%10 + num//10 for num in n]
            if sum(digit_sum) % 10 == 0:
                return 'The card is valid'
            return 'Invalid card'

new_card = ValidCard('xxxxxxxxxxxxxxxx')
print(new_card.validate())



    

