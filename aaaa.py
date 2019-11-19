"""
image = request.files['image']
        if image and image.filename:
            filename = image.filename
            image.save(os.path.join('static/images', filename)) 
""" 