# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import os
import wx
import wx.xrc
import numpy


from segmentasi import segmentasi
from PIL import Image
from collections import defaultdict

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Project UAS I Wayan Wahyu Ivan M - 1805551097",
                          pos=wx.DefaultPosition, size=wx.Size(850, 465),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizeFrameMain = wx.BoxSizer(wx.VERTICAL)

        bSizerMainFrame = wx.BoxSizer(wx.VERTICAL)

        self.panelMain = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizeMain = wx.BoxSizer(wx.VERTICAL)

        bSizeMainPanel = wx.BoxSizer(wx.VERTICAL)

        bSizeBox = wx.BoxSizer(wx.HORIZONTAL)

        bSizeData = wx.BoxSizer(wx.VERTICAL)

        bSizeData.SetMinSize(wx.Size(500, -1))
        bSizeRGB = wx.BoxSizer(wx.HORIZONTAL)

        bSizeRGB.SetMinSize(wx.Size(500, -1))
        sbImage = wx.StaticBoxSizer(wx.StaticBox(self.panelMain, wx.ID_ANY, u"Image RGB Composite"), wx.VERTICAL)

        sbImage.SetMinSize(wx.Size(200, 200))
        self.imgRgb = wx.StaticBitmap(sbImage.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(150, 150), 0)
        sbImage.Add(self.imgRgb, 0, wx.ALIGN_CENTER | wx.ALL, 0)

        self.fpRgb = wx.FilePickerCtrl(sbImage.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*",
                                       wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
        sbImage.Add(self.fpRgb, 0, wx.ALL | wx.EXPAND, 0)

        bSizeRGB.Add(sbImage, 1, wx.ALL, 5)

        bSizeData.Add(bSizeRGB, 1, wx.ALL, 0)

        bSizeInfo = wx.BoxSizer(wx.HORIZONTAL)

        bSizeInfo.SetMinSize(wx.Size(500, -1))
        sbHasil = wx.StaticBoxSizer(wx.StaticBox(self.panelMain, wx.ID_ANY, u"Data Hasil"), wx.VERTICAL)

        sbHasil.SetMinSize(wx.Size(200, 200))
        bsCluster = wx.BoxSizer(wx.VERTICAL)

        self.labelCluster = wx.StaticText(sbHasil.GetStaticBox(), wx.ID_ANY, u"Cluster", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.labelCluster.Wrap(-1)
        bsCluster.Add(self.labelCluster, 0, wx.ALL, 5)

        self.hasilCluster = wx.StaticText(sbHasil.GetStaticBox(), wx.ID_ANY, u"null", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.hasilCluster.Wrap(-1)
        bsCluster.Add(self.hasilCluster, 0, wx.ALL, 5)

        sbHasil.Add(bsCluster, 1, wx.EXPAND, 5)

        bSizeInfo.Add(sbHasil, 1, wx.ALL | wx.EXPAND, 5)

        sbCrop = wx.StaticBoxSizer(wx.StaticBox(self.panelMain, wx.ID_ANY, u"Crop Coordinate"), wx.VERTICAL)

        sbCrop.SetMinSize(wx.Size(200, 200))
        bsFormTop = wx.BoxSizer(wx.HORIZONTAL)

        self.lbLoStart = wx.StaticText(sbCrop.GetStaticBox(), wx.ID_ANY, u"Longitude Start", wx.DefaultPosition,
                                       wx.Size(100, -1), 0)
        self.lbLoStart.Wrap(-1)
        bsFormTop.Add(self.lbLoStart, 0, wx.ALL, 5)

        self.longStart = wx.TextCtrl(sbCrop.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(100, -1), 0)
        bsFormTop.Add(self.longStart, 0, wx.ALL, 0)

        sbCrop.Add(bsFormTop, 1, wx.EXPAND, 0)

        bsFormBottom = wx.BoxSizer(wx.HORIZONTAL)

        self.lbLoStop = wx.StaticText(sbCrop.GetStaticBox(), wx.ID_ANY, u"Longitude Stop", wx.DefaultPosition,
                                      wx.Size(100, -1), 0)
        self.lbLoStop.Wrap(-1)
        bsFormBottom.Add(self.lbLoStop, 0, wx.ALL, 5)

        self.longStop = wx.TextCtrl(sbCrop.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(100, -1), 0)
        bsFormBottom.Add(self.longStop, 0, wx.ALL, 0)

        sbCrop.Add(bsFormBottom, 1, wx.EXPAND, 5)

        bsFormLeft = wx.BoxSizer(wx.HORIZONTAL)

        self.lbLaStart = wx.StaticText(sbCrop.GetStaticBox(), wx.ID_ANY, u"Latitude Start", wx.DefaultPosition,
                                       wx.Size(100, -1), 0)
        self.lbLaStart.Wrap(-1)
        bsFormLeft.Add(self.lbLaStart, 0, wx.ALL, 5)

        self.latStart = wx.TextCtrl(sbCrop.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(100, -1), 0)
        bsFormLeft.Add(self.latStart, 0, wx.ALL, 0)

        sbCrop.Add(bsFormLeft, 1, wx.EXPAND, 0)

        bsFormRight = wx.BoxSizer(wx.HORIZONTAL)

        self.lbLaStop = wx.StaticText(sbCrop.GetStaticBox(), wx.ID_ANY, u"Latitude Stop", wx.DefaultPosition,
                                      wx.Size(100, -1), 0)
        self.lbLaStop.Wrap(-1)
        bsFormRight.Add(self.lbLaStop, 0, wx.ALL, 5)

        self.latStop = wx.TextCtrl(sbCrop.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                   wx.Size(100, -1), 0)
        bsFormRight.Add(self.latStop, 0, wx.ALL, 0)

        sbCrop.Add(bsFormRight, 1, wx.EXPAND, 0)

        bSizeInfo.Add(sbCrop, 1, wx.ALL, 5)

        bSizeData.Add(bSizeInfo, 1, wx.ALL, 0)

        bSizeBox.Add(bSizeData, 0, wx.ALL | wx.EXPAND, 10)

        bSizeHasil = wx.BoxSizer(wx.VERTICAL)

        bSizeHasil.SetMinSize(wx.Size(300, -1))
        sbClip = wx.StaticBoxSizer(wx.StaticBox(self.panelMain, wx.ID_ANY, u"Hasil Clip Grid"), wx.VERTICAL)

        self.imgClip = wx.StaticBitmap(sbClip.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.imgClip.SetMinSize(wx.Size(150, 150))

        sbClip.Add(self.imgClip, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btnClip = wx.Button(sbClip.GetStaticBox(), wx.ID_ANY, u"Clip Grid", wx.DefaultPosition, wx.DefaultSize, 0)
        sbClip.Add(self.btnClip, 0, wx.ALL | wx.EXPAND, 5)

        bSizeHasil.Add(sbClip, 1, wx.EXPAND, 5)

        sbSegmentation = wx.StaticBoxSizer(wx.StaticBox(self.panelMain, wx.ID_ANY, u"Hasil Segmentasi"), wx.VERTICAL)

        self.imgSegmentasi = wx.StaticBitmap(sbSegmentation.GetStaticBox(), wx.ID_ANY, wx.NullBitmap,
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        self.imgSegmentasi.SetMinSize(wx.Size(200, 200))

        sbSegmentation.Add(self.imgSegmentasi, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        self.btSegmen = wx.Button(sbSegmentation.GetStaticBox(), wx.ID_ANY, u"Make Segmentation", wx.DefaultPosition,
                                  wx.DefaultSize, 0)
        sbSegmentation.Add(self.btSegmen, 0, wx.ALL | wx.EXPAND, 5)

        bSizeHasil.Add(sbSegmentation, 1, wx.EXPAND, 5)

        bSizeBox.Add(bSizeHasil, 0, wx.ALL | wx.EXPAND, 10)

        bSizeMainPanel.Add(bSizeBox, 1, wx.EXPAND, 0)

        bSizeMain.Add(bSizeMainPanel, 1, wx.EXPAND, 0)

        self.panelMain.SetSizer(bSizeMain)
        self.panelMain.Layout()
        bSizeMain.Fit(self.panelMain)
        bSizerMainFrame.Add(self.panelMain, 1, wx.EXPAND | wx.ALL, 0)

        bSizeFrameMain.Add(bSizerMainFrame, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(bSizeFrameMain)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.fpRgb.Bind(wx.EVT_FILEPICKER_CHANGED, self.loadImage)
        self.btnClip.Bind(wx.EVT_BUTTON, self.clipGrid)
        self.btSegmen.Bind(wx.EVT_BUTTON, self.makeSegmentation)

    def __del__(self):
        pass
    segmen = segmentasi()

    def showMessage(self, message):
        dialog = wx.MessageDialog(None, message, "Info", wx.OK | wx.ICON_INFORMATION)
        dialog.ShowModal()

    def showMessageError(self, message):
        dialog = wx.MessageDialog(None, message, "Error", wx.OK | wx.ICON_ERROR)
        dialog.ShowModal()

    def loadImage(self, event):
        path = event.GetPath()
        isImage = self.segmen.openImage(path)
        if isImage:
            loadImage = Image.open(path)
            arrayimg = numpy.array(loadImage)
            img = self.convertToImage(arrayimg, 150, 150, False)
            bitmapImage = wx.Bitmap(img)
            self.imgRgb.SetBitmap(bitmapImage)
        event.Skip()

    def clipGrid(self, event):
        if (self.longStart.GetValue() == None or self.longStart.GetValue() == ""):
            self.showMessageError("Image RGB Belum Dimasukkan!")
        else:
            lonStart = self.longStart.GetValue()
            latStart = self.latStart.GetValue()
            lonEnd = self.longStop.GetValue()
            latEnd = self.latStop.GetValue()

            print(lonStart)
            print(latStart)
            print(lonEnd)
            print(latEnd)

            self.segmen.SetCropCoordinate(lonStart, lonEnd, latStart, latEnd)
            self.segmen.CropImage()
            img = self.convertToImage(self.segmen.crop_band, 150, 200, False)
            bitmapImage = wx.Bitmap(img)
            self.imgClip.SetBitmap(bitmapImage)
            self.showMessage("Clip Image Berhasil!")
            event.Skip()

    def makeSegmentation(self, event):
        if (self.longStart.GetValue() == None or self.longStart.GetValue() == ""):
            self.showMessageError("Crop Coordinate Belum Dimasukkan!")
        else:
            clusterSegmen = self.segmen.clustering()
            loadImage = Image.open(clusterSegmen).convert('P')
            arrayimg = numpy.array(loadImage)
            img = self.convertToImage(arrayimg, 150, 200, True)
            bitmapImage = wx.Bitmap(img)
            self.imgSegmentasi.SetBitmap(bitmapImage)
            print(self.segmen.freq)
            clusterText = ""
            for cek in self.segmen.freq:
                clusterText += "RGB ("+str(cek[0]*32)+","+str(cek[0]*32)+","+str(cek[0]*32)+ ") = " + str(cek[1]) +"\n"
            self.hasilCluster.SetLabel(clusterText)
            self.showMessage("Segmentasi Berhasil!")
            event.Skip()

    def convertToImage(self, array, w_in, h_in, isFloat):
        newW = w_in
        newH = h_in
        print(self.segmen.TAG, "Declaring RGB")

        if isFloat:
            rgb = array * 32
            print(self.segmen.TAG, "Convert Image to RGB")
            pilImage = Image.fromarray(rgb).convert("RGB")
            image = wx.Image(pilImage.size[0], pilImage.size[1])
            image.SetData(pilImage.tobytes())
        else:
            print(self.segmen.TAG, "Convert Image to RGB")
            pilImage = Image.fromarray(array).convert("RGB")
            image = wx.Image(pilImage.size[0], pilImage.size[1])
            image.SetData(pilImage.tobytes())

        print(self.segmen.TAG, "Resize Image")
        H = image.GetHeight()
        W = image.GetWidth()
        if (W > H):
            newH = newH * H / W
        else:
            newW = newW * W / H

        image = image.Scale(newW, newH)
        return image

class MainApp(wx.App):
    def OnInit(self):
        myframe = mainFrame(None)
        myframe.Show(True)
        return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()