import wx  
import pyspi  
class MyApp(wx.App):
    def OnInit(self):  
       self.frame = MyFrame(parent=None, title='py爬虫展示')  
       self.SetTopWindow(self.frame)
       self.frame.Show()  
       self.frame.Center()
       return True

class MyFrame(wx.Frame):
	def __init__(self,parent,id=wx.ID_ANY,title="",
				pos=wx.DefaultPosition,size=(500,500),
				style=wx.DEFAULT_FRAME_STYLE,
				name="MyFrame"):
		super(MyFrame,self).__init__(parent,id,title,
									pos,size,style,name)

		self.panel=wx.Panel(self)
		self.panel.SetBackgroundColour(wx.WHITE)
		button1=wx.Button(self.panel,
								label="Get Price",
								pos=(288,40))
		self.btnId1=button1.GetId()
		self.Bind(wx.EVT_BUTTON,self.getPrice,button1)
##############
		self.multiLabel1=wx.StaticText(self.panel,-1,"price")
		self.multiText1=wx.TextCtrl(self.panel,-1,"if you want to get the price of IphoneX，press the button \n",
							size=(200,100),style=wx.TE_MULTILINE)
		self.multiText1.SetInsertionPoint(0)

		self.multiLabel2=wx.StaticText(self.panel,-1,"model")
		self.multiText2=wx.TextCtrl(self.panel,-1,"if you want to get the brands of phones，press the button \n",
							size=(200,100),style=wx.TE_MULTILINE)
		self.multiText2.SetInsertionPoint(0)

		self.richLabel=wx.StaticText(self.panel,-1,"reputation")
		self.richText=wx.TextCtrl(self.panel,
			-1,"if you want to get the reputation of IphoneX press the button \n",size=(200, 100),style=wx.TE_MULTILINE|wx.TE_RICH2)

		self.richText.SetInsertionPoint(0)
		self.richText.SetStyle(44,52,wx.TextAttr("white", "black"))
		points = self.richText.GetFont().GetPointSize()		
		f = wx.Font(points + 3, wx.ROMAN, wx.ITALIC, wx.BOLD, True) #创建一个字体  
		self.richText.SetStyle(68, 82, wx.TextAttr("blue", wx.NullColour, f)) #用新字体设置样式  
		sizer = wx.FlexGridSizer(cols=2, hgap=6, vgap=6)		
		sizer.AddMany([self.multiLabel1, self.multiText1, self.richLabel, self.richText,self.multiLabel2, self.multiText2])  
		self.panel.SetSizer(sizer)

		button2=wx.Button(self.panel,label="Get Good Reputation",pos=(288,140))
		self.btnId2=button2.GetId()
		self.Bind(wx.EVT_BUTTON,self.getRepu,button2)
		button3=wx.Button(self.panel,label="Get different model",pos=(288,240))
		self.btnId3=button2.GetId()
		self.Bind(wx.EVT_BUTTON,self.getBrand,button3)

	def getPrice(self,event):
		for price in pyspi.getPrice():
			self.multiText1.AppendText(price.text+"\n")
		

	def getRepu(self,event):
		

		self.richText.AppendText(pyspi.getRepu()) 
		
	def getBrand(self,event):		
		for t in pyspi.getBrand():
			self.multiText2.AppendText(t.text+"\n")
			


if __name__=="__main__":
	app = MyApp(False)  
	app.MainLoop()  