from flask import Flask, render_template, send_file, make_response, url_for, Response,request,redirect
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import werkzeug
from classifier.RaceClassifier import *
app = Flask(__name__)
api = Api(app)

model = RaceClassifier(model_path = "fair_face_models/res34_fair_align_multi_7_20190809.pt")

parser = reqparse.RequestParser()
parser.add_argument('query')

class PredictRace(Resource):
    ''' def get(self,image_path):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']

        
        prediction = model.predict(image_name = "detected_faces/race_Latino_face0.jpg")

        # Output either 'Negative' or 'Positive' along with the score
        if(prediction == 0):
            pred_text = "White"
        elif(prediction == 1):
            pred_text = "Black"
        elif(prediction == 2):
            pred_text = "Latino_Hispanic"
        elif(prediction == 3):
            pred_text = "East Asian"
        elif(prediction == 4):
            pred_text = "Southeast Asian"
        elif(prediction == 5):
            pred_text = "Indian"
        elif(prediction == 6):
            pred_text = "Middle Eastern"
            
 

        # create JSON object
        output = {'pred_race': pred_text, 'prediction': prediction} 
        
        return output '''
    def post(self):
        # read like a stream
        
        '''if not request.json or 'image' not in request.json: 
            abort(400)
             
        # get the base64 encoded string
        im_b64 = request.json['image']

        # convert it into bytes  
        img_bytes = base64.b64decode(im_b64.encode('utf-8'))

        # convert bytes data to PIL Image object
        img = Image.open(io.BytesIO(img_bytes))

        # PIL image object to numpy array
        img_arr = np.asarray(img)      
        print('img shape', img_arr.shape)'''
        eye_cascade = cv2.CascadeClassifier('detectors/haarcascade_eye.xml')
        face_cascade = cv2.CascadeClassifier('detectors/haarcascade_frontalface_default.xml')
    
        if (request.method == 'POST'):
            output = {}
            file = request.files['file'] 
            if file:
                try:
                    # Reading the image sent by the user.
                    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    gray = cv2.bilateralFilter(gray,5,1,1)
                    # Detecting the faces in the image
                    faces = face_cascade.detectMultiScale(gray, 1.2, 10)
                    
                    faces = faces[faces[:, 0].argsort()]
                    # Looping over the faces and getting the ROI
                    for i,(x,y,w,h) in enumerate(faces):
                        roi = img[y:y+h, x:x+w]
                        eyes = eye_cascade.detectMultiScale(roi)
                        if(len(eyes)>0):
                            # Passing the ROI to our model
                            race_prediction, gender_prediction, age_prediction = model.predict(roi)
                        # Getting the ethinicity related to the index passed
                        ethinicity = PredictRace.getEthinicity(race_prediction)
                        gender = PredictRace.getGender(gender_prediction)
                        age = PredictRace.getAge(age_prediction)
                        # Prepare the output
                        output['Face {}'.format(i)] = {'ethinicity' : ethinicity, 'gender' : gender, 'age' : age }
                except:
                    return {"error": "We could not detect any faces. Please try another image"}

                return output

    # Static method for predicting the ethinicity based on index passed
    @staticmethod
    def getEthinicity(prediction):
        if(prediction == 0):
            pred_text = "White"
        elif(prediction == 1):
            pred_text = "Black"
        elif(prediction == 2):
            pred_text = "Latino_Hispanic"
        elif(prediction == 3):
            pred_text = "East Asian"
        elif(prediction == 4):
            pred_text = "Southeast Asian"
        elif(prediction == 5):
            pred_text = "Indian"
        elif(prediction == 6):
            pred_text = "Middle Eastern"
        return pred_text
    @staticmethod
    def getGender(prediction):
        if(prediction == 0):
            pred_text = "Male"
        elif(prediction == 1):
            pred_text = "Female"
        return pred_text
    @staticmethod
    def getAge(prediction):
        if(prediction == 0):
            pred_text = "0-2"
        elif(prediction == 1):
            pred_text = "3-9"
        elif(prediction == 2):
            pred_text = "10-19"
        elif(prediction == 3):
            pred_text = "20-29"
        elif(prediction == 4):
            pred_text = "30-39"
        elif(prediction == 5):
            pred_text = "40-49"
        elif(prediction == 6):
            pred_text = "50-59"
        elif(prediction == 7):
            pred_text = "60-69"
        elif(prediction == 8):
            pred_text = "70+"
        return pred_text
        
api.add_resource(PredictRace, '/predict')
if __name__ == '__main__':
    app.run(debug=True)
