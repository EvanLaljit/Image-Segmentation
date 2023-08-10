from image_processing import process_img
from dataset import dataset
from mask import mask

#initialize dataset class with img path, process_img path, and mask path
data = dataset('path_to_imgs',processed_img_path='path_to_edited_imgs',mask_path='path_to_masked_imgs')
#get paths using dataset class functions
img = data.get_img_path()
mask_path = data.get_mask_path()
processed_img_path = data.get_processed_img_path()

#intiialzie image processing class
p = process_img()

#use class function to crop image and send to folder
p.crop(img,(270, 400, 1150, 900),processed_img_path)

#define parameters for masking. here, we use points to mask two different objects (one point each)
label = [[1],[1]]
point= [[[640,150]],[[225,150]]]

#initialize mask class
mask_flag_foil = mask('default')

#mask
mask_flag_foil.mask_point(processed_img_path,mask_path,point,label,invert=True)