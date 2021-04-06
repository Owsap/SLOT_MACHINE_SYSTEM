''' 1. '''
# Search
	def BINARY_ActEmotion(self, emotionIndex):
		if self.interface.wndCharacter:
			self.interface.wndCharacter.ActEmotion(emotionIndex)

# Add below
	if app.ENABLE_SLOT_MACHINE_SYSTEM:
		def __OpenSlotMachineWnd(self):
			if self.interface:
				self.interface.ToggleSlotMachineWindow()

		def BINARY_SlotMachineReels(self, win, jackpot, r1, r2, r3):
			if self.interface:
				self.interface.SetSlotMachineReels(win, jackpot, r1, r2, r3)

''' 2. '''
# Search
		self.serverCommander = stringCommander.Analyzer()
		for serverCommandItem in serverCommandList.items():
			self.serverCommander.SAFE_RegisterCallBack(
				serverCommandItem[0], serverCommandItem[1]
			)

# Add above
		if app.ENABLE_SLOT_MACHINE_SYSTEM:
			serverCommandList["OpenSlotMachineWnd"] = self.__OpenSlotMachineWnd
