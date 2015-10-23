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


i = Image.open(input_file)
pixels = i.load() # this is not a list
output_tree = TTree("Physics", "Physics")
print "Setup complete \nOpened picture " + input_file + "  \nConverting to .root format and outputing to " + output_file_name


# Setup output branches
#X_v = r.vector('Double_t')()
#Y_v = r.vector('Double_t')()
#Pixel_v =r.vector('Double_t')()

# Create a struct which acts as the TBranch for non-vectors
gROOT.ProcessLine( "struct MyStruct{ Double_t X_v; Double_t Y_v; Double_t Pixel_v; };")
from ROOT import MyStruct

# Assign the variables to the struct
s = MyStruct() 
output_tree.Branch('X_v',AddressOf(s,'X_v'),'X_v/D')
output_tree.Branch('Y_v',AddressOf(s,'Y_v'),'Y_v/D')
output_tree.Branch('Pixel_v',AddressOf(s,'Pixel_v'),'Pixel_v/D')

#output_tree.Branch("X",X_v)
#output_tree.Branch("Y",Y_v)
#output_tree.Branch("Pixel",Pixel_v)

width, height = i.size
for y in range(height):
    cur_row_ttl = 0
    for x in range(width):
        cur_pixel = pixels[x, y]
        cur_pixel_mono = sum(cur_pixel) / len(cur_pixel)
        cur_row_ttl += cur_pixel_mono
        s.X_v = x
        s.Y_v = y
        s.Pixel_v = 255 - cur_pixel_mono
        output_tree.Fill()
#        print "x=", x, " y=", y, " pixel=", cur_pixel_mono 

output_tree.Write()
output_file.Close()
