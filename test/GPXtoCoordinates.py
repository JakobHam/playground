import json
import gpxpy

def gpx_to_coordinates(gpx_file):
    with open(gpx_file, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
        coordinates = []

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    coordinates.append([point.longitude, point.latitude])

        return coordinates

def write_coordinates_to_file(coordinates, output_file):
    with open(output_file, 'w') as output_file:
        json.dump(coordinates, output_file)

if __name__ == "__main__":
    gpx_file_path = "/Users/jakobsmac/Public/test/Skive_Vadum_Strand.gpx"
    output_file_path = "/Users/jakobsmac/Public/test/coordinates_output.json"

    coordinates = gpx_to_coordinates(gpx_file_path)
    write_coordinates_to_file(coordinates, output_file_path)

    print(f"Coordinates written to {output_file_path}")