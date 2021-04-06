#
# File: uiSlotMachineSystem.py
# Version: 1.0.0.0
# Author: Owsap
# Date: 2021.03.21
#

import app
import ui
import item
import net
import localeInfo
import uiToolTip
import player
import chat
import snd

# Bet Values
# @ game/constants.cpp
SLOT_MACHINE_BET_VALUES = {
	1 : 1500000,
	2 : 2000000,
	3 : 2500000,
	4 : 3000000,
	5 : 3500000,
	6 : 4000000,
	7 : 4500000,
	8 : 5000000,
	9 : 5500000,
	10 : 6000000,
	11 : 6500000,
	12 : 7000000,
	13 : 7500000,
	14 : 8000000,
	15 : 8500000,
	16 : 9000000,
	17 : 9500000,
	18 : 10000000,
	19 : 15000000,
	20 : 20000000,
	21 : 25000000,
	22 : 30000000,
	23 : 35000000,
	24 : 40000000,
	25 : 45000000,
	26 : 50000000,
}

# Reel Icons
SLOT_MACHINE_REELS = {
	1 : 124400, # Jackpot 1 Reserved
	2 : 134400, # Jackpot 2 Reserved
	3 : 144400, # Jackpot 3 Reserved

	4 : 123400,
	5 : 133400,
	6 : 143400,

	7 : 121400,
	8 : 131400,
	9 : 141300,

	#10 : 123300,
	#11 : 133300,
	#12 : 143300,

	#13 : 122000,
	#14 : 132000,
	#15 : 142000,

	#16 : 120300,
	#17 : 130300,
	#18 : 140300,

	#19 : 120000,
	#20 : 130000,
	#21 : 140000,
}

# Actions
SLOT_MACHINE_CLOSE = 0
SLOT_MACHINE_OPEN = 1
SLOT_MACHINE_START = 2

# Reel Icon Index
SLOT_MACHINE_REEL1 = 0
SLOT_MACHINE_REEL2 = 1
SLOT_MACHINE_REEL3 = 2

# Board Index
SLOT_MACHINE_PLAY_BOARD = 0
SLOT_MACHINE_INFO_BOARD = 1

# Max Jackpots
SLOT_MACHINE_MAX_JACKPOTS = 3

ENABLE_SOUND = True
ENABLE_EFFECT = True

# For testing only
DEBUG = False

SLOT_MACHINE_TOOLTIP_DICT = {
	1 : localeInfo.SLOT_MACHINE_INFO_TOOLTIP_1,
	2 : localeInfo.SLOT_MACHINE_INFO_TOOLTIP_2,
	3 : localeInfo.SLOT_MACHINE_INFO_TOOLTIP_3,
	4 : "[ENTER]",
	5 : localeInfo.SLOT_MACHINE_INFO_TOOLTIP_4,
	6 : "[ENTER]",
	7 : localeInfo.SLOT_MACHINE_INFO_TOOLTIP_5,
}

class SlotMachineWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Construct()
		self.toolTip = uiToolTip.ToolTip()

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.__Construct()

	# Construct window
	def __Construct(self):
		self.isLoaded = False
		self.isInformationPage = False

		self.isRolling = False

		self.reelResult = {}
		self.rollTime = {}
		self.isRolled = {}

		self.hasWon = 0
		self.hasJackpot = 0
		self.betIndex = 0

		self.toolTip = None
		self.toolTipHelp = None

	# Load window
	def __LoadWindow(self):
		# Try to load UIScript
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/SlotMachineWindow.py")
		except:
			import exception
			exception.Abort("SlotMachineWindow.__LoadWindow")

		# Try to bind objects
		try:
			self.__BindObject()
		except:
			import exception
			exception.Abort("SlotMachineWindow.__BindObject")

		# Try to bind events
		try:
			self.__BindEvent()
		except:
			import exception
			exception.Abort("SlotMachineWindow.__BindEvent")

	# Bind objects
	def __BindObject(self):
		Child = self.GetChild
		self.board = Child("Board")
		self.titleBar = Child("TitleBar")
		self.titleBarText = Child("TitleBarText")

		self.boardContainer = Child("BoardContainerBgImg")

		self.slotMachineWnd = Child("SlotMachineWindow")
		#self.slotMachineBoard = Child("SlotMachineBoardImage")
		self.reelIconSlot = Child("ReelIconSlot")

		#self.bettingBoard = Child("BettingBoardImage")
		self.betButton = Child("BetButton")
		self.bettingText = Child("BettingText")
		#self.betInputBoard = Child("BetInputBoardImage")
		#self.moneyIcon = Child("MoneyIconImg")
		self.betValue = Child("BetValueEditLine")
		self.downBetButton = Child("DownBetButton")
		self.upBetButton = Child("UpBetButton")

		self.informationWnd = Child("InformationWindow")
		self.informationWnd.Hide()
		#self.jackpotBoard = Child("JackpotBoardImage")
		self.jackpotReelIconSlot = Child("JackpotReelIconSlot")

		self.informationButton = Child("InformationButton")

		self.jackpotEffect = Child("JackpotEffectAniImg")
		self.jackpotEffect.Hide()

		self.successEffect = Child("SuccessEffectAniImage")
		self.successEffect.Hide()

		self.reelIconEffectList = []
		self.reelIconEffectList.append(self.GetChild("ReelIconEffectAniImage1"))
		self.reelIconEffectList.append(self.GetChild("ReelIconEffectAniImage2"))
		self.reelIconEffectList.append(self.GetChild("ReelIconEffectAniImage3"))
		for reelIconEffect in self.reelIconEffectList:
			reelIconEffect.Hide()

		self.helpToolTipButton = Child("HelpToolTipButton")

	def __BindEvent(self):
		# Title Bar
		if self.titleBar:
			self.titleBar.SetCloseEvent(ui.__mem_func__(self.__OnClickCloseTitleBar))

		# Bet Button
		if self.betButton:
			self.betButton.SetEvent(ui.__mem_func__(self.__OnClickBetButton))

		# Down Bet Button
		if self.downBetButton:
			self.downBetButton.SetEvent(ui.__mem_func__(self.__OnClickDownBetButton))

		# Up Bet Button
		if self.upBetButton:
			self.upBetButton.SetEvent(ui.__mem_func__(self.__OnClickUpBetButton))

		# Information (Jackpot) Button
		if self.informationButton:
			self.informationButton.SetToggleUpEvent(ui.__mem_func__(self.__OnClickInformationButton))
			self.informationButton.SetToggleDownEvent(ui.__mem_func__(self.__OnClickInformationButton))

		# Help ToolTip Button
		if self.helpToolTipButton:
			self.toolTipHelp = self.__CreateGameTypeToolTip(localeInfo.SLOT_MACHINE_INFO_TOOLTIP, SLOT_MACHINE_TOOLTIP_DICT)
			self.toolTipHelp.SetTop()
			self.helpToolTipButton.SetToolTipWindow(self.toolTipHelp)

		# Jackpot Effect
		if self.jackpotEffect:
			self.jackpotEffect.SetEndFrameEvent(ui.__mem_func__(self.__OnHideJackpotEffect))

		# Success Effect
		if self.successEffect:
			self.successEffect.SetEndFrameEvent(ui.__mem_func__(self.__OnHideSuccessEffect))

		# Slot Reel Effect
		if self.reelIconEffectList:
			for reelIconEffect in self.reelIconEffectList:
				reelIconEffect.SetEndFrameEvent(ui.__mem_func__(self.__OnHideSlotReelEffect))

		for slotPos in xrange(self.reelIconSlot.GetSlotCount()):
			# Get random itemVnum.
			itemVnum = SLOT_MACHINE_REELS[app.GetRandom(1, len(SLOT_MACHINE_REELS))]

			# Select item information.
			item.SelectItem(itemVnum)
			itemIcon = item.GetIconImage()
			(width, height) = item.GetItemSize()

			# Set item icon on reel slot.
			self.reelIconSlot.SetSlot(slotPos, 0, width, height, itemIcon, (1.0, 1.0, 1.0, 0.5))
			self.reelIconSlot.SetSlotCount(slotPos, 0)
			self.reelIconSlot.ShowSlotBaseImage(slotPos)

		self.reelIconSlot.RefreshSlot()

		for slotPos in xrange(self.jackpotReelIconSlot.GetSlotCount()):
			uniqueSlot = 1

			if slotPos >= 3 and slotPos <= 5:
				uniqueSlot = 2
			elif slotPos >= 6 and slotPos <= 8:
				uniqueSlot = 3
			else:
				uniqueSlot = 1

			# Get jackpot itemVnum.
			itemVnum = SLOT_MACHINE_REELS[uniqueSlot]

			# Select item information.
			item.SelectItem(itemVnum)
			itemIcon = item.GetIconImage()
			(width, height) = item.GetItemSize()

			# Set item icon on jackpot reel slot.
			self.jackpotReelIconSlot.SetSlot(slotPos, 0, width, height, itemIcon, (1.0, 1.0, 1.0, 0.5))
			self.jackpotReelIconSlot.SetSlotCount(slotPos, 0)
			self.jackpotReelIconSlot.ShowSlotBaseImage(slotPos)

		self.jackpotReelIconSlot.RefreshSlot()

		# Click up bet button.
		self.__OnClickUpBetButton()

	# Create game type info tooltip.
	def __CreateGameTypeToolTip(self, title, descList):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetTitle(title)

		for desc in descList.itervalues():
			if desc == "[ENTER]":
				# Show horizontal line if token is found in desc.
				toolTip.AppendHorizontalLine()
			else:
				toolTip.AutoAppendTextLine(desc)
				toolTip.AppendSpace(1)

		toolTip.TextAlignHorizonalCenter()
		toolTip.SetTop()
		return toolTip

	# Hide Jackpot Effect
	def __OnHideJackpotEffect(self):
		# Jackpot Effect
		if self.jackpotEffect:
			self.jackpotEffect.Hide()

	# Hide Success Effect
	def __OnHideSuccessEffect(self):
		# Success Effect
		if self.successEffect:
			self.successEffect.Hide()

	# Hide Slot Reel Effect
	def __OnHideSlotReelEffect(self):
		# Slot Reel Effect
		for reelIconEffect in self.reelIconEffectList:
			reelIconEffect.Hide()

	# On click information button.
	def __OnClickInformationButton(self):
		if self.isInformationPage:
			self.isInformationPage = False
			self.OnShowBoard(SLOT_MACHINE_PLAY_BOARD)
		else:
			self.isInformationPage = True
			self.OnShowBoard(SLOT_MACHINE_INFO_BOARD)

	# On show board.
	def OnShowBoard(self, index):
		if index > 0:
			self.informationWnd.Show()
			self.slotMachineWnd.Hide()

			self.informationButton.Down()
		else:
			self.informationWnd.Hide()
			self.slotMachineWnd.Show()

			self.informationButton.SetUp()

	# On click close title bar.
	def __OnClickCloseTitleBar(self):
		# Close board.
		self.Close()

	# On click increase (up) bet button.
	def __OnClickUpBetButton(self):
		# Check valid bet index.
		if self.betIndex >= len(SLOT_MACHINE_BET_VALUES):
			return

		# Try to increase bet value.
		try:
			# Increase bet value and set text value.
			self.betIndex += 1
			self.betValue.SetText(localeInfo.NumberToMoneyString(SLOT_MACHINE_BET_VALUES[self.betIndex]))
		except KeyError:
			return

	# On click decrease (down) bet button.
	def __OnClickDownBetButton(self):
		# Check valid bet index.
		if self.betIndex <= 1:
			return

		# Try to decrease bet value.
		try:
			# Decrease bet value and set text value.
			self.betIndex -= 1
			self.betValue.SetText(localeInfo.NumberToMoneyString(SLOT_MACHINE_BET_VALUES[self.betIndex]))
		except KeyError:
			return

	# On click bet button.
	def __OnClickBetButton(self):
		curMoney = player.GetMoney()
		if curMoney < SLOT_MACHINE_BET_VALUES[self.betIndex]:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SLOT_MACHINE_NEED_GOLD)
			return

		## Network
		# Slot machine start with chosen bet.
		if not DEBUG:
			net.SendStartSlotMachine(SLOT_MACHINE_START, self.betIndex)
		else:
			self.OnSetReels(False, False,\
				app.GetRandom(1, len(SLOT_MACHINE_REELS)),\
				app.GetRandom(1, len(SLOT_MACHINE_REELS)),\
				app.GetRandom(1, len(SLOT_MACHINE_REELS))\
			)

		# Play money sound.
		if not self.isRolling:
			if ENABLE_SOUND:
				snd.PlaySound("sound/ui/money.wav")

	## Network
	# On set reel slots.
	def OnSetReels(self, win, jackpot, r1, r2, r3):
		# Check if machine is rolling.
		if not self.isRolling:
			# Set slot machine information.
			self.hasWon = win
			self.hasJackpot = jackpot

			self.reelResult[SLOT_MACHINE_REEL1] = r1 # slot reel 1
			self.reelResult[SLOT_MACHINE_REEL2] = r2 # slot reel 2
			self.reelResult[SLOT_MACHINE_REEL3] = r3 # slot reel 3

			# Check all slot reels.
			for slotPos in xrange(self.reelIconSlot.GetSlotCount()):
				# Set reel slot roll time and set unrolled.
				self.rollTime[slotPos] = app.GetGlobalTimeStamp() + int(2 * (slotPos + 1))
				self.isRolled[slotPos] = False

			# Stop slot machine rolling.
			self.isRolling = True

	# On reset reel slots.
	def OnReset(self):
		# Stop slot machine rolling.
		self.isRolling = False

		# Clear any previous jackpots and/or wins.
		self.hasWon = 0
		self.hasJackpot = 0

		for slotPos in xrange(self.reelIconSlot.GetSlotCount()):
			# Stop reel slot roll time and set unrolled.
			self.rollTime[slotPos] = 0
			self.isRolled[slotPos] = False

	# On board update.
	def OnUpdate(self):
		# Check if machine is rolling.
		if not self.isRolling:
			return

		# Check all reel slots.
		for slotPos in xrange(self.reelIconSlot.GetSlotCount()):
			# Check if slot has been rolled.
			if not self.isRolled[slotPos]:
				# Get reel slot roll time.
				leftSec = max(0, self.rollTime[slotPos] - app.GetGlobalTimeStamp())
				if leftSec > 0:
					# Randomly change reel slot item icon.
					self.OnChangeReelResult(slotPos)
				else:
					# Set reel slot.
					self.OnSetReelResult(slotPos)

					# Stop reel slot roll time and set as rolled.
					self.rollTime[slotPos] = 0
					self.isRolled[slotPos] = True

		# Check if all reel slots have been rolled.
		for slotPos in xrange(self.reelIconSlot.GetSlotCount()):
			if self.isRolled[slotPos] != True:
				return

		# Check if reel slots contain jackpot.
		if self.hasJackpot != 0 and self.hasWon != 0:
			if ENABLE_SOUND:
				# Play jackpot sound.
				snd.PlaySound("sound/effect/etc/firecracker/firecracker_xmas.wav")
				snd.PlaySound("sound/effect/etc/levelup_2/levelup1_2.wav")

			if ENABLE_EFFECT:
				# Show jackpot effect frame.
				if self.jackpotEffect and not self.isInformationPage:
					self.jackpotEffect.ResetFrame()
					self.jackpotEffect.Show()

				# Show reel boom effect.
				for slotPos in xrange(self.reelIconSlot.GetSlotCount()):
					if self.reelIconEffectList and not self.isInformationPage:
						self.reelIconEffectList[slotPos].ResetFrame()
						self.reelIconEffectList[slotPos].Show()

				# Show success effect frame.
				if self.successEffect and not self.isInformationPage:
					self.successEffect.ResetFrame()
					self.successEffect.Show()

		# Check if reel slots contain a win.
		elif self.hasWon != 0 and self.hasJackpot == 0:
			if ENABLE_SOUND:
				# Play win sound.
				snd.PlaySound("sound/ui/pvp.wav")
				snd.PlaySound("sound/ui/quest_success.wav")

			if ENABLE_EFFECT:
				# Show jackpot effect frame.
				if self.jackpotEffect and not self.isInformationPage:
					self.jackpotEffect.ResetFrame()
					self.jackpotEffect.Show()

				# Show success effect frame.
				if self.successEffect and not self.isInformationPage:
					self.successEffect.ResetFrame()
					self.successEffect.Show()
		else:
			if ENABLE_SOUND:
				# Play lose sound.
				snd.PlaySound("sound/ui/quest_fail.wav")

		# Stop slot machine rolling.
		self.OnReset()

	# On change reel results.
	def OnChangeReelResult(self, slotPos):
		# Get random itemVnum.
		itemVnum = SLOT_MACHINE_REELS[app.GetRandom(1, len(SLOT_MACHINE_REELS))]

		# Select item information.
		item.SelectItem(itemVnum)
		itemIcon = item.GetIconImage()
		(width, height) = item.GetItemSize()

		# Set item icon on reel slot.
		self.reelIconSlot.SetSlot(slotPos, 0, width, height, itemIcon, (1.0, 1.0, 1.0, 0.5))
		self.reelIconSlot.SetSlotCount(slotPos, 0)
		self.reelIconSlot.ShowSlotBaseImage(slotPos)
		self.reelIconSlot.RefreshSlot()

	def OnSetReelResult(self, slotPos):
		# Try to get network itemVnum.
		try:
			itemVnum = SLOT_MACHINE_REELS[self.reelResult[slotPos]]
		except IndexError:
			itemVnum = 63017

		# Select item information.
		item.SelectItem(itemVnum)
		itemIcon = item.GetIconImage()
		(width, height) = item.GetItemSize()

		# Set item icon on reel slot.
		self.reelIconSlot.SetSlot(slotPos, 0, width, height, itemIcon, (1.0, 1.0, 1.0, 0.5))
		self.reelIconSlot.SetSlotCount(slotPos, 0)
		self.reelIconSlot.ShowSlotBaseImage(slotPos)
		self.reelIconSlot.RefreshSlot()

		# Check if reel slot is unique.
		if self.reelResult[slotPos] <= SLOT_MACHINE_MAX_JACKPOTS:
			if ENABLE_SOUND:
				# Play jackpot reel icon sound.
				snd.PlaySound("sound/ui/quest_receive.wav")

			if ENABLE_EFFECT:
				# Show reel boom effect.
				if self.reelIconEffectList and not self.isInformationPage:
					self.reelIconEffectList[slotPos].ResetFrame()
					self.reelIconEffectList[slotPos].Show()

	# Open board.
	def Open(self):
		## Network
		# Open slot machine.
		if not DEBUG:
			net.SendStartSlotMachine(SLOT_MACHINE_OPEN)

		self.SetCenterPosition()
		self.SetTop()

		self.Show()

	# Close board.
	def Close(self):
		## Network
		# Close slot machine.
		if not DEBUG:
			net.SendStartSlotMachine(SLOT_MACHINE_CLOSE)

		# Check if the machine is still rolling.
		if self.isRolling:
			return

		self.Hide()

	# On press escape key.
	def OnPressEscapeKey(self):
		# Close board.
		self.Close()
		return True

	# On press exit key.
	def OnPressExitKey(self):
		# Close board.
		self.Close()
		return True
