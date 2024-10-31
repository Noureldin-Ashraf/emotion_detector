import requests 
import json 

def emotion_detector(text_to_analyze):  
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_obj= { "raw_document": { "text": text_to_analyze } } 
    response = requests.post(URL, json = json_obj, headers=header) 
    formatted_response = json.loads(response.text)

    if response.status_code == 200:

        emotion_data = formatted_response['emotionPredictions'][0]["emotion"]

        anger = emotion_data['anger']
        disgust = emotion_data['disgust']
        fear = emotion_data['fear']
        joy = emotion_data['joy']
        sadness = emotion_data['sadness']
        dominant_emotion = max(emotion_data, key=emotion_data.get)

    elif response.status_code == 400:

        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
        
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
        }