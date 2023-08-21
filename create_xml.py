

folder = "folder"
filename = "filename"
path = "path"
name = "name"
height = "480"
width = "640"
depth = "3"
xmin,ymin,xmax,ymax = "xmin","ymin","xmax","ymax"


def xml_create(folder,filename,path,name,height,width,depth,xmin,ymin,xmax,ymax):


	fw = open('delete.xml','w')

	fw.write(

	"<annotation>"+
		"<folder>"+folder+"</folder>"+
		"<filename>"+filename+"</filename>"+
		"<path>"+"/home/manju/Desktop/suprajit_13/MR_0.jpg"+"</path>"+
		"<source>"+
			"<database>Unknown</database>"+
		"</source>"+
		"<size>"+
			"<width>"+width+"</width>"+
			"<height>"+height+"</height>"+
			"<depth>"+depth+"</depth>"+
		"</size>"+
		"<segmented>0</segmented>"+
		"<object>"+
			"<name>"+name+"</name>"+
			"<pose>Unspecified</pose>"+
			"<truncated>0</truncated>"+
			"<difficult>0</difficult>"+
			"<bndbox>"+
				"<xmin>"+xmin+"</xmin>"+
				"<ymin>"+ymin+"</ymin>"+
				"<xmax>"+xmax+"</xmax>"+
				"<ymax>"+ymax+"</ymax>"+
			"</bndbox>"+
		"</object>"+
	"</annotation>")
	fw.close()


