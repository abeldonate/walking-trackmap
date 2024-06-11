import folium
import gpxpy
import os
import yaml

# Read the config
with open('config/config.yaml', 'r') as f:
    config_data = yaml.load(f, Loader=yaml.SafeLoader)

BASE_PATH = os.getcwd()
TRACKS_PATH = BASE_PATH + "/" + config_data.get("TRACKS_PATH")
FOCUS_COORDINATES = config_data.get("FOCUS_COORDINATES")
LINE_WEIGHT = config_data.get("LINE_WEIGHT")
ZOOM = config_data.get("ZOOM")

color_file = open(BASE_PATH + "/config/colors.hex")
COLORS = color_file.read().split("\n")
color_file.close()



def _name_to_title(name):
    return name.strip(".gpx").replace("_", " ")


def overlayGPX(tracks_path, zoom):
    result_map = folium.Map(location=FOCUS_COORDINATES, zoom_start=zoom)

    for i, gpx_path in enumerate(os.listdir(tracks_path)):
        print(gpx_path)  # Erase later
        gpx_file = open(tracks_path + "/" + gpx_path, 'r')
        gpx = gpxpy.parse(gpx_file)
        points = []
        for track in gpx.tracks:
            for segment in track.segments:
                for gpxpoint in segment.points:
                    points.append(tuple([gpxpoint.latitude, gpxpoint.longitude]))

        pline = folium.PolyLine(
            points, color=COLORS[i], weight=LINE_WEIGHT, opacity=1, tooltip=_name_to_title(gpx_path))

        result_map.add_child(pline)
        result_map.save(BASE_PATH + "/" + "resultingmap.html")


overlayGPX(TRACKS_PATH, ZOOM)
