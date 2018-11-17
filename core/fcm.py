from pyfcm import FCMNotification

push_service = FCMNotification(
    api_key="AAAABZoVnv0:APA91bHc842kZA4KPGQbFSTMhAFvOVdi-0BHb8-j4Grji6Yn2fj8AQDa2ZXpusjv8hlz8Nfv58KAGxrXYhViEagcjU2n6svx0sWrxVq0gwjR2bn4E9fBisZ5yU9hBHnqK85XESP4Nhph"
)
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging


def send_push(registration_id, title, text):
    return push_service.notify_single_device(registration_id=registration_id,
                                             message_title=title,
                                             message_body=text)


def send_multiple_push(registration_ids, title, text):
    return push_service.notify_multiple_devices(registration_ids=registration_ids,
                                                message_title=title,
                                                message_body=text)
