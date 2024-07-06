from django.http import JsonResponse
from controllers.facebook_controller import postToFacebook
from controllers.posts_controller import addPostToDB
import json

def createPost(request):
    try:
        if request.method != 'POST':
            return JsonResponse({'message': 'Invalid request method!'}, status=405)

        # Validate inputs
        if not request.body:
            return JsonResponse({'message': 'Empty body!'}, status=400)

        post_data = json.loads(request.body.decode('utf-8'))
        failed = postToFacebook(post_data)
        if(not failed):
            addPostToDB(post_data)
        else:
            return JsonResponse({'message': 'Failed to create post!'}, status=500)
        
        return JsonResponse({'message': 'Post created successfully!'})
        
    except Exception as e:
        self.output.info("Exception: " + str(e.__class__))
        return None
