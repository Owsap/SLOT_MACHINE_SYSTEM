''' 1. '''
# Search
IsQBHide = 0

# Add above
if app.ENABLE_SLOT_MACHINE_SYSTEM:
	import uiSlotMachineSystem

''' 2. '''
# Search @ def __init__
		self.wndQuestWindowNewKey = 0
		self.privateShopAdvertisementBoardDict = {}
		self.guildScoreBoardDict = {}
		self.equipmentDialogDict = {}

# Add below
		if app.ENABLE_SLOT_MACHINE_SYSTEM:
			self.wndSlotMachine = None

''' 3. '''
# Search @ def __MakeWindows
		self.wndMall = uiSafebox.MallWindow()
		wndChatLog = uiChat.ChatLogWindow()
		wndChatLog.BindInterface(self)
		self.wndChatLog = wndChatLog

# Add above
		if app.ENABLE_SLOT_MACHINE_SYSTEM:
			self.wndSlotMachine = uiSlotMachineSystem.SlotMachineWindow()

''' 4. '''
# Search
		# ACCESSORY_REFINE_ADD_METIN_STONE
		if self.wndItemSelect:
			self.wndItemSelect.Destroy()
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

# Add below
		if app.ENABLE_SLOT_MACHINE_SYSTEM:
			if self.wndSlotMachine:
				self.wndSlotMachine.Destroy()
				del self.wndSlotMachine

''' 5. '''
# Search @ def HideAllWindows
		if self.wndMessenger:
			self.wndMessenger.Hide()

		if self.wndGuild:
			self.wndGuild.Hide()

# Add below
		if app.ENABLE_SLOT_MACHINE_SYSTEM:
			if self.wndSlotMachine:
				self.wndSlotMachine.Hide()

''' 6. '''
# Search
	def ToggleGuildWindow(self):

# Add above
	if app.ENABLE_SLOT_MACHINE_SYSTEM:
		def ToggleSlotMachineWindow(self):
			if not player.IsObserverMode():
				if self.wndSlotMachine.IsShow():
					self.wndSlotMachine.Close()
				else:
					self.wndSlotMachine.Open()

		def SetSlotMachineReels(self, win, jackpot, r1, r2, r3):
			if not player.IsObserverMode():
				if self.wndSlotMachine.IsShow():
					self.wndSlotMachine.OnSetReels(win, jackpot, r1, r2, r3)
