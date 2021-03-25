from django.shortcuts import render
from severity_grading.predictions.dr_dme_grade import dr_dme_grade, dme_grade
from PIL import Image
from io import BytesIO
from pathlib import Path
import os
import numpy as np
import matplotlib.pyplot as plt


def dr_dme_grading(request):
    template_name = 'severity_grading/dr_dme_grade_analysis.html'
    context = {
        'status': 'not-uploaded'
    }
    if request.method == 'POST':
        if request.POST.get("upload_img"):
            image_files = request.FILES.getlist('browse_img')
            if not image_files:
                context = {
                    'status': 'no-image'
                }
                return render(request, template_name, context)
            images = []
            for img in image_files:
                image = Image.open(BytesIO(img.read()))
                images.append(image)
            for file in os.listdir("media/dr_dme_grading/"):
                os.remove("media/dr_dme_grading/" + file)
            images[0].save("media/dr_dme_grading/grade_dr.jpg", "JPEG", quality=100)

            context = {
                'status': "uploaded",
                'predict': "false"
            }
            return render(request, template_name, context)

        elif request.POST.get("predict_img"):
            my_file = Path("media/dr_dme_grading/grade_dr.jpg")
            if my_file.is_file():
                input_image = Image.open("media/dr_dme_grading/grade_dr.jpg")
            else:
                context = {
                    'status': "no-image"
                }
                return render(request, template_name, context)
            predictions = dr_dme_grade(input_image)
            predictions = 100*predictions
            grade = np.argmax(predictions[0])

            # Change here
            predictions1 = dme_grade(input_image)
            predictions1 = 100*predictions1
            grade1 = np.argmax(predictions1[0])

            context = {
                'status': "uploaded",
                'predict': "true",
                'predictions': predictions[0],
                'grade': grade,
                'predictions1': predictions1[0],
                'grade1': grade1
            }
            return render(request, template_name, context)

    return render(request, template_name, context)
