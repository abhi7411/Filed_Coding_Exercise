from flask import Flask, request
from methods import *
import random
app = Flask(__name__)

@app.route("/")
def home():
	return "Coding Exercise for Filed ^_^"

def CheapPaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, Amount, SecurityCode):
	''' 
		This returns True if the payment is processed else False.
		Currently it is returning a random value based on this the payment is further processed 
	
	'''
	return random.choices([True, False])

def ExpensivePaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, Amount, SecurityCode):
	''' 
		This returns True if the payment is processed else False.
		Currently it is returning a random value based on this the payment is further processed 
	
	'''
	return random.choices([True, False])

def PremiumPaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, Amount, SecurityCode):
	''' 
		This returns True if the payment is processed else False.
		Currently it is returning a random value based on this the payment is further processed 
	
	'''
	return random.choices([True, False])

@app.route("/ProcessPayment", methods=['POST'])
def ProcessPayment():
	''' 
		This returns response on the processing of the request along with the status code of it.
		It also validates the data and processess the request accordingly with given business rules. 
	
	'''

	CreditCardNumber	= request.values.get('CreditCardNumber')
	CardHolder			= request.values.get('CardHolder')
	ExpirationDate		= request.values.get('ExpirationDate')
	Amount				= request.values.get('Amount')
	SecurityCode		= request.values.get('SecurityCode') if 'SecurityCode' in request.values else None
	# print(CreditCardNumber)
	# print(CardHolder)
	# print(ExpirationDate)
	# print(Amount)
	try:
		# print("")
		valid_details = is_valid_card_number(CreditCardNumber) and is_valid_card_holder_name(CardHolder) and is_valid_expiry_date(ExpirationDate) and is_valid_security_code(SecurityCode) and is_valid_amount(Amount)
		if valid_details:
			Amount = float(Amount)
			if Amount <= 20:
				transactionStatus = CheapPaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, Amount, SecurityCode)
			elif Amount >= 21 and Amount <= 500:
				try:
					transactionStatus = ExpensivePaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, Amount, SecurityCode)
				except:
					transactionStatus = CheapPaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, Amount, SecurityCode)
			elif Amount > 500:
				for i in range(3):
					# print("Processing Payment try {}/3".format(i+1))
					transactionStatus = PremiumPaymentGateway(CreditCardNumber, CardHolder, ExpirationDate, Amount, SecurityCode)
					if transactionStatus == True: # Checking if processed
						break
			if transactionStatus:
				response = "Payment is processed", 200
			else:
				response = "Sorry - Payment was not processed", 200
		else:
			response = "The request is invalid, Bad Request", 400
	except Exception as e:
		# print(str(e))
		response = "Internal server error", 500
	# print("")
	return response


if __name__ == "__main__":
    app.run()