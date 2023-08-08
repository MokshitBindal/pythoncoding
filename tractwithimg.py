from exif import Image

api_map = "AIzaSyBFw0Qbyq9zTFTd-tUY6dZWTgaQzuU17R8"

img_path = 'IMG_1789.jpeg'
with open(img_path, 'rb') as src:
    img = Image(src)


def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == "S" or ref == "W":
        decimal_degrees = -decimal_degrees
    return decimal_degrees


def image_coordinates(image_path):
    with open(img_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            coords = (decimal_coords(img.gps_latitude, img.gps_latitude_ref),
                      decimal_coords(img.gps_longitude, img.gps_longitude_ref))
        except AttributeError:
            print('No Coordinates')
    else:
        print('The Image has no EXIF information')

    print(f"Image {src.name}")
    print(f"Device: {img.make} {img.model}, OS Version:{img.get('software', 'Not Known')}")
    print(f"Was taken: {img.datetime_original}")
    print(f"Coordinates: {coords}")
    print(f"Altitude: {img.gps_altitude}")
    print(f"http://maps.google.com?q={coords[0]},{coords[1]}")

    picture = f'<img style="height:500px; width:500px;" src="./{img_path}">'
    maps = f'<iframe style="height:500px;width:500px;border:0;" frameborder="0" src="https://www.google.com/maps/embed/v1/place?q={coords[0]},{coords[1]}&key={api_map}"></iframe>'
    file = open('gps.html', 'w')
    file.write(f'{picture} {maps}')
    file.close()


image_coordinates(img_path)
