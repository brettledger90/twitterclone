from django.shortcuts import render
from .models import Tweet
 

def timeline(request):
    userID = []
    for id in request.user.profile.related_to.all():
        userID.append(id)

    userID.append(request.user.id)
    tweets = Tweet.objects.filter(user_id__in= userID)
    print(tweets)
    return render(request, 'timeline.html', {'tweets':tweets})


# def CreateTweets(request):
#     if request.method == 'GET':
#         form = PostForm()
#     else:
#         # A POST request: Handle Form Upload
#         form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
#         # If data is valid, proceeds to create a new post and redirect the user
#         if form.is_valid():
#             content = form.cleaned_data['content']
            
#             post = m.Post.objects.create(content=content)
                                         
#             return HttpResponseRedirect(reverse('post_detail',
#                                                 kwargs={'post_id': post.id}))
 
#     return render(request, 'profile.html', {
#         'form': form,
#     })
