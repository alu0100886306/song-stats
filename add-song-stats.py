import argparse
import csv
import os
from tqdm import tqdm

HEADER = ['Track Name', 'Artist', 'Value', 'TopPos', 'TopMonth', 'Year','danceability',
	  'energy', 'key', 'loudness', 'mode', 'speechiness',
    	  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
    	  'duration_ms', 'time_signature']
songs_array = []

def song_stats_from_csv(input_filepath):
	region = os.path.splitext(os.path.basename(input_filepath))[0]

	output_filepath = 'song_stats_' + region + '.csv'

	with open(input_filepath, 'r') as csv_input:
	
		reader = csv.reader(csv_input)
		header = next(reader)	
		
		# Count the num of lines the csv file has (used for the progress bar)
		lines = [line for line in csv_input]

		for row in tqdm(csv.reader(lines), total=len(lines)):
			found = False
			if len(songs_array)>0:
				for song in songs_array:
					if song['TN'] == row[1] and song['A'] == row[2] and song['Y'] == row[5]:
						song['V'] += 101-int(row[0])
						if row[0] < song['TP']:
							song['TP'] = row[0]
							song['M'] = row[6]
						found = True
						break
			if not found:
				aux = {'TN':row[1], 'A':row[2], 'V':(101-int(row[0])),
					'TP':row[0], 'M':row[6], 'Y':row[5]}
				#adding the rest of attr
				for i in range(9,22):
					aux['a' + str(i-8)] = row[i]
				songs_array.append(aux)

	with open(output_filepath, 'w') as csv_output:

		writer = csv.writer(csv_output)
		writer.writerow(HEADER)
		for song in songs_array:
			writer.writerow(song.values())
		
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Get songs stats from waf.csv')
	parser.add_argument('input_file', help='input file in waf.csv format')
	args = parser.parse_args()

	song_stats_from_csv(args.input_file)
