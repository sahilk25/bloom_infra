import frappe
import requests
from frappe.utils import get_site_name
from frappe.core.doctype.user.user import generate_keys

def update_user(User, method):
	if User.user_type == "System User":
		if User.api_key == None:
			generate_keys(User.email)
		site_name = get_site_name(frappe.local.request.host)
		user_api = frappe.conf.get("user_api")
		print("test: ", user_api)
		print("method: ", method)
		
		payload = {
			"Familyname": User.last_name ,
			"UserEmail": User.email , 
			"UserName": User.email ,
			"Firstname": User.first_name ,
			"SiteName": site_name ,
			# "enabled": User.enabled ,
			"APIKey": User.api_key ,
			"ApplicationAccessDetails": "test" ,
			"SecretKey": User.api_secret

		}
		print("PAYLOAD: ", payload)
		hit_api = requests.post(user_api, json=payload)
		print(hit_api.content)
	 
	return None