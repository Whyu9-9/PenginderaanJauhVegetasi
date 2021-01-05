from osgeo import gdal
from pyproj import Proj
from sklearn.cluster import KMeans
import os
import numpy as np

class segmentasi:
	TAG = "segmentasi.class"

	imagePath = ""
	image = None
	freq = None
	output_cols = 0
	output_rows = 0
	lonStartCrop = 0
	latStartCrop = 0
	lonEndCrop = 0
	latEndCrop = 0

	crop_band = None

	def __init__(self):
		print("create segmentasi class")

	#Check Image File
	def openImage(self, path):
		print(self.TAG, "File Image Path : ", path)
		openImage = gdal.Open(path, gdal.GA_ReadOnly)
		if not openImage:
			print(self.TAG, "Type : Not Image File")
			return False
		else:
			print(self.TAG, "Type : Image File")
			self.imagePath = path
			self.image = openImage
			return True

	def OpenMtlFile(self, path):
		issue = []
		issue.clear()
		if "mtl" in path.lower():
			file = open(path, 'r')
			line = file.readlines()

			for x in line:
				if x.startswith("    CORNER_UL_LON_PRODUCT"):
					data = x.split()
					lonStart = data[2]
					print("Lon start: " + lonStart)
					self.lonStartDefault = lonStart

				if x.startswith("    CORNER_UR_LAT_PRODUCT"):
					data = x.split()
					latStart = data[2]
					print("Lat Start: " + latStart)
					self.latStartDefault = latStart

				if x.startswith("    CORNER_UR_LON_PRODUCT"):
					data = x.split()
					lonEnd = data[2]
					print("Lon end: " + lonEnd)
					self.lonEndDefault = lonEnd

				if x.startswith("    CORNER_LL_LAT_PRODUCT"):
					data = x.split()
					latEnd = data[2]
					print("lat end: " + latEnd)
					self.latEndDefault = latEnd

			# check imprt value from mtl file
			if self.lonStartDefault == 0:
				issue.append("CORNER_UL_LON_PRODUCT not found")
			if self.latStartDefault == 0:
				issue.append("CORNER_UR_LAT_PRODUCT not found")
			if self.lonEndDefault == 0:
				issue.append("CORNER_UR_LON_PRODUCT not found")
			if self.latEndDefault == 0:
				issue.append("CORNER_LL_LAT_PRODUCT not found")

			if issue:
				issueBuf = ""
				for item in issue:
					issueBuf += item + "\n"
				self.isMtl = False
				print(issueBuf)
			else:
				self.isMtl = True
				print('check mtl success')
		else:
			print('error')

	def SetCropCoordinate(self, lonStart, lonEnd, latStart, latEnd):
		self.lonStartCrop = lonStart
		self.lonEndCrop = lonEnd
		self.latStartCrop = latStart
		self.latEndCrop = latEnd

		print("lonStart: ", self.lonStartCrop)
		print("lonEnd: ", self.lonEndCrop)
		print("latStart: ", self.latStartCrop)
		print("latEnd: ", self.latEndCrop)

	def CropImage(self):
		self.cols = self.image.RasterXSize
		self.rows = self.image.RasterYSize
		bands = self.image.RasterCount
		print("cols: ", self.cols, "\nrows: ", self.rows, "\nbands: ", bands)

		gt = self.image.GetGeoTransform()
		print("GeoTransform: ", gt)
		x0 = gt[0]
		y0 = gt[3]
		pwidth = gt[1]
		pheight = gt[5]
		x_end = self.cols * pwidth + x0
		y_end = self.cols * pheight + y0

		myProj = Proj(
			"+proj=utm +zone=50, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
		lon, lat = myProj(x0, y0, inverse=True)
		x_utm, y_utm = myProj(lon, lat)
		print("lon: ", lon, "\nlat: ", lat)
		print("x_utm", x_utm, "\ny_utm", y_utm)

		x_mulai_crop_utm, y_mulai_crop_utm = myProj(
			self.lonStartCrop, self.latStartCrop)
		x_akhir_crop_utm, y_akhir_crop_utm = myProj(
			self.lonEndCrop, self.latEndCrop)
		print("x_mulai_crop_utm: ", x_mulai_crop_utm, "\ny_mulai_crop_utm: ", y_mulai_crop_utm, "\nx_akhir_crop_utm: ",
			  x_akhir_crop_utm, "\ny_akhir_crop_utm: ", y_akhir_crop_utm)

		xoff = int((x_mulai_crop_utm - x0) / pwidth)
		yoff = int((y_mulai_crop_utm - y0) / pheight)
		print("xoff: ", xoff, "\nyoff: ", yoff)

		self.output_cols = int((x_akhir_crop_utm - x_mulai_crop_utm) / pwidth)
		self.output_rows = int((y_akhir_crop_utm - y_mulai_crop_utm) / pheight)

		print("output_cols: ", self.output_cols)
		print("output_rows: ", self.output_rows)

		band_image = self.image.GetRasterBand(1)

		self.crop_band = band_image.ReadAsArray(
			xoff, yoff, self.output_cols, self.output_rows)
		print(self.crop_band)

	def clustering(self):
		print(self.TAG, "Define KMeans Cluster 40")
		km = KMeans(n_clusters=4)
		band = self.image.RasterCount
		data = np.empty((self.output_cols*self.output_rows, band))
		for i in range(1, band+1):
			data[:, i-1] = self.crop_band.flatten()
		print(self.TAG, "Define Band Base Process")
		km.fit(data)
		print(self.TAG, "Predict Classes")
		x = km.predict(data)

		print(self.TAG, "Creating Shape from predicted classes")
		out_data = km.labels_.reshape((self.output_rows, self.output_cols))
		arr_list = km.labels_
		(unique, counts) = np.unique(arr_list, return_counts=True)
		self.freq = np.asarray((unique, counts)).T

		print(self.TAG, "Saving The Original Image with Gdal")
		path = os.path.dirname(__file__)
		driverTiff = gdal.GetDriverByName("GTiff")
		cloneImg = driverTiff.Create(path+"\\temp\\classified2.tif", self.output_cols, self.output_rows, 1, gdal.GDT_Float32)
		cloneImg.SetGeoTransform(self.image.GetGeoTransform())
		cloneImg.SetProjection(self.image.GetProjection())
		cloneImg.GetRasterBand(1).SetNoDataValue(255)
		cloneImg.GetRasterBand(1).WriteArray(out_data)
		cloneImg = None
		print(self.TAG, "Saving Done")
		return path+"\\temp\\classified2.tif"