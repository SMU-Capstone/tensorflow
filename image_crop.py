from PIL import Image, ImageDraw
import json


def image_crop(img_path, annot_path):
    try:
        img = Image.open(img_path)
        with open(annot_path, 'r', encoding='utf8') as f:
            bounding = json.load(f)['Bounding'][0]
            if bounding['Drawing'] == 'BOX':
                x1 = int(bounding['x1'])
                y1 = int(bounding['y1'])
                x2 = int(bounding['x2'])
                y2 = int(bounding['y2'])

                cropping_area = (x1, y1, x2, y2)
                cropped_img = img.crop(cropping_area)

            elif bounding['Drawing'] == 'POLYGON':
                polygon_count = int(bounding['PolygonCount'])
                polygon = []

                for index in range(polygon_count):
                    point = tuple(map(float, str(bounding['PolygonPoint'][index]["Point" + str(index+1)]).split(',')))
                    polygon.append(point)

                mask = Image.new('L', img.size, 0)
                draw = ImageDraw.Draw(mask)
                draw.polygon(polygon, fill=255, outline=None)
                black = Image.new('L', img.size, 0)
                cropped_img = Image.composite(img, black, mask)

            cropped_img.save(img_path)

    except Exception as e:
        print(e)
