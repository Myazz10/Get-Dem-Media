from datetime import datetime
from django.shortcuts import render
from .pytube_api import YouTubeFox
# from .youtube_dl_api import YouTubeTiger
from website.comments import get_comments
from api.models import Pytube, YoutubeDL


def home(request):
    pytube_api = Pytube.objects.all().first()
    youtube_dl_api = YoutubeDL.objects.all().first()

    today = datetime.now()
    context = {}
    result = False

    if request.method == 'POST':
        submission_form = request.POST.get('submission')

        if submission_form == 'url-form':
            search_url = request.POST.get('search')
            checked_radio = request.POST.get('file-type')
            force_download = request.POST.get('force-download')

            if checked_radio == 'mp3':
                if pytube_api and pytube_api.switch:
                    fox = YouTubeFox(search_url)

                    if not fox.validate_link():
                        context['invalid_url'] = 'This is not a valid YouTube url... Get a valid url please!'
                    else:
                        api_error, request_amount = fox.download(force_download, 'mp3')

                        if request_amount == 20:
                            context['timeout'] = f'{request_amount} amount of requests has been sent in the ' \
                                                 f'background and none was successful. The API is down at this time. '

                        else:
                            if not api_error:
                                result, audio = fox.get_audio()

                                if audio:
                                    context['audio'] = audio
                                    context['title'] = fox.video_details['title']
                                    context['thumbnail'] = fox.video_details['thumbnail']
                                    context['author'] = fox.video_details['author']
                                    context['publish_date'] = fox.video_details['publish_date']
                                    context['views'] = fox.video_details['views']
                                    context['length'] = fox.video_details['length']

                                    fox.clean_up()

                                else:
                                    context['special_characters_flag'] = 'This video url cannot be converted right now. Please ' \
                                                                             'try again in 24 hours. You may also try another url ' \
                                                                             'now. '
                            else:
                                context['api_error'] = 'There is an API error here! Please retry...'

                elif youtube_dl_api and youtube_dl_api.switch:
                    pass
                    """tiger = YouTubeTiger(search_url)

                    flag = tiger.validate_link()

                    if not flag:
                        context['invalid_url'] = 'This is not a valid YouTube url... Get a valid url please!'

                    else:
                        api_error = tiger.download(force_download, 'mp3')

                        if not api_error:
                            result, audio = tiger.get_audio()

                            if audio:
                                context['audio'] = audio
                                context['title'] = tiger.video_details['title']
                                context['thumbnail'] = tiger.video_details['thumbnail']
                                context['author'] = tiger.video_details['author']
                                context['publish_date'] = tiger.video_details['publish_date']
                                context['views'] = tiger.video_details['views']
                                context['length'] = tiger.video_details['length']

                                tiger.clean_up()

                            else:
                                context[
                                    'special_characters_flag'] = 'This video url cannot be converted right now. Please ' \
                                                                 'try again in 24 hours. You may also try another url ' \
                                                                 'now. '
                        else:
                            context['api_error'] = 'There is an API error here! Please retry...'"""

                else:
                    context['switch_off'] = "Sorry, this website's functionality is turned off."

            elif checked_radio == 'mp4':
                if pytube_api and pytube_api.switch:
                    fox = YouTubeFox(search_url)

                    if not fox.validate_link():
                        context['invalid_url'] = 'This is not a valid YouTube url... Get a valid url please!'
                    else:
                        api_error = fox.download(force_download)

                        if not api_error:
                            result, video = fox.get_video()

                            if video:
                                context['video'] = video
                                context['title'] = fox.video_details['title']
                                context['thumbnail'] = fox.video_details['thumbnail']
                                context['author'] = fox.video_details['author']
                                context['publish_date'] = fox.video_details['publish_date']
                                context['views'] = fox.video_details['views']
                                context['length'] = fox.video_details['length']

                                fox.clean_up()

                            else:
                                context['special_characters_flag'] = 'This video url cannot be converted right now. Please ' \
                                                                     'try again in 24 hours. You may also try another ' \
                                                                     'url now. '
                        else:
                            context['api_error'] = 'There is an API error here! Please retry...'

                elif youtube_dl_api and youtube_dl_api.switch:
                    print('MP4 -> YouTube-DL Work\n')

                else:
                    context['switch_off'] = "Sorry, this website's functionality is turned off."

            elif checked_radio == 'mp3-playlist':
                # get_mp3_playlist(search_url)
                pass

            elif checked_radio == 'mp4-playlist':
                # get_mp4_playlist(search_url)
                pass
            else:
                pass

        elif submission_form == 'comment-form':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            get_comments(name, email, message)
            success_comment = f"Hi {name.title()}, thanks for the contact! We'll get back to you soon."
            context['success_comment'] = success_comment

    context['result'] = result
    context['current_year'] = today.year

    return render(request, 'website/home.html', context)
