import folium
import branca
"""
Create iframe Marker
"""

def popup_frame(each):
    picture_url = each['picture_url']
    listing_url = each['listing_url']

    html = """
		<h4> House Street View </h4><br>
		"""

    html = html + """
        <h4> Listing Information: </h4><br>
        """
    html = html + """<h4> House Info </h4><br>"""
    html = html + """<img src =""" + picture_url + """>""" + """<br>"""
    html = html + """Host Name: """ + each['host_name'] + """<br>"""

    return html
