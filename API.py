import anki_vector # this code imports the anki vector function

import io # imports io for byte or string handling

from PIL import Image # this imports python imaging library

with anki_vector.Robot() as robot: # calls the anki vector robot object
        with anki_vector.Robot() as robot:
                for photo_info in robot.photos.photo_info: 
			print(f"opening photo {photo_info.photo_id}")
			photo = robot.photos.get_photo(photo_info.photo_id)
			image = Image.open(io.BytesIO(photo.image))
			image.show() # this for loop repeats the API connection to vector until there is photo data available once this is done it displays the data in a window with a ID for the photo

			

			
