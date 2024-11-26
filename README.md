# Annotation Validation

This application provides several utilities for managing image annotation files. Below are the available functions:

## Functions

### find_empty_xml
This function identifies and returns a list of empty XML files. These files may have been generated when a bounding box was created but later deleted, leaving the XML file without any labels. These files are typically unnecessary and can be safely deleted.

### find_un_annotated_images
This function scans the dataset and returns a list of images that have not been annotated yet. It helps ensure that all images are accounted for and properly labeled.

### rename_class_names
This function allows you to rename existing class names in your annotation files. You can specify new class names, and the function will update the corresponding class labels in the dataset.

### delete_class_names
This function allows you to delete specific class names from your annotations. Use this function to remove any classes that are no longer required or relevant for your project.

### split_folder
This function splits a given folder containing images into two subfolders: one for training data and one for testing data. You can customize the splitting ratio to suit your needs.

### change_image_xml
This function modifies the XML annotations associated with images. It ensures that the annotations are updated and correctly reflect any changes made to the images or their metadata.

## Usage

To use these functions, follow the instructions provided in the documentation or script usage details.
