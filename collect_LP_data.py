import json
import pandas as pd
import skimage.io as io

temp = pd.read_json('Indian_Number_plates.json',lines=True)


for counter, i in enumerate(temp.iterrows()):
    if counter > (0.7 * len(temp)):
        image_store_location = 'val_images\\'
    else:
        image_store_location = 'train_images\\'
    image_url = i[1]['content']
    try:
        image = io.imread(image_url)
    except:
        print('uff')
        continue
    _ = io.imsave(image_store_location +'LP'+'_'+'{:06}.png'.format(counter), image)
    with open(image_store_location+'LP'+'_'+'{:06}.txt'.format(counter), 'w') as f:
        data = i[1]['annotation'][0]
        width_im = data['imageWidth']
        height_im = data['imageHeight']
        width = data['points'][1]['x'] - data['points'][0]['x']
        height = data['points'][1]['y'] - data['points'][0]['y']
        xcenter = data['points'][0]['x'] + (width / 2)
        ycenter = data['points'][0]['y'] + (height / 2)
        f.write('0'+' '+str(xcenter)+' '+str(ycenter)+' '+str(width)+' '+str(height)+'\n')

# print(temp.iloc[0]['annotation'][0])