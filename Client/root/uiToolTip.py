''' 1. '''
# Search @ class ToolTip
	def AlignHorizonalCenter(self):
		for child in self.childrenList:
			(x, y) = child.GetLocalPosition()
			child.SetPosition(self.toolTipWidth/2, y)

		self.ResizeToolTip()

# Add above
	if app.ENABLE_SLOT_MACHINE_SYSTEM:
		def TextAlignHorizonalCenter(self):
			for child in self.childrenList:
				(x, y) = child.GetLocalPosition()
				try:
					if child.GetText() != "":
						child.SetPosition(self.toolTipWidth / 2, y)
				except:
					pass

			self.ResizeToolTip()
