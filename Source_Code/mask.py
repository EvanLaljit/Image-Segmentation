import os
import cv2
import numpy as np
import tifffile # saving images to TIF
import torch
from PIL import Image, ImageEnhance


class mask():

  def __init__(self,model_type):

    from segment_anything import SamAutomaticMaskGenerator, sam_model_registry, SamPredictor
    self.model_type = model_type # 'default', "vit_l", "vit_b"

    match self.model_type:

  # define path of downloaded checkpoint(s) from github page
      case 'default':
          checkpoint = 'sam_vit_h_4b8939.pth'

      case 'vit_l':
          checkpoint = 'sam_vit_l_0b3195.pth'

      case 'vit_b':
          checkpoint = 'sam_vit_b_01ec64.pth'

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # if available use GPU for speed-up

    sam = sam_model_registry[model_type](checkpoint=checkpoint)
    sam.to(device)
    predictor = SamPredictor(sam)
    generator = SamAutomaticMaskGenerator(sam)
    self.generator = generator
    self.predictor = predictor

#for automatically creating masks without specifying points/boxes
def mask_generator(self,PATH_TO_IMG,PATH_TO_MASK):

  # create output folder if it does not exist
  if not os.path.exists(PATH_TO_MASK):
    os.makedirs(PATH_TO_MASK)

  for filename in os.listdir(PATH_TO_IMG):
   # read image
    img_path = os.path.join(PATH_TO_IMG, filename)
    img = np.array(Image.open(img_path).convert('RGB'))# use of PIL to ensure compatible with PyTorch

   # masking
    mask = self.generator.generate(img)

    #output image
    out = mask[0]['segmentation']
    out = np.logical_not(out)

  # out = cv2.bitwise_not(out.astype(np.uint8)).astype(bool) # use this in case masked and unmasked areas are flipped
    outname = 'mask_' + filename.replace('.jpg', '.tif')

    # save binary mask to output folder with same filename
    output_path = os.path.join(PATH_TO_MASK, outname)
    tifffile.imwrite(output_path, out)

#for masking using only points, paths defined as strings; points and labels defined as lists
  def mask_point(self,path_to_img,path_to_mask,input_point,input_label,invert=False):
    for filename in os.listdir(path_to_img):
    # read image
        img_path = os.path.join(path_to_img, filename)
        img = np.array(Image.open(img_path).convert('RGB')) # use of PIL to ensure compatible with PyTorch

    # masking
        self.predictor.set_image(img)
        out = 0

        #for loops are for masking multiple different objects
        for i,j in zip(input_point,input_label):

         #masking object with no box
          mask ,_, _ = self.predictor.predict(
                    point_coords=np.array(i),
                    point_labels=np.array(j),
                    multimask_output=False
    )

          #convert masks to type bool and combine all masks
          mask = np.array(mask,dtype=bool)
          out |= mask

        #convert out to type bool
        out = np.array(out,dtype=bool)

        #invert mask colors
        if invert == True:
          out = np.logical_not(out)

        #save binary mask to output folder with same filename
        outname = 'mask_' + filename.replace('.jpg', '.tif')
        output_path = os.path.join(path_to_mask, outname)
        tifffile.imwrite(output_path, out)

#for masking using only boxes; paths defined as strings; box defined with list in xyxy format
  def mask_box(self,path_to_img,path_to_mask,input_box,invert=False):
    for filename in os.listdir(path_to_img):
    # read image
        img_path = os.path.join(path_to_img, filename)
        img = np.array(Image.open(img_path).convert('RGB')) # use of PIL to ensure compatible with PyTorch

    # masking
        self.predictor.set_image(img)
        out = 0

        #for loops are for masking multiple different objects

        for i in zip(input_box):

         #masking object with no box
          mask ,_, _ = self.predictor.predict(
                    box = np.array(i),
                    multimask_output=False
    )
          #convert masks to type bool and combine all masks
          mask = np.array(mask,dtype=bool)
          out |= mask

        #convert out to type bool
        out = np.array(out,dtype=bool)

        #invert mask colors
        if invert == True:
          out = np.logical_not(out)

        #save binary mask to output folder with same filename
        outname = 'mask_' + filename.replace('.jpg', '.tif')
        output_path = os.path.join(path_to_mask, outname)
        tifffile.imwrite(output_path, out)

#for masking using combination of points and boxes; paths defined as strings; points, labels and boxes defined as stated above
  def mask_box_point(self,path_to_img,path_to_mask,input_point,input_label,input_box,invert=False):

    for filename in os.listdir(path_to_img):
    # read image
        img_path = os.path.join(path_to_img, filename)
        img = np.array(Image.open(img_path).convert('RGB')) # use of PIL to ensure compatible with PyTorch

    # masking
        self.predictor.set_image(img)
        out = 0

    #for loops are for masking multiple different object
        for l,m,n in zip(input_point,input_label,input_box):

            if l == [0]: #masking object with no point
                mask ,_, _ = self.predictor.predict(
                    box = np.array(n),
                    multimask_output=False,
    )
            elif n == [0]: #masking object with no box
                mask ,_, _ = self.predictor.predict(
                    point_coords=np.array(l),
                    point_labels=np.array(m),
                    multimask_output=False,
        )
            elif (l !=[0]) & (n !=[0]): #masking object with both point and box
                mask ,_, _ = self.predictor.predict(
                    point_coords=np.array(l),
                    point_labels=np.array(m),
                    box = np.array(n),
                    multimask_output=False
    )

            #convert masks to type bool and combine all masks
            mask = np.array(mask,dtype=bool)
            out |= mask

        #convert out to type bool
        out = np.array(out,dtype=bool)
        #invert mask colors
        if invert == True:
          out = np.logical_not(out)

        #save binary mask to output folder with same filename
        outname = 'mask_' + filename.replace('.jpg', '.tif')
        output_path = os.path.join(path_to_mask, outname)
        tifffile.imwrite(output_path, out)



