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
p.crop(img,(0,0,1600,965),processed_img_path)

#define parameters for masking. here, we use boxes and points to mask one object (one point and one box)
box = [[405,340,1175,550]]
label = [[1,1]]
point = [[[1020,415],[1020,445]]] 

#initialize mask class
mask_fish = mask('default')

#mask
mask_fish.mask_box_point(processed_img_path,mask_path,point,label,box)