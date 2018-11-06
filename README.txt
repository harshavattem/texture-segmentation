# TO BE DONE IN ORDER

# To download the images from the Brodatz database. Not necessary as textures are already provided.
python2 download.py


# To generate the 4x4 mosaic of textures
python2 collage.py


# To carry out the segmentation. The names of input, output files are mosaic.png, out.png (can be changed in argument)
python2 gabor.py -infile mosaic.png -outfile out.png -k 16 -gk 17 -M 35 -sigma 7 -spw 2


# Dataset on Google Drive (downloaded and preprocessed textures): https://drive.google.com/open?id=1IC7aQBgQPI_t7SB8wc2ehKY99Om2VrKI 
# ** The Textures folder must be in the same location as the codes. **

# Sample outputs are included in the Design Document.