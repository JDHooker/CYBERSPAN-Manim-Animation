# CYBERSPAN Manim Video

Created by John - Summer 2025

This repository's code creates a simple video that gives an overivew of CYBERSPAN using
[Manim](https://www.manim.community/), a python animation library.

<div align="center">
  <img src="assets/manim.png" alt="Manim Logo" width="400" />
</div>

# Overview and Usage

The `/testing` folder contains the code that creates a small Manim video, for testing purposes.
The `/cyberspan` folder contains the code that creates a Manim video for the CYBERSPAN
animation. Running `manim -pqh main.py CYBERSPAN` in the cyberspan folder will produce the
video with a text-to-speech voiceover which is shown in [CYBERSPAN_TTS.mp4](assets/demos/CYBERSPAN_TTS.mp4).
Running `manim -pqh main_no_tts.py CYBERSPAN` in the cyberspan folder will produce the video
without the text to speech voiceover (which is much shorter) and shown in [CYBERSPAN.mp4](assets/demos/CYBERSPAN.mp4).
I also put music over one version of the TTS (Conqui -- although I think this is worse than the current TTS service)
and its output is shown in [CYBERSPAN_TTS_Music.mp4](assets/demos/CYBERSPAN_TTS_Music.mp4).

Note: Make sure to enable the virtual environment (`source venv/bin/activate` in the root directory -- `deactivate`
to deactivate it when done generating videos) and run `pip install -r requirements.txt` to install the
needed dependencies. Then your Manim commands to generate the videos should work.

# What the Animation Shows

The animation shows the creation of a number of fundamental networking devices and connects them.
It then connects them to a number of endpoint devices. The animation then shows packets flowing into
the network to endpoint devices before a red packet representing anomalous traffic flows through the network. 
It then does a short animation of a possible firewall being a part of the network before going into an animation
without the network describing the SPAN/Mirroring port of CYBERSPAN. CYBERSPAN is then inserted into the network with
the network fading back in and then the packet movements resume. This time, when the anomalous red envelope
representing anomalous traffic enters, the CYBERSPAN shield provides an alert. The animation then lists some
fundamental text relating to CYBERSPAN ("Zeek", "Clustering", "Storage", and "Agentless") and then some text
relating to the dashboard of CYBERSPAN ("Customizable", "Interpretable", "MITRE TTPs", "API"). Finally it
directs the watcher to [cyberspan.us](https://cyberspan.us) to learn more.

# How it Works and Next Steps

Manim does a lot of the interpolation for you to create the animation effects. All you really
need to do is define the objects (as svgs, images, or basic shapes) and call animation methods on them.
For example, you can create a text object and then call the `write()` animation on it to get a fancy
writing effect to show the text on screen. Explore the [Manim documentation](https://docs.manim.community/en/stable/reference_index/animations.html)
for more involved animations. You can also define waits that pause and runtimes for animations to control
how quickly they change.

There are a number of different [ai voiceover services](https://voiceover.manim.community/en/stable/services.html) that
you can use as well. I think the ai voiceovers that are free aren't great so if you wanted to use this video in production I 
would recommend recording a voiceover and layering it on top (you can do this through Manim, but it is probably simpler
to use a separate recording/editing service).
