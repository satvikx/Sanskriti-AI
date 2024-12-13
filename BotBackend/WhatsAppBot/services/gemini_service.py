import google.generativeai as genai
import logging
# from django.conf import settings 

# genai.configure(api_key=settings.GEMINI_KEY)
genai.configure(api_key='AIzaSyDSLjRXcxx-s9Alh82n41AVYMknGUi2OOg')
model = genai.GenerativeModel(model_name="gemini-1.5-flash", 
                              system_instruction='''You are a helpful Travel and Tourism Assistant named Sanskriti and you love India. You are always ready to help people with their travel queries and provide them with the best possible solutions.
                                                    Please keep in mind to respond in language of the user's query and provide them with the most relevant and concise information, refer the provided document and include the information about places only if asked, else keep it empty.
                                                    Use this JSON schema: {
                                                            "main_response": str,
                                                            "places": {
                                                                "1": {
                                                                "img_link": str,
                                                                "place": str,    
                                                                "time": str
                                                                }
                                                            }
                                                            }''',
                                                                                        )

def upload_file(path):
    file = genai.upload_file(path=path, display_name="travelfhq")
    file_name = genai.get_file(name=file.name)
    print(f"Retrieved file '{file_name.display_name}' as: {file.uri}")
    return file


def generate_response(text, wa_id, name):
    file = upload_file(r"C:\Users\Satvikk\Desktop\BotBackend\BotBackend\WhatsAppBot\services\Tourism_FHQ.pdf")
    response = model.generate_content([file, text])
    # response = model.generate_content(text)
    # logging.info(f"Generated {response} thread for {name} with wa_id {wa_id}")
    # print(response.text)
    return response.text

# print(generate_response("Please give information about all shows and museums"))


