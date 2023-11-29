import unittest
import requests
import json 

class Numbers(unittest.TestCase):

    def test_api_get(self):

        cevap = requests.get("https://api.github.com/events")
        print (cevap.text)

    def test_api_post(self):
        payload = {"key1":"value1"}
        gonder = requests.post("https://api.github.com/events", data=payload)
        print(gonder.status_code)

    def test_api_get2(self):
        payload = {"key1":"value1"}
        cevap = requests.post("https://automationexercise.com/api/productsList", data=payload)
        print (cevap.text)
        print (cevap.status_code)

    def test_api_get3(self):
        cevap = requests.get("https://automationexercise.com/api/brandsList")
        icerik = json.loads(cevap.text)
        item_id = icerik["brands"][1]["id"]
        self.assertEqual(2, item_id)

    def test_api_post2(self):
        payload = {"search_product":"top"}
        gonder = requests.post("https://automationexercise.com/api/searchProduct", data=payload)
        icerik = json.loads(gonder.text)
        self.assertEqual("Tops", icerik["products"][0]["category"]["category"])

    def test_api_post3(self):
        payload = {"canim_canim":"top"}
        gonder = requests.post("https://automationexercise.com/api/searchProduct", data=payload)
        print (gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual("Tops", icerik["products"][0]["category"]["category"])     
        
    def test_api_post4(self):
        gonder = requests.get("https://automationexercise.com/api/searchProduct")
        print (gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual(405, icerik["responseCode"])
    def test_api_post5(self):
        gonder = requests.post("https://automationexercise.com/api/searchProduct")
        print(gonder.text)
        icerik = json.loads(gonder.text)
        self.assertEqual(400, icerik["responseCode"])
        self.assertEqual("Bad request, search_product parameter is missing in POST request.", icerik["responseMessage"])
    def test_api_post6(self):
        
        valid_email = "your_valid_email@example.com"
        valid_password = "your_valid_password"

        payload = {
            "email": valid_email,
            "password": valid_password
        }

        gonder = requests.post("https://automationexercise.com/api/verifyLogin", data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)
        
        self.assertEqual(200, icerik["responseCode"])
        self.assertEqual("User exists!", icerik["responseMessage"])
    def test_api_post7(self):
       
        valid_password = "your_valid_password"

        payload = {
            "password": valid_password
        }

        gonder = requests.post("https://automationexercise.com/api/verifyLogin", data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)

        self.assertEqual(400, icerik["responseCode"])
        self.assertEqual("Bad request, email or password parameter is missing in POST request.", icerik["responseMessage"])
    def test_api_delete1(self):
        
        gonder = requests.delete("https://automationexercise.com/api/verifyLogin")
        print(gonder.text)
        icerik = json.loads(gonder.text)

        self.assertEqual(405, icerik["responseCode"])
        self.assertEqual("This request method is not supported.", icerik["responseMessage"])
    def test_api_post8(self):
        
        invalid_email = "invalid_email@example.com"
        invalid_password = "invalid_password"

        payload = {
            "email": invalid_email,
            "password": invalid_password
        }

        gonder = requests.post("https://automationexercise.com/api/verifyLogin", data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)

        self.assertEqual(404, icerik["responseCode"])
        self.assertEqual("User not found!", icerik["responseMessage"])
    def test_api_post9(self):
        valid_payload = {
            "name": "Your Name",
            "email": "your_email@example.com",
            "password": "your_password",
            "title": "Mr",
            "birth_date": "01",
            "birth_month": "01",
            "birth_year": "1990",
            "firstname": "John",
            "lastname": "Doe",
            "company": "Your Company",
            "address1": "123 Main Street",
            "address2": "Apt 45",
            "country": "Your Country",
            "zipcode": "12345",
            "state": "Your State",
            "city": "Your City",
            "mobile_number": "1234567890"
        }

        gonder = requests.post("https://automationexercise.com/api/createAccount", data=valid_payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)

        self.assertEqual(201, icerik["responseCode"])
        self.assertEqual("User created!", icerik["responseMessage"])
    def test_api_delete2(self):
        valid_email = "your_email@example.com"
        valid_password = "your_password"

        payload = {
            "email": valid_email,
            "password": valid_password
        }

        gonder = requests.delete("https://automationexercise.com/api/deleteAccount", data=payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)

        self.assertEqual(200, icerik["responseCode"])
        self.assertEqual("Account deleted!", icerik["responseMessage"])
    def test_api_put1(self):
        valid_payload = {
            "name": "Updated Name",
            "email": "updated_email@example.com",
            "password": "updated_password",
            "title": "Mrs",
            "birth_date": "02",
            "birth_month": "02",
            "birth_year": "1995",
            "firstname": "Jane",
            "lastname": "Doe",
            "company": "Updated Company",
            "address1": "456 New Street",
            "address2": "Unit 67",
            "country": "Updated Country",
            "zipcode": "54321",
            "state": "Updated State",
            "city": "Updated City",
            "mobile_number": "9876543210"
        }

        gonder = requests.put("https://automationexercise.com/api/updateAccount", data=valid_payload)
        print(gonder.text)
        icerik = json.loads(gonder.text)

        self.assertEqual(200, icerik["responseCode"])
        self.assertEqual("User updated!", icerik["responseMessage"])
    def test_api_get4(self):
        valid_email = "existing_user@example.com"

        params = {
            "email": valid_email
        }

        gonder = requests.get("https://automationexercise.com/api/getUserDetailByEmail", params=params)
        print(gonder.text)
        icerik = json.loads(gonder.text)

        self.assertEqual(200, icerik["responseCode"])
        self.assertIn("User Detail", icerik)

if __name__ == '__main__':
    unittest.main()