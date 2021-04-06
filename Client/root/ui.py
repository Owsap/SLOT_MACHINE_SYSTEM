''' 1. Ignore if it already exists '''
# Search @ class.AniImageBox
	def __init__(self, layer = "UI"):
		Window.__init__(self, layer)

# Add below
		if app.ENABLE_SLOT_MACHINE_SYSTEM:
			self.end_frame_event = None
			self.key_frame_event = None

''' 2. Ignore if it already exists '''
# Search @ class.AniImageBox
	def __del__(self):
		Window.__del__(self)

# Add below
		if app.ENABLE_SLOT_MACHINE_SYSTEM:
			self.end_frame_event = None
			self.key_frame_event = None

''' 3. Ignore if it already exists '''
# Search
	def OnEndFrame(self):
		pass

# Replace with
	if app.ENABLE_SLOT_MACHINE_SYSTEM:
		def OnEndFrame(self):
			if self.end_frame_event:
				self.end_frame_event()

		def SetEndFrameEvent(self, event):
			self.end_frame_event = event

		def ResetFrame(self):
			wndMgr.ResetFrame(self.hWnd)

		def OnKeyFrame(self, cur_frame):
			if self.key_frame_event:
				self.key_frame_event(cur_frame)

		def SetKeyFrameEvent(self, event):
			self.key_frame_event = event
	else:
		def OnEndFrame(self):
			pass
