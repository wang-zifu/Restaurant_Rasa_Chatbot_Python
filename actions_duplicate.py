# from __future__ import absolute_import
# from __future__ import division
# from __future__ import unicode_literals
#
# import json
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet
#
# import zomatopy
#
#
# # Action search
# class ActionSearchRestaurants(Action):
# 	def name(self):
# 		return 'action_search_restaurants'
#
# 	def run(self, dispatcher, tracker, domain):
# 		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
# 		zomato = zomatopy.initialize_app(config)
# 		loc = tracker.get_slot('location')
# 		cuisine = tracker.get_slot('cuisine')
# 		location_detail=zomato.get_location(loc, 1)
# 		d1 = json.loads(location_detail)
# 		lat=d1["location_suggestions"][0]["latitude"]
# 		lon=d1["location_suggestions"][0]["longitude"]
# 		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
# 		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
# 		d = json.loads(results)
# 		dispatcher.utter_message("check json values : " + d)
# 		response=""
# 		if d['results_found'] == 0:
# 			response= "no results"
# 		else:
# 			for restaurant in d['restaurants']:
# 				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
#
# 		# dispatcher.utter_message("-----" + response)
#
# 		# response = "We will add later response result"
# 		# try:
# 		# 	file = open("body.txt", "w")
# 		# 	counter = 1
# 		#
# 		# 	for restaurant in d['resturants']:
# 		# 		file.write("{}. Restaurant Name: {}\n Restaurant locality address: {}\n Average budget for two people: {}\n Zomato user rating: {}\n\n".format(
# 		# 				counter,restaurant['restaurant']['name'], restaurant['restaurant']['location']['address'], "2 people ", "4.6"))
# 		# 		counter += 1
# 		# 	file.close()
# 		# except:
# 		# 	response = "no results"
# 		#
# 		# 	dispatcher.utter_message("Foodie Rasa Chatbot Assignment : ", response)
#
# 		return [SlotSet('location', loc)]
#
#
#
#
