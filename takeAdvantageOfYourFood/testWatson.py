import json
import os
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
	'2018-03-19',
	url='https://gateway.watsonplatform.net/visual-recognition/api',
	iam_apikey='{iam_api_key}')

print(os.path)

with open('takeAdvantageOfYourFood/static/IngredientsImages/18/1.jpg', 'rb') as images_file:
	classes = visual_recognition.classify(
		images_file,
		threshold='0.6',
		classifier_ids='food').get_result()
	print(json.dumps(classes, indent=2))