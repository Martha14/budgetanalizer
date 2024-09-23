import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET
import os

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    annotations = []
    for member in root.findall('object'):
        bbox = member.find('bndbox')
        annotation = {
            'filename': root.find('filename').text,
            'class': member.find('name').text,
            'xmin': int(bbox.find('xmin').text),
            'ymin': int(bbox.find('ymin').text),
            'xmax': int(bbox.find('xmax').text),
            'ymax': int(bbox.find('ymax').text)
        }
        annotations.append(annotation)
    return annotations

# Przykład użycia
annotations = parse_xml('Photos/Labeled22.xml')
print(annotations)


import cv2

def draw_bounding_boxes(image, annotations):
    for ann in annotations:
        cv2.rectangle(image, (ann['xmin'], ann['ymin']), (ann['xmax'], ann['ymax']), (255, 0, 0), 2)
        cv2.putText(image, ann['class'], (ann['xmin'], ann['ymin'] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    return image

# Przykład użycia
image_path = 'Photos/IMG_20240725_195659.jpg'
image = cv2.imread(image_path)
annotated_image = draw_bounding_boxes(image, annotations)
cv2.imshow('Annotated Image', annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




# def xml_to_csv(path):
#     xml_list = []
#     for xml_file in glob.glob(path + '/*.xml'):
#         tree = ET.parse(xml_file)
#         root = tree.getroot()
#         for member in root.findall('object'):
#             value = (root.find('filename').text,
#                      int(root.find('size')[0].text),
#                      int(root.find('size')[1].text),
#                      member[0].text,
#                      int(member[4][0].text),
#                      int(member[4][1].text),
#                      int(member[4][2].text),
#                      int(member[4][3].text))
#             xml_list.append(value)
#     column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
#     xml_df = pd.DataFrame(xml_list, columns=column_name)
#     return xml_df

# def main():
#     for directory in ['train', 'test']:
#         image_path = os.path.join(os.getcwd(), 'Photos/{}'.format(directory))
#         xml_df = xml_to_csv(image_path)
#         xml_df.to_csv('data/{}_labels.csv'.format(directory), index=False)
#         print('Successfully converted xml to csv.')

# main()
