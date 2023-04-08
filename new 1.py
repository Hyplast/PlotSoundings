from sounding import Sounding

# import datetime as dt
# # Limit the time
# now = dt.datetime.utcnow()
# # Depending on the current time and availability of the model data, adjusting
# # the hours below might be necessary to get any data
# start_time = now.strftime('%Y-%m-%dT00:00:00Z')
# end_time = now.strftime('%Y-%m-%dT18:00:00Z')


#Makkonen 220 km FAI
#start_time = "2022-05-24T10:00:00Z"
#end_time = "2022-05-24T15:00:00Z"


# #Makkonen 200 km FAI
# start_time = "2021-07-26T10:00:00Z"
# end_time = "2021-07-26T15:00:00Z"

# #Makkonen 162 km avoin kolmio
# start_time = "2022-06-07T10:00:00Z"
# end_time = "2022-06-07T15:00:00Z"


# #Makkonen 508 km 
# start_time = "2021-06-11T10:00:00Z"
# end_time = "2021-06-11T15:00:00Z"

# #Makkonen 389 km 
# start_time = "2020-06-11T10:00:00Z"
# end_time = "2020-06-11T15:00:00Z"

# #Makkonen 432 km 
# start_time = "2021-05-29T10:00:00Z"
# end_time = "2021-05-29T15:00:00Z"



# #Makkonen 160 km FAI 
# start_time = "2021-06-10T10:00:00Z"
# end_time = "2021-06-10T15:00:00Z"

# #Makkonen 180 km FAI 
# start_time = "2020-05-26T10:00:00Z"
# end_time = "2020-05-26T15:00:00Z"


# #Savukoski 150 km 
# start_time = "2016-06-06T10:00:00Z"
# end_time = "2016-06-06T15:00:00Z"

#3000 tonnin keliä 
#start_time = "2020-05-25T10:00:00Z"
#end_time = "2020-05-25T15:00:00Z"

#keliä vielä 8 jälkeen 
start_time = "2021-07-03T10:00:00Z"
end_time = "2021-07-03T15:00:00Z"


# #keliä vielä 8 jälkeen 
# start_time = "2021-05-30T10:00:00Z"
# end_time = "2021-05-30T15:00:00Z"


# #Huippu keli Pallaksella 
# start_time = "2014-04-18T10:00:00Z"
# end_time = "2014-04-18T15:00:00Z"

# #Sahlström 190 km 
# start_time = "2012-06-12T10:00:00Z"
# end_time = "2012-06-12T15:00:00Z"

# #Sahlström 141 FAI km 
# start_time = "2022-08-09T10:00:00Z"
# end_time = "2022-08-09T15:00:00Z"

# #Sahlström 111 FAI km 
# start_time = "2020-08-28T10:00:00Z"
# end_time = "2020-08-28T15:00:00Z"

# #Sahlström 143 FAI km 
# start_time = "2020-07-15T10:00:00Z"
# end_time = "2020-07-15T15:00:00Z"

# #Rämö 257 km 
# start_time = "2015-05-30T10:00:00Z"
# end_time = "2015-05-30T15:00:00Z"

# #Rämö 201 km 
# start_time = "2014-05-17T10:00:00Z"
# end_time = "2014-05-17T15:00:00Z"


# #Kumpulainen 296 km 
# start_time = "2022-04-27T10:00:00Z"
# end_time = "2022-04-27T15:00:00Z"

# #Kumpulainen 267 km 
# start_time = "2022-04-29T10:00:00Z"
# end_time = "2022-04-29T15:00:00Z"

# #Kumpulainen 160 km FAI 
# start_time = "2021-06-07T10:00:00Z"
# end_time = "2021-06-07T15:00:00Z"


# #Hamne 160 km FAI 
# start_time = "2020-05-22T10:00:00Z"
# end_time = "2020-05-22T15:00:00Z"

# #Keinanen 208 km 
# start_time = "2022-05-20T10:00:00Z"
# end_time = "2022-05-20T15:00:00Z"

# #Haastava Elokuinen keli  
# start_time = "2022-08-14T10:00:00Z"
# end_time = "2022-08-14T15:00:00Z"

# #Junnonaho 231 km 
# start_time = "2020-05-23T10:00:00Z"
# end_time = "2020-05-23T15:00:00Z"

snd = download_stored_query("fmi::observations::weather::sounding::multipointcoverage",
                                args=["starttime=" + start_time,
                                        "endtime=" + end_time,
                                        "place=Jokioinen"])
										
	for sounding in soundings:
    plot_sounding(sounding)
	
	sounding = snd.soundings[0]