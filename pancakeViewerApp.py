#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.7.2 on Mon Jun 13 21:27:40 2016
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
from MainFrame import MainFrame

class PancakeViewerApp(wx.App):
    def OnInit(self):
        mainFrame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(mainFrame)
        mainFrame.Show()
        return True

# end of class PancakeViewerApp

if __name__ == "__main__":
    gettext.install("pancakeViewerApp") # replace with the appropriate catalog name

    pancakeViewerApp = PancakeViewerApp(0)
    pancakeViewerApp.MainLoop()