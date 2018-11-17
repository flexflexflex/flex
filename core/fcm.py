from pyfcm import FCMNotification

push_service = FCMNotification(api_key="<api-key>")
# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging


def send_push(registration_id, title, text):
    return push_service.notify_single_device(registration_id=registration_id,
                                             message_title=title,
                                             message_body=text)


def send_multiple_push(registration_ids, title, text):
    return push_service.notify_multiple_devices(registration_ids=registration_ids,
                                                message_title=title,
                                                message_body=text)
