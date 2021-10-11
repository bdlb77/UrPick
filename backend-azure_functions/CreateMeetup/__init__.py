import logging
import uuid

import azure.functions as func


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    title = req.params.get('title')
    zip_code = req.params.get('zipCode')
    print(zip_code)
    if not title:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            title = req_body.get('title')
            zip_code = req_body.get('zipCode')
    if title:
        new_meetup = {
            "id": str(uuid.uuid4()),
            "title": title,
            "zipCode": zip_code
        }
        doc.set(func.Document.from_dict(new_meetup))

        return func.HttpResponse(f"Successfully created Meetup: {title}")

    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
