#!usr/bin/env python

import os
import RPi.GPIO as GPIO

# Setup:  Specify audio file names and durations and Raspberry Pi pins to use

track_name_list = ['let_it_go.mp3', 'home.mp3', 'generations.mp3', 'coming_soon.mp3']
track_length_list = [227, 261, 202, 3]
pin_list = [23, 24, 17, 27, 22]

# File locations on RPi to save audio files and a log of tracks played

track_path = "/home/pi/Desktop/museum_mp3_player_project/mp3_files/"
log_path = "/home/pi/Desktop/museum_mp3_player_project/logs/visitor_log.txt"

GPIO.setmode(GPIO.BCM)

for pin in pin_list:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def log_play_event(track_name):		
	fp = fopen(log_path,'w')
	fp.write('%s,%s' (time.asctime(), track_name))
	fp.close()
	
	
# When the script is started, a loop listens for a button press and starts playing the corresponding track.
# The Pi stops listening for button presses for the duration of the song, so playback cannot be interrupted.
	
time_current_track = 0
time_started = 0

while True:
	for button_number in 0:length(track_name_list):
		if GPIO.input(pin_list[button_number])==False and time.time() - time_started > time_current_track:
			time_current_track = track_length_list[button_number]
			time_started = time.time()
			os.system('mpg123 -q %s%s' % (track_path, track_name_list[button_number])
			
			log_play_event(track_name_list[button_number])
    time.sleep(0.2)
