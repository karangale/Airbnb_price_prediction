import folium
import branca
"""
Create iframe Marker
"""

def airbnb_popup_frame(each):
    picture_url = each['picture_url']
    listing_url = each['listing_url']

    info = '<h4> Listing Information </h4>'
    info = info + '<b> House Info </b><br>'
    info = info + '<img src =' + picture_url +\
        'height = "300" width = "300">' + '<br><br>'
    info = info + '<b>Location: </b>' + each['street'] + '<br>'
    info = info + '<b>Property Type: </b>' + each['property_type'] + '<br>'
    info = info + '<b>Number of Bathrooms: </b>' +\
        str(int(each['bathrooms'])) + '<br>'
    info = info + '<b>Number of Bedrooms: </b>' +\
        str(int(each['bedrooms'])) + '<br>'
    info = info + '<b>Number of Beds: </b>' + str(int(each['beds'])) + '<br>'
    info = info + '<b>Listing URL: </b>' + '<a href="' +\
        listing_url + '" target="_blank">' + listing_url + '</a>' + '<br>'

    return info

def restaurant_popup_frame(each):

    info = '<h4>' + each['Name'].title() + '</h4>'
    info = info + '<b>Address: </b>' + each['Address'].title() + '<br>'

    return info
