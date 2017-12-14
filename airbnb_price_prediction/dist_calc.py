import sys
import re
import pandas as pd
import geopy.distance

fname1 = sys.argv[1]
fname2 = sys.argv[2]

rest_zips = {}

rest_df = pd.read_csv(fname1)
rest_df = rest_df.dropna()

idx = -1
for index, rest in rest_df.iterrows():
	idx += 1

	rest_id, latt, longi, comb = rest
	
	zipcode = int(rest_id[-5:])

	if zipcode in rest_zips.keys():
		rest_zips[zipcode].append(idx)
	else:
		rest_zips[zipcode] = [idx]


airbnb_df = pd.read_csv(fname2)
airbnb_df = airbnb_df.dropna()

headers = list(airbnb_df)

wr_data = []
for header in headers:
	wr_data.append(header)

wr_data.append('Rest Count')

wr_data = ", ".join(wr_data)
wr_data += "\n"

idx = 0
for index1, air in airbnb_df.iterrows():

	wr_airbnb = []

	for ii in range(0, 41):
		wr_airbnb.append('%s' % air[ii])

	zipcode_airbnb = int(air[10])

	rest_cnt = 0

	if zipcode_airbnb in rest_zips.keys():

		rests = rest_zips[zipcode_airbnb]
		coords_1 = (air[14] , air[15])

		for rest in rests:
			coords_2 = (rest_df.iloc[rest, 1], rest_df.iloc[rest, 2])

			if geopy.distance.great_circle(coords_1, coords_2).km < 0.5:
				rest_cnt += 1

	wr_airbnb.append(str(rest_cnt))
	wr_airbnb = ','.join(wr_airbnb) + '\n'

	wr_data += wr_airbnb

	idx += 1
	print("Done: %d Progress: %f" % (idx, idx/36987.0) )

	if idx > 4:
		break

fw = open("rest_count1.csv", 'w')
fw.write(wr_data)
fw.close()
