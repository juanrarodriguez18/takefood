import json
import os
from watson_developer_cloud import VisualRecognitionV3
import dotenv

dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

visual_recognition = VisualRecognitionV3(
	'2018-03-19',
	url='https://gateway.watsonplatform.net/visual-recognition/api',
	iam_apikey=os.environ.get('WATSON_API_KEY'))

with open('takeAdvantageOfYourFood/static/IngredientsImages/18/1.jpg', 'rb') as images_file:
	classes = visual_recognition.classify(
		images_file,
		threshold='0.85',
		classifier_ids='food').get_result()
	print(json.dumps(classes, indent=2))