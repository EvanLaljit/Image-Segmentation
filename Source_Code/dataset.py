import os
class dataset():
  
  #define img_path, mask_path, and processed_img_path as strings. img_path used for the origianl set of imags,
  #processed_img_path will hold the edited images, and mask_path is where to put the masks
  #can automatically make the mask and processed img folders
  
  def __init__(self, img_path,mask_path='',processed_img_path = '',):
    self.image_path = img_path

    self.processed_img_path = processed_img_path

    self.mask_path = mask_path

  def get_img_path(self):

    return self.image_path

  def get_processed_img_path(self):
    #make folder if it doesnt exist
    if not os.path.exists(self.processed_img_path):
        os.makedirs(self.processed_img_path)

    return self.processed_img_path

  def get_mask_path(self):
    #make folder if it doesnt exist
    if not os.path.exists(self.mask_path):
      os.makedirs(self.mask_path)

    return self.mask_path