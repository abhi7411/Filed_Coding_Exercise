import requests
from datetime import date

def fetchTestCases():
	testCases = [
		{
			'TestCase' : 'Valid Check',
			'CreditCardNumber' : '4539774507799998',
			'CardHolder' : 'Ram Das',
			'ExpirationDate' : '2022-12',
			'Amount' : 20.0,
			'SecurityCode' : '123' 
		},
		{
			'TestCase' : 'Credit Card Check',
			'CreditCardNumber' : '000000',
			'CardHolder' : 'Ashok',
			'ExpirationDate' : '2025-12',
			'Amount' : 20.0,
			'SecurityCode' : '123' 
		},
		{
			'TestCase' : 'Amount Check',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : 'Ram',
			'ExpirationDate' : '2022-12',
			'Amount' : -20.0,
			'SecurityCode' : '123' 
		},
		{
			'TestCase' : 'Old Expiry Date Check',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : 'Ram',
			'ExpirationDate' : '2020-01',
			'Amount' : 20.0,
			'SecurityCode' : '123' 
		},
		{
			'TestCase' : 'Security Code extra number Check',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : 'Ram',
			'ExpirationDate' : '2022-12',
			'Amount' : 20.0,
			'SecurityCode' : '1234' 
		},
		{
			'TestCase' : 'Security Code alphanumeric Check',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : 'Ram',
			'ExpirationDate' : '2022-12',
			'Amount' : 20.0,
			'SecurityCode' : '12a' 
		},
		{
			'TestCase' : 'Date value given as string Check',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : 'Ram',
			'ExpirationDate' : 'date',
			'Amount' : 20.0,
			'SecurityCode' : '123' 
		},
		{
			'TestCase' : 'Processing gateway based on Amount Check',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : 'Ram',
			'ExpirationDate' : '2019-02',
			'Amount' : 500.0,
			'SecurityCode' : '123' 
		},
		{
			'TestCase' : 'Card holder name Check',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : '122424',
			'ExpirationDate' : '2019-02',
			'Amount' : 500.0,
			'SecurityCode' : 'a12' 
		},
		{
			'TestCase' : 'Card holder name Check with non letters',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : '-";/>@#$%^&*(():',
			'ExpirationDate' : '2019-02',
			'Amount' : 500.0,
			'SecurityCode' : 'a12' 
		},
		{
			'TestCase' : 'Zero Amount Check',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : 'Ram',
			'ExpirationDate' : '2019-02',
			'Amount' : 00.0,
			'SecurityCode' : '123' 
		},
		{
			'TestCase' : 'Retury Payment Check',
			'CreditCardNumber' : '4539774507799684',
			'CardHolder' : 'Ram',
			'ExpirationDate' : '2025-02',
			'Amount' : 1500.0,
			'SecurityCode' : '123' 
		}

	]
	return testCases

def ExecuteTestCases():
	for TestCase in fetchTestCases():
		response = requests.post('http://127.0.0.1:5000/ProcessPayment', data=TestCase)
		print("Executing TestCase", TestCase['TestCase'], "--> Response is -", response.text, "| Status Code -", response.status_code)
	return

if __name__ == "__main__":
	ExecuteTestCases()