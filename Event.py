import re
import json
import base64
class Event:


    def convert_to_json(self, event_file):
        # takes event file as input
        # and converts to json
        file = open(event_file, 'r')
        data = file.read()
        file.close()

        data= data.replace('\\"', "'")

        list= re.findall(r'(\w+):\s*(?:"([^"]*)")',data)

        dictionary = {}

        for entry in list:
            dictionary[entry[0]] = entry[1]

        json_object = json.dumps(dictionary, indent=4)

        return dictionary



    def decode_message(this, message):

        #decodes the base64 string

        base64_bytes = message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        output_message = message_bytes.decode('ascii')
        return output_message

    def xor(this, a, b):
        #xors two given hex numbers
        result = int(a, 16) ^ int(b, 16) # convert to integers and xor them together
        return '{:x}'.format(result)     # convert back to hexadecimal

    def generate_event(this, json):
        #decodes the hint and computes the
        #xor of all the numbers in them
        #sequence and the number in the
        #hint to find out the missing
        #number
        this.decode_message(json["hint"])
        result = this.xor("0x17F", json["one"])
        result = this.xor(result, json["two"])
        result = this.xor(result, json["three"])
        result = this.xor(result, json["four"])
        json["five"] = result
        return json




event = Event()
json= event.convert_to_json("event_data.txt")  #converts the event to json
result = event.generate_event(json)

print(result)
