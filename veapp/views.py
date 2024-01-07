from django.shortcuts import get_object_or_404, redirect, render
import requests
from veapp.forms import CommentForm, EditCommentForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from veapp.models import UserInteraction, Video
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    videos = Video.objects.all()
    return render(request, 'index.html', {'videos': videos})

def registration(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')


def showUsers(request):
    all_users = User.objects.all()
    context = {'all_users': all_users}
    return render(request, 'showUsers.html', context)

# def video_detail(request, video_id):
#     video = get_object_or_404(Video, pk=video_id)
#     comments = UserInteraction.objects.filter(video=video, comments__isnull=False)
#     all_videos = Video.objects.exclude(id=video.id)

#     form = CommentForm()

#     if request.method == 'POST':
#         # Check if the request has a comment_id parameter for editing
#         comment_id = request.POST.get('comment_id')
        
#         if comment_id:
#             # If comment_id is present, it means the user wants to edit the comment
#             comment = get_object_or_404(UserInteraction, pk=comment_id)
#             form = CommentForm(request.POST, instance=comment)
            
#             if form.is_valid():
#                 form.save()

#         else:
#             # If comment_id is not present, it means the user wants to add a new comment
#             form = CommentForm(request.POST)
            
#             if form.is_valid():
#                 comment_text = form.cleaned_data['comment']
#                 user_interaction = UserInteraction(user=request.user, video=video, comments=comment_text)
#                 user_interaction.save()

#     # Fetch the updated comments after editing or adding a new comment
#     comments = UserInteraction.objects.filter(video=video, comments__isnull=False)
#     form = CommentForm()

#     return render(request, 'video_detail.html', {'video': video, 'comments': comments, 'form': form, 'all_videos': all_videos})




def video_detail(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    comments = UserInteraction.objects.filter(video=video, comments__isnull=False).order_by('-created_at')
    form = CommentForm()
    edit_comment_form = EditCommentForm()
    all_videos = Video.objects.exclude(id=video.id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        edit_comment_form = EditCommentForm(request.POST)

        if form.is_valid():
            comment_text = form.cleaned_data['comment']
            user_interaction = UserInteraction(user=request.user, video=video, comments=comment_text)
            user_interaction.save()
            return redirect('veapp:video_detail', video_id=video_id)

        elif edit_comment_form.is_valid():
            comment_id = edit_comment_form.cleaned_data['comment_id']
            edited_comment_text = edit_comment_form.cleaned_data['edited_comment']
            comment_instance = UserInteraction.objects.get(id=comment_id)
            comment_instance.comments = edited_comment_text
            comment_instance.save()

            return redirect('veapp:video_detail', video_id=video_id)

    return render(request, 'video_detail.html', {
        'video': video, 
        'comments': comments, 
        'form': form, 
        'edit_comment_form': edit_comment_form,
        'all_videos': all_videos,
    })


def vpn_info_without_ip(request):
    context = {
        'user_ip': None,
    }
    return render(request, 'vpn_info.html', context)

def vpn_info_with_ip(request, user_ip):
    if request.method == 'POST':
        user_ip = request.POST.get('user_ip', '')

        api_url = f'https://ipinfo.io/{user_ip}?token=204d70adaa1382'
        response = requests.get(api_url)

        if response.status_code == 200:
            vpn_data = response.json()
            country_name = vpn_data.get('country', '')
            country_code = vpn_data.get('countryCode', '')
            ip_address = vpn_data.get('ip', '')
            city = vpn_data.get('city', '')
            region = vpn_data.get('region', '')
            organization = vpn_data.get('org', '')
            postal_code = vpn_data.get('postal', '')
            timezone = vpn_data.get('timezone', '')

            country_flags = {
                'US': 'https://www.countryflags.io/US/flat/64.png',
                'CA': 'https://www.countryflags.io/CA/flat/64.png',
                'FR': 'https://www.countryflags.io/FR/flat/64.png',
            }

            logo_url = country_flags.get(country_code, '')

            context = {
                'country_name': country_name,
                'country_code': country_code,
                'ip_address': ip_address,
                'city': city,
                'region': region,
                'organization': organization,
                'postal_code': postal_code,
                'timezone': timezone,
                'logo_url': logo_url,
                'user_ip': user_ip,
            }

            return render(request, 'vpn_info.html', context)
        else:
            return render(request, 'error.html', {'error_message': 'Unable to fetch VPN information'})

    context = {
        'user_ip': user_ip,
    }
    return render(request, 'vpn_info.html', context)

def delete_comment(request, comment_id):
    comment = get_object_or_404(UserInteraction, pk=comment_id)

    # Check if the logged-in user is the owner of the comment
    if request.user == comment.user:
        comment.delete()

    # Redirect to the video detail page after deletion
    return redirect('veapp:video_detail', video_id=comment.video.id)

