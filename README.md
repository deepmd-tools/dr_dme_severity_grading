# Severity Grading of Diabetic Retinopathy and Diabetic Macular Edema
## Also Includes: Segmentation of Retinal Lesions associated with Diabetic Retinopathy using patch-based U-NET in Retinal Fundus Images

# See project demo: [DR DME Grading](https://youtu.be/ksnPtXhDN5M)

Diabetic Retinopathy (DR) is a complication of diabetes that can affect the eyes, affecting the blood vessels present in the retina (Light Sensitive Tissue) which lines the back of the eye. This is the most common cause of blindness and vision impairment among working-age adults and vision loss among people with diabetes. In this project, I carried out the following things:

Python3 • Django • NumPy • Pandas • Matplotlib • PIL • TensorFlow • Keras • Patch Based Segmentation • HTML5 • CSS3 • Bootstrap • JavaScript

• Trained Convolution Neural Networks (CNNs) architecture for 4 types of Retinal Lesions Segmentation (Microneurysms, Hemorrhages, Hard Exudates and Soft Exudates) associated with Diabetic Retinopathy.

• Trained CNNs for segmentation of Optic Disc in Retinal Fundus Images.

• Trained pre-trained Inception-V3 Network Architecture for severity grading of Diabetic Retinopathy (5-Class Classification: No DR, Mild Non-Proliferative DR (NPDR), Moderate DR, Severe NPDR, and Proliferative DR)

• Trained pre-trained Inception-V3 Network Architecture for severity grading of Diabetic Macular Edema (3-Class Classification: No-DME: Grade 0, Grade 1 and Grade 2)

• Implemented Custom Loss Function using Binary Cross-Entropy and Dice Loss and Combined them to calculate the final loss. The model was then Optimized using Adam Optimization Algorithm.

• Implemented Dice Coefficient and Mean Intersection over Union (IoU) to monitor the training process.

• Built a web application using Django Framework to deploy trained models.

