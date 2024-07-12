import json

from controllers.facebook_controller import postToFacebook
from controllers.posts_controller import addPostToDB
from django.http import JsonResponse
from services.post_parser import *


def createPost(request):
    try:
        if request.method != "POST":
            return JsonResponse({"message": "Invalid request method!"}, status=405)

        # Validate inputs
        if not request.body:
            return JsonResponse({"message": "Empty body!"}, status=400)

        post_data = json.loads(request.body.decode("utf-8"))
        failed = postToFacebook(post_data)
        if not failed:
            addPostToDB(post_data)
        else:
            return JsonResponse({"message": "Failed to create post!"}, status=500)
        return JsonResponse({"message": "Post created successfully!"})
    except Exception as e:
        print("Exception: " + str(e.__class__))
        return None


def post_from_whatsapp_bulk_text(request):
    if request.method == "POST":
        try:
            # Decode the request body
            bulk_data = json.loads(request.body.decode("utf-8"))
            # print(bulk_data)

            # Get the content field directly, no need to decode it again
            content = bulk_data.get("content")
            if not content:
                return JsonResponse(
                    {"message": "Content field is missing!"}, status=400
                )

            # Extract full info from content
            full_info = extract_post_full_info_from_whatsapp_bulk_text(content)
            for post in full_info:
                postToFacebook(
                    {
                        "title": "Sample Post",
                        "content": post["Free Text"],
                        "author": "John Doe",
                        "date": post["Date-Time"],
                    }
                )

            return JsonResponse({"message": "Post created successfully!"})
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON data!"}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)
    else:
        return JsonResponse({"message": "Invalid request method!"}, status=405)
