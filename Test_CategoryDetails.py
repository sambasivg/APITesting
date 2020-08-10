import requests
import unittest


API_URL = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"


class CategoryList(unittest.TestCase):
    # Get API Response
    response = requests.get(API_URL)
    # Read API Data
    response_body = response.json()
    category_name = "Carbon credits"
    canre_list = True
    promotions_name = "Gallery"
    promotions_description = "2x larger image"

# validate API status code and Content types
    def test_category_details_check_status_code_equals_200(self):
        # validate whether API status code is equal to 200 or not
        assert self.response.status_code == 200, \
            "Response status code Expected : 200, but found : " + str(self.response.status_code)
        # validate whether API response headers 'Content-Type'  is "application/json" or not
        assert self.response.headers['Content-Type'] == "application/json", \
            "Response content type Expected:application json, but found : " + str(self.response.headers['Content-Type'])

    # validate Category names
    def test_verify_category_name(self):
        # Validate whether response body Name parameter value equal to Carbon credits or not
        if self.response_body["Name"] != self.category_name:
            raise Exception("Category name is Not matched")

    # validate CanRelist values
    def test_verify_canre_list(self):
        # Validate whether response body "CanRelist" parameter value equal to true or not
        assert self.response_body["CanRelist"] == bool(self.canre_list), \
            "Response Body Parameter CanRelist  Expected : True, but found" + str(self.response_body["CanRelist"])

    # validate promotion=galery and its description
    def test_verify_promotions_name_and_description(self):
        for promotionalRecord in self.response.json()['Promotions']:
            if promotionalRecord["Name"] == self.promotions_name:
                #  when promotion name is Gallery Verify whether Promotion description have 2x larger image or not
                assert self.promotions_description in promotionalRecord["Description"], \
                      "Data not matched! Expected : 2x larger image, but found : " + str(promotionalRecord['Description'])


if __name__ == '__main__':
    unittest.main()

