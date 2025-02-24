
<h1 align="center">
  ✨ YouTube Transcript API ✨
</h1>

### -------Daniel's docs for server START------------

[![YouTube](![Untitled design-16](https://github.com/user-attachments/assets/82959b79-8825-4549-b8be-013dc68dd317)
)](https://www.youtube.com/watch?v=uEU61wVBx5Y)


# Run flask server to get transcript in JSON form


## 1. Run below commend in the terminal

```
python server.py
```


## 2. Paste http://127.0.0.1:8000 into your browser

<img width="837" alt="Screenshot 2025-02-12 at 2 11 25 PM" src="https://github.com/user-attachments/assets/a0784f73-4024-4d49-a143-32d7f9559982" />


## 3.Edit your http://127.0.0.1:8000 URL in browser into http://127.0.0.1:8000/transcript

### -------Daniel's docs for server END------------

<p align="center">
  <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=BAENLEW8VUJ6G&source=url">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate">
  </a>
  <a href="https://github.com/jdepoix/youtube-transcript-api/actions">
    <img src="https://github.com/jdepoix/youtube-transcript-api/actions/workflows/ci.yml/badge.svg?branch=master" alt="Build Status">
  </a>
  <a href="https://coveralls.io/github/jdepoix/youtube-transcript-api?branch=master">
    <img src="https://coveralls.io/repos/github/jdepoix/youtube-transcript-api/badge.svg?branch=master" alt="Coverage Status">
  </a>
  <a href="http://opensource.org/licenses/MIT">
    <img src="http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat" alt="MIT license">
  </a>
  <a href="https://pypi.org/project/youtube-transcript-api/">
    <img src="https://img.shields.io/pypi/v/youtube-transcript-api.svg" alt="Current Version">
  </a>
  <a href="https://pypi.org/project/youtube-transcript-api/">
    <img src="https://img.shields.io/pypi/pyversions/youtube-transcript-api.svg" alt="Supported Python Versions">
  </a>
</p>

<p align="center">
  <b>This is a python API which allows you to retrieve the transcript/subtitles for a given YouTube video. It also works for automatically generated subtitles, supports translating subtitles and it does not require a headless browser, like other selenium based solutions do!</b>
</p>
<p align="center">
 Maintenance of this project is made possible by all the <a href="https://github.com/jdepoix/youtube-transcript-api/graphs/contributors">contributors</a> and <a href="https://github.com/sponsors/jdepoix">sponsors</a>. If you'd like to sponsor this project and have your avatar or company logo appear below <a href="https://github.com/sponsors/jdepoix">click here</a>. 💖
</p>

<p align="center">
  <a href="https://www.searchapi.io">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://www.searchapi.io/press/v1/svg/searchapi_logo_white_h.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://www.searchapi.io/press/v1/svg/searchapi_logo_black_h.svg">
      <img alt="SearchAPI" src="https://www.searchapi.io/press/v1/svg/searchapi_logo_black_h.svg" height="40px" style="vertical-align: middle;">
    </picture>
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://supadata.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://supadata.ai/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://supadata.ai/logo-light.svg">
      <img alt="supadata" src="https://supadata.ai/logo-light.svg" height="40px">
    </picture>
  </a>
</p>

## Install

It is recommended to [install this module by using pip](https://pypi.org/project/youtube-transcript-api/):

```
pip install youtube-transcript-api
```

You can either integrate this module [into an existing application](#api) or just use it via a [CLI](#cli).

## API

The easiest way to get a transcript for a given video is to execute:

```python
from youtube_transcript_api import YouTubeTranscriptApi

YouTubeTranscriptApi.get_transcript(video_id)
```

> **Note:** By default, this will try to access the English transcript of the video. If your video has a different language, or you are interested in fetching a different language's transcript, please read the section below.

This will return a list of dictionaries looking somewhat like this:

```python
[
    {
        'text': 'Hey there',
        'start': 7.58,
        'duration': 6.13
    },
    {
        'text': 'how are you',
        'start': 14.08,
        'duration': 7.58
    },
    # ...
]
```
### Retrieve different languages

You can add the `languages` param if you want to make sure the transcripts are retrieved in your desired language (it defaults to english).

```python
YouTubeTranscriptApi.get_transcript(video_id, languages=['de', 'en'])
```

It's a list of language codes in a descending priority. In this example it will first try to fetch the german transcript (`'de'`) and then fetch the english transcript (`'en'`) if it fails to do so. If you want to find out which languages are available first, [have a look at `list_transcripts()`](#list-available-transcripts).

If you only want one language, you still need to format the `languages` argument as a list

```python
YouTubeTranscriptApi.get_transcript(video_id, languages=['de'])
```
### Batch fetching of transcripts

To get transcripts for a list of video ids you can call:

```python
YouTubeTranscriptApi.get_transcripts(["video_id1", "video_id2"], languages=['de', 'en'])
```

`languages` also is optional here.

### Preserve formatting

You can also add `preserve_formatting=True` if you'd like to keep HTML formatting elements such as `<i>` (italics) and `<b>` (bold).

```python
YouTubeTranscriptApi.get_transcripts(video_ids, languages=['de', 'en'], preserve_formatting=True)
```

### List available transcripts

If you want to list all transcripts which are available for a given video you can call:

```python
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
```

This will return a `TranscriptList` object  which is iterable and provides methods to filter the list of transcripts for specific languages and types, like:

```python
transcript = transcript_list.find_transcript(['de', 'en'])
```

By default this module always picks manually created transcripts over automatically created ones, if a transcript in the requested language is available both manually created and generated. The `TranscriptList` allows you to bypass this default behaviour by searching for specific transcript types:

```python
# filter for manually created transcripts
transcript = transcript_list.find_manually_created_transcript(['de', 'en'])

# or automatically generated ones
transcript = transcript_list.find_generated_transcript(['de', 'en'])
```

The methods `find_generated_transcript`, `find_manually_created_transcript`, `find_transcript` return `Transcript` objects. They contain metadata regarding the transcript:

```python
print(
    transcript.video_id,
    transcript.language,
    transcript.language_code,
    # whether it has been manually created or generated by YouTube
    transcript.is_generated,
    # whether this transcript can be translated or not
    transcript.is_translatable,
    # a list of languages the transcript can be translated to
    transcript.translation_languages,
)
```

and provide the method, which allows you to fetch the actual transcript data:

```python
transcript.fetch()
```

### Translate transcript

YouTube has a feature which allows you to automatically translate subtitles. This module also makes it possible to access this feature. To do so `Transcript` objects provide a `translate()` method, which returns a new translated `Transcript` object:

```python
transcript = transcript_list.find_transcript(['en'])
translated_transcript = transcript.translate('de')
print(translated_transcript.fetch())
```

### By example
```python
from youtube_transcript_api import YouTubeTranscriptApi

# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts('video_id')

# iterate over all available transcripts
for transcript in transcript_list:

    # the Transcript object provides metadata properties
    print(
        transcript.video_id,
        transcript.language,
        transcript.language_code,
        # whether it has been manually created or generated by YouTube
        transcript.is_generated,
        # whether this transcript can be translated or not
        transcript.is_translatable,
        # a list of languages the transcript can be translated to
        transcript.translation_languages,
    )

    # fetch the actual transcript data
    print(transcript.fetch())

    # translating the transcript will return another transcript object
    print(transcript.translate('en').fetch())

# you can also directly filter for the language you are looking for, using the transcript list
transcript = transcript_list.find_transcript(['de', 'en'])  

# or just filter for manually created transcripts  
transcript = transcript_list.find_manually_created_transcript(['de', 'en'])  

# or automatically generated ones  
transcript = transcript_list.find_generated_transcript(['de', 'en'])
```

### Using Formatters
Formatters are meant to be an additional layer of processing of the transcript you pass it. The goal is to convert the transcript from its Python data type into a consistent string of a given "format". Such as a basic text (`.txt`) or even formats that have a defined specification such as JSON (`.json`), WebVTT (`.vtt`), SRT (`.srt`), Comma-separated format (`.csv`), etc...

The `formatters` submodule provides a few basic formatters to wrap around you transcript data in cases where you might want to do something such as output a specific format then write that format to a file. Maybe to backup/store and run another script against at a later time.

We provided a few subclasses of formatters to use:

- JSONFormatter
- PrettyPrintFormatter
- TextFormatter
- WebVTTFormatter
- SRTFormatter

Here is how to import from the `formatters` module.

```python
# the base class to inherit from when creating your own formatter.
from youtube_transcript_api.formatters import Formatter

# some provided subclasses, each outputs a different string format.
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import WebVTTFormatter
from youtube_transcript_api.formatters import SRTFormatter
```

### Provided Formatter Example
Lets say we wanted to retrieve a transcript and write that transcript as a JSON file in the same format as the API returned it as. That would look something like this:

```python
# your_custom_script.py

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

# Must be a single transcript.
transcript = YouTubeTranscriptApi.get_transcript(video_id)

formatter = JSONFormatter()

# .format_transcript(transcript) turns the transcript into a JSON string.
json_formatted = formatter.format_transcript(transcript)


# Now we can write it out to a file.
with open('your_filename.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)

# Now should have a new JSON file that you can easily read back into Python.
```

**Passing extra keyword arguments**

Since JSONFormatter leverages `json.dumps()` you can also forward keyword arguments into `.format_transcript(transcript)` such as making your file output prettier by forwarding the `indent=2` keyword argument.

```python
json_formatted = JSONFormatter().format_transcript(transcript, indent=2)
```

### Custom Formatter Example
You can implement your own formatter class. Just inherit from the `Formatter` base class and ensure you implement the `format_transcript(self, transcript, **kwargs)` and `format_transcripts(self, transcripts, **kwargs)` methods which should ultimately return a string when called on your formatter instance.

```python

class MyCustomFormatter(Formatter):
    def format_transcript(self, transcript, **kwargs):
        # Do your custom work in here, but return a string.
        return 'your processed output data as a string.'

    def format_transcripts(self, transcripts, **kwargs):
        # Do your custom work in here to format a list of transcripts, but return a string.
        return 'your processed output data as a string.'
```

## CLI

Execute the CLI script using the video ids as parameters and the results will be printed out to the command line:  

```  
youtube_transcript_api <first_video_id> <second_video_id> ...  
```  

The CLI also gives you the option to provide a list of preferred languages:  

```  
youtube_transcript_api <first_video_id> <second_video_id> ... --languages de en  
```

You can also specify if you want to exclude automatically generated or manually created subtitles:

```  
youtube_transcript_api <first_video_id> <second_video_id> ... --languages de en --exclude-generated
youtube_transcript_api <first_video_id> <second_video_id> ... --languages de en --exclude-manually-created
```

If you would prefer to write it into a file or pipe it into another application, you can also output the results as json using the following line:  

```  
youtube_transcript_api <first_video_id> <second_video_id> ... --languages de en --format json > transcripts.json
```  

Translating transcripts using the CLI is also possible:

```  
youtube_transcript_api <first_video_id> <second_video_id> ... --languages en --translate de
```  

If you are not sure which languages are available for a given video you can call, to list all available transcripts:

```  
youtube_transcript_api --list-transcripts <first_video_id>
```

If a video's ID starts with a hyphen you'll have to mask the hyphen using `\` to prevent the CLI from mistaking it for a argument name. For example to get the transcript for the video with the ID `-abc123` run:

```
youtube_transcript_api "\-abc123"
```

## Proxy  

You can specify a https proxy, which will be used during the requests to YouTube:

```python  
from youtube_transcript_api import YouTubeTranscriptApi  

YouTubeTranscriptApi.get_transcript(video_id, proxies={"https": "https://user:pass@domain:port"})
```  

As the `proxies` dict is passed on to the `requests.get(...)` call, it follows the [format used by the requests library](https://requests.readthedocs.io/en/latest/user/advanced/#proxies).  

Using the CLI:  

```  
youtube_transcript_api <first_video_id> <second_video_id> --https-proxy https://user:pass@domain:port
```

## Cookies

Some videos are age restricted, so this module won't be able to access those videos without some sort of authentication. To do this, you will need to have access to the desired video in a browser. Then, you will need to download that pages cookies into a text file. You can use the Chrome extension [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en) and select "Netscape" during export, or the Firefox extension [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/).

Once you have that, you can use it with the module to access age-restricted videos' captions like so.

```python  
from youtube_transcript_api import YouTubeTranscriptApi  

YouTubeTranscriptApi.get_transcript(video_id, cookies='/path/to/your/cookies.txt')

YouTubeTranscriptApi.get_transcripts([video_id], cookies='/path/to/your/cookies.txt')
```

Using the CLI:

```
youtube_transcript_api <first_video_id> <second_video_id> --cookies /path/to/your/cookies.txt
```

## Warning  

This code uses an undocumented part of the YouTube API, which is called by the YouTube web-client. So there is no guarantee that it won't stop working tomorrow, if they change how things work. I will however do my best to make things working again as soon as possible if that happens. So if it stops working, let me know!  

## Contributing

To setup the project locally run (requires [poetry](https://python-poetry.org/docs/) to be installed):
```shell
poetry install --with test,dev
```

There's [poe](https://github.com/nat-n/poethepoet?tab=readme-ov-file#quick-start) tasks to run tests, coverage, the linter and formatter (you'll need to pass all of those for the build to pass):
```shell
poe test
poe coverage
poe format
poe lint
```

If you just want to make sure that your code passes all the necessary checks to get a green build, you can simply run:
```shell
poe precommit
```

## Donations

If this project makes you happy by reducing your development time, you can make me happy by treating me to a cup of coffee, or become a [Sponsor of this project](https://github.com/sponsors/jdepoix) :)  

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=BAENLEW8VUJ6G&source=url)
