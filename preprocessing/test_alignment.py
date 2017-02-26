import os
TRANSCRIPT_DIR = '/usr0/home/minghai1/MOSI/MOSI_data/Transcript/Final'
P2FA_TRANSCRIPT_DIR = '/usr0/home/minghai1/MOSI/MOSI_data/Transcript/CSV_P2FACorrected'

for root, dirs, files in os.walk(P2FA_TRANSCRIPT_DIR):
	for file in files:
		f = open(root+file)
		words = []
		for line in f.readlines():
			word = line.strip().split(',')[0]
			if word != 'sp':
				words.append(word)
		transcript = ' '.join(words)
		f.close()
		final_file = file.split('.')[0]+'.annotprocessed'
		f = open(TRANSCRIPT_DIR+final_file)
		flag = True
		for line in f.readlines():
			segmented_trans = line.strip().split('_')[2]
			if transcript.find(segmented_trans) == -1:
				flag = False
				print transcript
				print segmented_trans
				print '-----'
		if flag:
			print file.split('.')[0]+' is fine'
		f.close()
