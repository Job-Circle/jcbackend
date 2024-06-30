from django.http import JsonResponse
from controllers.facebook_controller import postToFacebook
from controllers.posts_controller import addPostToDB
import json

def createPost(request):
    if request.method == 'POST':
        post_data = json.loads(request.body.decode('utf-8'))
        failed = postToFacebook(post_data)
        if(not failed):
            addPostToDB(post_data)
        return JsonResponse({'message': 'Post created successfully!'})
    else:
        return JsonResponse({'message': 'Invalid request method!'}, status=405)

