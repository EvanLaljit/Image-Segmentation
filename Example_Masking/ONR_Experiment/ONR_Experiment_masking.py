from image_processing import process_img
from dataset import dataset
from mask import mask

#initialize dataset class with img path, process_img path, and mask path
data = dataset('path_to_imgs',processed_img_path='path_to_edited_imgs',mask_path='path_to_masked_imgs')
#get paths using dataset class functions
img = data.get_img_path()
mask_path = data.get_mask_path()
processed_img_path = data.get_processed_img_path()


#define parameters for masking. here, we use one point to mask one object
label = [[1]]
point= [[[400,300]]]

#initialize mask class
mask_onr_experiments = mask('default')

#mask
mask_onr_experiments.mask_point(processed_img_path,mask_path,point,label,invert=True)