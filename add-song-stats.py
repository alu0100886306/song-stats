# vim: tabstop=8 expandtab shiftwidth=8 softtabstop=8
import argparse
import csv
import os

HEADER = ['Track Name', 'Artist', 'Value', 'TopPos', 'TopMonth', 'Year','danceability',
	  'energy', 'key', 'loudness', 'mode', 'speechiness',
    	  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
    	  'duration_ms', 'time_signature', 'score', 'exito']
songs_array = []

def song_stats_from_csv(input_filepath):
        region = os.path.splitext(os.path.basename(input_filepath))[0]

        output_filepath = 'song_stats_' + region + '.csv'

        max_value = {'2017': 0, '2018': 0}

        with open(input_filepath, 'r') as csv_input:

                reader = csv.reader(csv_input)
                header = next(reader)	

                # Count the num of lines the csv file has (used for the progress bar)
                lines = [line for line in csv_input]

                for row in csv.reader(lines):
                        found = False
                        if len(songs_array)>0:
                                for song in songs_array:
                                        if song['TN'] == row[1] and song['A'] == row[2] and song['Y'] == row[5]:
                                                song['V'] += 101-int(row[0])
                                                if max_value[song['Y']] < song['V']:
                                                        max_value[song['Y']] = song['V']
                                                if row[0] < song['TP']:
                                                        song['TP'] = row[0]
                                                        song['M'] = row[6]
                                                found = True
                                                break
                        if not found:
                                aux = {'TN':row[1], 'A':row[2], 'V':(101-int(row[0])),'TP':row[0], 'M':row[6], 'Y':row[5]}
                                if max_value[aux['Y']] < aux['V']:
                                        max_value[aux['Y']] = aux['V']
                                #adding the rest of attr
                                for i in range(9,22):
                                        aux['a' + str(i-8)] = row[i]
                                songs_array.append(aux)
                for song in songs_array:
                        song['S'] = int(round(song['V']*100/max_value[song['Y']]/10 , 0))
                        if song['S'] > 1:
                                song['E'] = "Si"
                        else:
                                song['E'] = "No"

        with open(output_filepath, 'w') as csv_output:
                writer = csv.writer(csv_output)
                writer.writerow(HEADER)
                for song in songs_array:
                        writer.writerow(song.values())
		
if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Add audio features to .csv')
        parser.add_argument('input_file', help='input file in .csv format')
        args = parser.parse_args()

        song_stats_from_csv(args.input_file)
