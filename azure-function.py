import logging
import azure.functions as func
import logging.handlers
import socket
import json

SYSLOG_HOST = "10.0.0.4"
SYSLOG_PORT = 514

# Set up SysLogHandler outside the main function
syslogger = logging.getLogger('MySysLogger')
syslogger.setLevel(logging.INFO)
handler = logging.handlers.SysLogHandler(address=(SYSLOG_HOST, SYSLOG_PORT), facility=logging.handlers.SysLogHandler.LOG_LOCAL3, socktype=socket.SOCK_STREAM)
handler.setFormatter(logging.Formatter('%(message)s\n'))
handler.append_nul = False
syslogger.addHandler(handler)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Log the HTTP request object
    #logging.info(f'HTTP Payload: {req.get_body().decode()}')

    try:
        request_json = req.get_json()
        #logging.info(f'Received JSON data: {json.dumps(request_json)}')  # Log the request_json
    except ValueError as e:
        syslogger.error(f"Failed to parse JSON from request: {e}")
        logging.error(f"Invalid JSON content: {req.get_body().decode()}")
        return func.HttpResponse("Bad Request - Invalid JSON", status_code=400)

    # Process and send to syslog
    if isinstance(request_json, list):
        for alert in request_json:
            send_to_syslog(alert)
    else:
        send_to_syslog(request_json)

    return func.HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200
    )

def send_to_syslog(data):
    try:
        syslogger.info(json.dumps(data))
    except Exception as e:
        syslogger.error(f"Failed to send data to syslog: {e}")
        logging.error(f"Error processing data: {json.dumps(data)}")
