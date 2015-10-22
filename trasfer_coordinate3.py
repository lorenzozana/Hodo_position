import os, sys, math
import ROOT as r
from ROOT import TTree, TFile, AddressOf, gROOT

from PIL import Image

if len(sys.argv) < 2:
    print "\nYou must enter the png file you wish to convert as the first arguement. Exiting \n"
    sys.exit(1)

try:    input_file = sys.argv[1]
except:
    print "\nThe entered file cannot be opened, please enter a vaild .lhe file. Exiting. \n"
    sys.exit(1)
    pass

if len(sys.argv) > 2:    output_file_name = sys.argv[2]
else:                    output_file_name = "pics_pixels.root"

try:    output_file = TFile(output_file_name, "RECREATE")
except:
    print "Cannot open output file named: " + output_file_name + "\nPlease enter a valid output file name as the 2nd arguement. Exiting"
    sys.exit(1)
    pass

output_tree = TTree("Physics", "Physics")
print "Setup complete \nOpened file " + str(sys.argv[1]) + "  \nConverting to .root format and outputing to " + output_file_name


pixels = i.load(input_file) # this is not a list
output_tree = TTree("Physics", "Physics")
print "Setup complete \nOpened picture " + str(sys.argv[1]) + "  \nConverting to .root format and outputing to " + output_file_name


# Setup output branches
X_v = r.vector('Double_t')()
Y_v = r.vector('Double_t')()
Pixel_v =r.vector('Double_t')()

# Create a struct which acts as the TBranch for non-vectors
gROOT.ProcessLine( "struct MyStruct{ Int_t n_particles; Double_t weight; };")
from ROOT import MyStruct

# Assign the variables to the struct
s = MyStruct() 
output_tree.Branch("X",X_v)
output_tree.Branch("Y",Y_v)
output_tree.Branch("Pixel",Pixel_v)

width, height = i.size
row_averages = []
for y in range(height):
    cur_row_ttl = 0
    for x in range(width):
        cur_pixel = pixels[x, y]
        cur_pixel_mono = sum(cur_pixel) / len(cur_pixel)
        cur_row_ttl += cur_pixel_mono
        X_v = x
        Y_v = y
        Pixel_v = 255 - cur_pixel_mono
        output_tree.Fill()
        print "x=", x, " y=", y, " pixel=", cur_pixel_mono 
    cur_row_avg = cur_row_ttl / width
    row_averages.append(cur_row_avg)
        
print "Brighest row:",
print max(row_averages)
output_tree.Write()
output_file.Close()
