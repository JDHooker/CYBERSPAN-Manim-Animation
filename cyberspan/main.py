import os
from dotenv import load_dotenv


from manim import *
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.openai import OpenAIService
from manim_voiceover.services.gtts import GTTSService
# from manim_voiceover.services.elevenlabs import ElevenLabsService
# from manim_voiceover.services.coqui import CoquiService

"""
Location for svgs, make sure to credit at end:

https://www.svgrepo.com/collection/clarity-line-icons/
https://www.svgrepo.com/collection/clarity-project-icons/
https://www.svgrepo.com/collection/technology-icon-set-2/
https://www.svgrepo.com/collection/communication-and-network/
https://www.svgrepo.com/collection/electronics-4/
https://www.svgrepo.com/collection/technological-devices/2
https://www.svgrepo.com/svg/357689/envelope-exclamation
"""

class CYBERSPAN(VoiceoverScene):

    def write_cyberspan(self):
        possible_fonts = ["Avenir", "DIN Condensed", "Monaco", "Verdana"]

        # Define Text Objects
        c_text = Text("CYBERSPAN", font="Monaco", font_size=80).shift(UP)
        by_text = Text("by IntelliGenesis", font="Monaco").shift(DOWN)

        # Write them in and then Unwrite
        with self.voiceover(text="Welcome to this simple Cyberspan explainer by IntelliGenesis. We will walk through a high level overview of Cyberspan in this video.") as tracker:
            self.play(Write(c_text))
            self.wait(0.5)
            self.play(Write(by_text))

            self.wait(2)
            self.play(Unwrite(c_text), Unwrite(by_text))


    def network_visualization(self):

        with self.voiceover(text="Your network has some connection to the internet, which is provided by your internet service provider.") as tracker:
            # Make the internet and move it.
            internet_text = Text("Internet", font="Monaco").shift(UP * 2)
            internet_svg = SVGMobject("assets/internet.svg").scale(0.5)

            self.play(FadeIn(internet_svg), Write(internet_text))
            self.wait(1.5)
            self.play(Unwrite(internet_text))
            self.play(internet_svg.animate.shift(LEFT * 6), run_time=2)
            self.wait()

        with self.voiceover(text="The modem is the translator between the internet and your network and converts between analog and digital signals.") as tracker:
            # Make the modem and move it and connect to internet, then move internet off screen.
            modem_text = Text("Modem", font="Monaco").shift(UP * 2)
            modem_svg = SVGMobject("assets/TechnologyIconSet2/modem-svgrepo-com.svg").scale(0.5)
            internet_modem_link = Line(color=WHITE).scale(0.75).shift(LEFT * 4.5)

            self.play(Write(modem_text), FadeIn(modem_svg))
            self.wait()
            self.play(Unwrite(modem_text))
            self.play(modem_svg.animate.shift(LEFT * 3), run_time=2)
            self.play(Create(internet_modem_link))
            self.wait()
            self.play(internet_svg.animate.shift(LEFT * 3), internet_modem_link.animate.shift(LEFT * 3), modem_svg.animate.shift(LEFT * 3), run_time=1.5)
            self.wait()

        with self.voiceover(text="The router is connected between the modem and the rest of the network to control the flow of packets between the networks.") as tracker:
            # Make the router and move it and connect it to the modem.
            router_text = Text("Router", font="Monaco").shift(UP * 2)
            router_svg = SVGMobject("assets/TechnologyIconSet2/router-svgrepo-com.svg").scale(0.5)
            modem_router_link = Line(color=WHITE).scale(0.75).shift(LEFT * 4.5)

            self.play(Write(router_text), FadeIn(router_svg))
            self.wait()
            self.play(Unwrite(router_text))
            self.play(router_svg.animate.shift(LEFT * 3), run_time=2)
            self.play(Create(modem_router_link))
            self.wait()

        with self.voiceover(text="It is likely your network also has a switch to control where packets go within your network to make sure they get to the correct device.") as tracker:
            # Make the switch and move it and connect it to the router.
            switch_text = Text("Switch", font="Monaco").shift(UP * 2)
            switch_svg = SVGMobject("assets/Clarity/network-switch-svgrepo-com.svg").scale(0.5).shift(DOWN * 0.15)
            router_switch_link = Line(color=WHITE).scale(0.75).shift(LEFT * 1.5)

            self.play(Write(switch_text), FadeIn(switch_svg))
            self.wait()
            self.play(Unwrite(switch_text))
            self.play(Create(router_switch_link))
            self.wait()

        with self.voiceover(text="We can also add more complex devices within the network like a laptop, a desktop, a server, or a WiFi access point.") as tracker:
            # Make new devices and connect them to the switch and write and unwrite them.
            computer_svg = SVGMobject("assets/Clarity/computer-svgrepo-com.svg").scale(0.5).shift(RIGHT * 3, UP * 3)
            host_svg = SVGMobject("assets/Clarity/host-svgrepo-com.svg").scale(0.5).shift(RIGHT * 3, UP * 1)
            server_svg = SVGMobject("/Users/intern4/manim/cyberspan/assets/Clarity/rack-server-svgrepo-com.svg").scale(0.5).shift(RIGHT * 3, DOWN)
            wifi_svg = SVGMobject("assets/CommunicationAndNetwork/wifi-svgrepo-com.svg").scale(0.3).shift(RIGHT * 3, DOWN * 3)

            new_devices_vg = VGroup(computer_svg, host_svg, server_svg, wifi_svg)

            computer_text = Text("Laptop", font="Monaco", font_size=32).shift(RIGHT * 5, UP * 3)
            host_text = Text("Desktop", font="Monaco", font_size=32).shift(RIGHT * 5, UP * 1)
            server_text = Text("Server", font="Monaco", font_size=32).shift(RIGHT * 5, DOWN * 1)
            wifi_text = Text("WiFi", font="Monaco", font_size=32).shift(RIGHT * 5, DOWN * 3)

            new_text_vg = VGroup(computer_text, host_text, server_text, wifi_text)

            computer_line = Line(switch_svg.get_right() + (UP * 0.15) + (RIGHT * 0.15), computer_svg.get_left() + (LEFT * 0.15))
            host_line = Line(switch_svg.get_right() + (UP * 0.15) + (RIGHT * 0.15), host_svg.get_left() + (LEFT * 0.15))
            server_line = Line(switch_svg.get_right() + (UP * 0.15) + (RIGHT * 0.15), server_svg.get_left() + (LEFT * 0.15))
            wifi_line = Line(switch_svg.get_right() + (UP * 0.15) + (RIGHT * 0.15), wifi_svg.get_left() + (LEFT * 0.15))
            
            line_vg = VGroup(computer_line, host_line, server_line, wifi_line)

            self.play(FadeIn(new_devices_vg))
            self.wait()

            # Create an AnimationGroup where each pair animates together
            animations = AnimationGroup(
                *[
                    AnimationGroup(Create(line, reverse=True), Write(text), lag_ratio=0.25)
                    for line, text in zip(line_vg, new_text_vg)
                ],
                lag_ratio=1  # Wait for previous pair to finish before starting next
            )

            self.play(animations)
            self.wait(2)
            self.play(Unwrite(new_text_vg))
            self.wait(2)

        with self.voiceover(text="Lets make our network a little more coplex by adding a phone and laptop to the WiFi.") as tracker:
            # Do wifi devices and connections.
            phone_svg = SVGMobject("assets/CommunicationAndNetwork/smartphone-mobile-phone-svgrepo-com.svg").scale(0.5).shift(RIGHT * 6, DOWN * 3)
            laptop_svg = SVGMobject("assets/Clarity/computer-svgrepo-com.svg").scale(0.5).shift(RIGHT * 6, DOWN * 1)

            wifi_devices_vg = VGroup(phone_svg, laptop_svg)

            wifi_laptop_line = Line(wifi_svg.get_right() + (RIGHT * 0.15), laptop_svg.get_left() + (LEFT * 0.15))
            wifi_phone_line = Line(wifi_svg.get_right() + (RIGHT * 0.15), phone_svg.get_left() + (LEFT * 0.15))

            wifi_device_line_vg = VGroup(wifi_laptop_line, wifi_phone_line)

            self.play(FadeIn(wifi_devices_vg))
            self.play(Create(wifi_device_line_vg))
            self.wait(2)

        with self.voiceover(text="During the normal course of communication, devices on your network will send and receive packets through the modem, router, and switch. But what do you do when there is anomalous traffic?") as tracker:
            # Start packet demonstration.
            envelope1 = SVGMobject("assets/Unicon/envelope-svgrepo-com.svg").scale(0.3).shift(LEFT * 8)
            envelope2 = SVGMobject("assets/Unicon/envelope-svgrepo-com.svg").scale(0.3).shift(LEFT * 8)
            envelope3 = SVGMobject("assets/Unicon/envelope-red.svg").scale(0.3).shift(LEFT * 8)

            self.play(Create(envelope1))
            self.play(Create(envelope2))
            self.play(Create(envelope3))

            self.play(envelope1.animate.move_to(switch_svg.get_right() + (RIGHT * 0.3)))
            self.play(envelope1.animate.move_to(computer_svg.get_center() + (LEFT * 0.3)))
            self.play(envelope1.animate.shift(RIGHT * 1.5))

            self.play(FadeOut(envelope1), envelope2.animate.move_to(switch_svg.get_right() + (RIGHT * 0.3)))
            self.play(envelope2.animate.move_to(wifi_svg.get_center() + (LEFT * 0.3)))
            self.play(envelope2.animate.shift(RIGHT * 0.5))
            self.play(envelope2.animate.move_to(laptop_svg.get_center() + (LEFT * 0.3)))
            self.play(envelope2.animate.shift(UP * 1))

            self.play(FadeOut(envelope2), envelope3.animate.move_to(switch_svg.get_right() + (RIGHT * 0.3)))
            self.play(envelope3.animate.move_to(host_svg.get_center() + (LEFT * 0.3)))
            self.play(envelope3.animate.shift(RIGHT * 1.5))
            self.wait()
            self.play(FadeOut(envelope3))
            self.wait()

        with self.voiceover(text="Some networks have basic firewalls, much of the time connected to the router, but these generally are not dynamic and will not be able to identify new and emerging threats.") as tracker:
            # Emphasize Firewall
            firewall_svg = SVGMobject("assets/firewall.svg").scale(0.5).shift(LEFT * 3 + DOWN * 2)
            router_firewall_line = Line(router_svg.get_bottom() + (DOWN * 0.15), firewall_svg.get_top() + (UP * 0.15))
            
            self.play(Create(firewall_svg))
            self.play(Create(router_firewall_line))
            self.wait(2)

            self.play(FadeOut(firewall_svg), FadeOut(router_firewall_line))
            self.wait(3)
        
        # Fade Out Everything
        all_objects_vg = VGroup(internet_modem_link, modem_svg, modem_router_link, router_svg, router_switch_link, switch_svg, computer_line, computer_svg, host_line, host_svg, server_line, server_svg, wifi_line, wifi_svg, wifi_laptop_line, laptop_svg, wifi_phone_line, phone_svg)
        
        self.play(FadeOut(all_objects_vg))
        self.wait()

        with self.voiceover(text="Cyberspan works by connecting to the SPAN or mirroring port on the switch, which gets a copy of all traffic passsed through the switch.") as tracker:
            # Explain CYBERSPAN with SPAN Port
            shield_svg = SVGMobject("assets/shield.svg").scale(1.5)
            cyberspan_server_svg = SVGMobject("assets/Clarity/rack-server-svgrepo-com.svg").shift(LEFT * 2 + DOWN)
            switch_2_svg = SVGMobject("assets/Clarity/network-switch-svgrepo-com.svg").shift(RIGHT * 2 + DOWN)
            span_text = Text("SPAN/Mirroring Port", font="Monaco").shift(UP * 2)

            self.play(Create(shield_svg))
            self.wait()
            self.play(Transform(shield_svg, cyberspan_server_svg), FadeIn(switch_2_svg))
            self.play(Write(span_text))


        self.play(FadeOut(shield_svg), FadeOut(switch_2_svg), FadeOut(span_text))

        # Insert CYBERSPAN shield into network
        new_shield_svg = SVGMobject("assets/shield.svg").scale(1.5)
        self.play(Create(new_shield_svg))
        self.wait()
        self.play(FadeIn(all_objects_vg), new_shield_svg.animate.move_to(switch_svg.get_top() + (UP * 2)).scale(0.3))
        switch_shield_line = Line(switch_svg.get_top() + (UP * 0.15), new_shield_svg.get_bottom() + (DOWN * 0.15))
        self.play(Create(switch_shield_line))
        self.wait()

        with self.voiceover(text="Now as packets pass through the network and specifically the switch, Cyberspan is able to get a copy of all traffic and use artificial intelligence and machine learning models to identify anomalous traffic.") as tracker:
            # Show packets moving and CYBERSPAN getting copies
            envelope4 = SVGMobject("assets/Unicon/envelope-svgrepo-com.svg").scale(0.3).shift(LEFT * 8)
            envelope5 = SVGMobject("assets/Unicon/envelope-svgrepo-com.svg").scale(0.3).shift(LEFT * 8)
            envelope6 = SVGMobject("assets/Unicon/envelope-red.svg").scale(0.3).shift(LEFT * 8)

            self.play(Create(envelope4))
            self.play(Create(envelope5))
            self.play(Create(envelope6))

            self.play(envelope4.animate.move_to(switch_svg.get_right() + (RIGHT * 0.3)))
            envelope7 = envelope4.copy()

            self.play(envelope4.animate.move_to(computer_svg.get_center() + (LEFT * 0.3)), envelope7.animate.move_to(new_shield_svg.get_top() + (UP * 0.5)))
            self.play(envelope4.animate.shift(RIGHT * 1.5), FadeOut(envelope7))
        
            self.play(FadeOut(envelope4), envelope5.animate.move_to(switch_svg.get_right() + (RIGHT * 0.3)))

            envelope8 = envelope5.copy()

            self.play(envelope5.animate.move_to(wifi_svg.get_center() + (LEFT * 0.3)), envelope8.animate.move_to(new_shield_svg.get_top() + (UP * 0.5)))
            self.play(envelope5.animate.shift(RIGHT * 0.5), FadeOut(envelope8))
            self.play(envelope5.animate.move_to(laptop_svg.get_center() + (LEFT * 0.3)))
            self.play(envelope5.animate.shift(UP * 1))

            self.play(FadeOut(envelope5), envelope6.animate.move_to(switch_svg.get_right() + (RIGHT * 0.3)))

            envelope9 = envelope6.copy()
            warning_svg = SVGMobject("assets/Clarity/warning.svg").scale(0.3).move_to(new_shield_svg.get_center())

            self.play(envelope6.animate.move_to(host_svg.get_center() + (LEFT * 0.3)), envelope9.animate.move_to(new_shield_svg.get_center()))
            self.play(envelope6.animate.shift(RIGHT * 1.5), FadeOut(envelope9))
            self.play(FadeOut(envelope6), FadeIn(warning_svg))
            self.play(FadeOut(warning_svg))
            self.play(FadeIn(warning_svg))
            self.play(FadeOut(warning_svg))
            self.play(FadeIn(warning_svg))
            self.play(FadeOut(warning_svg))
            self.wait()


        with self.voiceover(text="Cyberspan uses Zeek to interpret raw network data and convert it into formats usable for analysis. It then runs clustering and other models to identify anomalous traffic on the network. It also stores recent Zeek and packet capture data to be able to trace back anomalous events. Cyberspan is also agentless, meaning instead of needing to manage software on all devices, to run Cyberspan you only need to be concerned about the server it runs on.") as tracker:
            # Describe CYBERSPAN Tools/Architecture
            left_server_svg = SVGMobject("assets/Clarity/rack-server-svgrepo-com.svg").shift(LEFT * 3)
            self.play(Transform(new_shield_svg, left_server_svg), FadeOut(all_objects_vg), FadeOut(switch_shield_line))

            description_text_1 = Text("Zeek", font="Monaco").shift(RIGHT * 3 + UP * 3)
            description_text_2 = Text("Clustering", font="Monaco").shift(RIGHT * 3 + UP * 1)
            description_text_3 = Text("Storage", font="Monaco").shift(RIGHT * 3 + DOWN * 1)
            description_text_4 = Text("Agentless", font="Monaco").shift(RIGHT * 3 + DOWN * 3)

            text_animation = AnimationGroup(
                Write(description_text_1), 
                Write(description_text_2), 
                Write(description_text_3), 
                Write(description_text_4), 
            lag_ratio=3)

            self.play(text_animation)
            self.wait()
        self.play(Unwrite(description_text_1), Unwrite(description_text_2), Unwrite(description_text_3), Unwrite(description_text_4))
        self.wait()


        with self.voiceover(text="Cyberspan also provides a dashboard and tools that are customizable and interpretable. It is also integrated with recommendations for what to do for different kinds of anomalous events. It also provides an application programming interface for custom integrations and data uses.") as tracker:
            dashboard_png = ImageMobject("assets/CYBERSPAN_Dashboard.png").shift(LEFT * 3).scale(0.2)
            cyberspan_png = ImageMobject("assets/CyberspanLogo.png").shift(LEFT * 3).scale(1.75)

            self.play(FadeOut(left_server_svg), FadeOut(new_shield_svg), FadeIn(dashboard_png))

            description_text_5 = Text("Customizable", font="Monaco").shift(RIGHT * 3 + UP * 3)
            description_text_6 = Text("Interpretable", font="Monaco").shift(RIGHT * 3 + UP * 1)
            description_text_7 = Text("MITRE TTPs", font="Monaco").shift(RIGHT * 3 + DOWN * 1)
            description_text_8 = Text("API", font="Monaco").shift(RIGHT * 3 + DOWN * 3)

            text_animation = AnimationGroup(
                Write(description_text_5), 
                Write(description_text_6),
                Write(description_text_7), 
                Write(description_text_8), 
            lag_ratio=3)

            self.play(text_animation)
            self.wait()
        self.play(Unwrite(description_text_5), Unwrite(description_text_6), Unwrite(description_text_7), Unwrite(description_text_8),
                    FadeOut(dashboard_png), FadeIn(cyberspan_png))
        self.wait()

        with self.voiceover(text="Follow this link to learn more.") as tracker:
            # Learn More
            final_text = Text("To Learn More Visit\n   cyberspan.us", font="Monaco", line_spacing=2, t2c={"cyberspan.us": BLUE_C}).shift(RIGHT * 3)
            self.play(Write(final_text))
            self.wait()

            word = final_text[16:]
            self.play(Circumscribe(word))
            self.wait()
            self.play(Unwrite(final_text), FadeOut(cyberspan_png))
            self.wait()


    def credit_scene(self):
        # Credits
        credits_text = Text("Credits:", font="Monaco").shift(DOWN * 5)
        credit1_text = Text("Manim for Animation", font="Monaco").shift(DOWN * 6)
        credit2_text = Text("SVGRepo for SVGs", font="Monaco").shift(DOWN * 7)
        credit3_text = Text("Coqui TTS", font="Monaco").shift(DOWN * 8)
        credit4_text = Text("freesound.org: wheatfield", font="Monaco").shift(DOWN * 9)

        # Add the objects to the scene
        self.add(credits_text, credit1_text, credit2_text, credit3_text, credit4_text)

        with self.voiceover(text="Thank you for watching.") as tracker:
            self.play(
                credits_text.animate.shift(UP * 14),
                credit1_text.animate.shift(UP * 14),
                credit2_text.animate.shift(UP * 14),
                credit3_text.animate.shift(UP * 14),
                credit4_text.animate.shift(UP * 14),
                run_time=15
            )


    def construct(self):
        load_dotenv()
        # self.set_speech_service(CoquiService())
        self.set_speech_service(GTTSService())

        self.write_cyberspan()
        self.network_visualization()
        self.credit_scene()


