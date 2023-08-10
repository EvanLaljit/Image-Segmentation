from PIL import Image, ImageEnhance
import os
class process_img():

#define input folder with original images, output folder to put edited images, and strength of effect (value > 0)
  def contrast(self,input_path,contrast_value,output_path):
    for file in os.listdir(input_path):
      img_path = os.path.join(input_path,file)
      img = Image.open(img_path)
      contraster = ImageEnhance.Contrast(img)
      img_contrast = contraster.enhance(contrast_value)

      out_path = os.path.join(output_path,file)
      img_contrast.save(out_path)

#define input folder with original images, output folder to put edited images, and strength of effect (value > 0)
  def brightness(self,input_path,brightness_value,output_path):
    for file in os.listdir(input_path):
      img_path = os.path.join(input_path,file)
      img = Image.open(img_path)
      brightnesser = ImageEnhance.Brightness(img)
      img_brightness = brightnesser.enhance(brightness_value)

      out_path = os.path.join(output_path,file)
      img_brightness.save(out_path)


#define input folder with original images, output folder to put edited images, and strength of effect (value > 0)
  def sharpness(self,input_path,sharpness_value,output_path):
      for file in os.listdir(input_path):
        img_path = os.path.join(input_path,file)
        img = Image.open(img_path)
        sharpnesser = ImageEnhance.Sharpness(img)
        img_sharpness = sharpnesser.enhance(sharpness_value)

        out_path = os.path.join(output_path,file)
        img_sharpness.save(out_path)

#define input folder with original images, output folder to put edited images, and rectangular region of interest to crop (roi),
#defined in xyxy format (left side, top side, right side and bottom side of the rectangle)
  def crop(self,input_path,roi,output_path):
      for file in os.listdir(input_path):
        img_path = os.path.join(input_path,file)
        img = Image.open(img_path)
        img_crop = img.crop(roi)

        out_path = os.path.join(output_path,file)
        img_crop.save(out_path)